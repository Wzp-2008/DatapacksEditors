"""
 Author : wzpMC
 Date:   2022/1/20
 Time:   11:58
"""


def readLang(filepath: str) -> dict:
    """
    read a .lang file
    :param filepath: The File's path you want to read
    :return: A dict with ID and translation
    """
    R = {}
    with open(filepath, "r",encoding="utf-8") as fp:
        lines = fp.readlines()
    for i in lines:
        sp = i.split("=")
        id = sp[0]
        content = sp[1]
        R[id] = content
    return R
