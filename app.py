import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
from chatbot import chat_model

st.title("LLM Powered Chatbot")

st.header("Hello There! I am JARVIS. How can i help you today.")


def load_model():

    return chat_model()

model = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content = "You are a helpful and polite AI assistant.")
    ]


for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user: "):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("AI: "):
            st.markdown(message.content)


if user_input := st.chat_input("Type your message here....."):

    with st.chat_message("user: "):
        st.markdown(user_input)


    st.session_state.messages.append(HumanMessage(content = user_input))

    with st.chat_message("AI: "):

        with st.spinner("Thinking......"):

            try:

                result = model.invoke(st.session_state.messages)
                st.markdown(result.content)

                st.session_state.messages.append(result)

            except Exception as e:

                st.error(f"an error occured: {e}")

