from markovjson import MarkovWordJson, MarkovNLPJson
from os.path import isfile

# for names modelling at char level makes sense
# word level could make more sense for things like song lyrics
mkov = MarkovNLPJson(order=2)
model = "questions"  # or "places"
path = f"{model}_w{mkov.order}.mkovjson"



with open(f"datasets/{model}.txt") as f:
    for line in f.readlines():
        if not line.strip():
            continue
        line = " ".join(line.split(" ")[1:]).replace("?", "").lower()
        mkov.add_string(line.strip())



for i in range(10):
    print(mkov.generate_string())