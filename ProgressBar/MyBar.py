from threading import Thread
from time import sleep
from .utils import time2str
from .utils import bsize2str


class MyBar(Thread):
    now: int
    now_old: int
    full: int
    running: bool

    def __init__(self, full: int = 0, now: int = 0):
        super().__init__()
        self.now = now
        self.now_old = now
        self.full = full
        self.running = False

    def run(self) -> None:
        self.running = True
        while self.running:
            if self.full == self.now:
                self.close_bar()
            else:
                self.on_update()
                self.now_old = self.now
                sleep(1)

    def close_bar(self):
        self.now = self.full
        self.on_update()
        self.running = False

    def add(self, num: int = 1):
        if self.running:
            self.now += num
        else:
            raise RuntimeError("Cannot adding num when bar was closed!")

    def on_update(self) -> None:
        """
        每秒钟都会调用
        若要重写此方法，请务必考虑当总长度未知时的情况 即：当属性full为-1时
        注意：当总长度未知时，下载速度时可以算的
        属性now即当前下载到多少，单位字节
        属性now_old即一秒前下载到多少，单位字节
        属性full为总长度，单位字节
        """
        sec_download = self.now - self.now_old
        left_time_str = "未知"
        speed_str = bsize2str(sec_download)
        now_progress = 0
        left_progress = 50
        if self.full != -1:
            if sec_download != 0:
                left_time = (self.full - self.now) // sec_download
                left_time_str = time2str(left_time)
            progress = self.now // ((self.full // 50) + 1)
            now_progress = int(progress)
            left_progress = 50 - now_progress
            if self.full == self.now:
                now_progress = 50
                left_progress = 0
        print("\r|", '▇' * now_progress, '□' * left_progress, '|  ', speed_str, '/s', '  剩余时间：', left_time_str, end="",
              sep="", flush=True)
