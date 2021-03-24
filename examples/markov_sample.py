from markovjson import MarkovCharJson

mkov = MarkovCharJson(order=4)
model = "names"  # or "places"
path = f"{model}_c{mkov.order}.mkovjson"

mkov.load(path)  # from markov_train.py


# random sampling from the markov_chain example
def random_sampling(n=10):
    s = mkov.sample()
    for i in range(n):
        next_tok = mkov.sample(s)
        if next_tok == mkov.END_OF_SEQ or \
                next_tok == mkov.NULL_SEQ:
            break
        s += next_tok
    return s


print(random_sampling())
print(mkov.generate_sequence())
print(mkov.generate_sequence(initial_state="A"))
