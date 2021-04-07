import yaml
import json
from datetime import datetime
from pathlib import Path
from models import maestro_schema

class default_maestro_values():

    def set_config_values():
        maestro = maestro_schema.mcq()
        cfg = default_maestro_values.read_yml_file()
        
        publish = cfg["publish"]
        maestro.author = publish["author_name"]
        maestro.internal_reference = publish["internal_reference"]
        maestro.message = publish["message"]
        maestro.metadata = publish["metadata"]
        maestro.organizations = publish["organizations"]
        maestro.project_id = publish["project_id"]
        maestro.project_name = publish["project_name"]
        maestro.publishing_author = publish["publishing_author"]
        maestro.publishing_status = publish["publishing_status"]
        maestro.reference = publish["reference"]
        maestro.tenant_id = publish["tenant_id"]

        maestro.content = default_maestro_values.get_content_values(cfg)
        #maestro.content.items = default_maestro_values.get_items_values(cfg)
        #maestro.content.items.explanations = default_maestro_values.get_explanations_values(cfg)
        #maestro.content.items.interactions = default_maestro_values.get_interactions_values(cfg)
        #maestro.content.items.interactions.response_options = default_maestro_values.get_response_options_values(cfg)

        return maestro
    
    def get_content_values(cfg):
        contentObj = cfg["content"]
        content = maestro_schema.content()
        content.active = contentObj["active"]
        content.kaplan_type = contentObj["kaplan_type"]
        content.metadata = contentObj["metadata"]
        content.recommended_time = contentObj["recommended_time"]
        content.schema = contentObj["schema"]
        return content

    def get_items_values():
        cfg = default_maestro_values.read_yml_file()
        itemsObj = cfg["items"]
        items = maestro_schema.items()
        items.active = itemsObj["active"]
        items.created_at = default_maestro_values.get_current_date_time()
        items.default_value = itemsObj["default_value"]
        items.kaplan_type = itemsObj["kaplan_type"]
        items.max_score = itemsObj["max_score"]
        items.metadata = itemsObj["metadata"]
        items.min_score = itemsObj["min_score"]
        items.position = 0
        items.recommended_time = itemsObj["recommended_time"]
        items.schema = itemsObj["schema"]
        items.updated_at = default_maestro_values.get_current_date_time()
        return items

    def get_explanations_values():
        cfg = default_maestro_values.read_yml_file()
        explanation_obj = cfg["explanation"]
        explanation = maestro_schema.explanations()
        explanation.created_at = default_maestro_values.get_current_date_time()
        explanation.active = explanation_obj["active"]
        explanation.kaplan_type = explanation_obj["kaplan_type"]
        explanation.metadata = explanation_obj["metadata"]
        explanation.recommended_time = explanation_obj["recommended_time"]
        explanation.schema = explanation_obj["schema"]
        explanation.title = explanation_obj["title"]
        return explanation

    def get_interaction_values():
        cfg = default_maestro_values.read_yml_file()
        interactions_obj = cfg["interactions"]
        interaction = maestro_schema.interaction()
        interaction.active = interactions_obj["active"]
        interaction.created_at = default_maestro_values.get_current_date_time()
        interaction.case_sensitive = interactions_obj["case_sensitive"]
        interaction.default_value = interactions_obj["default_value"]
        interaction.display_type = interactions_obj["display_type"]
        interaction.expected_length = interactions_obj["expected_length"]
        interaction.interaction_type = interactions_obj["interaction_type"]
        interaction.kaplan_type = interactions_obj["kaplan_type"]
        interaction.max_choices = interactions_obj["max_choices"]
        interaction.max_length = interactions_obj["max_length"]
        interaction.max_score = interactions_obj["max_score"]
        interaction.metadata = interactions_obj["metadata"]
        interaction.min_score = interactions_obj["min_score"]
        interaction.position = 0
        interaction.recommended_time = interactions_obj["recommended_time"]
        interaction.schema = interactions_obj["schema"]
        interaction.updated_at = default_maestro_values.get_current_date_time()
        return interaction

    def get_response_options_values():
        cfg = default_maestro_values.read_yml_file()
        response_options_obj = cfg["response_options"]
        response_options = maestro_schema.responseOptions()
        response_options.active = response_options_obj["active"]
        response_options.created_at = default_maestro_values.get_current_date_time()
        response_options.kaplan_type = response_options_obj["kaplan_type"]
        response_options.metadata = response_options_obj["metadata"]
        response_options.recommended_time = response_options_obj["recommended_time"]
        response_options.schema = response_options_obj["schema"]
        response_options.set = response_options_obj["set"]
        response_options.updated_at = default_maestro_values.get_current_date_time()
        response_options.value = response_options_obj["value"]
        return response_options

    def read_yml_file():
        cfg_values = ""
        base_path = Path(__file__).parent
        with open(base_path / "maestro_schema_config.yml", "r") as ymlfile:
            cfg_values = yaml.load(ymlfile)
        return cfg_values
    
    def get_current_date_time():
       now = datetime.now()
       dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
       return dt_string

        