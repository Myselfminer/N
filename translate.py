def lang():
    return "English (EN_EN)"
def langstr1():
    return "Language has been set to"
def langstr2():
    return "You can change this in the root folder by renaming your \
favorite Languange file to translate.py"
def binderror():
    return "Unable to bind Port. Maybe there's \
already a server running on that port?"
def porterror():
    return "Bind Error"
def porterror2():
    return "Please make sure that you have entered the right ip\
adress in the config and no other Server is running on that port"
def openport(ip,port):
    return "Opening Server at "+ip+":"+port
def welcome(ver):
    return "You are using N v. "+ver
def shutdown(why):
    return "Stopping Server due to "+why
def coreerror():
    return "Couldn't start core loop"
def shutdowncomplete():
    return "Server was stopped"
def shutdownprefix():
    return "[Shutdown]"
def startprefix():
    return "[INIT]"
def comm_not_found(comm):
    return "Command "+comm[0]+" not found. Type ?help for help."
def helphead(page,last):
    return "---Help page "+str(page)+" of "+str(last)+"---"
def helphelp():
    return "Type ?help <page> to go to browse through the help"
def whitelist_added(player):
    return "Successfully added "+player+" to whitelist"
def whitelist_removed(player):
    return "Succesfully removed "+player+" from the whitelist"
def whitelist_remove_failed(player):
    return "Couldn't remove "+player+" from the whitelist"
def whitelist_name_already_in_use(player):
    return "Player "+player+" is already on the whitelist"
def whitelist_syntax():
    return "Usuage: .whitelist <add/remove> <Name>"
