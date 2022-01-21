import zipfile,os,linecache
version = None
versiondict = {}
gname = None
def ex(name,path=os.getcwd()):
    global gname
    gname = name
    zipFile = zipfile.ZipFile(name+".zip")
    zipFile.extractall(path)
def read(name):
    cwd = os.getcwd()
    ex(name,name)
    swd = name
    os.chdir(swd+'/')
    global version
    l = linecache.getline("manifest.txt",1)
    version =  l.replace(" version=","") 
    l = linecache.getline("manifest.txt",3)
    exec(l.replace("install = ",""))
def clean():
    global versiondict
    global gname
    versiondict[gname] = version
def main(name):
    print(os.getcwd())
    read(name)
    clean()
main("Aria2")