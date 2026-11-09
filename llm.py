
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

class MODEL:
    def __init__(self, model_name, api_key, temp):
        self.model_name = model_name
        self.api_key = api_key
        self.temp = float(temp)

    def Groq_model(self):
        llm_model = ChatGroq(
            model=self.model_name,
            api_key=self.api_key,
            temperature=self.temp
        )
        return llm_model


if __name__ == "__main__":
    model = os.getenv("GROQ_MODEL")
    api_key = os.getenv("GROQ_APIKEY")
    temp = os.getenv("QWEN_TEMP")

    if not all([model, api_key, temp]):
        raise ValueError("Check GROQ_MODEL, GROQ_APIKEY, and QWEN_TEMP in .env")

    llm_model = MODEL(model, api_key, temp).Groq_model()
    print("Groq model initialized successfully!")
