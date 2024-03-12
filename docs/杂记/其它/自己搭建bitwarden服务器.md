自己搭建bitwarden服务器



### 起因

一直没用专属的密码管理软件，而后注册的地方越来越多，密码相似的过多了和一些不太重要的地方忘记密码成了问题。

打算自己搭个密码服务器，最后选中bitwarden这个软件

优点是，开源，支持自建节点，插件和应用商店的评分基本都是五星。

[bitwarden官网](https://bitwarden.com/)

这种密码服务器打算是放在内网用，相对而言更安全一点。同时以前也做了外网访问内网的方式，就做的本地部署。





### 总体简介

整体采用docker-compose部署，主要为让vaultwarden和负责代理的nginx的通信。

配置中的SSL证书可采用自签方式和腾讯云服务器两种方式部署。

其中自签方式不可用于IOS的app，即使将签名证书导入到手机设为信任也是不能用的。

最初照着官方wiki搞了挺久也没弄成功，做了自签的证书手机又报错，就照着自己的情况写了这篇博客。希望能让看到这篇博客的人少走点弯路。

vaultwarden和bitwarden的区别联系就不一点点说了，网上总结的比我要强好多。

vaultwarden wiki [vaultwarden Wiki](https://github.com/dani-garcia/vaultwarden/wiki)

vaultwarden官方映像 [vaultwarden/server](https://hub.docker.com/r/vaultwarden/server)



#### 需要准备的东西

部署设备（需要支持docker） 

域名和服务器（自签可省略，仅用于生成证书。这里用的腾讯云，如果有其它方式能弄到证书也可以）

国内的这些云服务器商应该都能做证书，选腾讯是因为目前正在用。



#### 环境

时间 2024.3

设备 radxa rock5b 

其中路由器已经做好域名劫持，将网址解析到设备的内网地址。远程访问方式也早已配好，可远程通过域名访问。

系统 armbian v24.2 , docker version 20.10.21



### 开始搭建

docker 等的安装，ip地址的获取，域名的劫持等就不再一一介绍了。

如果想测试一下没有ssl证书的vaultwarden效果可以使用

注：官方docker页面的命令

```shell
docker run -d --name vaultwarden -v /vw-data/:/data/ -p 80:80 vaultwarden/server:latest
```

命令测试一下效果，这时用可以直接通过ip访问网页的，测完记得删掉这个容器



测完后依次执行以下命令

#### 建立数据存放文件夹

```shell
# 数据存储目录 可自己修改
vaultwarden_dir=/mnt/user/appdata/vaultwarden

# 用于存放bitwarden数据
mkdir -p $vaultwarden_dir/bitwarden
# 存储nginx的配置文件
mkdir -p $vaultwarden_dir/nginx
# 存储ssl证书和私钥
mkdir -p $vaultwarden_dir/ssl/certs
mkdir -p $vaultwarden_dir/ssl/private
```



##### 自签证书生成

这里执行命令之后会出现填信息的部分，按照提示填一下即可。

注意域名部分，将其替换为你劫持的域名。

比如我在路由器中劫持 5b.mydomain.com 192.168.1.52 其中192.168.1.52为我的开发板ip,5b.mydomain.com将要用到的域名。

```shell
# 自签证书
openssl req \
 -x509 -nodes \
 -days 365 \
 -newkey rsa:4096 \
 -keyout /etc/ssl/private/nginx-bitwarden.key \
 -out /etc/ssl/certs/nginx-bitwarden.crt
```



##### 增强访问安全性

可省略，若省略则后面nginx中的对应配置记得删掉

这个生成的略慢，要稍微等一下

```shell
openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```



##### 腾讯云服务器SSL证书

腾讯云SSL证书可去搜详细的图文教程

这里简单写下流程

1. 登录腾讯云控制台找到SSL证书模块

2. 找到我的证书->申请免费证书

3. 填完表格进行申请即可。
   这里我是有云服务器和域名的，选的自动dns验证，不确定无服务器和无域名能不能申请。

4. 申请完等一会儿，在我的证书里可以找到下载页面，选择任意包含crt和key的就可以。

5. 将下载的证书可私钥放到要部署的服务器上。



#### 相关的密钥证书复制

```shell
# 如果不是自签证书则替换为对应key存放位置
cp /etc/ssl/private/nginx-bitwarden.key $vaultwarden_dir/ssl/private/nginx-bitwarden.key
# 如果不是自签证书则替换为对应crt证书存放位置
cp /etc/ssl/certs/nginx-bitwarden.crt $vaultwarden_dir/ssl/certs/nginx-bitwarden.crt
cp /etc/ssl/certs/dhparam.pem $vaultwarden_dir/ssl/certs/dhparam.pem
```



##### nginx配置文件

位置 

```shell
$vaultwarden_dir/nginx.conf
```

内容 

没生成

```shell
$vaultwarden_dir/ssl/certs/dhparam.pem
```

的话记得删掉对应的配置，否则不用动



```conf
events {}

http{
  server {
    listen 80;
    return 301 https://$host$request_uri;   
  }

  server {
    listen 443 ssl;

    ssl_certificate /etc/ssl/certs/nginx-bitwarden.crt;
    ssl_certificate_key /etc/ssl/private/nginx-bitwarden.key;
    ssl_dhparam /etc/ssl/certs/dhparam.pem;

    location / {
        proxy_pass http://bitwarden;
    proxy_set_header        Host $host;
        proxy_set_header        X-Real-IP $remote_addr;
        proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Proto $scheme;
    }

  location /notifications/hub {
    proxy_pass http://bitwarden:3012;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
  }

  location /notifications/hub/negotiate {
    proxy_pass http://bitwarden:80;
  }
}
}
```



##### docker-compose文件

位置

```shell
$vaultwarden_dir/docker-compose.yml
```

内容

可修改的地方，端口，nginx的映像，建议只改端口

```yml
version: '3'

services:
  bitwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    expose:
      - "80"
      - "3012"
    volumes:
      - ./bitwarden:/data
    restart: on-failure
    environment:
      WEBSOCKET_ENABLED: 'true'

  nginx:
    image: nginx:1.15-alpine
    container_name: vaultwarden-nginx
    restart: always
    ports:
      - "7920:80"        #基本忽略即可
      - "7930:443"       #要暴露的端口，用于连接
    volumes:
      - ./nginx:/etc/nginx
      - ./ssl:/etc/ssl


```



文件配置完成之后

可在`$vaultwarden_dir`下使用 `docker-compose up`命令启动映像

若无报错 同时可正常访问，可使用 `docker-compose up -d`命令使其挂起



然后就能使用 [域名]:[ip]访问自建的bitwarden服务器了





参考博客：

[Self Hosting Bitwarden on the Raspberry Pi - Pi My Life Up](https://pimylifeup.com/raspberry-pi-bitwarden/)

参考项目：

[JulianRunnels/Vaultwarden_Self_Host](https://github.com/JulianRunnels/Vaultwarden_Self_Host)
