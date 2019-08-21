# Finding synonyms and antonyms of words

# Importing wordnet from nltk.corpus
from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())

# print(synonyms) # We get all synonyms of word "good" but with repititions.
print(set(synonyms)) # We get all synonyms of word "good" without repititions.
print(set(antonyms)) # We get all antonyms of word "good" without repititions.

