import default_maestro_schema
import json
import xmltodict
from models import maestro_schema


class xml:
    def parse(xml_file, tag_name):
        maestro_schema.mcq = default_maestro_schema.default_maestro_values.set_config_values()
        maestro_schema.mcq = xml.parse_xml(xml_file, tag_name, maestro_schema.mcq)
        json_string = xml.tojson(maestro_schema.mcq)
        print(json_string)
    
    def parse_xml(xml_file, tag_name, schema):
        with open(xml_file) as xml_data:
                    root = xmltodict.parse(xml_data.read())
                    if root != None and root["assessmentItem"] != None:
                        schema.content.items = xml.read_items(root["assessmentItem"], tag_name)
                        schema.content.tags = xml.read_tags(tag_name)
        return schema
    
    def read_explanation(assessment_item):
        if assessment_item.__contains__("modalFeedback"):
            explanation_list = []
            explanation = default_maestro_schema.default_maestro_values.get_explanations_values()
            explanation.content = assessment_item["modalFeedback"]["p"]
            explanation_list.append(explanation)
            return explanation_list
            
        raise Exception("modalFeedback not found")

    def read_response_options(assessment_item):
        try:
            options_list = []
            list = assessment_item["itemBody"]["choiceInteraction"]["simpleChoice"]
            if list!=None and len(list)>0:
                counter = 0
                for option in list:
                    response_option = default_maestro_schema.default_maestro_values.get_response_options_values()
                    response_option.id= "TBD"
                    response_option.name = "TBD"
                    response_option.parent = "TBD"
                    response_option.stem= option["#text"]
                    response_option.position = counter
                    options_list.append(response_option)
                    counter+= 1
            return options_list
        except:
            raise Exception("Error in reading response options")

        return ""

    def read_interactions(assessment_item):
        obj = maestro_schema.interactions()
        obj.m001040_interaction_1 = default_maestro_schema.default_maestro_values.get_interaction_values()
        obj.m001040_interaction_1.response_options = xml.read_response_options(assessment_item)
        return obj

    def read_tags(tag_name):
        tag_list = []
        tag = maestro_schema.tag()
        tag.created_at = "TBD"
        tag.id= "TBD"
        tag.name = tag_name
        tag.tag_type = "TBD"
        tag.tenant_id = "TBD"
        tag.title = "TBD"
        tag.updated_at = "TBD"
        tag_list.append(tag)
        return tag_list

    def read_items(assessment_item, tag_name):
        items_list = []
        item = default_maestro_schema.default_maestro_values.get_items_values()
        item.explanations = xml.read_explanation(assessment_item)
        item.interactions = xml.read_interactions(assessment_item)
        item.tags = xml.read_tags(tag_name)
        item.id = "TBD"
        item.name = "TBD"
        item.parent = "TBD"
        if assessment_item["itemBody"] !=None:
            item.stem = assessment_item["itemBody"]["p"]
        items_list.append(item)
        return items_list

    def tojson(py):
        return json.dumps(py, default=lambda o:o.__dict__,sort_keys=True, indent=4)
