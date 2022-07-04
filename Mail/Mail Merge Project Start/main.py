#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
names = []
with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

for name in names_list:
    names.append(name.strip())

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    text = starting_letter.read()

for name in names:
    text_replace = text.replace("[name]", f"{name}")
    with open(f"Output/ReadytoSend/mail_to_{name}.txt", mode="w") as mail:
        mail.write(text_replace)


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
