#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
# file_invited_names = os.getcwd()
fileInvitedNames = "Input/Names/invited_names.txt"
fileStartLetter = "Input/Letters/starting_letter.txt"
folderOutputLetter = "Output/ReadyToSend/"
PLACE_HOLDER = "[name]"
nameList = []
with open(fileInvitedNames, "r") as file:
    lines = file.readlines()
    # get all the name
    for line in lines:
        # remove spaces and new lines with strip()
        nameList.append(line.strip())

# print(name_list)
#Replace the [name] placeholder with the actual name.
# get the letter contents
letterContentsStart = ""
with open(fileStartLetter, "r") as file:
    letterContentsStart = file.readlines()
for name in nameList:
    letterContents = letterContentsStart
    letterContents[0] = letterContents[0].replace(PLACE_HOLDER, name)
    # save letters
    with open(folderOutputLetter + name + ".txt", "w") as file:
        # write letter
        for line in letterContents:
            file.write(line)
