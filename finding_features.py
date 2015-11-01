import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import MySQLdb
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.api import StemmerI
from nltk.stem.regexp import RegexpStemmer
from nltk.stem.isri import ISRIStemmer
from nltk.stem.rslp import RSLPStemmer
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree
from nltk.corpus import wordnet


def get_tokens(row):
		token = word_tokenize(row)
		#token.append(i)
	        return token


def stopword1(token):
	#stop_word =[]
	stop_word=set(stopwords.words("english"))
	#print stop_word
	for i in token:
		if i not in stop_word:
 			filter_word.append(i)		
        return
def steming():
	ps=PorterStemmer
 	for i in filter_word:
           after_steming.append(i) 
def pos():
	 tagged = nltk.pos_tag(after_steming)
  	 return tagged
def chunk(tagged):
	chunkGram= r"""chunk: {<NN>}"""
	chunkParser=nltk.RegexpParser(chunkGram)
	after_chunked=chunkParser.parse(tagged)
	#after_chunked.draw()
	#after_chunked=nltk.ne_chunk(tagged)
        return after_chunked

def find_syno(k):
	syn=[]
	for i in wordnet.synsets(k):
		for j in i.lemmas():
			syn.append(j.name())
	print "Synonymes of",k
	print syn
	 

        


filter_word=[]
after_steming=[]
after_pos=[]

if __name__ == "__main__":
	
	db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="subrata17", # your password
                      db="testdb1") # name of the data base
        cur = db.cursor()

        cur.execute("SELECT reviewText FROM  reviewElectronicsHelpful WHERE prodid=0439886341 LIMIT 2")
        i=0
	for row in cur.fetchall() :
           print "\n\n","Review = : ",i," Data = : ",row
           
	   string1=row[0]
	   print ""
	   token=get_tokens(string1)
	   print("tokens = %s") %(token)
           stopword1(token)
	   print ""
	   print("Stop Word = %s") %(filter_word)
           steming()
	   print ""
	   print("Steming = %s") %(after_steming)
	   tagged=pos()
	   print ""
           print("POS = %s") %(tagged)
           after_chunked=chunk(tagged)
	   print ""
	   print("Chunk = %s") %(after_chunked)
	   print ""
	   for k in after_steming:
	        find_syno(k)
	   i+=1
	
