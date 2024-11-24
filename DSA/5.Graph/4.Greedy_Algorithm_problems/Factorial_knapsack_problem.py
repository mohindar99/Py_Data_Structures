class Items:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.ratio=value/weight

def knapsnapMethod(items,capacity):
    items.sort(key=lambda i:i.ratio,reverse=True)
    unusedcapacity=0
    totalvalue=0
    for i in items:
        if unusedcapacity+i.weight<=capacity:
            unusedcapacity+=i.weight
            totalvalue+=i.value
        else:
            unusedweight=capacity-unusedcapacity
            value=unusedweight*i.ratio
            totalvalue+=value
            unusedcapacity+=unusedweight
        if unusedcapacity==capacity:
            break
    print(f"Total value obtained:{totalvalue}")

itemA=Items(20,100)
itemB=Items(30,120)
itemC=Items(10,60)
clist=[itemA,itemB,itemC]
knapsnapMethod(clist,50)
