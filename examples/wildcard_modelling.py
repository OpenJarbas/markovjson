from markovjson.topic_modelling import MarkovTopic
from os.path import join, dirname
from os import listdir


folder = join(dirname(__file__), "questions")

container = MarkovTopic(order=3)

for f in listdir(folder):
    if f.endswith(".txt"):
        container.register_topic_from_file(join(folder, f))


utt = "what is the speed of light"
container.tokenize(utt, wildcards=True)
# ['what', 'is', 'the', '[/]']

container.score_tokens(utt)
# {'[/LABEL=commands.txt]': {'what': 0, 'is': 0, 'the': 0, '[/]': 1}, 
# '[/LABEL=open_question.txt]': {'what': 0.9659863945578231, 'is': 0.9598765432098766, 'the': 0, '[/]': 1}, 
# '[/LABEL=statement.txt]': {'what': 0, 'is': 0, 'the': 0.9135802469135803, '[/]': 1},
# '[/LABEL=requests.txt]': {'what': 0, 'is': 0, 'the': 0, '[/]': 0}, 
# '[/LABEL=yes_no_question.txt]': {'what': 0, 'is': 0, 'the': 0, '[/]': 1}}

container.predict_topic(utt, thresh=0.2)
# {'[/LABEL=commands.txt]': 0.25, 
# '[/LABEL=open_question.txt]': 0.7314657344419249,
# '[/LABEL=statement.txt]': 0.4783950617283951, 
# '[/LABEL=yes_no_question.txt]': 0.25}


for utt in ["how fast can you run",
            "what is your favorite food",
            "open the pod bay doors",
    "could it rain tomorrow",
    "will it rain",
    "did it rain yesterday",
    "will it rain today",
    "could you pass the salt please",
    "would you hold the door open? thanks",
    "today i saw a black cat",
    "do you like cheese?",
    "do you prefer cats or dogs",
            "eat your food"]:
    print(utt)
    print(container.predict_topic(utt, thresh=0.2))