"""Example script for querying the PDF RAG chatbot.""" 
 
import requests 
 
def ask_question(question): 
    response = requests.post("http://localhost:8000/query", json={"question": question}) 
    return response.json() 
 
if __name__ == "__main__": 
    result = ask_question("What is the main topic of this document?") 
    print(result) 
