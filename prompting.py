from langchain_core.prompts import PromptTemplate

class TEMPLATE_PROMPT:
    def __init__(self, template):
        self.template = template

    def PROMPT(self):
        prompt = PromptTemplate.from_template(self.template)
        return prompt