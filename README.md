# rag-text-splitter
 In this repo, I explored text splitting techniques to process large documents effectively for downstream tasks like question answering, summarization, or semantic search. Here's what I learned and what the key files contribute:


✅ Purpose of the Repo
To experiment with text splitting strategies using Python and LangChain-style logic, helping to chunk long documents into manageable pieces while preserving semantic meaning.

🗂️ Key Files & What I Learned
length_based.py
🔹 Implements Length-based Splitter, which breaks text into chunks based on character or token length.
🔹 Helps in handling context limits of LLMs.

text_structure_based.py
🔹 Uses document structure (headings, paragraphs, etc.) for splitting.
🔹 Preserves semantic integrity by splitting at logical boundaries.

markdown.py
🔹 Parses and splits Markdown documents efficiently.
🔹 Handles heading levels and sections to keep context intact.
python_code.py
🔹 Designed to split Python code files intelligently.
🔹 Maintains code block integrity and function-level chunks.
