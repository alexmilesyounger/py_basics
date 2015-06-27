shopping_list = list()

print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
	new_item = input("> ")

	if new_item == 'DONE':
		break # this is the command for exiting the loop

	shopping_list.append(new_item)
	print("Added! List has {} items.".format(len(shopping_list)))
	continue # this is the command that tells the loop to go back to continue looping, in this case, since it's at the end of the list, it will go back to the beginning

print("Here's your list:")

# for item in shopping_list:
# 	print(item)

last_item = shopping_list.pop()
shopping_list.append('and')
shopping_list.append(last_item)
return_list = ', '.join(shopping_list)
print(return_list)