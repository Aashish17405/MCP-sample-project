from mcp.server.fastmcp import FastMCP
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the weather for the specified location using OpenWeatherMap API
    """
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        return "Error: OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY in your .env file."
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            )
            response.raise_for_status()
            data = response.json()
            
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            print(f"Weather data for {city}: {data}")

            return f"Weather in {city}: {weather_desc}, Temperature: {temp}°C (feels like {feels_like}°C), Humidity: {humidity}%"

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return f"Error: City '{city}' not found."
        else:
            return f"Error: Failed to get weather data. Status code: {e.response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")