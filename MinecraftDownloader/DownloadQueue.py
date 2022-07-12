from os import path
from threading import Thread
from typing import List

from requests import session
from requests.sessions import Session, HTTPAdapter
from ProgressBar import MyBar

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"}


class FileObject(Thread):
    url: str
    save: path
    size: int
    req_session: Session
    bar: MyBar

    def __init__(self, req_session: Session, url: str, save: path, size: int):
        super().__init__()
        self.url = url
        self.save = save
        self.req_session = req_session
        self.size = size

    def run(self) -> None:
        r = self.req_session.get(self.url, stream=True)
        if not path.exists(self.save):
            with open(self.save, 'ab') as fp:
                for data in r.iter_content(128):
                    self.bar.add(len(data))
                    fp.write(data)
        else:
            self.bar.add(self.size)


class DownloadQueue(object):
    req_session: Session = session()
    bar: MyBar = MyBar()
    files: List[FileObject] = []
    thread_num: int = 8
    now_file: int = 0

    def __init__(self):
        self.req_session.mount("https://", HTTPAdapter(max_retries=5))
        self.req_session.mount("http://", HTTPAdapter(max_retries=5))

    def add_file(self, url: str, save: path, adding_bar: MyBar, size: int):
        file = FileObject(self.req_session, url, save, size)
        self.bar.full += file.size
        file.bar = self.bar
        file.req_session = self.req_session
        self.files.append(file)
        adding_bar.add()

    def start_download(self):
        self.bar.new_bar()
        self.bar.start()
        while True:
            now_count: int = 0
            for f in self.files:
                if f.is_alive():
                    now_count += 1
            left_file = len(self.files)
            if left_file == 0 and now_count == 0:
                break
            if now_count < self.thread_num and left_file != 0:
                for i in range(self.thread_num - now_count):
                    self.files[self.now_file].start()
                    self.now_file += 1
