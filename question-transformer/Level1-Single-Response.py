import xmltodict
import json
import pprint
from pathlib import Path
from lxml import etree
import xml.etree.ElementTree as ET

from models import MaestroSchema
from models import DitaMapModel
from collections import OrderedDict

def parseDitamap():
        ditaList = []
        base_path = Path(__file__).parent
        file_path = (base_path / "sampleFiles/mcqFiles/toc.ditamap").resolve()
        deserializer = XML2Py()
        pyObject = deserializer.parse(file_path)
        with open(file_path) as ditamap:
                mapTopicHead = xmltodict.parse(ditamap.read())
                object = json.dumps(mapTopicHead)
                if mapTopicHead != None:
                        taxonomy1List = mapTopicHead["map"]["topichead"]
                        if taxonomy1List != None and len(taxonomy1List) > 0:
                                for taxonomy1 in taxonomy1List:
                                        taxonomy2List = taxonomy1["topichead"]
                                        if taxonomy2List != None and len(taxonomy2List) > 0:
                                                if taxonomy2List.__contains__("@navtitle"):
                                                        data  = ""
                                                else:
                                                        for taxonomy2 in taxonomy2List:
                                                                taxonomy3List = taxonomy2["topichead"]
                                                                if taxonomy3List !=None and len(taxonomy3List) > 0:
                                                                        for taxonomy3 in taxonomy3List:
                                                                                ditaFileList = taxonomy3["topicref"]
                                                                                if ditaFileList != None and len(ditaFileList)>0:
                                                                                        for file in ditaFileList:
                                                                                                ditaList.append(file["@href"])

                                                                                
# def parseTaxonomy3(taxonomy3List):

def deserialize(xml_bytes: bytes) -> etree.ElementTree:
    """
    Deserializes an XML bytestream, in the context of an XSD.
    :param xml_bytes: XML document, which may specify encoding
    :param xsd_path: path to XSD on local disk
    :return: deserialized ElementTree
    """
    base_path = Path(__file__).parent
    file_path = (base_path / "sampleFiles/mcqFiles/toc.xml").resolve()
    xsd_path = file_path

    with open(xsd_path) as xsd_file:
        schema = etree.XMLSchema(etree.parse(xsd_file))

    deserialized = etree.fromstring(xml_bytes)
    schema.assertValid(deserialized)
    
    return deserialized


deserialize("", )
parseDitamap()
