# 进入博客所在目录
cd /home/zx/blog/myblog
# 更新
git pull
# 重新生成readme和config文件
python3 create_config_and_indexs.py
# 重启docker下的vuepress
docker stop vuepress
docker run vuepress