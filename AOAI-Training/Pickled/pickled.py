import pickle 
import os.path
def pickled(variable,string) :
    directory = os.path.join("C:/Users/lenovo/Desktop/AOAI/pickled",string+".pickle")
    pickle_out = open(directory,"wb")
    pickle.dump(variable,pickle_out)
    pickle_out.close()
def unpickled(string) :
    directory = os.path.join("C:/Users/lenovo/Desktop/AOAI/pickled",string+".pickle")
    pickle_in = open(directory,"rb")
    variable = pickle.load(pickle_in)
    return variable