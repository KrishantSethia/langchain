from langchain.llms.openai import OpenAI

result = OpenAI(openai_api_key="your api key").predict("what is github")
