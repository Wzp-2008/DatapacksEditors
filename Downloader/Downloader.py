"""
 Author : wzpMC
 Date:   2022/1/22
 Time:   13:41
"""
import os

import requests
from PyQt6.QtCore import QThread
from loguru import logger as log


class Downloader(QThread):

    def __init__(self, url, path, func, mute):
        """
        Downloader
        :param url: the url you need to download
        """
        super().__init__()
        self.url = url
        self.filesize = int(requests.head(url).headers['Content-Length'])
        self.path = path
        self.func = func
        self.mute = mute
        log.info(f"size = {self.filesize}")

    def run(self):
        self.mute.lock()
        log.info("starting download")
        self.func.setMaximum(self.filesize)
        r = requests.get(self.url, stream=True)
        value = 0
        try:
            with open(self.path, "ab") as fp:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        fp.write(chunk)
                        value += len(chunk)
                        self.func.setValue(value)
        except Exception as e:
            log.error(e)
            return
        log.success("downloaded!")
        self.func.setValue(0)
        self.mute.unlock()
