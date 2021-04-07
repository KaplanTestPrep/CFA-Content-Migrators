import xmltodict
import json
import pprint
import default_maestro_schema


from xml_parser import ditamap
from xml_parser import dita
from xml_parser import xml_parse
from models import maestro_schema
from collections import OrderedDict
from pathlib import Path

base_path = (Path(__file__).parent / "sampleFiles/mcqFiles/").resolve()
ditamap_file_path = (base_path / "toc.ditamap").resolve()

def parse_samc():
        xml_tag_list = get_xml_list()
        if xml_tag_list!=None and len(xml_tag_list)>0:
                for xml_tag in xml_tag_list:
                        for xml in xml_tag.xml_list:
                                xml_parse.xml.parse(base_path/"questions"/xml, xml_tag.tag_name)

def get_xml_list():
        xml_list = []
        ditafile_list = ditamap.ditamapParsing.parseDitamap(ditamap_file_path)
        if ditafile_list !=None and len(ditafile_list)>0:
                for ditaFile in ditafile_list:
                        ditaObj = dita.ditaParsing.parseDitaFile((base_path/ditaFile).resolve())
                        xml_list.append(ditaObj)
        return xml_list


parse_samc()
