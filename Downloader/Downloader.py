"""
 Author : wzpMC
 Date:   2022/1/22
 Time:   13:41
"""
from os import remove, path
from threading import Thread

from loguru import logger as log
from typing import Optional, Dict, List
from requests import Session
from requests.structures import CaseInsensitiveDict

from .utils import many2one
from ProgressBar import MyBar
from ProgressBar.utils import bsize2str


class DownloadThread(Thread):
    bar: MyBar
    url: str
    session: Session
    headers: Dict[str, str]
    proxies: Dict[str, str]
    num: int
    save: str
    begin: int
    to: int
    is_one: bool

    def __init__(self, save: str, url: str, bar: MyBar, num: int, session: Session, begin: int, to: int,
                 headers: Dict[str, str], proxies: Dict[str, str],
                 is_one: bool = False):
        super().__init__()
        self.url = url
        self.bar = bar
        self.session = session
        if headers is None:
            headers = {}
        if proxies is None:
            proxies = {}
        self.headers = headers.copy()
        self.proxies = proxies
        self.num = num
        self.save = save
        self.begin = begin
        self.to = to
        self.is_one = is_one

    def run(self) -> None:
        log.info(f"NetworkThread-{self.num} Starting")
        save_name = f"{self.save}.{self.num}.tmp"
        if not self.is_one:
            self.headers["Range"] = f"bytes={self.begin}-{self.to}"
        if self.is_one:
            save_name = self.save
        if path.exists(save_name):
            remove(save_name)
        r = self.session.get(self.url, proxies=self.proxies, headers=self.headers, stream=True)
        with open(save_name, "ab") as fp:
            for c in r.iter_content(1024):
                fp.write(c)
                self.bar.add(len(c))
        log.info(f"NetworkThread-{self.num} done")


class Downloader(object):
    thread_name: str
    session: Session
    headers: Dict[str, str]
    proxies: Dict[str, str]
    thread_num: int

    def __init__(self, thread_name: str = "NetworkThread", session: Optional[Session] = None,
                 headers: Optional[Dict[str, str]] = None, proxies: Optional[Dict[str, str]] = None,
                 thread_num: int = 8):
        """
        多线程下载器
        :param thread_name: 线程名称
        :param session: 请求会话
        :param headers: 请求头，默认为Edge102.0.1245.33请求头
        :param proxies: 代理设置，需要设置http和https两个
        :param thread_num: 线程数，默认为8
        """
        if session is None:
            session = Session()
        self.session = session
        if headers is None:
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"}
        self.headers = headers
        if proxies is None:
            proxies = {}
        self.proxies = proxies
        self.thread_num = thread_num
        self.thread_name = thread_name

    def download(self, url: str, save2: Optional[str] = None, bar: Optional[MyBar] = None) -> None:
        """
        进行下载
        :param url: 需下载的url
        :param save2: 保存位置
        :param bar: 进度条
        """
        log.info(f"Downloading... url={url} saveto={save2}")
        headers = self.headers.copy()
        headers["referer"] = url
        if bar is None:
            bar = MyBar()
        if path.exists(save2):
            remove(save2)
        head_rep = self.session.head(url, headers=self.headers, proxies=self.proxies)
        response_head: CaseInsensitiveDict[str] = head_rep.headers
        try:
            file_long = response_head["content-length"]
        except KeyError:
            file_long = -1
        file_long = int(file_long)
        bar.full = file_long
        if file_long == -1:
            log.info(f"{self.thread_name}  Cannot get file long, using single thread")
            t = DownloadThread(save2, url, bar, 0, self.session, -1, -1, self.headers, self.proxies, True)
            bar.new_bar()
            t.start()
            while bar.running:
                pass
            return
        downloaded = 0
        part = (file_long // self.thread_num) + 1
        log.info(f"Theoretical size of each segment {bsize2str(part)}")
        threads: List[DownloadThread] = []
        for i in range(self.thread_num):
            file_long -= part
            if file_long < 0:
                file_long += part
                part = file_long - self.thread_num + 1
                print(part)
            threads.append(DownloadThread(save2, url=url, bar=bar, session=self.session, headers=self.headers,
                                          begin=downloaded, to=downloaded + part, proxies=self.proxies, num=i))
            downloaded += part + 1
            log.info(f"The {i}th thread needs to download {part}")
        log.info(f"Starting download with {self.thread_num} threads")
        bar.new_bar()
        for t in threads:
            t.start()
        while bar.running:
            pass
        many2one(self.thread_num, save2)
        bar.reset()