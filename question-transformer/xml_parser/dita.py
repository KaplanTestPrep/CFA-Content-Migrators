import xmltodict
import json
from models import dita_model

class ditaParsing():

    def parseDitaFile(file_path):
            xmlList = []
            with open(file_path) as dita:
                    root = xmltodict.parse(dita.read())
                    if root != None:
                           return ditaParsing.parseQuestionItem(root["question"]["title"]["navtitle"],
                                                          root["question"]["questionGroup"]["questionItem"])

    def parseQuestionItem(tag_name, item_list):
        if item_list!=None:
            ditaObj = dita_model.dita()
            ditaObj.tag_name = tag_name
            for item in item_list:
                ditaObj.xml_list.append(item["@href"])
            return ditaObj