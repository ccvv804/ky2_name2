import os
import codecs
def search(dirname):    
    global data2
    data1 = ''
    data2 = ''
    z=codecs.open('list.txt','a',encoding="utf-8")
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.KY2': 
                    #print(full_filename)
                    r=full_filename
                    #print(r)
                    rx=r.replace(".KY2", "")
                    won=rx.count('\\')
                    r2=rx
                    while won != 0:
                        r1=rx.find('\\')
                        won = won -1
                        r2=rx[r1+1:]
                        rx=r2
                    print(rx)
                    f=open(r,'rb')
                    f.seek(48)
                    fanu=f.read(256)
                    fanu1=fanu.split(b'\0',1)[0]
                    momiji=fanu1.decode('UTF-8')
                    f.seek(48+256+256)
                    funga=f.read(256)
                    funga1=funga.split(b'\0',1)[0]
                    funz=funga1.decode('UTF-8')                    
                    data1 = rx+'\n'+momiji+'\n'+funz+'\n'+'\n'     
                    z.write(data1)                    
                    #print(funz)        
    except :
        pass
    z.close()

search("/RKY2")
