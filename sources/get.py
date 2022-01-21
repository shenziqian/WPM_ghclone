import os
from pyaria2 import Jsonrpc
import install
def get():
    install.main("Aria2")
    jsonrpc = Jsonrpc("127.0.0.1",6800)
    jsonrpc.addUris("https://gitee.com/shen-ziqian/wpm-pkgs-mirror/repository/blazearchive/main.zip?Expires=1642421402&Signature=X9sMFQi9C5f8VvXesoAyVo9lQTVuhWRVSEWnPfaxoNE%3D")
    install.ex("wpm-pkgs-mirror-main.zip")
    os.chdir("wpm-pkgs-mirror-main")
get()