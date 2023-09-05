import nltk
import re

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them"""

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemma = WordNetLemmatizer()

sentences = nltk.sent_tokenize(paragraph)
# print(sentence)

corpus=[]
# Iterate through each sentence
for sentence in sentences:
    # Remove non-alphabetic characters and convert to lowercase
    review = re.sub('[^a-zA-Z]', ' ', sentence).lower()

    # Tokenize the sentence into words
    words = nltk.word_tokenize(review)

    # Remove stopwords and apply lemmatization
    review = [lemma.lemmatize(word) for word in words if word.lower() not in set(stopwords.words("english"))]

    review = ''.join(review)
    print(review)
    corpus.append(review)

    # print(corpus)


from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

x = cv.fit_transform(corpus).toarray()

print(x)







