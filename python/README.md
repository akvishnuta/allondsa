# Python

A collection of Python modules exploring different domains — from data structures and algorithms to AI agent patterns and deep learning.

## Modules

| Module | Description |
|--------|-------------|
| [**agent**](agent/README.md) | Tool-using AI agent that answers questions using a weather API and calculator — demonstrates the LLM tool-calling (function calling) pattern |
| [**datastructures**](datastructures/) | Data structures & algorithms problems (arrays, two-pointers, etc.) |
| [**deeplearning**](deeplearning/README.md) | Deep learning fundamentals — NumPy, Pandas, PyTorch, TensorFlow, Keras, CNNs, RNNs, transfer learning |
| [**finetuning**](finetuning/) | Model fine-tuning experiments |

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Deactivating

When you're done, exit the virtual environment:

```bash
deactivate
```

## Running files

Always source the virtual environment first, then run:

```bash
source .venv/bin/activate
python datastructures/arrays.py
```

Or run in one line without leaving the current shell activated:

```bash
source .venv/bin/activate && python datastructures/arrays.py
```

Some modules (like `agent/`) have their own additional dependencies — see their inner READMEs for details.
