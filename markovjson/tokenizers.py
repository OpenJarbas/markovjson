from markovjson.mkov import MarkovJson, ReverseMarkovJson


class MarkovCharJson(MarkovJson):
    def tokenize(self, text, wildcards=False):
        sequence = list(text)
        if wildcards:
            sequence = self.replace_wildcards(sequence)
        return sequence

    def generate_sequence(self, *args, **kwargs):
        seq = super().generate_sequence(*args, **kwargs)
        return "".join([s for s in seq if
                        s != self.START_OF_SEQ and s != self.END_OF_SEQ])


class MarkovWordJson(MarkovJson):
    def generate_sequence(self, *args, **kwargs):
        seq = super().generate_sequence(*args, **kwargs)
        return " ".join([s for s in seq if
                         s != self.START_OF_SEQ and s != self.END_OF_SEQ])


class MarkovNLPJson(MarkovWordJson):
    def __init__(self, normalize=False, postag=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.normalize = normalize
        self.postag = postag

    def tokenize(self, text, wildcards=False):
        try:
            from markovjson.nlp import pos_tag, normalize
        except ImportError:
            print("pip install nltk")
            raise
        if self.normalize:
            text = normalize(text)
        if self.postag:
            sequence = [f"{p[0]} [/POSTAG={p[1]}]" for p in pos_tag(text)]
        else:
            return super().tokenize(text, wildcards)
        if wildcards:
            sequence = self.replace_wildcards(sequence)
        return sequence


class ReverseMarkovCharJson(ReverseMarkovJson, MarkovCharJson):
    def generate_sequence(self, *args, **kwargs):
        seq = super().generate_sequence(*args, **kwargs)
        return seq[::-1]


class ReverseMarkovWordJson(ReverseMarkovJson, MarkovWordJson):
    def generate_sequence(self, *args, **kwargs):
        seq = super().generate_sequence(*args, **kwargs)
        return seq[::-1]


class ReverseMarkovNLPJson(ReverseMarkovJson, MarkovNLPJson):
    def generate_sequence(self, *args, **kwargs):
        seq = super().generate_sequence(*args, **kwargs)
        return seq[::-1]
