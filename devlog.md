 
## 2026-06-13 
### PDF Chunking Strategies 
- Semantic chunking splits based on meaning not character count 
- Recursive character splitter best for general PDF text 
- 10-20 percent overlap between chunks reduces context loss 
- Next: benchmark chunking strategies on sample PDF 
 
## 2026-06-14 
### FastAPI Backend Structure for RAG 
- FastAPI chosen for async support and automatic docs generation 
- Endpoints: /upload, /query, /history for core chatbot features 
- Pydantic models used for request and response validation 
- Background tasks handle PDF processing without blocking API 
 
## 2026-06-16 
### Streamlit Frontend Integration Notes 
- Streamlit used for rapid UI development for RAG chatbot 
- st.file_uploader handles PDF uploads from browser 
- st.chat_message renders user and assistant bubbles cleanly 
- Session state stores chat history across multiple queries 
 
## 2026-06-19 
### Memory Management in RAG Chatbot 
- Conversation memory stores previous QA pairs for context 
- Buffer memory keeps last N messages to avoid token overflow 
- Summary memory compresses old turns into short summary 
- LangChain ConversationBufferWindowMemory used for implementation 
