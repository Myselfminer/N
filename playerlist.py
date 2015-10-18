import config
class players:
    def __init__(self):
        self.path=config.install_path+"reg\\N_NOW_RUNNING\\PLAYERS\\LIST.nreg"
    def get_names_str(self,level):
        a=open(self.path,"r")
        b=a.readlines()
        string=""
        for i in b:
            string=string+i
        a.close()
        return string
    def get_names_list(self, level):
        a=open(self.path,"r")
        b=a.readlines()
        string=[]
        for i in b:
            string.append(i)
        return string
    def add(self, name, uuid, level, entity_id):
        a=open(self.path,"a")
        a.write(name+";"+uuid+";"+entity_id+";"+level)
        a.close()
    def remove(self, name, uuid, level, entity_id):
        a=open(self.path, "r")
        b=a.readlines()
        b.remove(name+";"+uuid+";"+str(entity_id)+";"+str(level))
        a=open(self.path,"w")
        for i in b:
            a.write(i)
        a.close()
        del b
