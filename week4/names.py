lmbd = {}

with open("names.txt") as f:
    names = f.readlines()
    for elem in names:
         name, sex, quant = elem.strip().split(",")
         if sex == "F":
             lmbd[name] = int(quant)
for w in sorted(lmbd, key=lmbd.get, reverse=True):
    print w, lmbd[w]