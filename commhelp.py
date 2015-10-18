##def get(what):
##    if what=="q":
##        what=what.strip("?help ")
##        site=what
##    else:
##        a=open("commreg.temp","r")
##        a.readlines()
##        result=[]
##        for i in a:
##            result.append(a[i+site*5]+":"+a[i+site*5])
##        return result
def get():
    a=open("commreg.temp","r")
    b=a.readlines()
    new=[]
    for i in b:
        result=i.strip("\n")
        new.append(result)
    newer=""
    for i in new:
        newer=newer+i+"\n"
    return result
