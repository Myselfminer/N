def get(what=0):
    import config
    the=open(config.get("install_path")+"reg\\N_EVER_SAME\\PLUGINS\\ALL.nreg","r")
    list1=the.readlines()
    the.close()
    return list1
