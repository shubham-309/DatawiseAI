import os
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

# Initialize Pinecone
Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
print("Pinecone initialized")

def ingest_docs(directory):
    INDEX_NAME = os.getenv("INDEX_NAME")
    print("Loading Docs")
    print(directory)

    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                documents.append(Document(page_content=content, metadata={"filename": filename}))
    
    print(f"Loaded {len(documents)} documents")


    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=2000)
    split_documents = text_splitter.split_documents(documents=documents)
    print(f"Split into {len(split_documents)} chunks")

    print(f"Going to add {len(split_documents)} to Pinecone")
    embeddings = OpenAIEmbeddings()
    PineconeVectorStore.from_documents(documents=split_documents, embedding=embeddings, index_name=INDEX_NAME)

    print("**** Loading to vector store done ****")

# Set environment variables and ingest data into Pinecone
if __name__ == "__main__":
    ingest_docs("/Preprocessed_data")
