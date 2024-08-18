# Project Setup Guide

This guide will walk you through setting up the backend (Flask) and frontend (React) and documenting ingestion for Pinecone.

## Setting Up the Backend (Flask)

### Install the required packages:
```bash
pip install -r requirements.txt
```
Run the Flask server:
```bash
python app.py
```

Setting Up the Frontend (React)

Navigate to the frontend directory:
cd frontend

Install the dependencies:
```bash
npm install
```

Start the React development server:
```bash
npm run dev
```

Testing the Setup
Once both the backend and frontend servers are running, open your browser and go to:
http://localhost:3000

Here, you can interact with the chatbot.

Configure Environment Variables
Backend Environment Variables:
Create a .env file in the root directory of the backend project and add the following keys:
```bash
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------


Ingesting Documents to Pinecone
Follow these steps to ingest documents into Pinecone.

1. Create a Pinecone Account and API Key:
Sign up for a Pinecone account at Pinecone.

Navigate to the API key section in your Pinecone dashboard to generate an API key.
3. Create an Index:
In the Pinecone dashboard, create a new index and take note of the index name.
4. Set Up Environment Variables:
Create a .env file in your project directory and add your Pinecone API key and index name:
```bsh
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name
```
4. Run the Ingestion Script:
Ensure you have a script named ingestion.py in your backend directory. This script should handle creating chunks, generating vectors, and ingesting data into your Pinecone vector index. Run the script using:

```bash
python ingestion.py
```

Enjoy Using AI
Your setup is complete, and you can leverage RAG for data retrieval.

Happy coding!
