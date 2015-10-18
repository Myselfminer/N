import translate
def run(command):
    b=command.split(" ")
    if b[0]=="?help":
        import commhelp
        commhelp.get()
    if b[0]==".stop":
        import sys
        sys.exit()
    if b[0]=="?whitelist":
        import whitelist
        obj=whitelist.whitelist()
        return obj.get()
        del whitelist
    if b[0]=="?plugins":
        import pluginlist
        list1=pluginlist.get()
        list2=""
        for i in list1:
            list2=list2+"\n"+i
        del pluginlist
        return list2
    if b[0]==".whitelist":
        anzahl=0
        for i in b:
            anzahl=anzahl+1# Zaehle Elemente der Liste
        if anzahl==1 or 2:
            return translate.whitelist_syntax()
            do=False
        else:
            do=True
        if do:
            import whitelist
            obj=whitelist.whitelist()
            if b[1] == "add":
                return obj.add(b[2])
            if b[1] == "remove":
                return obj.remove(b[2])
            else:
                translate.whitelist_syntax()
    else:
        return translate.comm_not_found(b)
