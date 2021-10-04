#For finding the Student name & marks who got highest marks
d={'aman':39, 'ram':45, 'shyam':76, 'mohan':96, 'aaj':98}
a=max(d,key=d.get)
b=max(d.values())
print(a,b)
