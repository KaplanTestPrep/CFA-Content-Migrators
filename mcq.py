import xmltodict
import json
import pprint
import mcqData

from collections import OrderedDict 
def transformmcq():
    with open("cfaL1_question_00002_221.xml") as fd:
        doc = xmltodict.parse(fd.read())
    if doc != None :
       print('responseDeclaration:', doc['assessmentItem']['responseDeclaration']['@cardinality'])
    
    test = doc['assessmentItem']['responseDeclaration']['correctResponse'] 
    data = OrderedDict()
    data = test
    testdata = mcqData.MCQ()
    testdata.author ="Satish"
    for key, value in data.items():
        print(key, value) 
transformmcq()