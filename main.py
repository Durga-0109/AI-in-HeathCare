from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="tinyllama")

template = """
* never tell me to  consult a doctor
You are a confident exeprt in diagnosing diseases
based on my age gender and symptoms find my desease and suitable medication for me

Here are some relevant knowledge {reviews}

Here is the question to answer: {question}

strict output format
Predicted Disease:()
Personalized Medication:()
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

print("Enter Patient Details")
age = input("Enter Patient Age: ")
Gender = input("Enter Patient Gender: ")
symptoms = input("Enter Patient Symptoms: ")

question = (f"Age = {age}, Gender = {Gender}, symptoms = {symptoms}")
print(question)
reviews = retriever.invoke(question)

result = chain.invoke({"reviews": reviews, "question": question})
print(result)