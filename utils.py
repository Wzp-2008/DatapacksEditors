"""
 Author : wzpMC
 Date:   2022/1/20
 Time:   11:58
"""
from typing import List

import ping3
import requests


def readLang(filepath: str) -> dict:
    """
    read a .lang file
    :param filepath: The File's path you want to read
    :return: A dict with ID and translation
    """
    R = {}
    with open(filepath, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    for i in lines:
        sp = i.split("=")
        id = sp[0]
        content = sp[1].replace("\n", "")
        R[id] = content
    return R


def ContrastMinecraftVersion(version1: str, version2: str, equals: bool) -> bool:
    """
    Check Which Minecraft version is newer than other
    :param equals: Whether equality is allowed
    :param version1: First version
    :param version2: Second version
    :return: is bigger or smaller
    """
    v1 = list(map(int, version1.split(".")))
    v2 = list(map(int, version2.split(".")))
    if v1 == v2 and equals:
        return True
    if v1[1] > v2[1]:
        return True
    elif v1[1] == v2[1]:
        if len(v2) == 2 and len(v1) == 3:
            return True
        elif len(v2) == 3 and len(v1) == 3:
            if v1[2] > v2[2]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def selectServer(serverList: List[str]) -> str:
    """
    Choose the server which is the lowest ping
    :param serverList: URL list
    :return: the server which is the lowest ping
    """
    R = {}
    TIME = []
    for i in serverList:
        time = ping3.ping(i.replace("http://", "").replace("https://", "".replace("/", "")), timeout=1, unit='ms')
        R[time] = i
        TIME.append(time)
    return R[min(TIME)]


def getAllMinecraftVersion() -> List[dict]:
    sourceList = ["http://launchermeta.mojang.com", "https://bmclapi2.bangbang93.com", "https://download.mcbbs.net"]
    source = selectServer(sourceList) + "/mc/game/version_manifest.json"
    minecraftList = requests.get(source).json()
    mcVersions_list = []
    for i in minecraftList["versions"]:
        if i['type'] == "release":
            id = i['id']
            if ContrastMinecraftVersion(id, "1.16.5",True):
                url = i['url']
                mcVersions_list.append({"id": id, "url": url})
    return mcVersions_list


if __name__ == "__main__":
    print(getAllMinecraftVersion())
