# The result of get_tokens() function is used and POS tagging is done here

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
	
		i += 1
