from .utils import select_server
from .MinecraftDownloader import MinecraftDownloader
downloader = MinecraftDownloader(select_server())



