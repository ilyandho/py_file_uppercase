
fname = input('Enter file name:')
count = 0
try:
    fhand = open(fname)
except:
    print('File name cannot be oppened:', fname)
    exit()
for line in fhand:
    print(line.upper().strip())
    count = count+1
print(count)
