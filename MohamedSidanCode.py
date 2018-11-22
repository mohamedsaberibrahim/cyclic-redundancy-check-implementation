def verifier (data,key):
    l_key = len(key) 
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key) 
    if(int(remainder)==0):
        print("Correct signal.")
    else:
        print("Not correct signal.")
def generator(data, key): 
	l_key = len(key) 
	appended_data = data + '0'*(l_key-1)
	remainder = mod2div(appended_data, key) 
	codeword = data + remainder 
	return codeword
def readfromfile(fileName):
    infile=open(fileName,'r')
    data = infile.readline()
    key = infile.readline()
    return data, key
def writetofile(fileName,transmitted_data):
    outfile=open(fileName,'w')
    outfile.write(transmitted_data)