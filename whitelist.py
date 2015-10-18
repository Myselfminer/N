import config, translate
class whitelist:
    def __init__(self):
        self.path=config.install_path+"reg\\N_EVER_SAME\\PLAYER_PREFS\\whitelist.nreg"
    def get(self):
        a=open(self.path,"r")
        b=a.readlines()
        c=[]
        for i in b:
            d=i.strip("\n")
            c.append(d)
        e=""
        for i in c:
            e=e+i+"\n"
        return e
    def testforplayer(self, name):
        a=open(self.path,"r")
        b=a.readlines()
        if name in b:
            return True
        else:
            return False
    def add(self, name):
        a=open(self.path, "a")
        a.write("\n"+name)
        del a
#TODO: Mojang auth check
        return translate.whitelist_added(name)
    def remove(self, name):
        a=open(self.path, "r")
        b=a.readlines()
        try:
            b.remove(name)
            ok=True
        except:
            return translate.whitelist_remove_failed(name)
        if ok:
            a=open(self.path, "w")
            for i in b:
                a.write(i)
            return translate.whitelist_removed(name)
