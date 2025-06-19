file = open('fernando.txt', 'r')  # read mode
# file = open('fernando.txt', 'w') # write mode
# file = open('fernando.txt', 'a') # append mode
# file.write("\nI am unenployed\n")
content = file.read()
# line = file.readline()
# lines = file.readlines()
print(content)
# close the file
file.close()
