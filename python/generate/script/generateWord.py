#coding:utf-8
import os
import shutil
import time
import zipUtil

class GenerateWord:
    def __init__(self,outputDir,templatePath,data):
        self.__outputDir = os.path.abspath(outputDir)
        self.templatePath = os.path.abspath(templatePath.strip())
        self.data = data;
        self.__tempDir = "../temp"
        self.__outputFile = ""
    
    def start(self):
        timeStart = time.time()
        if not os.path.exists(self.templatePath):
            print("File %s is not exist!"%(self.templatePath))
            return
        if not self.templatePath.lower().endswith(".docx"):
            print("File %s is not docx document!"%self.templatePath)
            return
        fileDir,fileName = os.path.split(self.templatePath)
        name,sufix = os.path.splitext(fileName)
        zipFile = os.path.abspath(self.__tempDir.strip())+ "/" + name + ".zip"
        #copy file to ../temp directory and rename to zip file
        shutil.copy(self.templatePath, zipFile)
        #unzip
        outputPath = os.path.join(self.__tempDir,name)
        zipUtil.unzip_file(zipFile,outputPath)
        os.remove(zipFile)
        #write document
        print("I am writing doc file...")
        #zip
        zipUtil.zip_dir(outputPath,zipFile)
        strTime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        self.__outputFile = self.__outputDir + "/" + name + strTime + ".docx"
        shutil.copy(zipFile, self.__outputFile)
        shutil.rmtree(outputPath, True)
        timeEnd = time.time()
        timeSpent = timeEnd - timeStart
        print("Time used for generate word is %f s"%timeSpent)
    
    def setTempDir(self,tempDir):
        self.__tempDir = os.path.abspath(tempDir)
        
    def getTempDir(self):
        return self.__tempDir
        