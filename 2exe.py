# coding:utf-8
import os
import os.path

# Ui文件所在路径
dir = './'


def code2exe(pyfile):
    # cmd = 'pyinstaller -F -w {pyfile}'.format(pyfile=pyfile) # 隐藏CMD
    cmd = 'pyinstaller -F {pyfile}'.format(pyfile=pyfile)
    os.system(cmd)

if __name__ == "__main__":
    code2exe('淘宝秒杀脚本.py')
