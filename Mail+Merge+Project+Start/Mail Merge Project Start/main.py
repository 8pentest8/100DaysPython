#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt") as f_names:
    with open("./Input/Letters/starting_letter.txt") as letter:
        content = letter.read()

        for name in f_names:
            name_ = name.strip("\n")
            new = content.replace("[name]", name_)
            with open("./Output/ReadyToSend/letter_for_" + name_ + ".txt", "w") as send_l:
                send_l.write(new)




