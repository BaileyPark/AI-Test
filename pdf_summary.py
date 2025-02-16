import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain import FAISS
from langchain_community.chat_models.solar import SolarChat
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv
# .env 파일 로드
load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")

def process_text(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    documents = FAISS.from_texts(chunks, embeddings)
    return documents

def main():
    st.title("PDF 요약하기")
    st.divider()

    pdf = st.file_uploader('PDF파일을 업로드해주세요', type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = "" # 텍스트 변수에 PDF 내용을 저장
        for page in pdf_reader.pages:
            text += page.extract_text()

        documents = process_text(text)
        query = "업로드된 PDF 파일의 내용을 약 3~5문장으로 요약해주세요." #LLM에게 요약 요청

        if query:
            docs = documents.similarity_search(query)
            llm = SolarChat(model="solar-1-mini-chat", solar_api_key=api_key)
            chain = load_qa_chain(llm, chain_type="stuff")

            with get_openai_callback() as cost:
                response = chain.run(input_documents=docs, question=query)
                print(cost)

            st.subheader('--요약 결과--')
            st.write(response)

if __name__ == '__main__':
    main()




