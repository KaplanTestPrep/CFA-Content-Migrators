import xmltodict
import json
import pprint
import mcqData
# import yaml

from collections import OrderedDict

def bindStaticFields():
    with open('config.json') as config:
        data = json.load(config)
        #print(data['author_name'])

def transformmcq():
    bindStaticFields()
    
    with open("cfaL1_question_00002_221.xml") as fd:
        doc = xmltodict.parse(fd.read())
    if doc != None :
       print('responseDeclaration:', doc['assessmentItem']['responseDeclaration']['@cardinality'])
    
    test = doc['assessmentItem']['responseDeclaration']['correctResponse'] 
    data = OrderedDict()
    data = test

    # with open("config.yml", "r") as ymlfile:f
    #     cfg =  yaml.load(ymlfile)
    #     for section in cfg:
    #         print(section)


    pythonObj = mcqData.MCQ()
    jsonString = tojson(pythonObj)
    print('Test')
    for key, value in data.items():
        print(key, value) 

def tojson(py):
    return json.dumps(py, default=lambda o:o.__dict__,sort_keys=True, indent=4)
transformmcq()

