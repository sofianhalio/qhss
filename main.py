from requests import request
from threading import Thread

method = "GET"
cari_server = ["AkamaiGHost"]
save_file = "/storage/emulated/0/FreeHostScan/"

garis = "="*20
def banner():
    print garis
    print "Simple Script Cari Server Host"
    print "Coded by: Qiuby Zhukhi"
def ok(isi):    
    return "\033[32m{}\033[00m".format(isi)
def save_files(isi, f):
    file_name = f+"checkServer.txt"
    with open(file_name, "a+") as writer:
        writer.write(str(isi))
        
def open_host(f):
    list_host = []
    with open(f) as writer:
       for i in writer.readlines():
           i = i.replace("\n","")
           if i.startswith(":"):
               proxy, port = i.split(":");
               i = proxy
           list_host.append(i)
    return list_host
    
list_server = {}
def checker(h, m):
    try:
        get_resp = request(m, "http://"+h, timeout=5)
        headers = get_resp.headers["Server"]
        if headers in cari_server:  
            list_server.update({"Host":h,"Server": headers, "Status Code":get_resp.status_code})
        else:
            print "Host: {}\nServer: {}\nStatus Code: {}\r\n".format(h, headers, get_resp.status_code)
    except Exception as e:
        pass

thread_list = []
def watasi_wa_wibu_desu():
    while 1:
        banner()
        try:
            files = raw_input("Full path host: ")
            op = open_host(files)
            break
        except Exception as e:
            print e
            continue
    for i in op:
        t = Thread(target=checker, args=(i, method))
        t.daemon = True
        t.start()
        thread_list.append(t)
    join_kopi = [i.join() for i in thread_list]
    result()
    
def result():
    print "==== [Server Ditumukan] ===="
    for k,v in list_server.items():
        print k +": "+ok(str(v))
        save_files(k +": "+str(v)+"\r\n", save_file)
    print "Save di: "+save_file+"checkServer.txt"
if __name__ == "__main__":
    watasi_wa_wibu_desu()



