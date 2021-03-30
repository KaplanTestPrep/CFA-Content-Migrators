import xmltodict
import json

class ditamapParsing():
    
    def parseDitamap(file_path):
            ditaList = []
            with open(file_path) as ditamap:
                    mapTopicHead = xmltodict.parse(ditamap.read())
                    object = json.dumps(mapTopicHead)
                    if mapTopicHead != None:
                            ditamapParsing.parseTaxonomy1(mapTopicHead["map"]["topichead"], ditaList)
                            return ditaList
                
                                            
    def parseTaxonomy1(taxonomy1List, ditaList):
            if taxonomy1List != None and len(taxonomy1List) > 0:
                    for taxonomy1 in taxonomy1List:
                            ditamapParsing.parseTaxonomy2(taxonomy1["topichead"], ditaList)
            return ditaList

    def parseTaxonomy2(taxonomy2List, ditaList):
            if taxonomy2List != None and len(taxonomy2List) > 0:
                    if taxonomy2List.__contains__("topichead"):
                            ditamapParsing.parseTaxonomy3(taxonomy2List["topichead"], ditaList)
                    else:
                            for taxonomy2 in taxonomy2List:
                                    ditamapParsing.parseTaxonomy3(taxonomy2["topichead"], ditaList)
            return ditaList
                                                                                            
    def parseTaxonomy3(taxonomy3List, ditaList):
            if taxonomy3List !=None and len(taxonomy3List) > 0:
                    if taxonomy3List.__contains__("topicref"):
                            ditamapParsing.parseHref(taxonomy3List["topicref"], ditaList)
                    else:
                            for taxonomy3 in taxonomy3List:
                                    ditamapParsing.parseHref(taxonomy3["topicref"], ditaList)
            return ditaList 

    def parseHref(ditaFileList, ditaList):
            if ditaFileList != None and len(ditaFileList)>0:
                    if len(ditaFileList) == 1:
                            ditaList.append(ditaFileList["@href"])
                    else:
                            for file in ditaFileList:
                                    ditaList.append(file["@href"])
            return ditaList
