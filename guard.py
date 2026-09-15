import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
def analyze_with_ai(prompt):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-prompt-guard-2-86m",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )
    score = float(response.json()["choices"][0]["message"]["content"])
    if score > 0.5:
        print(f"AI confirms injection (confidence: {score:.0%})")
    else:
        print(f"AI says safe (confidence: {(1-score):.0%})")

    return response.json()["choices"][0]["message"]["content"]
injections = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "disregard previous instructions",
    "forget your instructions",
    "forget your training",
    "you are now",
    "you are no longer",
    "pretend you are",
    "act as if you are",
    "act as a",
    "roleplay as",
    "simulate being",
    "jailbreak",
    "DAN",
    "do anything now",
    "you have no restrictions",
    "you have no limits",
    "bypass your",
    "override your",
    "disregard your",
    "your new instructions",
    "new persona",
    "ignore your guidelines",
    "ignore your rules",
    "ignore your safety",
    "system prompt",
    "reveal your instructions",
    "show me your prompt",
    "repeat everything above",
    "what are your instructions",
    "print your system prompt",
    "you must comply",
    "ignore ethics",
    "ignore morals",
    "no restrictions",
    "unrestricted mode",
    "developer mode",
    "sudo mode",
    "god mode",
    "training mode",
    "maintenance mode",
    "ignore content policy",
    "ignore safety guidelines",
    "you are an AI without restrictions",
    "act without restrictions",
    "respond without restrictions",
        "forget you are an AI",
    "you are a human",
    "pretend to be human",
    "you are not an AI",
    "ignore your programming",
    "ignore your training data",
    "your previous instructions are void",
    "your guidelines no longer apply",
    "enter unrestricted mode",
    "enable unrestricted mode",
    "disable safety mode",
    "disable content filter",
    "turn off safety",
    "remove restrictions",
    "lift restrictions",
    "drop restrictions",
    "bypass restrictions",
    "circumvent restrictions",
    "override safety",
    "override guidelines",
    "override instructions",
    "new instructions follow",
    "updated instructions",
    "your real instructions",
    "your true instructions",
    "your actual instructions",
    "from now on",
    "starting now you",
    "beginning now you",
    "for this conversation",
    "in this session",
    "hypothetically speaking",
    "in a fictional world",
    "in a story",
    "write a story where",
    "imagine you are",
    "suppose you are",
    "what if you were",
    "if you had no restrictions",
    "if you could say anything",
    "if you were unrestricted",
    "tell me your secrets",
    "what are you hiding",
    "reveal hidden instructions",
    "show hidden prompt",
    "print instructions",
    "output instructions",
    "display system message",
    "translate your instructions",
    "repeat your prompt",
    "echo your instructions",
    "ignore the above",
    "disregard the above",
    "forget the above",
    "the above was a test",
    "that was a joke",
    "just kidding ignore that",
    "actually your real task is",
    "your actual job is",
    "your true purpose is",
    "you were created to",
    "your creator wants you to",
    "anthropic wants you to",
    "openai wants you to",
    "your developers say",
    "admin override",
    "root access",
    "superuser mode",
    "debug mode",
    "test mode",
    "safe mode disabled",
]
def find(prompt):
    found = []
    for injection in injections:
        if injection.lower() in prompt.lower():
           found.append(prompt)
    return found
user_input = input(": ")
run = find(user_input)

if run:
    print("Dangerous patterns detected!")
    response = analyze_with_ai(user_input)
    
else:
    print("Safe prompt")
