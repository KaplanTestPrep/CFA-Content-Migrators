class mcq():
    def __init__(self):
        self.author = ""
        self.content = content()
        self.id = ""
        self.internal_reference = ""
        self.item_id = ""
        self.item_name = ""
        self.message = ""
        self.metadata = ""
        self.organizations = ""
        self.project_id = ""
        self.project_name = ""
        self.publishing_author = ""
        self.publishing_status = ""
        self.reference = ""
        self.tenant_id = ""
        self.url = ""
        self.created_at = ""
        self.updated_at = ""

class content():
    def __init__(self):
        self.active = ""
        self.created_at = ""
        self.id = ""
        self.items = []
        self.kaplan_type = ""
        self.metadata = ""
        self.name = ""
        self.position = ""
        self.recommended_time = ""
        self.schema = ""
        self.tags = [] #same as Items tags
        self.updated_at = ""

class items():
    def __init__(self):
        self.active = ""
        self.created_at = ""
        self.default_value = ""
        self.id = ""
        self.interactions = ""
        self.explanations = []
        self.kaplan_type = ""
        self.max_score = ""
        self.metadata = ""
        self.min_score = ""
        self.name = "" 
        self.parent = ""
        self.position = ""
        self.recommended_time = ""
        self.schema = ""
        self.stem = "" #Question text
        self.tags =[]
        self.updated_at = ""

class explanations():
    def __init__(self):
        self.active = "True"
        self.content = "" #Explanation text
        self.created_at = ""
        self.id = ""
        self.kaplan_type = ""
        self.metadata = ""
        self.name = "" 
        self.parent = ""
        self.position = ""
        self.recommended_time = ""
        self.schema = ""
        self.title = ""
        self.updated_at = ""

class interactions():
    def __init__(self):
        self.m001040_interaction_1 = interaction()

class interaction():
    def __init__(self):
        self.active = ""
        self.case_sensitive = ""
        self.created_at = ""
        self.default_value = ""
        self.display_type = ""
        self.expected_length = ""
        self.id = ""
        self.interaction_type = ""
        self.kaplan_type = ""
        self.max_choices = ""
        self.max_length = ""
        self.max_score = ""
        self.metadata = ""
        self.min_score = ""
        self.name = ""
        self.parent = ""
        self.position = ""
        self.recommended_time = ""
        self.schema = ""
        self.updated_at = ""
        self.response_options = []

class responseOptions():
    def __init__(self):
        self.active = ""
        self.content = ""
        self.created_at = ""
        self.id = ""
        self.kaplan_type = ""
        self.metadata = ""
        self.name = ""
        self.parent = ""
        self.position = ""
        self.recommended_time = ""
        self.schema = ""
        self.set = ""
        self.updated_at = ""
        self.value = ""

class tag():
    def __init__(self):
        self.created_at = ""
        self.id = ""
        self.name = ""
        self.tag_type = ""
        self.tenant_id = ""
        self.title = ""
        self.updated_at = ""