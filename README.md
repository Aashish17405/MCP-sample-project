# 🤖 MCP Multi-Server Agent Project

A powerful demonstration of the **Model Context Protocol (MCP)** using multiple servers with both command-line and web interfaces. This project showcases how to integrate math operations and real-time weather data through MCP servers with a Groq LLM agent.

## 🌟 Features

- **Math Server**: Perform mathematical operations (addition, multiplication)
- **Weather Server**: Get real-time weather data using OpenWeatherMap API
- **Dual Interface**: Both command-line and Streamlit web interface
- **LLM Integration**: Uses Groq's language models for intelligent responses
- **MCP Protocol**: Demonstrates proper MCP server implementation with stdio transport

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client.py     │    │  Math Server    │    │ Weather Server  │
│  (Streamlit/    │◄──►│   (MCP/stdio)   │    │   (MCP/stdio)   │
│   Command Line) │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Groq LLM      │    │  Tools:         │    │  Tools:         │
│   (qwen model)  │    │  • add()        │    │  • get_weather()│
│                 │    │  • multiply()   │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- OpenWeatherMap API key (free)
- Groq API key (free)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd "MCP projects"

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.\.venv\Scripts\Activate.ps1
# On Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the project root:

```env
# Get your free API key from https://console.groq.com/
GROQ_API_KEY=your_groq_api_key_here

# Get your free API key from https://openweathermap.org/api
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

### 3. Run the Application

#### Option A: Streamlit Web Interface (Recommended)

```bash
streamlit run client.py
```

This opens a web interface at `http://localhost:8501` where you can:

- Ask math questions: "What is (15 + 25) × 3?"
- Request weather info: "What's the weather like in Tokyo?"
- Get combined responses: "Calculate 5×7 and tell me the weather in Paris"

#### Option B: Command Line Interface

Uncomment the command-line code in `client.py` and run:

```bash
python client.py
```

## 🛠️ Project Structure

```
MCP projects/
├── client.py           # Main application (Streamlit + CLI)
├── math_server.py      # MCP math operations server
├── weather.py          # MCP weather data server
├── requirements.txt    # Python dependencies
├── pyproject.toml     # Project configuration
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## 📋 Available Tools

### Math Server (`math_server.py`)

- **`add(a: int, b: int)`**: Add two integers
- **`multiply(a: int, b: int)`**: Multiply two integers

### Weather Server (`weather.py`)

- **`get_weather(city: str)`**: Get current weather for any city
  - Returns temperature, description, humidity, "feels like" temperature
  - Uses OpenWeatherMap API for real data

## 🔧 Technical Details

### MCP Implementation

- **Transport**: stdio (Standard Input/Output) for reliable communication
- **Protocol**: Model Context Protocol for tool discovery and execution
- **Architecture**: Multi-server setup with centralized client

### Dependencies

- `langchain-mcp-adapters`: MCP integration with LangChain
- `langchain-groq`: Groq LLM integration
- `langgraph`: Agent framework
- `streamlit`: Web interface
- `httpx`: Async HTTP client for weather API
- `python-dotenv`: Environment variable management

## 🧪 Example Interactions

### Math Operations

```
User: "What is 25 × 4 + 10?"
Agent: Let me calculate that for you.
       25 × 4 = 100
       100 + 10 = 110
       The answer is 110.
```

### Weather Queries

```
User: "What's the weather in London?"
Agent: The weather in London is currently clear sky
       with a temperature of 22.04°C (feels like 21.61°C)
       and humidity of 50%.
```

### Combined Requests

```
User: "Calculate 7×8 and tell me the weather in Tokyo"
Agent: I'll help you with both requests:

       Math: 7 × 8 = 56

       Weather: The weather in Tokyo is partly cloudy
       with a temperature of 18.5°C (feels like 17.2°C)
       and humidity of 65%.
```

## 🔑 API Keys Setup

### Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account
3. Generate an API key
4. Add to your `.env` file

### OpenWeatherMap API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key
4. Add to your `.env` file

## 🚨 Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'mcp'"**

   - Ensure virtual environment is activated
   - Run: `pip install -r requirements.txt`

2. **"API key not found" errors**

   - Check your `.env` file exists and has the correct keys
   - Ensure no extra spaces or quotes around the keys

3. **Streamlit connection errors**

   - Try running: `streamlit run client.py --server.address 127.0.0.1`

4. **MCP server startup issues**
   - Check that Python can find the server files
   - Ensure virtual environment is activated when running

### Debug Mode

To enable debug output, uncomment the debug print statements in `client.py`:

```python
print(f"[DEBUG] Tools available: {[tool.name for tool in tools]}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Learn More

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain/tree/master/libs/community/langchain_community/adapters/mcp)
- [Groq API Documentation](https://console.groq.com/docs)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

**Happy experimenting with MCP! 🚀**
