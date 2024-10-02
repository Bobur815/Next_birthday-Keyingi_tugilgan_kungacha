import random as r

def pl_vs_com ():
    round = int(input("Necha round o'ynamoqchisiz? "))
    round_count = durang_count = com_count = pl_count = 0
    tanlov = ['rock','paper','scissors']

    while round_count<round:
        print(f"-------------------------------\n{round_count+1} - round:")
        pl_tanlov = input("Quyidagilardan birini kiriting:\n- rock\n- paper\n- scissors\n").lower()
        while pl_tanlov not in tanlov:
            print("Xato kiritdingiz, qayta kiriting.")
            pl_tanlov = input("Quyidagilardan birini kiriting:\n- rock\n- paper\n- scissors\n").lower()
        
        com_tanlov = r.choice(tanlov)
        print("Kompyuterning tanlovi = ",com_tanlov)
        if com_tanlov==pl_tanlov:
            print("Durang")
            durang_count+=1
        elif pl_tanlov=='rock' and com_tanlov=='scissors' or pl_tanlov=='paper' and com_tanlov=='rock' or pl_tanlov=='scissors' and com_tanlov=='paper':
            print("Siz yutdingiz!")
            pl_count+=1
        else:
            print("Kompyuter yutdi!")
            com_count+=1
        round_count+=1
    print(f"O'yin tugadi!\n***************************\nNatijalar:\nSiz = {pl_count}\nKompyuter = {com_count}\nDurang = {durang_count}")
    if pl_count>com_count:
        print("Siz g'alaba qozondingiz!")
    elif com_count>pl_count:
        print("Kompyuter g'alaba qozondi")
    else:
        print("Durang")
    
def com_vs_com():

    round = int(input(" - ChatGPT vs Copilot - \nNecha round o'ynashsin? "))
    round_count = durang_count = gpt_count = copilot_count = 0
    tanlov = ['rock','paper','scissors']

    while round_count<round:
        print(f"-------------------------------\n{round_count+1} - round:")
        
        gpt_tanlov = r.choice(tanlov)
        copilot_tanlov = r.choice(tanlov)
        print("ChatGPT = ",gpt_tanlov,"\nCopilot = ",copilot_tanlov)
        if gpt_tanlov==copilot_tanlov:
            print("Durang")
            durang_count+=1
        elif copilot_tanlov=='rock' and gpt_tanlov=='scissors' or copilot_tanlov=='paper' and gpt_tanlov=='rock' or copilot_tanlov=='scissors' and gpt_tanlov=='paper':
            print("Copilot yutdi!")
            copilot_count+=1
        else:
            print("ChatGPT yutdi!")
            gpt_count+=1
        round_count+=1
    print(f"O'yin tugadi!\n***************************\nNatijalar:\nChatGPT = {gpt_count}\nCopilot = {copilot_count}\nDurang = {durang_count}")
    if gpt_count>copilot_count:
        print("ChatGPT g'alaba qozondi!")
    elif copilot_count>gpt_count:
        print("Copilot g'alaba qozondi")
    else:
        print("Durang")

if __name__=='__main__':
    print(" * "*20,"\n\tRock, Paper, Scissors o'yiniga Xush kelibsiz!\n","*  "*20)
    turi = int(input("O'yin turini tanlang:\n1 - Player vs Computer\n2 - Computer vs Computer\n"))
    if turi == 1:
        pl_vs_com()
    else:
        com_vs_com()

