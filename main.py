fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print("File not found. Please create it or search for another file.")
    exit()
count = 0
largest = 0
longest_line = ""
for line in fhand:
    stripped = line.strip()
    if len(stripped) > 40:
        count += 1
    if largest == 0 or len(stripped) > largest:
        largest = len(stripped)
        longest_line = line
print(f'Line: {line}\nCount: {count}\nLargest: {largest}\nLongest Line: {longest_line}')
print(str(stripped))