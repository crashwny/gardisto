import os

def collect():
    fpath = '/var/gardisto/collectors/'
    # newfiles = []
    flist = os.listdir(path=fpath)
    for i in flist:
        # newfiles.amend(i)
        cpu = i.find(cpu)
        disk = i.find(disk)
        ram = i.find(ram)
        service = i.find(service)

if __name__ == "__main__":
    collect()
