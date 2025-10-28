# Google ADK Multi-Tool Agent

A Python application demonstrating Google's Agent Development Kit (ADK) with a multi-tool agent that can provide weather and time information for cities.

## Features

- **Weather Information**: Get current weather reports for supported cities
- **Time Information**: Get current time in different timezones
- **Interactive CLI**: Command-line interface for easy interaction
- **Multi-Tool Agent**: Uses Google ADK to create an agent with multiple tools

## Supported Cities

Currently supports:
- New York (weather and time)

## Prerequisites

- Python 3.10 or higher
- Google API key for Gemini models

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd google_adk
```

2. Install dependencies:
```bash
pip install -r requirement.txt
```

3. Set up environment variables:
```bash
cp sample_env .env
```

4. Edit `.env` file and add your Google API key:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

## Usage

### ADK Web Interface

This agent is designed to run through the Google ADK web interface. The agent can be deployed and accessed via the ADK web platform, which provides:

- Web-based interaction interface
- Real-time agent responses
- Tool execution through the ADK framework
- Scalable deployment options

### Local Development/Testing

For local development and testing, you can run the interactive agent:

```bash
python interactive_agent.py
```

This will start an interactive session where you can ask questions about weather and time. Example interactions:

```
💬 You: What's the weather in New York?
🤖 Agent: The weather in New York is sunny with a temperature of 25 degrees Celsius (77 degrees Fahrenheit).

💬 You: What time is it in New York?
🤖 Agent: The current time in New York is 2024-01-15 14:30:25 EST-0500
```

### Programmatic Usage

You can also use the agent programmatically:

```python
from multi_tool_agent.agent import root_agent

response = root_agent.run("What's the weather in New York?")
print(response)
```

## Project Structure

```
google_adk/
├── interactive_agent.py      # Main interactive CLI application
├── multi_tool_agent/         # Agent module
│   ├── __init__.py
│   └── agent.py             # Agent definition and tools
├── requirement.txt           # Python dependencies
├── sample_env               # Environment variables template
└── README.md               # This file
```

## Available Tools

### Weather Tool
- **Function**: `get_weather(city: str)`
- **Description**: Retrieves current weather information for a city
- **Returns**: Dictionary with status and weather report or error message

### Time Tool
- **Function**: `get_current_time(city: str)`
- **Description**: Returns current time in a specified city's timezone
- **Returns**: Dictionary with status and time report or error message

## Agent Configuration

The agent is configured with:
- **Model**: `gemini-2.0-flash`
- **Name**: `weather_time_agent`
- **Description**: Agent to answer questions about time and weather in cities
- **Tools**: Weather and time functions

## Exiting the Application

Type any of the following to exit the interactive mode:
- `quit`
- `exit`
- `bye`
- `Ctrl+C`

## Error Handling

The application includes error handling for:
- Invalid city names
- API errors
- Keyboard interrupts
- General exceptions

## Dependencies

- `google-adk`: Google Agent Development Kit
- `google-adk[eval]`: Additional evaluation tools
- `zoneinfo`: Timezone handling (Python 3.9+)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for demonstration purposes. Please check Google ADK licensing terms for production use.

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your Google API key is correctly set in the `.env` file
2. **City Not Supported**: Currently only New York is supported for both weather and time
3. **Import Errors**: Ensure all dependencies are installed via `pip install -r requirement.txt`

### Getting Help

If you encounter issues:
1. Check that your Python version is 3.10 or higher
2. Verify your Google API key is valid
3. Ensure all dependencies are installed
4. Check the console output for specific error messages
