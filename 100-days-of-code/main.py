#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#create a variable named as placeholder to generate new each time
placeholder="[name]"


#to create a file which reads all the names in the file given
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

#to create a file which reads the letter content given in the file
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

for name in names:
    #Remove spaces at the beginning and at the end of the string
    stripped_name=name.strip()
    #To replace the name each time
    new_letter = letter_content.replace(placeholder,stripped_name)
    print(new_letter)
    #now to create letter for each person we are go to use the
    with open(f"./Output/ReadyToSend/letter_for_my_friend {stripped_name}.txt",mode="w") as letter_invitation:
        letter_invitation.write((new_letter))

