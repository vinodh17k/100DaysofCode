# Word Negation Tracking

import re
import nltk
from nltk.corpus import wordnet

sentence = "I was not happy with the team's performance in this World Cup"

# I was not_happy with the team's performance in World Cup

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ""

for word in words:
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        word = temp_word + word # Don't use word += temp_word since this makes not_happy to happynot_
        temp_word = ""
    if word != "not":
        new_words.append(word)

mod_sentence = ' '.join(new_words)
mod_sentence = re.sub(r"(\s+)'","'",mod_sentence)
print(mod_sentence)

# I was unhappy with the team's performance in World Cup
new_words2 = []

for word in words:
    antonyms = []
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word # Don't use word += temp_word
        temp_word = ""
    if word != "not":
        new_words2.append(word)

mod2_sentence = ' '.join(new_words2)
mod2_sentence = re.sub(r"(\s+)'","'",mod2_sentence)
print(mod2_sentence)