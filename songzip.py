#!/usr/local/bin/python3
import zipfile #引入zip管理模块
import os
import sys #引入sys模块，获取脚本所在目录

#定义一个函数，递归读取absDir文件夹中所有文件，并塞进zipFile文件中。参数absDir表示文件夹的绝对路径。
def writeAllFileToZip(absDir,zipFile):
    for f in os.listdir(absDir):
        absFile=os.path.join(absDir,f) #子文件的绝对路径
        #print(absFile)
        if os.path.isdir(absFile): #判断是文件夹，继续深度读取。
            #relFile=absFile[len(os.getcwd())+1:] #改成相对路径，否则解压zip是/User/xxx开头的文件。
            #print(relFile)
			#zipFile.write(relFile) #在zip文件中创建文件夹
            writeAllFileToZip(absFile,zipFile) #递归操作
        else: #判断是普通文件，直接写到zip文件中。
            #print(absFile)
            relFile=absFile[len(os.getcwd())+1:] #改成相对路径
            #print(relFile)	
            zipFile.write(relFile,f)
    return


for n in os.listdir(os.getcwd()):
    if os.path.isdir(n):
       zipName=n+".zip"
       zipFilePath=os.path.join(os.getcwd(),zipName) 
#先定义zip文件绝对路径。sys.path[0]获取的是脚本所在绝对目录。
#因为zip文件存放在脚本同级目录，所以直接拼接得到zip文件的绝对路径。

       zipFile=zipfile.ZipFile(zipFilePath,"w",zipfile.ZIP_DEFLATED) 
#创建空的zip文件(ZipFile类型)。参数w表示写模式。zipfile.ZIP_DEFLATE表示需要压缩，文件会变小。ZIP_STORED是单纯的复制，文件大小没变。

       absDir=os.path.join(os.getcwd(),n) 
#print(absDir)
#要压缩的文件夹绝对路径。

       writeAllFileToZip(absDir,zipFile) 
#开始压缩。如果当前工作目录跟脚本所在目录一样，直接运行这个函数。
#执行这条压缩命令前，要保证当前工作目录是脚本所在目录(absDir的父级目录)。否则会报找不到文件的错误。
print("压缩成功")