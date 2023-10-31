import psutil

#CPU
print(psutil.cpu_count(logical=False))
print(psutil.cpu_percent(interval=1))
print(psutil.cpu_times())
print(psutil.cpu_stats())

#RAM
print(psutil.virtual_memory())
print(psutil.swap_memory())

#Hard Disk
print(psutil.disk_usage('/'))
print(psutil.disk_partitions())

#documentation about commands: https://psutil.readthedocs.io/en/latest/