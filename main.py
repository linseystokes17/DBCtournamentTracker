import json
# initial printing
print('============================')
print('Welcome to Tournaments R Us')
print('============================')

# variables
nParticipants = int(input('Enter the number of participants: '))
participants = [None for a in range(0, nParticipants)]
slots = [a for a in range(1, nParticipants+1)]
exit = False

print(f'There are {nParticipants} participant slots ready for sign-ups.')

# functions
# assigns participant to slot
def addParticipant(name, slot):
    if participants[slot-1]==None:
        participants[slot-1]=name
        return True
    return False

# remove participant from slot
def removeParticipant(name, slot):
    if participants[slot-1] == name:
        participants[slot-1] = None
        return True
    return False

# view list of participants (all or 10 around slot #)
def viewParticipants(*args):
    if len(args) == 1:
        slot = int(args[0])
        for i in range(slot-5, slot+5):
            print(f"{slots[i]}: {participants[i]}")
    else:
        for i in range(0, nParticipants):
            print(f"{slots[i]}: {participants[i]}")

# search for participant by name
def searchParticipant(name):
    for i in range(0, nParticipants):
        if participants[i]==name:
            return slots[i]
    return 0

# print menu and gather inputs to add person
def addParticipantMenu():
    participant = input('Participant Name: ')
    slot = int(input(f'Starting slot #[1:{nParticipants}]: '))
    message = addParticipant(participant, slot)
    if not message:
        print(f'Slot #{slot}  is filled. Please try again.')
    else:
        print(f'Success:\n{participant} is signed up in starting slot #{slot}.')

# print menu and gather inputs to remove person
def removeParticipantMenu():
    participant = input('Participant Name: ')
    slot = int(input(f'Starting slot #[1:{nParticipants}]: '))
    message = removeParticipant(participant, slot)
    if not message:
        print(f'Error:\n{participant} is not in that starting slot.')
    else:
        print(f'Success:\n{participant} has been cancelled from starting slot #{slot}.')

# print menu and gather inputs to view participants
def viewParticipantMenu():
    slot = input(f'Starting slot #[1:{nParticipants}]: ')
    if slot!='':
        viewParticipants(slot)
    else:
        viewParticipants()

# print menu and gather inputs to search participants
def searchParticipantMenu():
    name = input('Who do you want to search: ')
    slot = searchParticipant(name)
    if slot == 0:
        print(f'{name} does not exist')
    else:
        print(f'{name} is in slot #{slot}')

# functionality to export list of participants
def exportParticipants():
    dict = {}
    for i in range(0, nParticipants):
        dict[slots[i]] = participants[i]
    try:
        with open("participants_list.json", "w") as outfile: 
            json.dump(dict, outfile, indent = 4)
        print('Export Successful')
    except:
        print('Export Unsuccessful')

# functionality to import list of participants
def importParticipants(file):
    global slots, participants
    try:
        with open(file) as f:
            dict = json.load(f)
            slots = list(dict.keys())
            participants = list(dict.values())
        return True
    except:
        return False

# menu to get file name for import
def importParticipantsMenu():
    file = input('What file do you want to use (full path): ')
    if importParticipants(file):
        print('Import Successful')
    else:
        print('Import Unsuccessful')

# general printing & menu commands
while not exit:
    print('\n============================')
    print('Participant Menu')
    print('============================')
    print('1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Search for Participant\n5. Export Participants\n6. Import Participants\n7. Exit\n')
    try:
        menuChoice = int(input())
        if menuChoice == 1:
            addParticipantMenu()
        if menuChoice== 2:
            removeParticipantMenu()
        if menuChoice == 3:
            viewParticipantMenu()
        if menuChoice == 4:
            searchParticipantMenu()
        if menuChoice == 5:
            exportParticipants()
        if menuChoice == 6:
            importParticipantsMenu()
        if menuChoice == 7:
            print('Are you sure you want to exit?\nAll data will be lost.')
            exitChoice = input('Exit? [y/n] ')
            if exitChoice == 'y':
                print('Goodbye!')
                exit = True
    except:
        print('That is not a valid menu option')
    