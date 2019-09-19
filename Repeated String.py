def repeatedString (s, n):
    string = s*10000000
    count = 0
    for i in range (n):
        if string[i]== 'a':
            count+=1
    print(count)

repeatedString ('aba', 10)