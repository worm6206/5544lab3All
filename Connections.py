import os

inputlist  = [0,107,348,414,686,698,1684,1912,3437,3980];
counter = 0;

for i in inputlist:
	counter = counter + 1
	output = [];
	fin = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\facebook.tar\facebook\facebook\\"+str(i)+".circles","r").readlines()
	if os.path.exists(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\\"+str(counter)+".txt"):
		fout = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\\"+str(counter)+".txt", "r+")
	else:
		fout = open(r"C:\Users\USER\Desktop\Spring2016\5544\Lab3\Connections\\"+str(counter)+".txt", "w+")
	fout.write(str(i))
	for lines in fin:
		words = lines.split()
		for j in range(len(words)):
			if ( j == 0) : continue
			if ( words[j] in output ) : continue
			else:
				output.append(words[j])
				fout.write("\n")
				fout.write(words[j])
		