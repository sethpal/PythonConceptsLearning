class CSStudent:
    stream="CS"
    def __init__(self,name,rollNum):
        self.name=name
        self.rollnum=rollNum
    def __init_(self):
        print("Default Constructor")

st1=CSStudent("Seth",1)
st2=CSStudent("Ravita",2)

print(st1.name+" || "+str(st1.rollnum)+"|| "+st1.stream)
print(st2.name+" || "+str(st2.rollnum)+" || "+st2.stream)