#Islam
def xor(a, b): 
	result = [] 
	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 
	return ''.join(result) 
def mod2div(divident, divisor): 
	pick = len(divisor) 
	tmp = divident[0 : pick] 
	while pick < len(divident): 
		if tmp[0] == '1': 
			tmp = xor(divisor, tmp) + divident[pick] 
		else:
			tmp = xor('0'*pick, tmp) + divident[pick] 
		pick += 1
	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 
	else: 
		tmp = xor('0'*pick, tmp) 
	checkword = tmp 
	return checkword 
#Sidan
def verifier (data,key):
    l_key = len(key) 
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key) 
    if(int(remainder)==0):
        print("Correct signal.\n")
    else:
        print("Not correct signal.\n")
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
#Saber
def alter(data,bit):
    bit-=1
    mydata = list(data)
    for i in range (len(mydata)):
        if i == bit:
            if(mydata[i] == '0'):
                mydata[i]='1';
            elif(mydata[i] == '1'):
                mydata[i]='0';   
    return ''.join(mydata)
def main():
    data = ""
    key = ""
    print("Welcome to CRC.")
    while (True):
        decision=input("Please Enter 1 to input data from console, 2 from file: ")
        if(decision=='1'):
            data=input("Please enter the data message: ")
            key=input("Please Enter the generator key: ")
            break
        elif(decision=='2'):
            INPUTFILE=input('Please enter file directory: ')
            data, key = readfromfile(INPUTFILE)
            break
        else:
            print("Please enter 1 or 2 only.")
    X=5
    while (X==5):
        print("Data to be transmitted: ",data," and key is: ",key)
        choice = input("To run verifier enter 1, to run generator enter 2, to run alter enter 3, 0 to cancel:\n")
        if(choice=='1'):
            verifier (data,key)
        elif(choice=='2'):
            codeword=generator(data, key)
            writetofile("Output.txt",codeword)
            print("Transmitted signal are printed in file \"Output.txt\" \n")
        elif(choice=='3'):
            bit = input("Please enter the bit while be altered: ")
            data = alter(data,int(bit))
        else:
            print("Thank you for using us. *_* ")
            X=0
    input("Enter any key to close the program.")
if __name__=="__main__":
    main()
