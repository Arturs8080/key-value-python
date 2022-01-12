name = input('Enter file:')
if len(name) < 1:
    name = 'mbox-short.txt'
opf = open(name)
# line 1-4, prompts user, takes input, creates a filehandle

lst = list()
counts = dict()
# lines 7-8 creates two lists and a dictionary

for line in opf:  # reads every line in the file

    if line.startswith('From '):  # separates lines that start with 'From '
        line = line.split()  # splits lines

        time = line[5]
        hrs = time[:2]
        # line 15 adds the 5th element of each line (timestamp) to list
        # line 16 takes hour (09:) out of element
lst.append(hrs)  # adds the first element (e.g. 09) to list

for hr in lst:  # reads every line in the list

    # creates a dictionary that counts the number of times an element is repeated.
    #counts[hr] = counts.get(hr, 0) + 1

    # sorts the key-value pair in 'counts' according to their key
    # for ky, va in sorted(counts.items()):
    #print(ky, va)
