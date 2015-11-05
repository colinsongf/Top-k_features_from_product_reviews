import itertools
import sys
import time
import nltk 
from nltk.corpus import stopwords
import MySQLdb
from nltk.stem import WordNetLemmatizer

# Tokenize the review text sentence
def tokenize(file_name):
    # Assumes that sentences are separated by a single '.'.
    # Assumes that words are separated by a single ' '.
    # Tokenizes each sentence, removes duplicate tokens, sorts tokens.
    return [sorted(list(set(e.split()))) for e in
            open(file_name).read().strip().split('.')]

def axtract(i):
	filter_word=[]
	stop_word1=set(stopwords.words("english"))
	for key in i:
		if key not in stop_word1:
 			filter_word.append(key)
	
	stop_word.append(filter_word)
	

def stopword1(token):
	filter_word=[]
	for i in token:
	  axtract(i)
	  
def axtract2(i):
	filter_word1=[]
	lema=WordNetLemmatizer()
	for key in i:
 		filter_word1.append(lema.lemmatize(key))
	after_lema.append(filter_word1)

def lema(stop_word):
	for i in stop_word:
	   axtract2(i)
 
def frequent_itemsets(sentences):
    # Counts sets with Apriori algorithm.
    SUPP_THRESHOLD = 4
    supps = []
 
    supp = {}
    for sentence in sentences:
        for key in sentence:
            if key in supp:
                supp[key] += 1
            else:
                supp[key] = 1
    #print "|C1| = " + str(len(supp))
    supps.append({k:v for k,v in supp.iteritems() if v >= SUPP_THRESHOLD})
    #print "|L1| = " + str(len(supps[0]))
 
    supp = {}
    for sentence in sentences:
        for combination in itertools.combinations(sentence, 2):
            if combination[0] in supps[0] and combination[1] in supps[0]:
                key = ','.join(combination)
                if key in supp:
                    supp[key] += 1
                else:
                    supp[key] = 1
    #print "|C2| = " + str(len(supp))
    supps.append({k:v for k,v in supp.iteritems() if v >= SUPP_THRESHOLD})
    #print "|L2| = " + str(len(supps[1]))
 
    supp = {}
    for sentence in sentences:
        for combination in itertools.combinations(sentence, 3):
            if (combination[0]+','+combination[1] in supps[1] and
                    combination[0]+','+combination[2] in supps[1] and
                    combination[1]+','+combination[2] in supps[1]):
                key = ','.join(combination)
                if key in supp:
                    supp[key] += 1
                else:
                    supp[key] = 1
    #print "|C3| = " + str(len(supp))
    supps.append({k:v for k,v in supp.iteritems() if v >= SUPP_THRESHOLD})
    #print "|L3| = " + str(len(supps[2]))
 
    return supps
 
def measures(supp_ab, supp_a, supp_b, transaction_count):
    # Assumes A -> B, where A and B are sets.
    conf = float(supp_ab) / float(supp_a)
    s = float(supp_b) / float(transaction_count)
    lift = conf / s
    if conf == 1.0:
        conv = float('inf')
    else:
        conv = (1-s) / (1-conf)
    return [conf, lift, conv]
 
def generate_rules(measure, supps, transaction_count):
    rules = []
    CONF_THRESHOLD = 0.70
    for i in range(2, len(supps)+1):
            for k,v in supps[i-1].iteritems():
                k = k.split(',')
                for j in range(1, len(k)):
                    for a in itertools.combinations(k, j):
                        b = tuple([w for w in k if w not in a])
                        [conf, lift, conv] = measures(v,
                                supps[len(a)-1][','.join(a)],
                                supps[len(b)-1][','.join(b)],
                                transaction_count)
                        if conf >= CONF_THRESHOLD:
                            rules.append((a, b, conf, lift, conv))
            rules = sorted(rules, key=lambda x: (x[0], x[1]))
            rules = sorted(rules, key=lambda x: (x[2]), reverse=True)
    return rules
    
stop_word =[]
after_lema=[]

def main():
    file = open("test.txt", "w")

    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="subrata17", # your password
                      db="testdb1") # name of the data base
    cur = db.cursor()

    cur.execute("SELECT reviewText FROM  reviewElectronicsHelpful WHERE prodid='0528881469'")
    for row in cur.fetchall() :
           file.write(row[0])
	   file.write("\n")
    file.close()
    
    sentences = tokenize("test.txt")
    
    stopword1(sentences)
    lema(stop_word)
    start_time = time.time()
    supps = frequent_itemsets(after_lema)
    print supps
    print ""
    
    end_time = time.time()
    print "Time spent finding frequent itemsets = {:.2f} seconds.".format(
          end_time - start_time)
 
    start_time = time.time()
    measure='conf'
    rules = generate_rules(measure, supps, len(after_lema))
    for rule in rules:
        print ("{{{}}} -> {{{}}}, "
               "conf = {:.2f}").format(
              ', '.join(rule[0]), ', '.join(rule[1]), rule[2], rule[3], rule[4])
    end_time = time.time()
    print "Time spent finding association rules = {:.2f} second.".format(
          end_time - start_time)
 
if __name__ == "__main__":
    main()
