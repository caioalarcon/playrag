# PlayRAG

A simple Retrieval-Augmented Generation (RAG) API built with FastAPI, LangChain, FAISS, and AWS S3.

## Features

- FastAPI endpoint for question answering
- LangChain's RetrievalQA with FAISS vector store and HuggingFace embeddings
- Automatic download of FAISS index from AWS S3
- Easy local or containerized deployment with Docker

## Prerequisites

- Python 3.11+
- AWS credentials with access to the S3 bucket containing the FAISS index

## Environment Variables

| Name                  | Description                                         |
| --------------------- | --------------------------------------------------- |
| AWS_ACCESS_KEY_ID     | Your AWS access key ID                              |
| AWS_SECRET_ACCESS_KEY | Your AWS secret access key                          |
| AWS_S3_BUCKET         | S3 bucket name where the FAISS index is stored      |
| AWS_S3_INDEX_KEY      | S3 object key (path) for the FAISS index file       |

Copy `.env.example` to `.env` and fill in your credentials.

## Installation

```bash
git clone <repository-url>
cd playrag
cp .env.example .env
pip install --no-cache-dir -r requirements.txt
```

## Running Locally

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

## API Usage

### GET /ask

Endpoint to ask a question to the RAG system.

| Query Parameter | Type   | Description         |
| --------------- | ------ | ------------------- |
| question        | string | Question to RAG API |

**Example Request:**

```bash
curl "http://localhost:8000/ask?question=What%20is%20LangChain?"
```

**Response:**

```json
{"answer": "LangChain is a framework for building applications powered by language models..."}
```

## Docker

Build and run with Docker:

```bash
docker build -t playrag .
docker run --env-file .env -p 8000:8000 playrag
```

## Index Management

The FAISS index is downloaded automatically from S3 on startup if not found locally at `faiss_store/local.index`.
To upload or update the index, use the `upload_index` function in `app/utils/s3.py`.

## Index Creation Boilerplate

A sample boilerplate for creating the FAISS index is provided in `rag_playground_boilerplate.zip`. Unzip and follow the instructions inside to split documents, generate embeddings, build your FAISS store, and upload it to S3.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.