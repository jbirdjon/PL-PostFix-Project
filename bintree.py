
def bin(n):
    file1 = open('postfix.txt', "w")#open file

    if n==0:
        yield 'o'
    else:
        for k in range(0,n):
            for l in bin(k):
                for r in bin(n-1-k):
                    yield (l,r)
    file1.close()

file1 = open('postfix.txt',"w")

for t in bin(2):

    postfix = ""
    for element in str(t):
        if element == 'o':
            postfix = postfix + 'o'
        elif element == ')':
            postfix = postfix + ','

    file1.write(postfix+"\n")
file1.close()
f = open("postfix.txt","r")
for line in f.readlines():
    stack = []
    if line != '':
        for character in line:
            print(character)
            if character != '\n':
                stack.append(character)
            if character == ',':
                print("Top of stack")
                print(stack.pop())
    print(stack)

f.close()