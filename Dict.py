from kot_v_sapogah import *

eurig1=loe("riigid_pealinnad.txt")
eurig2=loe1("riigid_pealinnad.txt")
while True:
    menu=input("""
1-Vaatama Euroopa riigid 
2-Otsige riiki või pealinna 
3-Lisa riik ja pealinn
4-Paranda riik või pealinn
5-Harjutus
""")
    if menu=="1":
        print(eurig1)
    elif menu=="2":
        eurig1=otsi(eurig1,eurig2)
    elif menu=="3":
        eurig1=lisa(eurig1,eurig2)
    elif menu=="4":
        eurig1,eurig2=paranda(eurig1,eurig2)
    else:
        print("Kirjutage ainult need numbrid, mis teil on ") 