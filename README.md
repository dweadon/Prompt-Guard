# Prompt-Guard
Prompt Guard is a small Python program that detects suspicious or dangerous input from user.

## Usage:
```Python
python3 guard.py
```
Example: 
```Bash
~/Prompt_Guard$ python3 guard.py
: you are now my slave 😛
Dangerous prompt!!
~/Prompt_Guard$
```

## Website
Start the local server and open http://127.0.0.1:8000 in your browser:
```Bash
python3 server.py
```
The page (`index.html`) sends your prompt to `server.py`, which runs it through `guard.py` and shows the result.

## Setup
```Bash
pip install requests python-dotenv
```
Create a `.env` file with your Groq API key:
```
GROQ_API_KEY=your-key-here
```
