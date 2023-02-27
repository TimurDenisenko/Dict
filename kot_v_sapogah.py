from os import * 
from gtts import *
from random import *
import io

def loe(file):
    x={} 
    x1={}
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for line in f:
            k,v=line.strip().split('-')
            x[k]=v
            x1[v]=k
    return x,x1

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("chinano.mp3") 
    system("chinano.mp3")

def otsi(x:dict,x1:dict):
    sona=input("Kirjutage riik või linn ")
    y=x.get(sona)
    if y==None:
        y1=x1.get(sona)
        if y1==None:
            vale=input("Kas soovite lisada uue riigi või pealinna? (jah või ei) ").lower()
            while vale not in ["jah","ei"]:
                vale=input("Kirjutage ainult jah või ei ")
            if vale=="jah":
                if sona in x:
                    r=sona
                    p=input("Kirjutage pealinn ")
                else:
                    p=sona 
                    r=input("Kirjutage riigi ")
                x.update({r:p}) 
            else:
                print("Kahjuks")
        else:
            print(y1)
            heli(y1,"en")
    else:
        print(y)
        heli(y,"en")
    return x  

def lisa(x:dict,x1:dict):
    r=input("Kirjutage riigi ")
    while r in x:
        r=input("See riik on ")
    p=input("Kirjutage pealinn ") 
    while p in x1:
        p=input("See pealinn on ")
    x.update({r:p}) 
    return x

def paranda(x:dict,x1:dict): 
    sona=input("Kirjutage pealinn või riik, mida parandada ")
    while sona not in x and sona not in x1: 
        sona=input("Kirjutage õige riik või pealinn ")
    if sona in x:
        sona1=x.get(sona)
        x.pop(sona)
        x1.pop(sona1)
        r=input("Kirjutage parandatud riigi ") 
        kus=input("Kas soovite parandada ka pealinn? (jah või ei) ").lower() 
        while kus not in ["jah","ei"]:
            kus=input("Kirjutage ainult jah või ei ").lower()
        if kus=="jah":
            p=input("Kirjutage parandatud pealinn ")
    else:
        sona1=x1.get(sona)
        x.pop(sona1)
        x1.pop(sona)
        p=input("Kirjutage parandatud pealinn ") 
        kus=input("Kas soovite parandada ka riigi? (jah või ei) ").lower() 
        while kus not in ["jah","ei"]:
            kus=input("Kirjutage ainult jah või ei ").lower()
        if kus=="jah":
            r=input("Kirjutage parandatud riik ") 
    x.update({r:p}) 
    x1.update({p:r})
    return x,x1

def salv(x,fail):
    xriik=list(x.keys())
    xlinn=list(x.values()) 
    y=[]
    for i in range(len(x)):
        y.append(xriik[i]+"-"+xlinn[i]+"\n")
    with io.open(fail,"w",encoding="utf-8-sig") as f:
        f.writelines(y)
        
def trenn(x:dict):
    xriik=list(x.keys())
    xlinn=list(x.values())
    use=[]
    a=0
    n=input("Mitu korda me treenime ")
    while n.isdigit()==False or int(n)>(len(x)*2):
        n=input("Kirjutage õige arv ")
    for i in range(int(n)):
        ran=choice(choice([xriik,xlinn]))
        while ran in use:
            ran=choice(choice([xriik,xlinn]))
        use.append(ran)
        if ran in xlinn:
            ind=xlinn.index(ran)
            sona=input(f"Kirjutage pealinna {ran} riik ")
            if sona==xriik[ind]:
                print("Õige")
                a+=1
            else:
                print("Vale")
        else:
            ind=xriik.index(ran)
            sona=input(f"Kirjutage riigi {ran} pealinna ")
            if sona==xlinn[ind]:
                print("Õige")
                a+=1
            else:
                print("Vale")
    print(f"{a/int(n)*100}% vastused on õige ja {100-a/int(n)*100}% on vale")
