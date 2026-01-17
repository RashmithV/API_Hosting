
# Chatbot API

A FastAPI-based REST API that leverages the Cerebras cloud SDK to provide intelligent chat completions.

## Features

- FastAPI web framework for high-performance API endpoints
- Integration with Cerebras Cloud's GPT-OSS-120B model
- Streaming chat completions with configurable parameters
- Health check endpoint
- Docker containerization

## Prerequisites

- Python 3.11+
- Cerebras API key
- Docker (optional)

## Installation

1. Clone the repository
2. Create a `.env` file and add your Cerebras API key:
    ```
    CEREBRAS_API_KEY=your_api_key_here
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Local Development

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker build -t cerebras-chatbot .
docker run -p 8000:8000 --env-file .env cerebras-chatbot
```

## API Endpoints

- **GET** `/test app for API` - Health check
- **POST** `/chat` - Send a chat prompt
  - Request: `{"prompt": "Your question here"}`
  - Response: `{"response": "API response"}`

## Configuration

- Model: `gpt-oss-120b`
- Max tokens: 1024
- Temperature: 0.7
- Top P: 0.8
## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `CEREBRAS_API_KEY` | Your Cerebras API authentication key | Yes |
| `HOST` | Server host address | No (default: 0.0.0.0) |
| `PORT` | Server port number | No (default: 8000) |

## Project Structure

```
cerebras-chatbot/
├── app.py                 # FastAPI application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
├── .env.example          # Environment variables template
└── README.md             # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
