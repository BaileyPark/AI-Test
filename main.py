import streamlit as st
from langchain_upstage import ChatUpstage
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
st.set_page_config(page_title="뭐든지 질문하세요!")
st.title('뭐든지 질문하세요~')

# .env 파일 로드
load_dotenv()

import os
api_key = os.getenv("UPSTAGE_API_KEY")

def generate_response(input_text):
    llm = ChatUpstage(model_name="solar-pro", upstage_api_key=api_key, upstage_api_base="https://api.upstage.ai/v1/solar", temperature=0)
    message = [HumanMessage(content=input_text)]  # ✅ HumanMessage 객체로 Wrapping
    response = llm(message)  # ✅ 올바른 형식으로 전달

    st.info(response)
    # st.info(llm(input_text))

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?')
    submitted = st.form_submit_button('보내기')
    generate_response(text)