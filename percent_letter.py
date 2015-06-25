user_string = input("What's your word? ")
user_num = input("What's your number? ")

try: # try is a conditional block that isn't sure if something will work on not
	our_num = int(user_num)
except: # this is the else to try's if, when execpt(ions) are raised with the above try statement this is where we go next in the logical flow
	our_num = float(user_num)

if not '.' in user_num: # no decimal point means the number is an integer, if that's the case...
	print(user_string[our_num]) # slice into the user string, using the user number as the index value, and then print the result
else: # if the number contains a decimal point and is thus a float
	ratio = round(len(user_string) * our_num) # find the length of the user string and multiply it by the user number (which in this case is a float, then round the result and assign it to the variable ratio
	print(user_string[ratio]) # slice into the user string, using the ratio as the index number (round must return an integer) and the print the result
	