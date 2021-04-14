from markovjson.topic_modelling import MarkovTopic
from os.path import join, dirname
from os import listdir
from pprint import pprint

folder = join(dirname(__file__), "intents")

container = MarkovTopic(order=4)

for f in listdir(folder):
    if f.endswith(".txt"):
        container.register_topic_from_file(join(folder, f))

utt = "turn off"

a = container.score_tokens(utt)
pprint(a)
# {'[/LABEL=hello.txt]': {'turn': 0, 'off': 0},
# '[/LABEL=joke.txt]': {'turn': 0, 'off': 0},
# '[/LABEL=thank.txt]': {'turn': 0, 'off': 0},
# '[/LABEL=lights_on.txt]': {'turn': 0.98, 'off': 0},
# '[/LABEL=lights_off.txt]': {'turn': 0.98, 'off': 1}}

pprint(container.predict_topic(utt))
# {'[/LABEL=lights_on.txt]': 0.49,
# '[/LABEL=lights_off.txt]': 0.99}
