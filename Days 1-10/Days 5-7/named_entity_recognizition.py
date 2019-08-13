import nltk

paragraph = "The Taj Mahal was built by Emperor Shah Jahan"

words = nltk.word_tokenize(paragraph)

tagged_words  = nltk.pos_tag(words) # POS Tag generation

namedEnt = nltk.ne_chunk(tagged_words) # Named Entity Recognizition
namedEnt.draw() # Visualizing Named Entity Recognizition
