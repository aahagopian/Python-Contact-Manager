#create the contact list from the data in contacts.txt

def main():
	import time
	# time module to improve output format
	inconFile=open('contacts.txt','r')
	# set readlines function to variable
	# allows line variable to iterate through each line in the file
	read = inconFile.readlines()
	contacts=[]
	for line in read:
		line = line.rstrip('\n')
		# new variable for the smaller list
		contactEl = line.split(', ')
		contacts.append(contactEl) 
	inconFile.close()
	choice = 1	
	againInput = 'y'
		#display a menu
	print('Welcome to my address book! ')
	time.sleep(1)
	again = True
	# initialize boolean to be true set as condition
	exitOption = True
	while exitOption==True:
			# if statement to check the value of choice
			if(choice>0 and choice<=6):
				print('1. Add new contact')
				print('2. View your address book')
				print('3. Search for contact')
				print('4. Edit a contact\'s information')
				print('5. Delete a contact')
				print('6. Exit the program')


				choice = int(input('Please select one of the above options (1-6). '))
				try:
					if choice==1:
						contacts.append(addnewcontact())
					elif choice==2:
						displayAddressBook(contacts)
					elif choice==3:
						searchContact(contacts)
					elif choice==4:
						modifyContact(contacts)
					elif choice==5:
						deleteContact(contacts)
					elif choice==6:
						exitOption = exitAddressBook(contacts)
						if exitOption==False:
							# choice equals 7 breaks the while loop
							choice=7
							time.sleep(1)
						again = False
				except ValueError:
					print('You must enter a choice between 1 and 6')
			else:
				print("OOPSIE, you made an invalid input, please check your input and enter again")
				choice = int(input('Please select one of the above options (1-6). '))


def addnewcontact():
	print('You have chosen to enter a new contact.')
	newName = input('Please enter the name of the new contact. ')
	newAddress = input('Please enter the new address. ')
	newNumber = input('Please enter the new phone number. ')
	newEmail = input('Please enter the new email address. ')
	#new element to append into the contacts list
	newElement = []
	newElement.append(newName)
	newElement.append(newAddress)
	newElement.append(newNumber)
	newElement.append(newEmail)
	# return new element to append in the main function
	return newElement

def displayAddressBook(contacts):
	# use the for loop to iterate through
	for contact in contacts:
		# this prints the contents of the smaller list without the brackets
		print(contact[0] + ', ' + contact[1] + ', ' + contact[2] + ', ' + contact[3])

def searchContact(contacts):
	searchChoice = str(input('Please enter the first and last name of the contact you are searching for. '))
	# the counter enables the loop to stay in the range of contact indices
	i = 0
	for contact in contacts:
		if contact[0]==searchChoice and i<len(contacts):
			print('The chosen contact information is: ' + contact[0] + ', ' + contact[1] + ', ' + contact[2] + ', ' + contact[3])
		# when i==length of contacts, the index is out of the contacts list
		elif contact[0]!=searchChoice and i==len(contacts)-1:
			print('That name does not exist in the address book. ')
		i+=1

def modifyContact(contacts):
	modChoice = str(input('Please enter the first and last name of the contact you would like to modify. '))
	# assign another variable for the individual contact list
	editCon = 1
	# initialize i to zero to check the for loop iteration vs the length of the list
	i = 0
	for contact in contacts:
		if contact[0]==modChoice and i<len(contacts):
			print('The chosen contact information is: ' + contact[0] + ', ' + contact[1] + ', ' + contact[2] + ', ' + contact[3])
			editCon = contact
		elif contact[0]!=modChoice and i==len(contacts)-1:
			print('That name does not exist in the address book. ')
		i+=1

	modType = str(input('Enter \'n\' to edit name, \'a\' to edit address, \'p\' to edit phone number, or \'e\' to edit email. '))
	if modType=='n':
		modName = str(input('Enter a new name for this contact. '))
		#set index to zero to modify the name
		# repeat with incrementing indices
		editCon[0] = modName
	# assign the modified items to each element in the smaller list
	elif modType=='a':
		modAddress = str(input('Enter a new address for this contact. '))
		editCon[1] = modAddress
	elif modType=='p':
		modNumber = str(input('Enter a new phone number for this contact'))
		editCon[2] = modNumber
	elif modType=='e':
		modEmail = str(input('Enter a new email address for this contact. '))
		editCon[3] = modEmail

def deleteContact(contacts):
	delChoice = str(input('Enter the first and last name of the contact that you would like to delete. '))
	i = 0	
	# for loop for finding the correct contact to deleter
	for contact in contacts:
		if contact[0]==delChoice:
					# index equals i because i tracks which contact the loop is on
			del contacts[i]
			print(delChoice, 'has been deleted from the address book. ')
		# i increments to reflect changing to the next contact
		i+=1
	
def exitAddressBook(contacts):
	# make another variable to reference the write file
	outconFile = open('contacts.txt','w')
	# each iteration of contact prints each element of the small list to a line
	for contact in contacts:
		outconFile.write(contact[0] + ', ' + contact[1] + ', ' + contact[2] + ', ' + contact[3] + '\n')
	outconFile.close()
	# choice will be used later to exit program
	againChoice = str(input('Would you like to return to the menu? (y or n)'))
	print('Now exiting the address book')
	if againChoice=='y':
		return True
	else:
		return False
	

main()

	               
