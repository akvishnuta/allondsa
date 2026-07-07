# Python — Data Structures & Algorithms

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