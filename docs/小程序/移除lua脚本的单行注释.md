移除lua脚本的单行注释



绝大多数游戏的mod都是用的lua，如果不想自己的mod被别人乱改可以加密



也可以使用这种脚本来增加修改的难度

默认为utf8格式文本，如果不对可以改python的脚本或者使用改文件编码的脚本对文件进行重新编码

具体正则部分的缺陷和解释参见正则分类[lua注释的清除](/正则表达式/lua注释的清除)



remove_comment.py

直接调用时为 python 参数1 参数2

参数1为文件夹名称 参数二为文件后缀

```python
import sys
import os
import re
# 卫语句
if len(sys.argv) < 3:
    return


luaRegular = re.compile(
    r"""(?m)((^[\t ]*?[^\t\n \]\[=]*?[\t ]+)--[^"\n\[\]]+?$)|(^[\t ]*--[\t ]*(?!(\[\[)|(\[=)|(\]\])|=]).*$)|(^\s*--\[(=*?)\[[\s\S]*?]\8][\t ]*$)"""
    )
slCommentRegular = re.compile(
    r"""(?m)(^[\t ]*?[^\t\n \]\[=]*?[\t ]+)--[^"\n\[\]]+?$"""
    )
slEDCommentRegular = re.compile(
    r"""(?m)(^\s*?[^\t \]\[=]*?\s+)--[^"\n\[\]]+?$""")
muCommentRegular = re.compile(r"""(?m)^\s*--\[(=*?)\[[\s\S]*?]\1][\t ]*$""")

finishingClearnRegular = re.compile(r"""(?m)^[\t ]*--(\]\])?[\t ]*$""")

removeMulSepRegular = re.compile(
    r"""(?m)\s+\n$"""
    )

modelDict = {
    "lua": [
                (luaRegular,r"\2"),
                (finishingClearnRegular,r""),
                (removeMulSepRegular,r"\n"),
            ]
}


# 路径 正则表达式 替换结果
def remove_comment(content, model):
    result=content
    for regular,repl in modelDict[model]:
        result=regular.sub(repl, result)
    return result


def walk_all_files():
    # print(sys.argv[1])
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            print("*"+file)
            if file.endswith("."+sys.argv[2]):
                fileBeingModified = root+os.sep+file
                print(fileBeingModified)
                try:
                    with open(fileBeingModified, "r", encoding="utf-8") as f:
                        fileContent = f.read()
                        result = remove_comment(fileContent, sys.argv[2])
                    with open(fileBeingModified, "w", encoding="utf-8") as f:
                        f.write(result)
                    print(fileBeingModified+"替换成功")
                except:
                    print(fileBeingModified+"替换失败")


if __name__ == '__main__':
    print(sys.argv[1])
    walk_all_files()
```



在windows下调用的脚本



使用方式：将要删除注释的文件夹拖到脚本文件上，注意，要和romove_comment.py在同一个文件夹下。会自动复制一个完全相同的文件夹，并在其中进行清楚注释的操作。



remove_comment.cmd

```shell
xcopy %1\* %1_remove_comment\ /s
python %~dp0\remove_comment.py %1_remove_comment lua > remove_log.log
```



