#coding=utf-8
"""
zip directory and unzip file
"""
 
import os,os.path
import zipfile
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)
    zf.close()
 
def unzip_file(zipFile, outputPath):
    zipFileObj = zipfile.ZipFile(zipFile,"r")
    zipFileObj.extractall(outputPath)
    zipFileObj.close()