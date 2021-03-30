import xmltodict
import json
import pprint

import models.MaestroSchema as myModule
from xmlParser import ditamap
from models import MaestroSchema
from models import DitaMapModel

from collections import OrderedDict
from pathlib import Path


def TestDitaMap():
        base_path = Path(__file__).parent
        file_path = (base_path / "sampleFiles/mcqFiles/toc.ditamap").resolve()
        ditafile_list = ditamap.ditamapParsing.parseDitamap(file_path)
        data=""
TestDitaMap()
