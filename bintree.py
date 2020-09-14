
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

def createtree():
    with open('postfix.txt') as pos:
        while True:
            character = pos.read(1)
            if not character: # program complete
                break
            print(character + " ")

def file2string(fname) :
    with open(fname, 'r') as f:
        return f.read()

def string2file(string,fname) :
    with open(fname,'w') as g:
        g.write(string)

file1 = open('postfix.txt',"w")

for t in bin(3): 
    file1.write(str(t)+"\n")
    print(str(t))
createtree()
