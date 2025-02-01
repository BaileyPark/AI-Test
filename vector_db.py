# from langchain.document_loaders import TextLoader # ❌ 최신 버전과 호환되지 않음
from langchain_community.document_loaders import TextLoader # ✅ 최신 버전에서 올바른 경로

# documents = TextLoader("C:/Users/qkrdu/PycharmProjects/AI-Test/AI.txt").load()
documents = TextLoader("/Users/pyj/Downloads/AI-Test/AI.txt").load()


from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

docs = split_docs(documents)

# from langchain.embeddings import SentenceTransformerEmbeddings # ❌ 최신 버전과 호환되지 않음
from langchain_community.embeddings import SentenceTransformerEmbeddings # ✅ 최신 버전에서 올바른 경로
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Chromadb에 벡터 저장
# from langchain.vectorstores import Chroma # ❌ 최신 버전과 호환되지 않음
from langchain_community.vectorstores import Chroma # ✅ 최신 버전에서 올바른 경로
db = Chroma.from_documents(docs, embeddings)

import os
api_key = os.getenv("UPSTAGE_API_KEY")

# from langchain_community.chat_models import ChatUpstage # ❌ 최신 버전과 호환되지 않음
from langchain_community.chat_models.solar import SolarChat # ✅ 최신 버전에서 올바른 경로

# llm = ChatUpstage(model_name="solar-pro", upstage_api_key=api_key, upstage_api_base="https://api.upstage.ai/v1/solar", temperature=0)
llm = SolarChat(model="solar-1-mini-chat", solar_api_key=api_key)

from langchain.chains.question_answering import load_qa_chain
chain = load_qa_chain(llm, chain_type="stuff", verbose=True)

query = "AI란?"
metching_docs = db.similarity_search(query)
answer = chain.run(input_documents=metching_docs, question=query)
print(answer)