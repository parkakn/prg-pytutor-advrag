# MIT Media Lab PRG - PyTutor

### Advanced Retrieval-Augmented Generation (RAG) with PDF Parsing using Multi-modal LLMs
Most documents are complex in that they include more than simple text; they include embedded documents such as tables, flowcharts, and figures. Conducting RAG over these complex documents require a sophisticated pipeline for data ingestion; the more accurate our stored data is, the more accurate the results from using RAG to expand a foundational model's knowledge of external data. 

Here, we provide a full data parsing pipeline, including parsing complex '.docx' and '.pdf' files to markdown format, chunking the document content, and serializing the contents for preparation for ingesting them into a database. 

#### Integration in PyTutor: [Slides](https://docs.google.com/presentation/d/1HD9Y2iA3lpsQaG8oD6beoHUR442n1fZ90REQL61qUe8/edit?usp=sharing)


---
### Demos:
* **Parsing**: `parse_documents.ipynb` 
* **Chunking and Serializing**: `RAG_Pipeline_Standardized.ipynb`

### Key Features

- **Supported Document Types**: Supports documents of `.docx` and `.pdf` formats with embedded tables and flowcharts
- **Conversion to Markdown Format**: Converts document content into Markdown format, optimized for integration with Large Language Models.
- **Multi-Modal LLM**: Leverages different choices of Multi-modal LLMs for parsing.


---
#### Clone the Repository:
   ```bash
   git clone https://github.com/your-username/mitmedialab-pytutor-rag.git