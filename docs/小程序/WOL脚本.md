WOL脚本

家里的nas比较费电，然后tp的路由器又不支持WOL操作，于是买了个小的arm结构的nas做常用数据的缓存，这个系统支持docker，原本想用docker装debian再装wakeonlan的包的，结果使用echo输出一条语句都花了40来秒，完全颠覆了我对性能的认知。终于放弃了通过docker来实现WOL了。幸好这个型号支持python。

最后再网上找的python脚本，按照需求重写了下

需求环境 python3 linux

python脚本 

直接调用方法

```shell
python3 wakeOnLan.py 参数1 参数2
```



参数1 为网卡MAC地址 参数2 为端口号 可忽略



wakeOnLan.py 



```python
import binascii
import re
import socket
import sys

# MAC地址的校验规则
MAC_REGULAR=re.compile(r"^[A-F0-9]{12}$")

# wake on lan
def wake_on_lan(mac,port):
    mac,port=check_args(mac,port)
    data="F"*12+mac*16
    send_data = binascii.unhexlify(data)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, ('255.255.255.255', port))
    sock.close()
    print("发送魔术包成功")

# 参数检查
def check_args(mac,port):
    mac=re.sub("[^\w]","",mac.upper())
    port=int(port)
    if not MAC_REGULAR.match(mac):
        raise ValueError("mac地址错误")
    if not (port==7 or port ==9):
        raise ValueError("端口错误")

    return mac,port

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("输入参数为mac地址 端口 端口可省略")
    else:
        mac=sys.argv[1]
        port=(len(sys.argv)>2 and sys.argv[2] or 7)
        wake_on_lan(mac,port)
```



一般使用可将上述命令保存为shell脚本



