from loguru import logger as log
from json import dumps, loads
from typing import Dict

from requests import Session, Response

from Downloader import Downloader
from ProgressBar import MyBar
from .utils import *
from .DownloadQueue import DownloadQueue
from _thread import start_new_thread


class MinecraftDownloader(object):
    base_url: str
    session: Session
    headers: Dict[str, str]
    proxies: Dict[str, str]
    downloader: Downloader

    def __init__(self, base_url: str, proxies: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.session = Session()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"}
        if proxies is None:
            proxies = {}
        self.proxies = proxies
        self.downloader = Downloader(headers=self.headers, proxies=self.proxies)

    def url_adopter(self, url: str) -> str:
        if self.base_url[-1] != "/":
            self.base_url += "/"
        url = url.replace("https://launcher.mojang.com/", self.base_url)
        url = url.replace("http://launcher.mojang.com/", self.base_url)
        url = url.replace("http://launchermeta.mojang.com/", self.base_url)
        url = url.replace("https://launchermeta.mojang.com/", self.base_url)
        url = url.replace("http://resources.download.minecraft.net/", self.base_url + "assets/")
        url = url.replace("https://resources.download.minecraft.net/", self.base_url + "assets/")
        url = url.replace("https://libraries.minecraft.net/", self.base_url + "maven/")
        url = url.replace("http://libraries.minecraft.net/", self.base_url + "maven/")
        return url

    def do_get(self, url) -> Response:
        url = self.url_adopter(url)
        return self.session.get(url, headers=self.headers, proxies=self.proxies)

    def get_raw_minecraft_versions_list(self) -> List[Dict[str, str]]:
        url = self.base_url + "/mc/game/version_manifest.json"
        return self.do_get(url).json()['versions']

    def get_latest_minecraft_version(self) -> str:
        url = self.base_url + "/mc/game/version_manifest.json"
        return self.do_get(url).json()["latest"]["id"]

    def get_all_minecraft_versions_list(self) -> List[str]:
        result: List[str] = []
        for v in self.get_raw_minecraft_versions_list():
            result.append(v['id'])
        return result

    def get_given_minecraft_versions_list(self, version_type: str) -> List[str]:
        result: List[str] = []
        for v in self.get_raw_minecraft_versions_list():
            if v['type'] == version_type:
                result.append(v['id'])
        return result

    def get_release_minecraft_versions_list(self) -> List[str]:
        return self.get_given_minecraft_versions_list("release")

    def get_snapshot_minecraft_versions_list(self) -> List[str]:
        return self.get_given_minecraft_versions_list("snapshot")

    def get_old_alpha_minecraft_versions_list(self) -> List[str]:
        return self.get_given_minecraft_versions_list("old_alpha")

    def get_minecraft_version_info(self, version: str) -> Optional[Dict[str, str]]:
        versions = self.get_raw_minecraft_versions_list()
        has = False
        i = {}
        for i in versions:
            if i['id'] == version:
                has = True
                break
        if not has:
            return
        version_json_response = self.do_get(i['url'])
        version_json_data = version_json_response.json()
        return version_json_data

    def get_minecraft_client(self, version: str, bar: MyBar) -> bool:
        init_game_dir()
        version_info = self.get_minecraft_version_info(version)
        game_path = path.join(version_path, version)
        if not path.exists(game_path):
            create_default(game_path)
        version_json_path = path.join(game_path, f"{version}.json")
        if not path.exists(version_json_path):
            with open(version_json_path, "w") as fp:
                fp.write(dumps(version_info))
        # noinspection PyTypeChecker
        client_url = version_info['downloads']['client']['url']
        version_jar_path = path.join(game_path, f"{version}.jar")
        if not path.exists(version_jar_path):
            self.downloader.download(self.url_adopter(client_url), version_jar_path, bar)
        # noinspection PyTypeChecker
        index_url = version_info["assetIndex"]["url"]
        # noinspection PyTypeChecker
        index_id = version_info["assetIndex"]["id"]
        assets_json_path = path.join(assets_index_path, f"{index_id}.json")
        if not path.exists(assets_json_path):
            assets_data = self.downloader.session.get(self.url_adopter(index_url)).json()
            with open(assets_json_path, "w") as fp:
                fp.write(dumps(assets_data))
        else:
            with open(assets_json_path, "r") as fp:
                assets_data = loads(fp.read())
        assets_objects_data = assets_data["objects"]
        q = DownloadQueue()
        q.req_session = self.downloader.session
        queue_bar: MyBar = MyBar(full=len(assets_objects_data.keys()))
        queue_bar.new_bar()
        queue_bar.start()
        for i in assets_objects_data.keys():
            data = assets_objects_data[i]
            hash_value = data['hash']
            size = data["size"]
            dir_path = path.join(assets_objects_path, hash_value[0:2])
            create_default(dir_path)
            save_path = path.join(dir_path, hash_value)
            p = hash_value[0:2] + "/" + hash_value
            default_url = f"https://resources.download.minecraft.net/{p}"
            url = self.url_adopter(default_url)
            q.add_file(url, save_path, queue_bar, size)
        while queue_bar.running:
            pass
        print("开始下载")
        q.start_download()
        return True
