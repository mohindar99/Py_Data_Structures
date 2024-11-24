# val=[10,10]*5
# print(val)
# sam=[1,2,3,4]
# sai=sam.copy()
# sai[0]="ram"
# print(sam)

class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=laptop(2)

    def show(self):
        print(self.name,self.roll)
        self.lap.show()



class laptop:
    def __init__(self,val):
        self.ram=16
        self.rom=512
        self.val=val

    def show(self):
        print(self.ram,self.rom)

s1=student('ram',23)
s1.show()