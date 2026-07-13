# Agents: Weather + Calculator

Tool-using agents that answer questions like  
*"What is the sum of the temperature in New York and Delhi?"*

Two implementations showing different frameworks:

| File | Framework | Pattern |
|------|-----------|---------|
| `weather_agent.py` | **Anthropic SDK** (vanilla) | Manual agent loop: send → tool_use → execute → repeat |
| `weather_agent_langgraph.py` | **LangGraph** | State-graph: nodes (call_llm ↔ execute_tools) + conditional routing |

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
┌─────────────────────────────────────────────────────┐
│  run_agent() loop                                   │
│                                                     │
│  ┌──────────┐   tools + history    ┌────────────┐  │
│  │  LLM      │ ◄───────────────── │  messages[]  │  │
│  │ (Claude)  │ ─── tool_use ────► │              │  │
│  │ (planner) │                    │  append      │  │
│  └─────┬─────┘                    │  result as   │  │
│        │                          │  "user" role │  │
│        ▼ tool_use                 └──────────────┘  │
│  ┌──────────────┐                                   │
│  │  Tool Runtime│  get_weather() / calculator()     │
│  └──────┬───────┘                                   │
│         │ result                                    │
└─────────┼───────────────────────────────────────────┘
          │ final text (no tool_use blocks)
          ▼
       Answer

## Supported Cities

`get_weather` currently supports: New York, Delhi, London, Tokyo, Paris, Sydney.

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

# Run with a CLI argument
python python/agent/weather_agent.py "What is the sum of temperature in New York and Delhi?"

# Or run interactively — you'll be prompted for a query
python python/agent/weather_agent.py
```

## Message Flow

The Anthropic Messages API uses only `"user"` and `"assistant"` roles (no `"tool"` role). Tool results are wrapped in a `"user"` message with `type: "tool_result"`:

```
user:      "What is the sum of temperature in New York and Delhi?"
assistant: tool_use(id="abc", name="get_weather", input={city: "New York"})
user:      tool_result(tool_use_id="abc", content={temp: 28.3})
assistant: tool_use(id="def", name="calculator", input={expr: "28.3 + 31.6"})
user:      tool_result(tool_use_id="def", content={result: 59.9})
assistant: "The sum is 59.9°C"
```

Each `tool_result` links back to its `tool_use` via `tool_use_id`. The `"user"` role is just the container — the `type: "tool_result"` field tells the API it's a tool response, not free-form user text.

## Extending

Add a new tool in three places:

1. **Implement** the function (e.g. `def search_web(...)`)
2. **Register it** in the `TOOLS` list with its JSON Schema
3. **Map it** in `TOOL_IMPLS` dict

The agent loop handles the rest automatically.
