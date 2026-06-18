lessons = input().split()
i = 1 
subj = lessons[i-1]

while subj != 'X':
    string = str(i) + ") " + subj
    print(string)
    i += 1
    subj = lessons[i-1]

