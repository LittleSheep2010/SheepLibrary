import json
import os

class SheepJson:
	
	# JsonLoader 子类
	class JsonLoader:
		def LoadJsonFile(self, JsonFile_path:str, CommitWareHouse_JsonWareHouse:SheepJson.JsonWareHouse=None, AutoSave:bool=True, ReturnSaveID:bool=True) -> any:
			fileReadingIO = open(JsonFile_path, "r")
			fileContents = fileReadingIO.read()

			# 检测文件是否正常
			if not os.path.exists(JsonFile_path):
				fileReadingIO.close(); return False
			
			# 检测是否自动保存到 JsonWareHouse
			if CommitWareHouse_JsonWareHouse != None and AutoSave:
				SaveID = len(CommitWareHouse_JsonWareHouse.uncommitJsonFileContents_list)
				CommitWareHouse_JsonWareHouse.uncommitJsonFileContents_list.append(fileContents)

				# 返回 SaveID
				if ReturnSaveID: return SaveID
				else: return False
			
			else:
				return fileContents

			fileReadingIO.close()

		def Save2WareHouseData(self, SaveContents:str, CommitWareHouse_JsonWareHouse:SheepJson.JsonWareHouse, ReturnSaveID:bool=True):
			SaveID = len(CommitWareHouse_JsonWareHouse.uncommitJsonFileContents_list)
			CommitWareHouse_JsonWareHouse.uncommitJsonFileContents_list.append(SaveContents)

			# 返回 SaveID
			if ReturnSaveID: return SaveID
			else: return False

		def ProcessJsonContents(self, SearchWareHouse_JsonWareHouse:SheepJson.JsonWareHouse, JsonContentsID_SaveID:int):
			JsonReadingIO_Buffer = json.loads(SearchWareHouse_JsonWareHouse.uncommitJsonFileContents_list[JsonContentsID_SaveID])
			return JsonReadingIO_Buffer

		def Save2File(self, SaveContents:dict, SaveFilePath:str):
			# 降级
			ProcessCompleteContents = json.dumps(SaveContents, ensure_ascii=False, indent=4, separators=(', ', ': '))

			# 保存文件
			fileWriteID = open(SaveFilePath, "w+")
			fileWriteID.write(ProcessCompleteContents)
			fileWriteID.close()
			return True

		
	# JsonWareHouse 子类
	class JsonWareHouse:

		# uncommit 保存处
		uncommitJsonFileContents_list = []