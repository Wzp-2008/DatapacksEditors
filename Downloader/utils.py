from os import remove
from time import time


def many2one(thread_num: int, save: str) -> int:
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
    return used
