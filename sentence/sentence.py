sentence=input("enter a sentence\n")
res=''
vowelll=[]
vowell=["a","e","i","o","u"]
for ch in range(len(sentence)):
    for i in range(len(vowell)):
        if sentence[ch]==vowell[i]:
            vowelll.append(vowell[i])

for j in range(len(sentence)):
    if sentence[j] not in vowell:
        res=res+sentence[j]
    else:
        x=vowelll.index(sentence[j])
        x=x+1
        new_v=vowelll[x]
        res+=new_v
print(res)
        