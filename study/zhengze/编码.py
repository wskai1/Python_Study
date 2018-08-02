# chardet 模块
import chardet
import psutil as psutil
from psutil._common import snetio

print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
s=chardet.detect(data)
print(s['encoding'])


##获取CPU信息
print(psutil.cpu_count()) # CPU逻辑数量

print(psutil.cpu_count(logical=False)) # CPU物理核心  # 2说明是双核超线程, 4则是4核非超线程
print(psutil.cpu_times()) #统计CPU的用户／系统／空闲时间：
# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(1):
    psutil.cpu_percent(interval=1, percpu=True)
print(psutil.virtual_memory())
print(psutil.swap_memory())

#可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
psutil.disk_partitions() # 磁盘分区信息
psutil.disk_usage('/') # 磁盘使用情况
psutil.disk_io_counters() # 磁盘IO


psutil.net_io_counters() # 获取网络读写字节／包的个数
snetio(bytes_sent=3885744870, bytes_recv=10357676702, packets_sent=10613069, packets_recv=10423357, errin=0, errout=0, dropin=0, dropout=0)
print(psutil.net_if_addrs()) # 获取网络接口信息
print(psutil.net_if_stats()) # 获取网络接口状态

print( psutil.pids() )# 所有进程ID
p = psutil.Process(3708) # 获取指定进程ID=3776，其实就是当前Python交互环境
print(p.name()) # 进程名称
#print(p.cwd()) # 进程工作目录
#print(p.cmdline() ) # 进程启动的命令行
#print(p.ppid()) # 父进程ID
print(p.parent()) # 父进程
print(p.children()) # 子进程列表
print(p.status()) # 进程状态
#print( p.username()) # 进程用户名
print( p.create_time()) # 进程创建时间