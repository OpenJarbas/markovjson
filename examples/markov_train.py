from markovjson import MarkovCharJson
from os.path import isfile

# for names modelling at char level makes sense
# word level could make more sense for things like song lyrics
mkov = MarkovCharJson(order=4)
model = "names"  # or "places"
path = f"{model}_c{mkov.order}.mkovjson"


if isfile(path):
    mkov.load(path)
else:
    with open(f"datasets/{model}.txt") as f:
        for line in f.readlines():
            if not line.strip():
                continue
            mkov.add_string(line.strip())

    mkov.save(path)