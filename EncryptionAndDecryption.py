#Tri(Will)Luong
#Professor Shebarro
#COSC 4343
#Assignment 2

#--------------------ONE TIME PAD ENCRYPTION-------------------------
#Helper method 1: Converting a particular string into a binary string.
def bitsConverter(a):

    #converting into binary using format() and ord().
    #converting a string into ascii first then to binary and wrap together in the format()
    return ''.join('{:08b}'.format(ord(c)) for c in a)

#Helper method 2: this method will xOR two binary string and return a result binary value.
def xOR(b,c):
    #result string:
    r = []
    for i, j in zip(b,c):
        #xOR between two numbers
        r.append(str(int(i) ^ int(j)))
    return "".join(r)

#Helper Method 3: Converting binary string into a text string:
def bitsToTextString(s):
    result_string = ""
    # #Breaking the binary code into 8-character block and then convert each block into ascii then
    # #into text.
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


#One Time Pad Encryption and Decryption process:
def oneTimePad():
    print("One Time Pad Encryption begins....")

    while True:
        print("Enter your message and key below! They must be of the same length")
        print("")
        msg = input("*******Please enter your message here to encrypt: ")
        key = input("*******Please enter your key to encrypt: ")

        try:
            #Checking if key and message length are equal or not
            if len(msg) == len(key):
                print("****Key and message are valid!*****")
                print("******Begin Encryption Process*****")
                #Conversion and encryption:
                binary_msg = bitsConverter(msg)
                binary_key = bitsConverter(key)
                encrypted_msg = xOR(binary_msg,binary_key)
                print("Encrypted Message: " + encrypted_msg)
                print("")
                #Decryption process:
                print("Begins Decryption.....")
                key2 = input("*****Please enter your key for decryption: ")
                binary_key2 = bitsConverter(key2)
                decrypted_msg_binary = xOR(binary_key2,encrypted_msg)
                decrypted_msg_text = bitsToTextString(decrypted_msg_binary)
                print("")
                print("Original Message: " + decrypted_msg_text)
                print("")

                break

            else:
                print("Invalid Input!!! Key and Message length are not equal!!!!")
                continue
            print("")

        except ValueError:
            print("****Program Is Compromised********")
            break
#--------------------ONE TIME PAD ENCRYPTION---------------------------------------




#-----------------------------RC4 Enryption and Decryption-------------------------
def rC4():
    print("RC4 Encryption begins....")
    print("")
    msg = input("*******Please enter your message here to encrypt: ")
    key = input("*******Please enter your key to encrypt: ")

    #RC4 encryption:
    keyStretch = rc4InitAndStream(key, msg)
    print("")
    print("The orinal message: " + msg)
    print("")
    print("The key stream: ")
    print(keyStretch)
    print("")
    binary_msg = bitsConverter(msg)
    binary_key = bitsConverter(keyStretch)
    encrypted_msg = xOR(binary_msg,binary_key)
    print("Encrypted Message: " + encrypted_msg)
    print("")

    #RC4 decryption:
    if len(keyStretch) == len(msg):
        # #RC4 decryption
        print("")
        print("RC4 decryption begins...")
        print("")
        #converting keystream into binary
        binary_key_stream = bitsConverter(keyStretch)
        decrypted_msg_binary = xOR(binary_key_stream,encrypted_msg)
        decrypted_msg_text = bitsToTextString(decrypted_msg_binary)
        print("The decrypted message: " + decrypted_msg_text)
        print("")
    else:
        print("")
        print("Invalid input! Keystream and message length are not equal!!!!")
        print("")



#Helper method 4: key initialization and keystream generator.
def rc4InitAndStream(key, msg):
    s = list(range(256))    #permutation table
    j = 0    #key initialization:
    msgLen = len(msg)
    for i in list(range(256)):
        j = (j + s[i] + ord(key[i % len(key)])) % 256
        #Swap bytes
        s[i], s[j] = s[j], s[i]

    #Key stream:
    j = 0
    k = 0
    retKeyStream = []
    #stretching out the keystream to the same length as the message length
    while(msgLen > 0):
        msgLen = msgLen - 1
        j = (j + 1) % 256
        k = (k + s[j]) % 256
        #swap bytes:
        s[j], s[k] = s[k], s[j]
        #Adding values to final string:
        retKeyStream.append(chr(s[(s[j] + s[k]) % 256]))

    return ''.join(retKeyStream)

#-----------------------------RC4 Enryption and Decryption-------------------------


#The program main menu:
def menu():
    str = ("1. One Time Pad\n2. RC4\n3. Exit\n Choose: ")
    #only allow int input
    while True:
        try:

            option = input(str)
            return int(option)
            break
        except:
            print("Invalid Opiton! Please try again!")
#main
def main():
    print("***************Please choose an option below to begin!**********")

    while True: #Looping the menu.
        option = menu()
        if option == 1:
            oneTimePad()
        elif option == 2:
            print("Decryption begins....")
            rC4()
        elif option == 3:
            print("Exit.")
            break
        else:
            print("Invalid Option! Please Try again!")

main()
