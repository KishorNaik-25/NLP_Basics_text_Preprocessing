import nltk


paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them"""

import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

wordnet = WordNetLemmatizer()

sentences = nltk.sent_tokenize(paragraph)
corpus=[]

for i in range(len(sentences)):
    # Remove non-alphabetic characters and convert to lowercase
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    words = review.split()
    # print(words)
    review = [wordnet.lemmatize(word) for word in words if word not in set(stopwords.words("english"))]
    print(review)
    review = ' '.join(review)
    # print(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()

print(X)







