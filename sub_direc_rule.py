def sub_dir(l):
    lt=[]
    for x in l:
        if x[:3]=="bix":
            lt.append("bix")
        elif x[:2]=="gg":
            lt.append("gg")
        elif (x[0].isnumeric()) == True:
            lt.append("number") 
        else:
            lt.append(x[0])           
    return lt
