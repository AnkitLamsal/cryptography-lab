monarchy_key = [['m','o','n','a','r'],
                ['c','h','y','b','d'],
                ['e','f','g','i','k'],
                ['l','p','q','s','t'],
                ['u','v','w','x','z']]

def find_index(key, char):
    for sub_list in key:
        if char in sub_list:
            return(key.index(sub_list),sub_list.index(char))
# (a,b)=find_index(monarchy_key, 'a')
def split_pad_text(text):
    temp = []
    i = 0
    # In this loop, checks the one after next value if same value repeated, adds x in between the value. 
    for char in text:
        if (len(text)>=i):
            if (text[i-1] == text[i]):
                temp.append('x')
                temp.append(text[i-1])
            else:
                temp.append(char)
        i+=1
    # Adding the x value if, there is odd value at last.
    if (len(temp)%2 == 1):
        temp.append('x')
    return temp

# split_two('hello')
def encrypt():
    plain_text = input("\n Enter the plain text which is to be encrypted:")
    split = split_pad_text(plain_text)
    enc_list = []
    for i in range(0, len(split),2):
        row_1, col_1 = find_index(monarchy_key,split[i])
        row_2, col_2 = find_index(monarchy_key,split[i+1])
        if (col_1==col_2):
            val1 = monarchy_key[(row_1+1)%5][col_1]
            val2 = monarchy_key[(row_2+1)%5][col_2]
        elif (row_1==row_2):
            val1 = monarchy_key[row_1][(col_1+1)%5]
            val2 = monarchy_key[row_2][(col_2+1)%5]
        else:
            val1 = monarchy_key[row_1][col_2]
            val2 = monarchy_key[row_2][col_1]
        enc_list.append(val1)
        enc_list.append(val2)
        enc_str = ''.join(enc_list)
    print(enc_str) 

def remove_pad(text):
    # print(text)
    temp = text
    if(text[len(text)-1] == 'x'):
        temp = text[0:len(text)-1]
    temp = list(temp)
    for i in range(0,len(temp)-2):
        # print(temp[i],temp[i+2])
        # print('\n')
        if(temp[i]==temp[i+2] and temp[i+1]=='x'):
            temp[i+1]=''
    removed = ''.join(temp)
    print("Decrypted Value is:"+removed)
            
            
def decrypt():
    cipher_text = input("Enter the plain text which is to be decrypted:")
    split = split_pad_text(cipher_text)
    dec_list = []
    for i in range(0, len(split),2):
        row_1, col_1 = find_index(monarchy_key,split[i])
        row_2, col_2 = find_index(monarchy_key,split[i+1])
        if (col_1==col_2):
            val1 = monarchy_key[(row_1-1)%5][col_1]
            val2 = monarchy_key[(row_2-1)%5][col_2]
        elif (row_1==row_2):
            val1 = monarchy_key[row_1][(col_1-1)%5]
            val2 = monarchy_key[row_2][(col_2-1)%5]
        else:
            val1 = monarchy_key[row_1][col_2]
            val2 = monarchy_key[row_2][col_1]
        dec_list.append(val1)
        dec_list.append(val2)
        dec_str = ''.join(dec_list)
    remove_pad(dec_str)

def menu():
    print("""Enter 'E' to Encrypt \nEnter 'D' to Decrypt. \n""")
    choice = input("\n What is Your Choice :")
    if(choice.lower()=='e'):
        encrypt()
    elif(choice.lower()=='d'):
        decrypt()
    else:
        menu()
    
menu()