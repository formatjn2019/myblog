import os
import re

MATCH_RULE = re.compile("^(.*)-\d(.md)$")


def scane_duplicate(folder_path):
    replace_dic = {}
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if MATCH_RULE.match(file_name):
                pre_path = os.path.join(root, "".join(MATCH_RULE.findall(file_name)[0]))
                now_path = os.path.join(root, file_name)
                delete_path = ""
                if replace_dic.get(pre_path) is None:
                    delete_path = pre_path
                    replace_dic[pre_path] = now_path
                elif replace_dic.get(pre_path) > now_path:
                    delete_path = now_path
                else:
                    delete_path = replace_dic.get(pre_path)
                    replace_dic[pre_path] = now_path
                if os.path.exists(delete_path) :
                    print("删除",delete_path)
                    os.remove(delete_path)

    for pre,cur in replace_dic.items():
        os.rename(cur,pre)


if __name__ == '__main__':
    scane_duplicate(r".")
