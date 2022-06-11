from os import remove
from time import time

K = 1024
M = K ** 2
G = K ** 3
T = K ** 4


def bsize2str(size: int) -> str:
    if size == 0:
        return "?"
    elif size < K:
        result = "%.2fB" % size
    elif size < M:
        result = "%.2fKB" % (size / K)
    elif size < G:
        result = "%.2fMB" % (size / M)
    elif size < T:
        result = "%.2fGB" % (size / G)
    else:
        result = "%.2fTB" % (size / T)
    return result


MIN = 60
HOUR = 60 * MIN
DAY = 24 * HOUR


def time2str(sec: int) -> str:
    if sec < MIN:
        return f"{sec}秒"
    elif sec < HOUR:
        m = sec // MIN
        s = sec - (MIN * m)
        if s == 0:
            return f"{m}分"
        return f"{m}分{s}秒"
    elif sec < DAY:
        h = sec // HOUR
        m = (sec - (h * HOUR)) // MIN
        s = sec - (MIN * m) - (h * HOUR)
        if s == 0 and m == 0:
            return f"{h}时"
        if m == 0:
            return f"{h}时{s}秒"
        if s == 0:
            return f"{h}时{m}分"
        return f"{h}时{m}分{s}秒"
    else:
        return "大于一天"


def many2one(thread_num: int, save: str) -> None:
    print("开始合并文件")
    start = time()
    long = 0
    with open(save, "ab") as fp:
        for i in range(thread_num):
            filename = f"{save}.{i}.tmp"
            with open(filename, "rb") as fc:
                content = fc.read()
                long += len(content)
                fp.write(content)
            remove(filename)
    end = time()
    used = int(end - start)
    try:
        print(f"合并完成，耗时：{time2str(used)}，速度：{bsize2str(long // used)}/s")
    except ZeroDivisionError:
        print(f"合并完成，耗时：%.2f毫秒，速度：太快了，没测出来"%((end - start)*1000))
