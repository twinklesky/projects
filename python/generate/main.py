#coding:utf-8
import os,sys
sys.path.append("./script")
import shutil
from config import Config
from script.generateWord import GenerateWord

if __name__ == '__main__':
    config = Config()
    tempDir = config.tempDir
    if os.path.exists(tempDir):
        shutil.rmtree(tempDir,True)
    os.mkdir(tempDir)
    
    print("start generate report...")
    gw = GenerateWord(r"d:/temp",r"./template/template.docx",None)
    gw.setTempDir(tempDir)
    gw.start()
    print("finished!")
    
    