import shutil
import psutil
disk_use=shutil.disk_usage("/");
print (disk_use)
use=disk_use.free/disk_use.total *100
print(use)
print(psutil.cpu_percent(0.1))
