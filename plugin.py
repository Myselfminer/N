import hook
import os
import config
plugin_path=config.get(install_path)+"plugins\\"
def init():
    path=os.listdir(plugin_path)
    a=open(config.get(install_path)+"reg\\N_NOW_RUNNING\\PLUGINS\\INITTEMP\\plugininit.py")
    a.write("def init():")
    for i in path:
        a.write("   import "+i+"\n   "+i+".init()")
    import plugininit
    plugininit.init()
def register_value_command(plugin_id, command, #todo!
