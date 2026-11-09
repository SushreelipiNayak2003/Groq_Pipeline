from llm import MODEL
from prompting import TEMPLATE_PROMPT
from Filter import PARSERS
from dotenv import load_dotenv
import os

load_dotenv()

model = os.getenv("GROQ_MODEL")
api_key = os.getenv("GROQ_APIKEY")
temp = float(os.getenv("QWEN_TEMP"))
template = os.getenv("GROQ_TEMPLATE")

llm_model = MODEL(model, api_key, temp).Groq_model()
prompt = TEMPLATE_PROMPT(template).PROMPT()
parser = PARSERS().OUTPARSER()

# Correct order: Prompt → LLM → Parser
chain = prompt | llm_model | parser

response = chain.invoke({
    "number": 5,
    "topic": "Python"
})

print(response)