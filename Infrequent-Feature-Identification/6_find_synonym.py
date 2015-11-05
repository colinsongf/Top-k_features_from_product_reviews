import nltk 
from nltk.corpus import wordnet

# This function finds synonyms in the list of stemmed/lemmatized words
# The parameter k comes from result of stemming/lemmatization functions
def find_syno(k):
	syn=[]
	for i in wordnet.synsets(k):
		for j in i.lemmas():
			syn.append(j.name())
	print "Synonymes of ============",k,
	print "============"
	print syn
