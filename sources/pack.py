import os
template = """version = 
authors = AUTHORS
install = 
"""
if os.path.exists("manifests.txt"):
    os.remove("manifests.txt")
manifest = open("manifest.txt","w")
manifest.write(template)
print("manifest生成完毕，请自行添加内容并压缩为xxx.zip,最后给https://gitee.com/shen-ziqian/wpm-pkgs-mirror.git 发个PR")