# 랭체인으로 LLM 기반의 AI 서비스 개발하기
# 챗봇 만들기

## 새 가상환경 생성
python -m venv .venv
### 가상환경 활성화 (Windows)
.venv\Scripts\activate
### 가상환경 활성화 (Mac/Linux)
source .venv/bin/activate

## 패키지 설치
### install
`pip install langchain==0.0.350`
`pip install streamlit==1.29.0`

openai 대신
`pip install langchain_upstage`

.env 파일 로드
`pip install python-dotenv`

### run
`streamlit run main.py`