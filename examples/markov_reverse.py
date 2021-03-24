from markovjson import ReverseMarkovCharJson

mkov = ReverseMarkovCharJson(order=4)
model = "places"  # or "names"
with open(f"datasets/{model}.txt") as f:
    for line in f.readlines():
        if not line.strip():
            continue
        mkov.add_string(line.strip())

# instead of iterating from the start, we iterate from the end
# we can check for names ending a certain way instead of starting
seq = mkov.generate_sequence(final_state="own")
print(seq)

mkov.get_state("own")  # notice padding token
# ('[/END]', 'n', 'w', 'o')
