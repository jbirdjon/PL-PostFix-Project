
def bin(n):
    file1 = open('postfix.txt', "w")#open file

    if n==0:
        file1.write('o')
        yield 'o'
    else:
        for k in range(0,n):
            for l in bin(k):
                for r in bin(n-1-k):
                    file1.write('x')
                    yield (l,r)
    file1.close()

file1 = open('postfix.txt',"w")

for t in bin(3):
    postfix = ""
    for element in str(t):
        if element == 'o':
            postfix = postfix + 'o'
        elif element == ')':
            postfix = postfix + ','

    file1.write(postfix+"\n")
