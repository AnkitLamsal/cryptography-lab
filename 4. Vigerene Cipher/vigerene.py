def char_to_num(value):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    value_len = list()
    for i in range(len(value)):
        for j in range(len(alphabet)):
            if value[i] == alphabet[j]:
                value_len.append(j)
    return value_len

def num_to_char(list_value):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    converted_str = ''
    for i in range(len(list_value)):
        for j in range(len(alphabet)):
            if list_value[i]==j:
                converted_str+=alphabet[j]
    return converted_str

def encrypt(message, key):
    message_len = len(message)
    if(message_len != len(key)):
        temp_key = key[::]
        diff = message_len - len(key)
        for x in range(diff):
            temp_key = temp_key + key[x]
        key = temp_key
    key_list = char_to_num(key)
    msg_list = char_to_num(message)
    cipher_list = list()
    for i in range(message_len):
        cipher_list.append((key_list[i]+msg_list[i])%26)
    cipher = num_to_char(cipher_list)   
    print("cipher text is:"+cipher) 

def decrypt(message, key):
    cipher_len = len(message)
    if(cipher_len != len(key)):
        temp_key = key[::]
        diff = cipher_len - len(key)
        for x in range(diff):
            temp_key = temp_key + key[x]
        key = temp_key
    key_list = char_to_num(key)
    cipher_list = char_to_num(message)
    plain_list = list()
    for i in range(cipher_len):
        plain_list.append((cipher_list[i]-key_list[i])%26)
    plain = num_to_char(plain_list)   
    print("plain text is:"+plain) 
        
# decrypt("hrvthaoml","ankit")
def menu():
    while(1):
        print("1. Enter Key (By default: hello)")
        print("2. Enter Message (By default: plain)")
        print("3. Encrypt Message.")
        print("4. Decrypt Message.")
        print("5. Exit")
        choice = input("Enter your choice:")
        if(choice == '1'):
            key = input("Key:")
            if(key == ''):
                key = 'hello'
        elif(choice == '2'):
            message = input("Message:")
            if(message == ''):
                message = 'plain'
        elif(choice == '3'):
            encrypt(message,key)
        elif(choice == '4'):
            decrypt(message,key)
        elif(choice == '5'):
            exit()
        else:
            print("wrong choice. terminating program")
            exit()
    
menu()