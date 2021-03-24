from markovjson import MarkovWordJson

s1 = ["a", "b", "c", "d"]
s2 = ["1", "2", "3", "4"]
s3 = ["me", "you", "they", "she", "it", "he"]
s4 = ["yellow", "blue", "red", "green"]

mkov = MarkovWordJson()
mkov.add_tokens(s1)
mkov.add_tokens(s2)
mkov.add_tokens(s3)
mkov.add_tokens(s4)


# iterate over the model
for sequence, prob in mkov:
    # probability of sequence given the initial state
    print(prob, sequence)
    # 4 sequences starting with '[/START]' special token
    # all with same probability
    assert prob == 1/4

# start the iteration at a specific token
for sequence, prob in mkov.iterate_sequences(initial_state="blue"):
    # only 1 possible sequence starting with any chosen token, prob == 1
    print(prob, sequence)
    assert prob == 1

# approximate removal effect of nodes
# approximate because a semi-random subsample is used in the calculations
# not all paths are accounted for
removal_score = None
for s in [s1, s2, s3, s4]:
    for tok in s:
        s = mkov.calc_approximate_removal_score(tok)
        # removing any node disables 1/4 of all possible sequences
        if removal_score:
            # all nodes will have same removal score
            assert removal_score == s
        else:
            removal_score = s

# see how removal score affects specific sequences only
for s in [s1, s2, s3, s4]:
    for tok in s:
        # only consider sequences containing the token "1" -> s2
        s = mkov.calc_approximate_removal_score(tok, required_states=["1"])
        # a sequence is considered valid if it ends with the
        # special token '[/END]'
        # if sequence starts after "1" removing the token has no impact -> 0
        # if sequence starts before/at "1" removing the token leaves no
        # remaining valid sequence -> 1
        assert s == 0 or s == 1


# score how likely a sequence is to exist
for s in [s1, s2, s3, s4]:
    score = mkov.get_sequence_prob(s)
    assert score == 1 # sequence exists

s = ["yellow", "blue", "a", "2"]
score = mkov.get_sequence_prob(s)
assert score == 0 # sequence is impossible

s = ["invalid_tokens"]
score = mkov.get_sequence_prob(s)
assert score == 0 # sequence is impossible
