from gensim.parsing import PorterStemmer

global_stemmer = PorterStemmer()

class StemmingHelper():

    word_lookup = {}

    @classmethod
    def stem(cls, word):
        stemmed = global_stemmer.stem(word)

        if stemmed not in cls.word_lookup:
            cls.word_lookup[stemmed] = {}
        cls.word_lookup[stemmed][word] = (cls.word_lookup[stemmed].get(word, 0) + 1)

        return stemmed

    @classmethod
    def original_form(cls, word):
        if word in cls.word_lookup:
            return max(cls.word_lookup[word].keys(), key=lambda x: cls.word_lookup[word][x])
        else:
            return word
