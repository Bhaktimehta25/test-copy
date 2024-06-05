from pydantic import BaseModel, ImportString
from typing import List
from helpers import structured_generator
import json

#Replace With Your Output
class Answers(BaseModel):
    Name: List[str]


#Replace with your input
input1 = "Fiber : Tomato"
input2 = "Base Carbs: Roti"
input3 = "Protein : Toor Dal"
input4= " "
input5 = "Gujarati"

#Replace with your prompt
prompt = f"Share 5 dishes ideas of {input5} cuisine with following ingredients, {input1}, {input2}, {input3},{input4} " 

#Replace With Your Model
openai_model = "gpt-4"

result = structured_generator(openai_model,prompt,Answers)
print(result.Name)  



