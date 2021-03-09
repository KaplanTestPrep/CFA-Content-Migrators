class MCQ():
    def __init__(self):
        self.author = "alexandra.leever@kaplan.com"
        self.content = Content()

class Content:
    def __init__(self):
        self.active = True
        self.created_at = "9 Mar 2021"
        self.id = "22bf75a8-a3eb-4f62-bd31-8cbfc4f21024" #TBD
        self.items = []

class Items:
    def __init__(self):
        self.active = True
        self.created_at = "9 Mar 2021"
        self.default_value = None
        self.id = "808d7b31-6750-4992-a00f-cfa61679c457"
        self.interactions = Interactions()
        self.explanations = []
        self.kaplan_type = "question"
        self.max_score = None
        self.metadata = None
        self.min_score = None
        self.name = "m001040" #TBD
        self.parent = "22bf75a8-a3eb-4f62-bd31-8cbfc4f21024"
        self.position = 0
        self.recommended_time = 0
        self.schema = "2.0"
        self.stem = "" #Question text
        

class Explanations():
    def __init__(self):
        self.active = True
        self.content = "" #Explanation text
        self.created_at = "9 Mar 2021"
        self.id = "6623beed-9418-46fd-ad2a-bdce285d03cc" #TBD
        self.kaplan_type = "feedback"
        self.metadata = None
        self.name = "m001040-explanation-0" #TBD
        self.parent = "808d7b31-6750-4992-a00f-cfa61679c457" #TBD
        self.position = 0 #TBD
        self.recommended_time = None
        self.schema = "2.0"
        self.title = "Explanation"
        self.updated_at = "9 Mar 2021"

class Interactions():
    def __init__(self):
        self.interactions = m001040_interaction_1()

class m001040_interaction_1():
    def __init__(self):
        self.active = True
        self.case_sensitive = False
        self.created_at = "9 Mar 2021"
        self.default_value = None
        self.display_type = "single-response"
        self.expected_length = None
        self.id = "2cc7c480-7e63-432b-b1ce-522c08d448b6"
        self.interaction_type = "choice-interaction"
        self.kaplan_type = "interaction"
        self.max_choices = 1
        self.max_length = None
        self.max_score = None
        self.metadata = None
        self.min_score = None
        self.name = "m001040_interaction_1" #TBD
        self.parent = "808d7b31-6750-4992-a00f-cfa61679c457"
        self.position = 0
        self.recommended_time = None
        self.schema = "2.0"
        self.updated_at = "9 Mar 2021"
        self.response_options = []

class ResponseOptions():
    def __init__(self):
        self.active = True
        self.content = ""
        self.created_at = "9 Mar 2021"
        self.id = ""
        self.kaplan_type = "response-option"
        self.metadata = None
        self.name = "m001040-interaction-1-option-1"
        self.parent = "2cc7c480-7e63-432b-b1ce-522c08d448b6"
        self.position = 0
        self.recommended_time = None
        self.schema = "2.0"
        self.set = None
        self.updated_at = "9 Mar 2021"
        self.value = None