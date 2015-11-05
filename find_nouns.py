# From the result of POS tagging, only words tagged as nouns are found

import MySQLdb
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# This function tokenize the review sentence and returns its result
def get_tokens(row):
    token = word_tokenize(row)
    return token
    
# This function performs POS tagging and returns its result
def pos(token):
    tagged = nltk.pos_tag(token)
    return tagged

# This function finds NOUNS from all the different tags
def Find_Noun(tagged):
	find_noun=[]
	word_tag_fd = nltk.FreqDist(tagged)
	temp=([wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'NN' or wt[1]=='NNP' or wt[1]=='NP' or wt[1]=='NNPC' or wt[1]=='NNS'])
	for i in temp:
		find_noun.append(i.lower())
	return find_noun

# Beginning of main
if __name__ == "__main__":

    # Connect to database
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
            user="root", # your username
            passwd="password", # your password
            db ="testdb1") # name of the data base
    cur = db.cursor()

    # Query statement
    cur.execute("SELECT reviewText FROM  reviewElectronicsHelpful WHERE prodid='0528881469'")
    i = 0
    for row in cur.fetchall() :
        print "\n\n","Review = : ",i," Data = : ",row
    	
    	# Function call
    	token = get_tokens(row[0])
    	print ""
    	print("tokens = %s") %(token)
    	
    	# Function POS() is called
    	tagged = pos(token)
    	print("POS = %s") %(tagged)
    	
    	# Function call
    	find_noun=Find_Noun(tagged)
    	print ""
    	print("find_noun = %s") %(find_noun)
    	
	    i += 1
