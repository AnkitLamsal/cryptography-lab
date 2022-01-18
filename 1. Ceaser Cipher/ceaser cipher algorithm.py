def encrypt_decrypt(val,add_val,choice):
    enc_dec_no = []
    # Encryption
    if choice == 'e':
        for number in val:
            number+=3
            number%=26
            enc_dec_no.append(number)
    # Decryption 
    elif choice == 'd':
        for number in val:
            number-=3
            if number in range(-2,1):#-2,-1,0
                number+=26
            print(number)
            enc_dec_no.append(number)
    return enc_dec_no

def letter_to_no(letters):
    letters=letters.lower()
    # Changing Unicode to Numbers
    numbers = [ord(letter) - 96 for letter in letters]
    return numbers

def no_to_letter(numbers):
    # Changing Numbers to Unicode 
    letter = [chr(number+96) for number in numbers]
    return letter

def encryption_decryption():
    choice = input(''' Enter "e" for encryption ! \n Enter "d" for decryption! ''')
    text = input("Enter the text:\t")
    y = int(input("Enter ceaser key:\t"))
    sentence_list = text.split()
    # Word Split and for loop for all text
    encrypted_decrypted_list = []
    for word in sentence_list:
        #conversion of letter to number
        word_ = letter_to_no(word)
        # Encryption/Decryption
        encrypted_decrypted_number = encrypt_decrypt(word_,y,choice)
        #conversion of number to letter
        encrypted_decrypted_text = no_to_letter(encrypted_decrypted_number)
        # joining all letters to word
        encrypted_decrypted_word = ''.join(encrypted_decrypted_text)
        encrypted_decrypted_list.append(encrypted_decrypted_word)
    # Joining all words to sentence 
    encrypted_decrypted_sentence = ' '.join(encrypted_decrypted_list)
    if choice =='e':
        print('''Your encrypted Sentence is:"'''+encrypted_decrypted_sentence+'''" ''')
    elif choice =='d':
        print('''Your decrypted Sentence is:"'''+encrypted_decrypted_sentence+'''" ''')
encryption_decryption()