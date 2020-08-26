import json

from FileProcessor.FileChecker import fileCheck, dirCheck
from JsonProcessor.JsonDocument import *

class JsonLoader:
    __uncommit_fileContents = []

    # 读取文件并存储到 (JsonLoder)__uncommit_fileContents
    # 返回 (int)JsonID / False
    # Read the file and store it to (JsonLoder) __ uncommit_fileContents
    # Return (int) JsonID / False
    def loadJson(self, filePath:str) -> any:
        if fileCheck(filePath): return False 

        readingFileIO = open(filePath, "r+") # 打开文件
        self.__uncommit_fileContents.append(readingFileIO.read()) # 暂存到 --> (self)__uncommit_fileContents

    # 处理读取出来的文件
    # 可以自动提交到 JsonDocument
    # Process the read file
    # Can be automatically submitted to JsonDocument
    def processJson(self, saveID, autoCommit:bool=True, commitToDocument:JsonDocument=None) -> any:
        if len(self.__uncommit_fileContents) < saveID: return False # 检查 saveID 是否存在

        loadingBuffer = json.loads(self.__uncommit_fileContents[saveID]) # 用 Json 读取文件信息

        # 自动提交
        if autoCommit and commitToDocument != None:
            commitToDocument.commitDocument(loadingBuffer)