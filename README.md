Project Setup Guide

Setting Up the Backend (Flask):

Install the required packages:

pip install -r requirements.txt

Run the Flask server:
python app.py

Setting Up the Frontend (React):

Navigate to the frontend directory:

Install the dependencies:
npm install

Start the React development server:
npm run dev

Testing the Setup:
Open your browser and go to http://localhost:3000 to interact with the chatbot.

Configure Environment Variables:
Create a .env file in the root directory of the backend project and add OPENAI API KEY, PINECONE API KEY, PINECONE INDEX NAME in the environment variable.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

To ingest documents to Pinecone, follow these steps:

Create a Pinecone Account and API Key:
- Sign up for a Pinecone account at Pinecone.
- Navigate to the API key section in your Pinecone dashboard to generate an API key.

Create an Index:
- In the Pinecone dashboard, create a new index. Take note of the index name as you'll need it later.
- Set Up Environment Variables:

Create a .env file in your project directory.
- Add your Pinecone API key and index name to the .env file:
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name

Run Ingestion Script:
- Ensure you have a script named ingestion.py in your backend directory. This script should handle creating chunks, generating vectors, and ingesting data into your Pinecone vector index.
- Run the script using the command:
python ingestion.py


Enjoy Using AI:

Your setup is now complete, and you can start leveraging RAG for data retrieval.
Happy coding!
