import psutil
import shutil

def check_disk_usage(disk):
    disk_use=shutil.disk_usage(disk)
    free=disk_use.free/disk_use.total * 100;
    return free > 20

def check_cpu_usage():
    cpu=psutil.cpu_percent(1)
    return cpu < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("Error!!!")
else:
    print("Everything is OK!")
