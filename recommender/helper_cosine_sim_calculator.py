# A Simple Cosine Sim implementation to compare Job Description and
# resume

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def get_sim( text1, text2):
	if text1 is None or text2 is None:
		#report error
		return -1
	tfidf = vectorizer.fit_transform([text1, text2])
	#print ((tfidf * tfidf.T).A)
	return ((tfidf * tfidf.T).A)[0,1]

if __name__ == '__main__':
    print "Cosine similarity = " + str(get_sim('a little bird', 'a little bird'))
    print get_sim('a little bird', 'a little bird chirps')
    print get_sim('a little bird', 'a big dog barks')
