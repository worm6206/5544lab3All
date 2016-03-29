import json
import os

list1 = [];
list2 = [];
if os.path.exists(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\data.json"):
	fout = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\data.json", "r+")
else:
	fout = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\data.json", "w+")
for i in range(1,11):
	fini = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\\"+str(i)+".txt", "r+")
	d = {}
	d['name'] ="Person"+str(i) + " (" +fini.readline()[:-1] +")"
	d['group'] =i
	list1.append(d)

for i in range(0,10):
	for j in range(i+1,10):
		counter = 0;
		fini = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\\"+str(i+1)+".txt", "r+").readlines()
		finj = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\\"+str(j+1)+".txt", "r+").readlines()
		for k in fini:
			for l in finj:
				if (k==l): counter = counter + 1
		d={}
		d['source'] =i
		d['target'] =j
		d['value'] =counter 
		list2.append(d)

json.dump( {"nodes":list1,"edges":list2}, fout, indent = 2)