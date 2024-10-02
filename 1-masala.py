import datetime
import time

def tugilgan_kun():
    while 1:
        print("Tug'ilgan kuningizni kiriting (Ex: Kun=1, Oy=1):")
        kun = int(input("Kun = "))
        oy = int(input("Oy = "))
        year = 2024
        tg = datetime.datetime(year,oy,kun)

        if datetime.datetime.now()>tg and oy!=2: # Tug'ilgan kun o'tib ketgan bo'lsa keyingi yilni oladi
            tg = tg.replace(year=2025)
        
        if kun>0 and kun<31 and oy > 0 and oy<13: # Sana to'g'ri kiritilganini tekshirish uchun 
            if oy ==2 and kun>29:
                print("Fevral oyida buncha kun yo'q.\nQayta kiriting.")
                time.sleep(3)
            else:
                if oy ==2 and kun ==29: # 29-Fevral bo'lsa joriy yildan keyingi kabisa yilini olish 
                    while 1:
                        year+=1
                        if year%4==0 and year%100!=0 or year%400==0:
                            tg = tg.replace(year=year)
                            break
                return tg
        else:
            print("Noto'g'ri formatda kiritdingiz.\nQayta kiriting:") # Noto'g'ri formatda kiritilgan bo'lsa qayta kiritiladi
            time.sleep(3)

if __name__=="__main__":
    tg = tugilgan_kun()
    bugun = datetime.datetime.now()
    if tg==bugun:
        print("Bugun")
    else:
        print(f"Keyingi tug'ilgan kun sanasi = {tg}\nTug'ilgan kungacha {(tg-bugun).days} kun, {(tg-bugun).seconds//60//60} soat bor")
