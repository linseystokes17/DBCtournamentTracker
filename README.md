# DBCtournamentTracker
Data Bootcamp Assessment 8

Pseudocode
1. initialize variables: 
	1. prompt for number (n) participants
	2. empty list of participants ['[empty]']*n
	3. slot list from 1-n
	4. exit (boolean)
2. define functions
	1. add a person(name, slot)
	2. remove a person(name, slot)
	3. view participants(*args)
		1. if len(*args) > 0 (there is a slot we want to look at)
			1. return the 5 slots before and after the intended slot
		2. else:
			1. return whole list
	4. search for participant(name)
	5. addPersonMenu()
	6. removePersonMenu()
	7. viewParticipantsMenu()
	8. searchPersonMenu()
3. printing (in while loop based on exit)
	1. print menu items (will repeat until exit)
		1. read inputChoice
	2. sign up screen (inputChoice = 1)
		1. prompt for name
		2. prompt for slot
		3. message = addPerson(name, slot)
		4. print message (error or success)
	3. removal screen (inputChoice = 2)
		1. prompt for slot
		2. prompt for name
		3. message = removePerson(name, slot)
		4. print message (error or success)
	4. view participants  (inputChoice = 3) ** what's the slot supposed to do?
		1. prompt for slot
		2. print '{slot}: {name}'
		3. if empty print '{slot}: [empty]'
	5. search for participant (inputChoice = 4)
		1. prompt for full name
		2. searchPerson(name)
		3. return slot number
	6. exit program (inputChoice = 5)
		1. display warnings
		2. prompt for y/n input
		3. display message if y and exit loop
		4. if no keep looping