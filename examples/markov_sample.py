from markovjson import MarkovCharJson

mkov = MarkovCharJson(order=4)
model = "places"  # or "places"
path = f"{model}_c{mkov.order}.mkovjson"

mkov.load(path)  # from markov_train.py


# random sampling from the markov_chain examples
def random_sampling(n=10):
    s = mkov.sample()
    for i in range(n):
        next_tok = mkov.sample(s)
        if next_tok == mkov.END_OF_SEQ or next_tok == mkov.NULL_SEQ:
            break
        s += next_tok
    return s


print(random_sampling())
print(mkov.generate_sequence())
print(mkov.generate_sequence(initial_state="X"))


# iterate over markov chain sequences
# NOTE  there could be infinite sequences depending on loops in the chain
#       topology, for this reason there is a max path length
#       that will be used to truncate results
# you can use mkov.iterate_paths if you need control over the iteration
# see iterate_over_names example below
for sequence, prob in mkov:
    # prob is the average of the transition probabilities for each step in
    # the sequence, prob = p1 + p2 + pN / len(probs)
    # 1 -> the only path in the markov chain is this sequence
    # 0 -> no sequences in the markov chain generate this sequence
    print(prob, sequence)

# this will take forever, don't do it unless your chain is really small!
# list(mkov)


def iterate_over_names(tokens=None, max_len=5):
    # iterate over all names with len <= 5
    for p, _ in mkov.iterate_sequences(initial_state=tokens, max_len=max_len):
        name = "".join([_ for _ in p if _ not in [mkov.START_OF_SEQ,
                                                  mkov.END_OF_SEQ,
                                                  mkov.NULL_SEQ]])
        print(name)


# names starting with A
iterate_over_names("Brit", max_len=8)
