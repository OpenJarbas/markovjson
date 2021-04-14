import re
import nltk

# TODO conditional download
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def normalize(X, stemmer=None, lemmatize=True):
    if isinstance(X, str):
        X = [X]
    documents = []

    if isinstance(stemmer, str):
        if "porter" in stemmer.lower():
            stemmer = nltk.PorterStemmer()
        elif "wordnet" in stemmer.lower():
            stemmer = nltk.stem.WordNetLemmatizer()
        elif "snowball" in stemmer.lower():
            stemmer = nltk.stem.SnowballStemmer("english",
                                                ignore_stopwords=True)

    for sen in range(0, len(X)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(X[sen]))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()

        # Lemmatization
        if lemmatize:
            document = document.split()
            try:
                document = [stemmer.lemmatize(word) for word in document]
            except:
                document = [nltk.stem.WordNetLemmatizer().lemmatize(word)
                            for word in document]

            document = ' '.join(document)

        documents.append(document)
    return documents


def pos_tag(sentence):
    toks = nltk.word_tokenize(sentence)
    return nltk.pos_tag(toks)

