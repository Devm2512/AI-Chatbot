from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate

load_dotenv()

def chat_model():
    llm = HuggingFaceEndpoint(
        repo_id = "meta-llama/Llama-3.1-8B-Instruct",
        task = "text-generation",
        max_new_tokens = 512
    )
    return ChatHuggingFace(llm=llm, model_id="mistralai/Mistral-7B-Instruct-v0.3")
