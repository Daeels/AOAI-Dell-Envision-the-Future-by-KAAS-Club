
import numpy as np
import sys
import pymongo
from pickled import *

pca = unpickled("pca")
clf_elec = unpickled("clf_elec")
clf_indus = unpickled("clf_indus")
clf_meca = unpickled("clf_meca")

client = pymongo.MongoClient("ommited, this is just for demonstration purposes")
db = client.students

notes = db.aoai.find_one({ "id" : str(sys.argv[1]) })["notes"]
liste = np.array([float(note) for note in notes]).reshape(1, -1)

X = pca.transform(liste)
print('{ "gi" : "' + str(float("{:.2f}".format(clf_indus.predict(X)[0]* 100))) + '", "gm" : "' + str(float("{:.2f}".format(clf_meca.predict(X)[0]* 100))) + '" , "ge" : "' + str(float("{:.2f}".format(clf_elec.predict(X)[0]* 100))) + '" }')
