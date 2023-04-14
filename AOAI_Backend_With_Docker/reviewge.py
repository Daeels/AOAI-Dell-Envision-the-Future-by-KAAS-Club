import numpy as np
import sys
from pickled import *
import pymongo

clf_elec_interest = unpickled("clf_elec_interest")

client = pymongo.MongoClient("mongodb+srv://tfa7a:tfa7a123@aoai-cluster.tzpfo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.students

notes = db.aoai.find_one({ "id" : str(sys.argv[1]) })["notes"]
liste = np.array([float(note) for note in notes]).reshape(1, -1)

#elec
X_elec = clf_elec_interest.predict(liste)
for j in range(len(X_elec[0])) : 
    X_elec[0][j] = round(X_elec[0][j]*5) 
    if X_elec[0][j] == 0 :
        X_elec[0][j] += 1
print('{ "list" :  '  + str([int(x) for x in X_elec[0]]) + '}')

