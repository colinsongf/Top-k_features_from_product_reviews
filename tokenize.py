# First, record is fetched from the database in line 16 and then reviews are then worked upon
# The text review sentences are tokenized one-by-one and finally all the tokens are printed

import MySQLdb
import nltk
from nltk.tokenize import word_tokenize


# This function tokenize the review sentence and returns its result
def get_tokens(row):
    token = word_tokenize(row)
    return token

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
	i += 1
