from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
doc = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 0,
    separator=" "
)

res = splitter.split_documents(doc)

print(res[0])