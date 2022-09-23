
list=[10,10,20,30,20]

def same_by(charact, list):
    flag=True
    for x in list: 
        if charact(x)==True:
           flag=True
        else:
           flag=False
           break
           
    if flag==True:
        return True
    else:   
        return False

if same_by(lambda x: x%10==0, list):
    print(True)
else:
    print(False)