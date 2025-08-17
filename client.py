# from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import asyncio
# import os

# load_dotenv()
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# async def main():
#     print("[DEBUG] Creating MultiServerMCPClient...")
#     client=MultiServerMCPClient({
#         "math": {
#             "command": "python",
#             "args": ["math_server.py"],
#             "transport": "stdio",
#         },
#         "weather": {
#             "command": "python",
#             "args": ["weather.py"],
#             "transport": "stdio",
#         }
#     })

#     print("[DEBUG] Getting tools...")
#     tools = await client.get_tools()

#     model = ChatGroq(model = "qwen/qwen3-32b")
#     print("[DEBUG] Creating agent...")
#     agent =  create_react_agent(model, tools)

#     print("[DEBUG] Testing math...")
#     math_response = await agent.ainvoke({
#         "messages": [
#             {"role": "user", "content": "What is (2 + 2) x 12? Explain step by step."}
#         ]
#     })
#     print("Math response:", math_response['messages'][-1].content)
    
#     print("[DEBUG] Testing weather...")
#     weather_response = await agent.ainvoke({
#         "messages": [
#             {"role": "user", "content": "What's the weather like in Hyderabad?"}
#         ]
#     })
#     print("Weather response:", weather_response['messages'][-1].content)

# asyncio.run(main())


import streamlit as st
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# --- Setup MCP + Agent (initialize once, cache it) ---
@st.cache_resource
def setup_agent():
    client = MultiServerMCPClient({
        "math": {
            "command": "python",
            "args": ["math_server.py"],
            "transport": "stdio",
        },
        "weather": {
            "command": "python",
            "args": ["weather.py"],
            "transport": "stdio",
        }
    })

    # Fetch tools (must be async → run with asyncio.run)
    tools = asyncio.run(client.get_tools())

    model = ChatGroq(model="qwen/qwen3-32b")
    agent = create_react_agent(model, tools)
    return agent

agent = setup_agent()

# --- Streamlit UI ---
st.title("🤖 MCP Agent with Streamlit")

user_input = st.text_area("Ask something (math or weather):")

if st.button("Send"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            try:
                # Run async agent in sync Streamlit
                response = asyncio.run(agent.ainvoke({
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                }))
                st.success(response['messages'][-1].content)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter a question first.")
