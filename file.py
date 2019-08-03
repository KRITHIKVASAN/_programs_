present = "D:\krithik\list.txt"
done = "D:\krithik\done.txt"
def readFile():
    with open(present,"r") as f:
        cur = f.read().splitlines()
    return cur

def readCompleted():
    with open(done,"r") as f:
        complete = f.read().splitlines()
    return complete

def writeFile(liss):
    with open(present,"w") as f:
        for i in range(len(liss)):
            f.write(liss[i])
            f.write("\n")

def writeCompleted(liss):
    with open(done,"w") as f:
        for i in range(len(liss)):
            f.write(liss[i])
            f.write("\n")

