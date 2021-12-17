linux下的源码编译问题

以debian为例

make命令无法执行

```bash
apt-get install gcc automake autoconf libtool make
```

编译报错，原因是缺少依赖

```bash
sudo apt-get install build-essential
```



