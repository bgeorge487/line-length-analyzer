# CIS 2131 Line Length Analyzer

# ask for a file to read
fname = input('Enter a file name: ')
# ensure the file exists
try:
    fhand = open(fname)
except:
    print(f"File can't be opened: {fname}")
    exit() # exit if no file exists
# set variables
count = 0
largest = 0
longest_line = ""
# loop through the file
for line in fhand:
    # strip each line
    stripped = line.strip()
    # check the length, over 40 characters long and it counts up
    if len(stripped) > 40:
        count += 1
    # find the largest line
    if largest == 0 or len(stripped) > largest:
        largest = len(stripped)
        longest_line = line
# print the results
print(f'Lines over 40 characters: {count}\nLongest line length: {largest}\nLongest Line: {longest_line}')
print(str(stripped))