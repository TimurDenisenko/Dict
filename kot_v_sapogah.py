from os import * 
from gtts import *
import io

def loe(file):
    x={} 
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for line in f:
            k,v=line.strip().split('-')
            x[k]=v
    return x

def loe1(file):
    x={} 
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for line in f:
            k,v=line.strip().split('-')
            x[v]=k
    return x

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("chinano.mp3") 
    os.system("chinano.mp3")

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
        x.pop(sona)
        r=input("Kirjutage parandatud riigi ") 
        kus=input("Kas soovite parandada ka pealinn? (jah või ei) ").lower() 
        while kus not in ["jah","ei"]:
            kus=input("Kirjutage ainult jah või ei ").lower()
        if kus=="jah":
            p=input("Kirjutage parandatud pealinn ")
    else:
        x1.pop(sona)
        p=input("Kirjutage parandatud pealinn ") 
        kus=input("Kas soovite parandada ka riigi? (jah või ei) ").lower() 
        while kus not in ["jah","ei"]:
            kus=input("Kirjutage ainult jah või ei ").lower()
        if kus=="jah":
            p=input("Kirjutage parandatud pealinn ") 
    x.update({r:p}) 
    x1.update({p:r})
    return x,x1

def trenn(x:dict,x1:dict):