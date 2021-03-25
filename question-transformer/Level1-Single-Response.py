import xmltodict
import json
import pprint
from pathlib import Path

from models import MaestroSchema
from models import DitaMap-Model
from collections import OrderedDict

def parseDitamap():
        base_path = Path(__file__).parent
        file_path = (base_path / "sampleFiles/mcqFiles/toc.ditamap").resolve()
        with open(file_path) as ditamap:
                doc = xmltodict.parse(ditamap.read())
                if doc!=None:
                        data = 


parseDitamap()