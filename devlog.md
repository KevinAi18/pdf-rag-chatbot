 
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
 
## 2026-06-21 
### Hybrid Search Implementation Notes 
- Hybrid search combines dense vector search with BM25 keyword search 
- Dense search handles semantic meaning and context understanding 
- BM25 handles exact keyword matches and rare technical terms 
- RRF algorithm merges ranked results from both search methods 
 
## 2026-06-24 
### PDF Table of Contents Parsing Notes 
- TOC extraction helps structure document for better chunking 
- PyMuPDF extracts TOC with page numbers and heading hierarchy 
- TOC used to split PDF into logical sections before chunking 
- Section aware chunking improves retrieval precision in RAG 
 
## 2026-06-24 
### PDF Table of Contents Parsing Notes 
- TOC extraction helps structure document for better chunking 
- PyMuPDF extracts TOC with page numbers and heading hierarchy 
- TOC used to split PDF into logical sections before chunking 
- Section aware chunking improves retrieval precision in RAG 
 
## 2026-06-26 
### Citation Generation in RAG Notes 
- Citations link generated answer back to source document chunks 
- Chunk metadata stores page number and source file for tracing 
- LLM prompted to include chunk id when generating final answer 
- Citations improve trust and let users verify chatbot answers 
 
## 2026-06-28 
### Query Rewriting in RAG Notes 
- Query rewriting clarifies ambiguous or incomplete user questions 
- LLM rephrases query using conversation history for better context 
- Multi-query generation creates several variations for broader search 
- Improves retrieval recall especially for follow up questions 
 
## 2026-07-01 
### Handling Scanned PDFs Notes 
- Scanned PDFs contain images of text not selectable text content 
- Tesseract OCR used to extract text from scanned document images 
- PaddleOCR tested as alternative with better accuracy on tables 
- Preprocessing with deskew and denoise improves OCR accuracy 
 
## 2026-07-03 
### Document Versioning in RAG Notes 
- Document versioning tracks updates to source PDFs over time 
- Old embeddings invalidated and replaced when document is updated 
- Version metadata stored alongside chunks for audit trail 
- Helps avoid serving outdated information from stale documents 
