# rounding a number to the nearest integer
double_number = 3.46789269
round(double_number)

# rounding with specific number of decimals
round(1.2345676,2) # --> 1.2

# rounding with keeping ending zeros
"%.3f" % 1.2300 # --> 1.230

# using {} in formatted string
name = 'Noora'
print(f"{{ Hello {name} }}") # { Hello Noora }

# removing spaces from the beginning and end of string
mystring.strip()

# Making a list from a string (by a comma for example)
mystring.split(',')

# Sort a list based on the second value of sublist
mylist.sort(key= lambda x:x[1])

# Sort a list based on the size of sublists (large to small)
my_list.sort(key=len,reverse=True)

# Sorting sublists of a list
sorted_lst = [sorted(sublist) for sublist in lst]

# text justification
text = 'Have a good day!"
text.ljust(5)
text.rjust(5)

# Path to a module
print(my_module.__file__)

# handling errors
try: 
  # code
except Exception as e:
  print(e) #print error
  pass # ignore error
