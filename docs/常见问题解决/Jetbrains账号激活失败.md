Jetbrains账号激活失败

#### 激活页面提示
Authorization Failed You can close this page and return to the IDE

#### 原因

产品连不上jetbrains的服务器

#### 解决方法

1. 如果用过破解版，可能是host将服务器解析到了本机或其它地址，可以修改host文件
2. 换网
3. 部分产品可以用离线激活码（不知道为何webstorm能用goland不能用，我是开源项目白嫖的权限）
4. 设置系统代理，我是用的猫，proxy setting -> Manual proxy configuration 
Host name  : localhost
port number : 猫上显示的数字