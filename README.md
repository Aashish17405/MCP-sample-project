# 🤖 MCP Multi-Server Agent Project

A comprehensive demonstration of the **Model Context Protocol (MCP)** featuring multiple specialized servers with an interactive Streamlit web interface. This project showcases how to integrate mathematical operations and real-time weather data through MCP servers powered by Groq's advanced language models.

## Demo

![MCP Agent Demo](https://github.com/user-attachments/assets/e067da25-2440-4f09-a563-aa33d1636fd6)


## 🌟 Features

- **Complete Math Server**: Perform all basic mathematical operations (addition, subtraction, multiplication, division with zero-division handling)
- **Weather Server**: Get real-time weather data using OpenWeatherMap API with detailed information
- **Streamlit Web Interface**: Beautiful, interactive web UI with real-time responses
- **Command-line Support**: Alternative CLI interface (commented code available)
- **Groq LLM Integration**: Uses Groq's Qwen-3-32B model for intelligent, context-aware responses
- **Robust MCP Implementation**: FastMCP-based servers with stdio transport protocol
- **Error Handling**: Comprehensive error handling for API failures and invalid inputs
- **Async Architecture**: Full async/await support for optimal performance

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Application                       │
│                         (client.py)                            │
│  ┌─────────────────┐           ┌─────────────────────────────┐ │
│  │  Streamlit UI   │           │     Command Line Interface │ │
│  │   (Active)      │           │      (Commented Out)       │ │
│  └─────────────────┘           └─────────────────────────────┘ │
│                                                                 │
│         ▲                                                       │
│         │                                                       │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │              LangGraph React Agent                          │ │
│  │              (Groq Qwen-3-32B)                             │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│         ▲                                                       │
│         │                                                       │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │           MultiServerMCPClient                              │ │
│  │         (langchain-mcp-adapters)                           │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
         │                                    │
         ▼                                    ▼
┌─────────────────┐                  ┌─────────────────┐
│   Math Server   │                  │ Weather Server  │
│ (math_server.py)│                  │  (weather.py)   │
│                 │                  │                 │
│ FastMCP Server  │                  │ FastMCP Server  │
│ stdio transport │                  │ stdio transport │
│                 │                  │                 │
│ Tools:          │                  │ Tools:          │
│ • add()         │                  │ • get_weather() │
│ • subtract()    │                  │                 │
│ • multiply()    │                  │ External API:   │
│ • divide()      │                  │ OpenWeatherMap  │
└─────────────────┘                  └─────────────────┘
```

### Key Components

1. **Client Layer** (`client.py`): Streamlit web interface with async support
2. **Agent Layer**: LangGraph React Agent with Groq LLM
3. **MCP Layer**: MultiServerMCPClient for tool discovery and execution
4. **Server Layer**: FastMCP-based servers with specialized tools
5. **External APIs**: OpenWeatherMap for real-time weather data

## 🚀 Quick Start

### Prerequisites

- Python 3.13+ (as specified in pyproject.toml)
- Virtual environment (recommended)
- OpenWeatherMap API key (free registration required)
- Groq API key (free registration required)

### 1. Clone and Setup

```bash
git clone https://github.com/Aashish17405/MCP-sample-project
cd "MCP projects"

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On Windows Command Prompt:
.\.venv\Scripts\activate.bat
# On Mac/Linux:
source .venv/bin/activate

# Install dependencies (using pip or uv)
pip install -r requirements.txt
# OR if you have uv installed:
# uv pip install -r requirements.txt
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

#### Option A: Streamlit Web Interface (Primary Interface)

```bash
streamlit run client.py
```

This opens a beautiful web interface at `http://localhost:8501` where you can:

- **Ask math questions**:
  - "What is (15 + 25) × 3?"
  - "Calculate 100 ÷ 4 and add 50"
  - "What's 12 - 8 + 15?"
- **Request weather information**:
  - "What's the weather like in Tokyo?"
  - "How's the weather in London today?"
  - "Tell me about the weather in New York"
- **Get combined responses**:
  - "Calculate 5×7 and tell me the weather in Paris"
  - "What's 20+30 and how's the weather in Mumbai?"

#### Option B: Command Line Interface (Available in Comments)

To enable the CLI interface, uncomment the CLI code at the top of `client.py` and comment out the Streamlit code, then run:

```bash
python client.py
```

## 🛠️ Project Structure

### File Descriptions

- **`client.py`**: Primary application file containing both Streamlit web interface and commented CLI code. Handles MCP client setup, agent creation, and user interactions.
- **`math_server.py`**: FastMCP server providing mathematical operations with comprehensive error handling.
- **`weather.py`**: FastMCP server for real-time weather data using OpenWeatherMap API.
- **`main.py`**: Basic entry point (currently just prints "Hello from mcp!")
- **`pyproject.toml`**: Modern Python project configuration with dependency management.

## 📋 Available Tools

### Math Server (`math_server.py`)

The math server provides four comprehensive mathematical operations:

- **`add(a: int, b: int) -> int`**: Add two integers
  - Example: `add(5, 3)` returns `8`
- **`subtract(a: int, b: int) -> int`**: Subtract second number from first
  - Example: `subtract(10, 4)` returns `6`
- **`multiply(a: int, b: int) -> int`**: Multiply two integers
  - Example: `multiply(6, 7)` returns `42`
- **`divide(a: int, b: int) -> float`**: Divide first number by second with zero-division protection
  - Example: `divide(15, 3)` returns `5.0`
  - Safe handling: `divide(10, 0)` returns `0` (prevents errors)

### Weather Server (`weather.py`)

The weather server provides real-time weather information:

- **`get_weather(city: str) -> str`**: Get comprehensive current weather for any city
  - **Returns**: Temperature, weather description, "feels like" temperature, humidity percentage
  - **Data Source**: OpenWeatherMap API (real-time data)
  - **Error Handling**:
    - Invalid city names return user-friendly error messages
    - API failures are gracefully handled
    - Missing API key detection and helpful error messages
  - **Example Response**: "Weather in Tokyo: clear sky, Temperature: 22°C (feels like 24°C), Humidity: 65%"

### Tool Integration Features

- **Async Support**: Both servers support asynchronous operations for optimal performance
- **Detailed Logging**: All operations include console logging for debugging
- **Type Safety**: Proper type hints for all functions
- **Error Recovery**: Robust error handling prevents crashes

## 🔧 Technical Details

### MCP (Model Context Protocol) Implementation

This project demonstrates a sophisticated MCP setup with the following technical characteristics:

#### Server Architecture

- **Framework**: FastMCP for simplified MCP server development
- **Transport Protocol**: stdio (Standard Input/Output) for reliable, lightweight communication
- **Process Management**: Each server runs as a separate Python process
- **Tool Discovery**: Automatic tool registration and discovery via MCP protocol
- **Type Safety**: Full type annotations for all tool functions

#### Client Architecture

- **MCP Client**: `MultiServerMCPClient` from `langchain-mcp-adapters`
- **Agent Framework**: LangGraph's `create_react_agent` for intelligent tool usage
- **LLM Integration**: Groq's Qwen-3-32B model for natural language understanding
- **Caching**: Streamlit's `@st.cache_resource` for efficient agent initialization
- **Async Handling**: Proper async/await patterns with `asyncio.run()` for Streamlit compatibility

#### Communication Flow

1. **User Input** → Streamlit interface captures user query
2. **Agent Processing** → LangGraph agent analyzes query and determines required tools
3. **Tool Selection** → Agent selects appropriate MCP server(s) and tools
4. **MCP Communication** → MultiServerMCPClient sends tool calls via stdio
5. **Tool Execution** → FastMCP servers execute tools and return results
6. **Response Generation** → Groq LLM generates natural language response
7. **UI Display** → Streamlit renders the final response to user

### Dependencies and Versions

#### Core MCP Stack

- **`mcp`** (v1.13.0+): Core Model Context Protocol implementation
- **`langchain-mcp-adapters`** (v0.1.9+): LangChain integration for MCP
- **`langgraph`** (v0.6.5+): Agent framework for tool orchestration

#### LLM and UI

- **`langchain-groq`** (v0.3.7+): Groq LLM integration with LangChain
- **`streamlit`** (v1.48.1+): Modern web interface framework

#### Utilities

- **`httpx`**: Async HTTP client for weather API calls
- **`python-dotenv`**: Environment variable management
- **`asyncio`**: Built-in async runtime for Python

### Performance Optimizations

- **Resource Caching**: Agent initialization cached to prevent repeated setup
- **Async Operations**: Non-blocking I/O for weather API calls
- **Efficient Transport**: stdio transport minimizes communication overhead
- **Process Isolation**: Each MCP server runs independently for stability

## 🔑 API Keys Setup

### Groq API Key (Required)

Groq provides access to state-of-the-art language models including Qwen-3-32B used in this project.

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account (no credit card required)
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key and add to your `.env` file as `GROQ_API_KEY=your_key_here`

**Free Tier**: Generous free tier with high rate limits suitable for development and testing.

### OpenWeatherMap API Key (Required)

OpenWeatherMap provides real-time weather data for cities worldwide.

1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to "API keys" tab in your account
4. Copy the default API key (or generate a new one)
5. Add to your `.env` file as `OPENWEATHER_API_KEY=your_key_here`

**Free Tier**:

- 1,000 API calls per day
- Current weather data for any location
- No credit card required

### Environment File Example

Create a `.env` file in your project root:

```env
# Groq API Key - Get from https://console.groq.com/
GROQ_API_KEY=gsk_1234567890abcdef...

# OpenWeather API Key - Get from https://openweathermap.org/api
OPENWEATHER_API_KEY=abcdef1234567890...
```

**Important**:

- Never commit your `.env` file to version control
- The `.env` file is already included in `.gitignore`
- Keep your API keys secure and don't share them publicly

## 🤝 Contributing

We welcome contributions to improve this MCP demonstration project!

### How to Contribute

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/MCP-sample-project
   cd "MCP projects"
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and ensure they work properly
5. **Test thoroughly** with both interfaces
6. **Commit your changes**:
   ```bash
   git commit -m "Add: description of your changes"
   ```
7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Submit a pull request** with a clear description of your changes

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy experimenting with MCP! 🚀**

_Built with ❤️ to demonstrate the power of Model Context Protocol_
