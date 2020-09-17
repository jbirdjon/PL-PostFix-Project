
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

for t in bin(3):

    postfix = ""
    for element in str(t):
        if element == 'o':
            postfix = postfix + 'o'
        elif element == ')':
            postfix = postfix + ','

    file1.write(postfix+"\n")
    print(t)
file1.close()
f = open("postfix.txt","r")
for line in f.readlines():
    stack = []
    stack2 = []
    combo =""
    if line != '':
        for character in line:
            if character != '\n' and character !=',':
                stack.insert(0,character)
            elif character == ',':
                combo = "("+stack.pop()+","+stack.pop()+")"
                stack.insert(0,combo)
        print(line)
        print(stack)
   # print(stack.pop())
f.close()
