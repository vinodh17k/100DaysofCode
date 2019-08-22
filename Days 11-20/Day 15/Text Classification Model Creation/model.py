# Text Classification using NLP

# Importing libraries
import os
import pathlib
import numpy as numpy
import nltk
import pickle
import re
from nltk.corpus import stopwords
from sklearn.datasets import load_files
# nltk.download('stopwords')

current_file = pathlib.Path(__file__)
current_location = current_file.parent.absolute()
os.chdir(current_location)
os.getcwd()

# Importing dataset (Original Source of Dataset is "http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz")
reviews = load_files("txt_sentoken/") # load files function should be used only for small datasets.
x,y = reviews.data,reviews.target # Since neg folder is first in text_sentoken, it's class is 0 and for pos its class is 1.

# for i in range(len(x)):
#     x[i] = ''.join(l[:-1] for l in open(x[i]))

# Storing as pickle files
with open('x.pickle','wb') as f:
    pickle.dump(x,f)

with open('y.pickle','wb') as f:
    pickle.dump(y,f)

# Unpickling the dataset
with open('x.pickle','rb') as f:
    x = pickle.load(f)

with open('y.pickle','rb') as f:
    y = pickle.load(f)

# print(x[1:2],y[1:2])

# Creating the corpus by pre-processing the dataset
corpus = []

for i in range(len(x)):
    review = re.sub(r'\\n','',str(x[i])) #Replacing all \n (new-line tags which are created during unpickling) with a single space
    review = re.sub(r'\W',' ',review) # Replacing special characters with a single space.
    review = review.lower() # Lowercasing if any uppercase letters
    review = re.sub(r'\s+[a-z]\s+',' ',review) # Replacing single alphabets surrounded by single space on both sides with a single space
    review = re.sub(r'^b\s+',' ',review) # Replacing single alphabets following a single space at start of the sentence with a single space
    review = re.sub(r'\s+b$',' ',review) # Replacing single alphabets followed a single space at end of the sentence with a single space
    review = re.sub(r'\s+',' ',review) # Replacing mutliple consecutive spaces with a single space
    corpus.append(review)

# print(corpus[1:2])

# Till now we have processed the data.
