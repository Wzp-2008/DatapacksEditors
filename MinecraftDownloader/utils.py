from typing import List, Optional
import ping3
from os import path, mkdir, getcwd
from loguru import logger as log


def select_server(server_list: Optional[List[str]] = None) -> str:
    """
    Choose the server which is the lowest ping
    :param server_list: URL list
    :return: the server which is the lowest ping
    """
    if server_list is None:
        server_list = ["http://launchermeta.mojang.com", "https://bmclapi2.bangbang93.com/"]
    result = {}
    time_list = []
    for i in server_list:
        time = ping3.ping(i.replace("http://", "").replace("https://", "".replace("/", "")), timeout=1, unit='ms')
        if time is None:
            time = float("INF")
        result[time] = i
        time_list.append(time)
        log.info(str(i) + " ping: " + str(time))
    log.info("Server: " + str(result[min(time_list)]))    
    return result[min(time_list)]


games_path = path.join(getcwd(), "games")
version_path = path.join(games_path, "versions")
assets_path = path.join(games_path, "assets")
assets_index_path = path.join(assets_path, "indexes")
assets_objects_path = path.join(assets_path, "objects")
libraries_path = path.join(games_path, "libraries")


def create_default(dir_path: str):
    if not path.exists(dir_path):
        mkdir(dir_path)


def init_game_dir():
    create_default(games_path)
    create_default(version_path)
    create_default(assets_path)
    create_default(assets_index_path)
    create_default(assets_objects_path)
    create_default(libraries_path)
