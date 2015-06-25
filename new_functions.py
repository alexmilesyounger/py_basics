my_sentence = "I'm a lumberjack and I'm OK! I sleep all night and I work all day!"

my_sentence.split() # split() will split a string at the spaces and return the values as a list, we could probably pass in other arguments to split them elsewhere, but the default behavior is to split the string at spaces
["I'm", 'a', 'lumberjack', 'and', "I'm", 'OK!', 'I', 'sleep', 'all', 'night', 'and', 'I', 'work', 'all', 'day!']

my_sentence
"I'm a lumberjack and I'm OK! I sleep all night and I work all day!"

sentence_list = my_sentence.split() # if I want to hold on to the list that the split() function returns I need to assign it to a variable

sentence_list
["I'm", 'a', 'lumberjack', 'and', "I'm", 'OK!', 'I', 'sleep', 'all', 'night', 'and', 'I', 'work', 'all', 'day!']

'_'.join(sentence_list) # the join() function will take an argument (iterable) and then join together the elements of the list using the string provided before the join function. In this case we're using an underscore as the string that the join() function is concatenating with the iterable string. The main thing here is that join() works on two strings, the one before join which is what gets added between each element in the iterable and the list/string. The join() function will not work with integers or floats, only strings.
"I'm_a_lumberjack_and_I'm_OK!_I_sleep_all_night_and_I_work_all_day!"

' '.join(sentence_list) # here I'm using the join() function with the sentence_list iterable and the concatenating it with a string of a single space
"I'm a lumberjack and I'm OK! I sleep all night and I work all day!"

''.join(sentence_list) # Here I'm using the join() function on the the sentence_list iterable and concatenating it with an empty string
"I'malumberjackandI'mOK!IsleepallnightandIworkallday!"

sentence_list # none of these changes to the strings using join() or split leave a lasting impression on the strings or lists I use them on. The only way for there to be a lasting impression is if I assign the result to a variable.
["I'm", 'a', 'lumberjack', 'and', "I'm", 'OK!', 'I', 'sleep', 'all', 'night', 'and', 'I', 'work', 'all', 'day!']