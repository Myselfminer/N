#This is the eventhandler file, every request goes throug this
import hook
def handle(data, thread):
    plugins=hook.testforhook_all()
    a=open("hookeventtemp.py","w")
    a.write("""def call(request):
   import sys
   liste=[]""")
    for i in plugins:
        a.write("   import "+i+"\n")
    for i in plugins:
        a.write("   liste.append("+i+".all(request))\n")
    a.write("   return liste")
    import hookeventtemp
    back=hookeventtemp.call(data)
