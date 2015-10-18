import translate, sys
sp=translate.shutdownprefix()
this=True
def shutdown(why):
    if why=="ok":
        print(sp+translate.shutdown("Server closed"))
        this=False
    elif why=="Rushtrough":
        print(sp+translate.shutdown("Core Error"))
        print(sp+translate.coreerror())
    elif why=="porterror":
        print(sp+translate.porterror())
        print(sp+translate.porterror2())
    print(sp+translate.shutdowncomplete())
    if this:
        sys.exit()
