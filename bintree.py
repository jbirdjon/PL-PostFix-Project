#Creates binary tree
def bin(n):
    if n==0:
        yield 'o'
    else:
        for k in range(0,n):
            for l in bin(k):
                for r in bin(n-1-k):
                    yield (l,r)

file1 = open('postfix.txt',"w")

#Writing to file
for t in bin(3):

    postfix = ""
    for element in str(t):
        if element == 'o':
            postfix = postfix + 'o'
        elif element == ')':
            postfix = postfix + ','

    file1.write(postfix+"\n")
    print(str(t)+"\t"+postfix)
file1.close()

#reading from file
f = open("postfix.txt","r")
for line in f.readlines():
    stack = []
    stack2 = []
    combo =""
    if line != '':
        for character in line:#reading characters in line
            if character != '\n' and character !=',':#appends character to stack as long as its not delimiter
                stack.append(character)
            elif character == ',':#Creates a combo and appends it to the stack
                pos=stack.pop()
                pos2=stack.pop()
                stack.append("("+pos2+","+pos+")")
    print(str(stack)+"\t"+line)#Verifys
f.close()
