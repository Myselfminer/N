import SocketServer, translate, config, handshake, threading, socket#, eventhandle
sp=translate.startprefix()
version="0.0.0 dev"
print sp+translate.welcome(version)
#main=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=config.get("port")
ip=config.get("ip")
ipbuffer=buffer(ip)
backlog=config.get("backlog")
consolefile=open("console.txt","w")
consolefile.write("NetherMc sagt hi")
consolefile.close()
print sp+translate.langstr1(), translate.lang(), translate.langstr2()
class Handle(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = eventhandle.handle(data, cur_thread)
        self.request.send(response)
#------------
main=SocketServer.TCPServer((ip,port),Handle)
#    main.bind((ipbuffer,port))
run=True
closed="Rushtrough"
#------------
try:
    main=SocketServer.TCPServer((ip,port),Handle)
#    main.bind((ipbuffer,port))
    run=True
    closed="Rushtrough"
except:
    import shutdown
    shutdown.shutdown("porterror")
print(translate.openport(str(ip),str(port)))
print "nie"
main.serve_forever()
print "jupp"
while run:
    main.listen(backlog)
    connection=["q",3]#main.accept()
    conn_socket=connection[0]
    conn_address=connection[1]
    actionfile=open("console.txt","r")
    action=actionfile.readlines()
    try:
        if action[0]==".stop":
            closed="ok"
            run=False
    except:
        pass
import shutdown
#main.shutdown()
shutdown.shutdown(closed)
main.close()
