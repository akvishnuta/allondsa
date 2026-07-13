# AI Agent: Weather + Calculator

A tool-using agent that answers questions like  
*"What is the sum of the temperature in New York and Delhi?"*

## Architecture

| Layer | Responsibility |
|-------|----------------|
| **LLM** (Claude) | Understands the query, decides which tool to call & with what args |
| **Agent Loop** | Sends messages ↔ LLM, intercepts tool-use blocks, runs tools, feeds results back |
| **Tool Runtime** | `get_weather()` → Open-Meteo free API | `calculator()` → expression evaluator |

```
User Query
    │
    ▼
┌─────────────────────┐
│   Agent Loop         │  ── tool_use ──►  Tool Runtime
│   (L message → LLM   │  ◄── result ──  (get_weather / calculator)
│    ↑ until text)     │
└─────────┬───────────┘
          │ final text
          ▼
      Answer
```

## Tools

### `get_weather(city: str)`
- **Source**: [Open-Meteo](https://open-meteo.com/) — free, no API key required
- **Returns**: current temperature (°C), wind speed, weather code

### `calculator(expression: str)`
- Evaluates simple arithmetic (no external dependency)
- Only allows `0-9 + - * / ( ) .`

## Usage

```bash
# Install dependencies
pip install -r python/agent/requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY=sk-...

# Run — answer: "What is the sum of the temperature in New York and Delhi?"
python python/agent/weather_agent.py
```

## Extending

Add a new tool in three places:

1. **Implement** the function (e.g. `def search_web(...)`)
2. **Register it** in the `TOOLS` list with its JSON Schema
3. **Map it** in `TOOL_IMPLS` dict

The agent loop handles the rest automatically.
