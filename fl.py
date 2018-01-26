from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5403)

@app.route('/booyah', methods=['GET','POST'])
def booyah(userstuff):
	print('Hello')
	import pickle
	import numpy
	from sklearn.metrics import pairwise
	from nltk.stem import PorterStemmer
	import re
	from nltk.corpus.stopwords import words
    
    
	with open('tfidf.pickle.dat', 'rb') as pickle_file:tfidf = pickle.load(pickle_file)

	with open('TEDxsubs.pickle.dat', 'rb') as pickle_file: AllSubs = pickle.load(pickle_file)
	def cleaner(MessyString):
		ProcessedSubs=[]
		LemmaString=''
		tempstring=MessyString
		tempstring=tempstring.replace('\n', ' ')
		for char in '0123456789!:",;-':
			tempstring=re.sub(char,'',tempstring)
		tempstring=re.sub('\?','',tempstring)
		tempstring=re.sub('\.','',tempstring)
		ProcessedSubs.append(tempstring)
		tempstring=tempstring.replace('\'', '')
		tempstring=tempstring.replace('  ', ' ')
		tempstring=tempstring.strip()+'\n'
		tempstring=tempstring.lower()
		#     l=nltk.wordnet.WordNetLemmatizer()#doesn't work well at all
		stemmer=nltk.stem.PorterStemmer()

		wordlist=tempstring.split()
		StopWords=nltk.corpus.stopwords.words("english")
		
		templist=[]
		for word in wordlist:   
			if not word in StopWords:
		#             templist.append(stemmer.stem(word)) #stemming didn't produce any better tsne models and resulted in increased numbers of words not found in google's vector space.
				templist.append(word)

		tfidf_vectorizer = TfidfVectorizer(max_features=N_fea, stop_words='english')
		tfidf = tfidf_vectorizer.fit_transform(templist)
		return(templist)

	def recommender(userstring, model):
		dist=[]
		sim=[]
		spmat=tfidf_vectorizer.transform([' '.join(cleaner(userstring))])
		for i in tfidf.todense():
			dist.append(pairwise.cosine_distances(spmat, i))
			sim.append(pairwise.cosine_similarity(spmat, i))
		return(numpy.argmin(dist), min(dist), AllSubs[numpy.argmin(dist)]) 
	ix, MIN, talk = recommender(userstuff, tfidf.todense())
	return flask.jsonify(talk)
