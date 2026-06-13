 
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
