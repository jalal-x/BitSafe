import string 
import random
import os
from cryptography.fernet import Fernet #encryption module 
from getpass import getpass
import json


print("Welcome to")
print("""
██████╗░██╗████████╗░██████╗░█████╗░███████╗███████╗
██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝
██████╦╝██║░░░██║░░░╚█████╗░███████║█████╗░░█████╗░░
██╔══██╗██║░░░██║░░░░╚═══██╗██╔══██║██╔══╝░░██╔══╝░░
██████╦╝██║░░░██║░░░██████╔╝██║░░██║██║░░░░░███████╗
╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝""") 

#########################################################################################################################################
with open("data.json") as file:
    data = json.load(file)

if data["password-made"] == "no":
    phrasekey =  Fernet.generate_key()  #encryption key
    with open("phrase_key.key", "wb")  as phrase_key:
        phrase_key.write(phrasekey)

    master_pwrd = input("Create a master password: ")
    with open('secretphrase.txt', 'w') as outfile:
            outfile.write(master_pwrd)
    with open('secretphrase.txt', 'rb') as file:
            contents = file.read()

    contents_encrypted = Fernet(phrasekey).encrypt(contents)
    with open("secretphrase.txt", "wb") as thefile:
        thefile.write(contents_encrypted)
    
    key =  Fernet.generate_key()  #encryption key

    with open("thekey.key", "wb")  as thekey:
        thekey.write(key)

    with open('passwords.txt', 'a') as outfile:
            outfile.write("-------------------------------------------\nSite:  DO NOT REMOVE\nPassword: DO NOT REMOVE\nUsername: DO NOT REMOVE\nNotes: DO NOT REMOVE\n-------------------------------------------")
            outfile.write('\n') #This makes a new line for the next variable to save on
    with open('passwords.txt', 'rb') as file:
            contents = file.read()

    contents_encrypted = Fernet(key).encrypt(contents)
    with open("passwords.txt", "wb") as thefile:
        thefile.write(contents_encrypted)

    print("Your password manager has been created!")
    with open('data.json', 'r') as file:
        data = json.load(file)

    data['password-made'] = 'yes'

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)

#########################################################################################################################################

print("\nwhat would you like to do?")
question = input("(a)dd password, (e)dit passwords, (g)enerate password, (r)ead passwords \n")

if question == "a":
    print("""
    ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
    ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
    ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
    ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
    ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

    ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
    ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
    ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
    ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
    ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")


    site = input("Site's name / LogIn page: ")

    password = input("what's the password you want to save? ")

    username = input("what is the username/email associated with it? ")

    notes = input("Add any notes here: ")

    final = "-------------------------------------------\n" "Site:  " + site + "\n" "Password: " + password + "\n" "Username: " + username + "\n" "Notes: " + notes + "\n" "-------------------------------------------"

    with open("thekey.key", "rb") as key:
        old_key = key.read()

    key =  Fernet.generate_key()  #encryption key

    with open("thekey.key", "wb")  as thekey:  #wb = write binary
        thekey.write(key)


    #########################################################################################
    #remove hashes after first password is added ... hash this part if you have no passwords **
    with open("passwords.txt", "rb") as thefile:
        content = thefile.read()
        contents_decrypted = Fernet(old_key).decrypt(content)
        with open("passwords.txt", "wb") as thefile:
            thefile.write(contents_decrypted)
    ##########################################################################################
    with open('passwords.txt', 'r') as file:
            contents = file.read()
    with open('passwords.txt', 'a') as outfile:
            outfile.write(final)
            outfile.write('\n') 
    with open('passwords.txt', 'rb') as file:
            contents = file.read()

    contents_encrypted = Fernet(key).encrypt(contents)
    with open("passwords.txt", "wb") as thefile:
        thefile.write(contents_encrypted)

    print("All of your passwords have been successfully saved")

elif question == "e":
    #####################################
    with open("thekey.key", "rb") as key:
        secretkey = key.read()
    #####################################

    with open("phrase_key.key", "rb") as key:
        old_phrasekey = key.read()


    phrasekey =  Fernet.generate_key()  #encryption key

    with open("phrase_key.key", "wb")  as phrase_key:  
        phrase_key.write(phrasekey)

    with open("secretphrase.txt", "rb")  as phrase_key:  
        phrase_key_read = phrase_key.read()
        phrase_key_decrypted = Fernet(old_phrasekey).decrypt(phrase_key_read)
    with open("secretphrase.txt", "wb") as thefile:
            thefile.write(phrase_key_decrypted)
    with open("secretphrase.txt", "r")  as phrase_key:  
        phrase_key_read = phrase_key.read()
    secretphrase = phrase_key_read

    with open('secretphrase.txt', 'rb') as file:
            contents = file.read()

    contents_encrypted = Fernet(phrasekey).encrypt(contents)
    with open("secretphrase.txt", "wb") as thefile:
        thefile.write(contents_encrypted)


    user_phrase = getpass()

   
    #######################################################################

    if user_phrase == secretphrase:
        print("correct")
        with open("passwords.txt", "rb") as thefile:
            content = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(content)
        with open("passwords.txt", "wb") as thefile:
            thefile.write(contents_decrypted)
        
        print("Congrats, you're files are decrypted.")
        
        done = input("press enter when your done reading your passwords \n")

        if done == "yes":
            with open('passwords.txt', 'r') as file:
                contents = file.read()
            with open('passwords.txt', 'w') as outfile: 
                outfile.write(contents)
            with open('passwords.txt', 'rb') as file:
                contents = file.read()

            contents_encrypted = Fernet(secretkey).encrypt(contents)
            with open("passwords.txt", "wb") as thefile:
                thefile.write(contents_encrypted)
            print("Thank you :)")

        else:
            print("Thank you :)")
            with open('passwords.txt', 'r') as file:
                contents = file.read()
            with open('passwords.txt', 'w') as outfile: 
                outfile.write(contents)
            with open('passwords.txt', 'rb') as file:
                contents = file.read()

            contents_encrypted = Fernet(secretkey).encrypt(contents)
            with open("passwords.txt", "wb") as thefile:
                thefile.write(contents_encrypted)

    else:
        print("Sorry, wrong secret phrase")

elif question == "g":
    characters = string.ascii_letters + string.digits + "@!#%$&)*(_-"

    random.choice(characters)

    #for i in range(16):
    on = random.sample(characters, 9)

    tw = random.sample(characters, 9)

    thre = random.sample(characters, 9)

    one = "".join(on)

    two = "".join(tw)

    three = "".join(thre)


    final = one + "-" + two + "-" + three


    print("Here is your generated password: \n" + final)
    ask = input("Do you want to add this to your password list? ")

    if ask == "yes":
            site = input("Site's name / LogIn page: ")

            password = final

            username = input("what is the username/email associated with it? ")

            notes = input("Add any notes here: ")

            final = "-------------------------------------------\n" "Site:  " + site + "\n" "Password: " + password + "\n" "Username: " + username + "\n" "Notes: " + notes + "\n" "-------------------------------------------"

            with open("thekey.key", "rb") as key:
                old_key = key.read()

            key =  Fernet.generate_key()

            with open("thekey.key", "wb")  as thekey:  
                thekey.write(key)

            #########################################################################################
            #remove hashes after first password is added ... hash this part if you have no passwords **
            with open("passwords.txt", "rb") as thefile:
                content = thefile.read()
                contents_decrypted = Fernet(old_key).decrypt(content)
                with open("passwords.txt", "wb") as thefile:
                    thefile.write(contents_decrypted)
            ##########################################################################################
            with open('passwords.txt', 'r') as file:
                    contents = file.read()
            with open('passwords.txt', 'a') as outfile: 
                    outfile.write(final)
                    outfile.write('\n') 
            with open('passwords.txt', 'rb') as file:
                    contents = file.read()

            contents_encrypted = Fernet(key).encrypt(contents)
            with open("passwords.txt", "wb") as thefile:
                thefile.write(contents_encrypted)

            print("All of your passwords have been successfully saved")
    else:
        print("Ok, bye")


elif question == "r":
    #####################################
    with open("thekey.key", "rb") as key:
        secretkey = key.read()
    #####################################

    with open("phrase_key.key", "rb") as key:
        old_phrasekey = key.read()


    phrasekey =  Fernet.generate_key() 

    with open("phrase_key.key", "wb")  as phrase_key: 
        phrase_key.write(phrasekey)


    with open("secretphrase.txt", "rb")  as phrase_key: 
        phrase_key_read = phrase_key.read()
        phrase_key_decrypted = Fernet(old_phrasekey).decrypt(phrase_key_read)
    with open("secretphrase.txt", "wb") as thefile:
            thefile.write(phrase_key_decrypted)
    with open("secretphrase.txt", "r")  as phrase_key: 
        phrase_key_read = phrase_key.read()
    secretphrase = phrase_key_read

    with open('secretphrase.txt', 'rb') as file:
            contents = file.read()

    contents_encrypted = Fernet(phrasekey).encrypt(contents)
    with open("secretphrase.txt", "wb") as thefile:
        thefile.write(contents_encrypted)


    user_phrase = getpass()


    if user_phrase == secretphrase:
        print("correct")
        with open("passwords.txt", "rb") as thefile:
            content = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(content)
        print("\n\n\n"+contents_decrypted.decode('utf-8'))
        with open("passwords.txt", "wb") as thefile:
            thefile.write(contents_decrypted)


        with open('passwords.txt', 'r') as file:
            contents = file.read()
        with open('passwords.txt', 'w') as outfile:
            outfile.write(contents)
        with open('passwords.txt', 'rb') as file:
            contents = file.read()

        contents_encrypted = Fernet(secretkey).encrypt(contents)
        with open("passwords.txt", "wb") as thefile:
            thefile.write(contents_encrypted)

        print("Congrats, you're files are decrypted.")

        done = input("press enter when your done reading your passwords \n")

        if done == "yes":
            print("Thank you :)")
        else:
            print("Thank you :)")

    else:
        print("Sorry, wrong master password")

else:
    print("sorry invalid input")
