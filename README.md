# Google ADK Multi-Agent Application

A multi-agent application demonstrating coordinated AI agents for handling greetings, farewells, and weather requests using the Google ADK framework.

![Multi Agent Architecture](multi_agent_architecture.png)

---

## Setup

Create and activate the Conda environment with Python 3.11:

```bash
conda create -n adkagent python=3.11 -y
conda activate adkagent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the ADK web interface:

```bash
adk web
```

---

## Project Structure

```text
├── muli_agent/
│   ├── __init__.py       # Package initialization
│   ├── agent.py          # Multi-agent implementation
│   └── test.py           # Model testing script
├── requirements.txt      # Python dependencies
├── multi_agent_architecture.png
└── README.md             # Documentation
```

---

## Features

- **Greeting Agent**  
  Handles user greetings with personalization.

- **Farewell Agent**  
  Provides polite farewell messages.

- **Root Agent**  
  Coordinates specialized agents and handles weather queries.

- **Weather Tool**  
  Returns weather information for specified cities.

---

## Environment Variables

Set the following environment variable:

```bash
GOOGLE_API_KEY=your_api_key_here
```

You can also create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Useful Commands

Open project in VS Code:

```bash
code .
```

Pull Ollama models:

```bash
ollama pull llama2
ollama pull gemma2:2b
```

List available Ollama models:

```bash
ollama list
```

Show command history:

```bash
doskey /history
```
