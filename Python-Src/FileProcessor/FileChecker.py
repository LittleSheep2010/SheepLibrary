import os

def fileCheck(filePath:str) -> bool:
    if os.path.exists(filePath):
        return os.path.isfile(filePath)
    else: return False

def dirCheck(dirPath:str) -> bool:
    if os.path.exists(dirPath):
        return os.path.isdir(dirPath)
    else: return False