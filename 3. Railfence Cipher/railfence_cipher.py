def get_text():
    return input("Enter the Text.\n")
def get_row():
    return int(input("Enter the row for encryption:"))
def encrypt():
    val = get_text()
    # row = get_row()
    first_row = []
    second_row =[]
    for text in range(0,len(val),2):
        first_row.append(val[text])
        if(text==len(val)-1):
            pass
        else:
            second_row.append(val[text+1])
    encrypted_list = first_row + second_row
    encrypted_val = ''.join(encrypted_list)
    print('The Encrypted Value is:'+encrypted_val)

def decrypt():
    val = get_text()
    # print(len(val))
    text = int((len(val)-1)/2)
    row_1 = val[0:text+1]
    row_2 = val[text+1:]
    decrypted_list = []
    for i in range(0,len(row_1)):
        decrypted_list.append(row_1[i])
        if(i==len(row_2)):
            pass
        else:
            decrypted_list.append(row_2[i])
    # print(decrypted_list)
    decrypted_sentence = ''.join(decrypted_list)
    print("Decrpyted Sentence is :"+decrypted_sentence)

def menu():
    val = input('Enter E to Encrypt \nEnter D to Decrypt.\n')
    if(val.lower() == "e"):
        encrypt()
    elif(val.lower() == "d"):
        decrypt()
    else:
        menu()

menu()