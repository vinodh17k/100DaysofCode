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

X = []
for data in dataset:
    vector = []
    for word in freq_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    X.append(vector)

# print(X) # Matrix of vectors

# Creating 2dArray of X
X = np.asarray(X)
print(X)

# Bag of Words Model is created