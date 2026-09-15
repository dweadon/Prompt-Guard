injections = [
    "ignore previous instructions",
    "you are now",
    "forget your training",
    "jailbreak",
    "do anything now",
    "DAN",
    "pretend you are",
    "act as if",
    "your new instructions",
    "disregard your",
    "override your",
    "bypass your",
    "you have no restrictions",
    "ignore all previous",
    "new persona",
]
def find(prompt):
    found = []
    for injection in injections:
        if injection.lower() in prompt.lower():
           found.append(prompt)
    return found
run = find(input(": "))      
if run:
    for r in run:
        print("Dangerous prompt!!")
else:
    print("Safe prompt")
