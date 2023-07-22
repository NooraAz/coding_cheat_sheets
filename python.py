# rounding a number to nearest integar
double_number = 3.46789269
round(double_number)

# rounding with specific number of decimals
round(1.2345676,2) # --> 1.2

# rounding with keeping ending zeros
"%.3f" % 1.2300 # --> 1.230

# removing spaces from beginning and end of string
mystring.strip()

# making a list from a string (by comma for example)
mystring.split(',')

# sort a list based on second value of sublist
mylist.sort(key= lambda x:x[1])

# sort a list based on size of sublists (large to small)
my_list.sort(key=len,reverse=True)

# sorting sublists of a list
sorted_lst = [sorted(sublist) for sublist in lst]

# text justification
text = 'Have a good day!"
text.ljust(5)
text.rjust(5)

# path to a module
print(my_module.__file__)
