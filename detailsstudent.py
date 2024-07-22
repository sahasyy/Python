import pickle
def write():
    f=open("studentdata.dat","wb")
    while True:
        r=int(input("Enter Roll No.:"))
        n=input("Enter Name:")
        data=[r,n]
        pickle.dump(data,f)
        ch=input("anymore? (y/n)")
        if ch in "Nn":
            break
    f.close()

def Search():
    found=0
    rollno=int(input("Enter roll no whose name to be displayed:"))
    f=open("studentdata.dat","rb")
    try:
        while True:
            rec=pickle.load(f)
            if rec[0]==rollno:
                print(rec[1])
                found=1
                break
    except EOFError:
        f.close()
    if found==0:
        print("no records")
write()
Search()
