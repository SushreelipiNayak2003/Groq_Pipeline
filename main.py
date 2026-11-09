from dotenv import load_dotenv
print(load_dotenv())

import os
model=os.getenv('GROQ_MODEL')
print(model)