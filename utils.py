import random

class MCMC():
    def __init__(self, data, tlen=1):
        self.model = self.create_model(data, tlen)
        
    def create_model(self, data, tlen):
        out = dict()
        for name in data:
            name = tlen*"<"+name+">"
            for i in range(len(name)-tlen):
                if name[i:i+tlen] not in out.keys():
                    out[name[i:i+tlen]] = {name[i+tlen]: 1}
                else:
                    if name[i+tlen] not in out[name[i:i+tlen]].keys():
                        out[name[i:i+tlen]][name[i+tlen]] = 1
                    else:
                        out[name[i:i+tlen]][name[i+tlen]] += 1
        return out
    
    def generate(self, start=""):
        tokenlaenge = len(list(self.model.keys())[0])
        name = tokenlaenge*"<"+start
        while name[-1]!=">":
            name = name+self.ziehe(self.model[name[-tokenlaenge:]])
        return name.replace("<", "").replace(">", "")
    
    def ziehe(self, dictionary):
        summe = sum(list(dictionary.values()))
        z = random.randint(0,summe-1)
        for k,v in dictionary.items():
            z -= v
            if z<0:
                return k
            

def load_data(path):
    with open(f"data/{path}.txt", "r", encoding="utf-8") as f:
        data = f.read().upper().split("\n")
    return data