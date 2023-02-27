from kot_v_sapogah import *
eurig1,eurig2=loe("riigid_pealinnad.txt")
while True:
    menu=input("""
1-Vaatama Euroopa riigid 
2-Otsige riiki või pealinna 
3-Lisa riik ja pealinn
4-Paranda riik või pealinn
5-Salvestama
6-Harjutus
""")
    if menu=="1":
        print(eurig1)
    elif menu=="2":
        eurig1=otsi(eurig1,eurig2)
    elif menu=="3":
        eurig1=lisa(eurig1,eurig2)
    elif menu=="4":
        eurig1,eurig2=paranda(eurig1,eurig2)
    elif menu=="5":
        salv(eurig1,"riigid_pealinnad.txt")
        print("Fail salvestatud!")
    elif menu=="6":
        trenn(eurig1)
    else:
        print("Kirjutage ainult need numbrid, mis teil on ") 