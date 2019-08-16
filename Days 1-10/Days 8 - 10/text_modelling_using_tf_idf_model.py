# TF-IDF Model.

# Pros: 
# • Some semantic information is preserved.

# TF = Term Frequency (Document specific, which means it changes from doc to doc for each word in doc.)
# IDF = Inverse Document Frequency (Constant for entire corpus/dataset for each word.)
# TF-IDF means TF*IDF

#       (Number of occurences of a word in a document)
# TF = -------------------------------------------------
#           (Number of words in that document)


#                       (Number of documents)
# IDF = log(----------------------------------------------)
#               (Number of documents containing word)


#  Eg::
#  Doc1 = "to be or not to be"
#  Doc2 = "to be a bee or not to be a bee without being a bee" 

# => TF of 'to' and 'be' is 2/6, TFs of 'or' and 'not' is 1/6 in Doc1
# => TF of 'bee' and 'a' is 3/14, TF of 'to' and 'be' is 2/14, TF of 'or','not','without','being' is 1/14 in Doc2
# This implies sum of TFs of words for each document is 1. 

# ----------------------------------------------------------------------------------------------------------------

# IDF of 'to','be','or','not' = log(2/2) = log 1 = 0
# IDF of 'a','bee','without','being' = log(2/1) = log 2 =  0.693

# This implies common words of all documents have IDF as '0'.
# And maximum IDF Value can only be "log(no.of documents)" if conditions satisfy.


# TF Table:
# --------------------------------------------
# | Words/Documents |    Doc1   |    Doc2    |
# --------------------------------------------
# |       to        |    0.333  |    0.142   |
# |       be        |    0.333  |    0.142   |
# |       or        |    0.167  |    0.071   |
# |       not       |    0.167  |    0.071   |
# |       a         |     0     |    0.214   |
# |       bee       |     0     |    0.214   |
# |       without   |     0     |    0.071   |
# |       being     |     0     |    0.071   |
# --------------------------------------------
# |     Total       |     1     |  1(approx) |
# --------------------------------------------


# IDF Table:
# --------------------------------
# |      Words      |  IDF Value |
# --------------------------------
# |       to        |      0     |
# |       be        |      0     |
# |       or        |      0     |
# |       not       |      0     |
# |       a         |    0.693   |
# |       bee       |    0.693   |
# |       without   |    0.693   |
# |       being     |    0.693   |
# --------------------------------

# Finally onto TF-IDF Calculations.
# TF-IDF(Word) =  TF(Document,Word)*IDF(Word)

# TF-IDF Table:
# ----------------------------------------------------------------------------------
# | Words/Documents |  to  |  be  |  or  |  not  |   a   |  bee  | without | being |
# ----------------------------------------------------------------------------------
# |       Doc1      |  0   |  0   |  0   |   0   |   0   |   0   |    0    |   0   |
# |       Doc2      |  0   |  0   |  0   |   0   | 0.148 | 0.148 |  0.495  | 0.495 |
# ----------------------------------------------------------------------------------

# This implies words that commonly occur in every document gets TF-IDF Values as '0' in every document due to IDF Values of '0' by default.

# Difference between bag of words and TF-IDF Models is:
# • Bag of Words Model contained only 0's and 1's which means all words assigned with 1 are equal important which really isn't the ideal case.
# • Whereas, in TF-IDF Model, we get know which words are most important and which words are less important.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import nltk
import re
import heapq # To get 'n' most frequent words
import numpy as np

paragraph = """Thank you all so very much. Thank you to the Academy. Thank you to all of you in this room. I have to congratulate the other incredible nominees this year. The Revenant was the product of the tireless efforts of an unbelievable cast and crew. First off, to my brother in this endeavor, Mr. Tom Hardy. Tom, your talent on screen can only be surpassed by your friendship off screen â€¦ thank you for creating a transcendent cinematic experience. Thank you to everybody at Fox and New Regency â€¦ my entire team. I have to thank everyone from the very onset of my career â€¦ To my parents; none of this would be possible without you. And to my friends, I love you dearly; you know who you are. And lastly, I just want to say this: Making The Revenant was about man's relationship to the natural world. A world that we collectively felt in 2015 as the hottest year in recorded history. Our production needed to move to the southern tip of this planet just to be able to find snow. Climate change is real, it is happening right now. It is the most urgent threat facing our entire species, and we need to work collectively together and stop procrastinating. We need to support leaders around the world who do not speak for the big polluters, but who speak for all of humanity, for the indigenous people of the world, for the billions and billions of underprivileged people out there who would be most affected by this. For our childrenâ€™s children, and for those people out there whose voices have been drowned out by the politics of greed. I thank you all for this amazing award tonight. Let us not take this planet for granted. I do not take tonight for granted. Thank you so very much."""

# Tokenizing data into sentences
dataset = nltk.sent_tokenize(paragraph)

# Pre-processing dataset

for i in range(len(dataset)):
    dataset[i] = dataset[i].lower() # Converting all uppercase to lowercase to maintain consistence for future processing
    dataset[i] = re.sub(r'\W',' ',dataset[i]) # Replacing all non-word characters with space.
    dataset[i] = re.sub(r'\s+',' ',dataset[i]) # Replacing all multiple spaces with single space.
    
# print(dataset) # Pre-processed dataset

# Creating the word-count dictionary/histogram
word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data) # Word Tokeinzing each sentence
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1 # If word isn't listed yet in word2count, make its count as 1.
        else:
            word2count[word] += 1 # Incrementing the number of times a word appears

# print(word2count) # Dicitionary containing words and their frequency of appearance as keys and values
freq_words = heapq.nlargest(100,word2count,key=word2count.get) # Syntax:(n,dict_name,key)
# print(freq_words) # Shows the most frequent 100 words based on word count.

# IDF Matrix

word_idfs = {}

for word in freq_words:
    doc_count = 0
    for data in dataset:
        if word in nltk.word_tokenize(data):
            doc_count += 1
    word_idfs[word] = np.log(len(dataset)/(1+doc_count)) # The +1 used here is a bias/standard as per real world applications due to some terms which are least frequent(or absent) in corpus which cause zero-divison error and it can be omitted as per our requirements, but +1 is recommended by every top-notch data scientists to maintain code consistency.

# TF Matrix

tf_matrix = {}
for word in freq_words:
    doc_tf = []
    for data in dataset:
        freq = 0
        for w in nltk.word_tokenize(data):
            if w == word:
                freq += 1
        tf_word = freq/len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
    tf_matrix[word] = doc_tf

# TF-IDF Calculations
tfidf_matrix = []
for word in tf_matrix.keys():
    tfidf_word = []
    for value in tf_matrix[word]:
        score = value * word_idfs[word]
        tfidf_word.append(score)
    tfidf_matrix.append(tfidf_word)

# Converting TF-IDF Matrix into 2D Array
X = np.asarray(tfidf_matrix)

# Transposing
X = np.transpose(X)

# This is our TF-IDF Model.