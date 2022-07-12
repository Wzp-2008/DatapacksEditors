from MinecraftDownloader import *
from ProgressBar import MyBar

bar = MyBar()
bar.start()
downloader.base_url = "https://bmclapi2.bangbang93.com"
result = downloader.get_minecraft_client("1.19",bar)
bar.stop()