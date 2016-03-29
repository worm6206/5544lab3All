import json
import os

inputlist  = [0,107,348,414,686,698,1684,1912,3437,3980];
counter = 0;
counter2 =0;
list1=[];
list2=[];

for i in inputlist:
	counter = counter + 1
	fout = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\data"+str(i)+".json", "w+")
	fin2 = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\\"+str(counter)+".txt", "r+").readlines()
	counter2 =0	
	for j in fin2:
		d={}
		d['name']= fin2[counter2][:-1]
		d['group']= counter2
		list1.append(d)
		counter2 = counter2 + 1
	fin = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\facebook.tar\facebook\facebook\\"+str(i)+".edges","r").readlines()
	print (counter)
	print (fin2)
	for j in fin:
		print (j)
		words = j.split()
		d={}
		try:
			d['source']= fin2.index((words[0]+"\n"))
		except ValueError: continue
		try:
			d['target']= fin2.index(words[1]+"\n")
		except ValueError: continue
		d['value'] = 1
		list2.append(d)
		counter2 = counter2 + 1 
	json.dump( {"nodes":list1,"edges":list2}, fout, indent = 2)

