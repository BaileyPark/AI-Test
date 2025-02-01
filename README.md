# 랭체인으로 LLM 기반의 AI 서비스 개발하기

## 새 가상환경 생성
`python -m venv .venv`

### 가상환경 활성화 (Windows)
`.venv\Scripts\activate`
### 가상환경 활성화 (Mac/Linux)
`source .venv/bin/activate`

---
# 챗봇 만들기

## 패키지 설치
### install
`pip install langchain`
`pip install streamlit`

openai 대신 upstage (공통)

~~`pip install langchain_upstage`~~

`pip install langchain_community`

.env 파일 로드 (공통)

`pip install python-dotenv`

### run
`streamlit run main.py`

---
# RAG 기반의 챗봇 만들기

## 패키지 설치
### install

`pip install unstructured`

크로마DB 설치
`pip install chromadb`

SentenceTransformerEmbeddings
`pip install sentence-transformers`

openai도 설치 필요
`pip install openai`

25/01/28을 기준으로 langchain_community가 릴리스되어 안되는 게 많아 변경을 많이 요함
25/01/29을 기준으로 langchain가 릴리스되어 안되는 게 많아 변경을 많이 요함

`# from langchain.document_loaders import TextLoader # ❌ 최신 버전과 호환되지 않음
from langchain_community.document_loaders import TextLoader # ✅ 최신 버전에서 올바른 경로`

`# from langchain.embeddings import SentenceTransformerEmbeddings # ❌ 최신 버전과 호환되지 않음
from langchain_community.embeddings import SentenceTransformerEmbeddings # ✅ 최신 버전에서 올바른 경로`

`# from langchain.vectorstores import Chroma # ❌ 최신 버전과 호환되지 않음
from langchain_community.vectorstores import Chroma # ✅ 최신 버전에서 올바른 경로`

`# from langchain_community.chat_models import ChatUpstage # ❌ 최신 버전과 호환되지 않음
from langchain_community.chat_models.solar import SolarChat # ✅ 최신 버전에서 올바른 경로`
