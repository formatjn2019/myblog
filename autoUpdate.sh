# 进入博客所在目录
cd /home/zx/blog/myblog
# 删除自动生成的READEME.md
find /home/zx/blog/myblog -name "README.md" | xargs rm -f
# 重置更改
git reset --hard
# 更新
git pull
# 重新生成readme和config文件
python3 create_config_and_indexs.py
# 重启docker下的vuepress
docker restart myblog
