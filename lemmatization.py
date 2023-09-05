import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them"""

lemm = WordNetLemmatizer()

sent = nltk.sent_tokenize(paragraph)

for i in range(len(sent)):
    words = nltk.word_tokenize(sent[i])
    words = [lemm.lemmatize(word)for word in words if word not in set(stopwords.words("english"))]
    print(words)
    sent[i]=''.join(words)
print(sent)