import openai 
import os 
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("API-KEY")

def create_question(string): 
    response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "There is a relation Question --> Answer, I am providing you the answer, give me a the question"},
            {"role": "user", "content": string}])
    return response['choices'][0]['message']['content']

if __name__ == "__main__": 
    print(create_question("print(\"Helo World\")"))
