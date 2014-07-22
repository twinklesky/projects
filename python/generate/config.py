#coding:utf-8
import configparser
class Config:
    def __init__(self):
        config = configparser.ConfigParser();
        config.read("config.ini", "utf-8")
        self.tempDir = config["default"]["tempDir"]
    
    