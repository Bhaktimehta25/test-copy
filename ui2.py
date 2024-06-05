import streamlit as st
from pydantic import BaseModel
from typing import List
from helpers import structured_generator
import json

# Define the Pydantic model to structure the expected output
class Answers(BaseModel):
    Name: List[str]

# Set the title of the Streamlit app
st.title("Dish Ideas Generator")

# Set a description for the app
st.write("This app generates dish ideas based on provided cuisine and ingredients.Fill in the ingredients and cuisine type, then press 'Generate Dish Ideas' to see the suggestions")

# Create input fields for the user to enter the required ingredients and cuisine type
input1 = st.text_input("Enter the first ingredient Fiber (e.g., Brocolli)", "Brocolli")
input2 = st.text_input("Enter the second ingredient Base Carbs: (e.g., Rice)", "Rice")
input3 = st.text_input("Enter the third ingredient Protein (e.g., Beans)", "Soya")
input4 = st.text_input("Enter the fourth ingredient (optional)", "")
input5 = st.text_input("Enter the type of cuisine (e.g., Mexican)", "Mexican")

# When the user presses the button, generate the prompt and get the results
if st.button("Generate Dish Ideas"):
    # Construct the prompt using the provided inputs
    prompt = f"Share 5 dishes ideas of {input5} cuisine with following ingredients, {input1}, {input2}, {input3},{input4}"

    # Define the model to be used (for example, OpenAI's GPT-4)
    openai_model = "gpt-4"

    # Call the structured_generator function with the model, prompt, and expected output structure
    result = structured_generator(openai_model, prompt, Answers)

    # Display the result in the Streamlit app
    st.write("Generated Dish Ideas:")
    for dish in result.Name:
        st.write(f"- {dish}")
