#Islam








#Sidan









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
