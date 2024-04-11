import pandas as pd
import os


path = r'\\mypath\\mypath\\Tickets\\'


def test():
    try:
        datee = "04-Jan-24"
        loginn = "111"
        columns_head = [2, 1, 7, 9, 10, 12, 16] # 1=Dateofcase, 7=Login1, 9=newshift1, 10=Login2, 12=newshift2, 16=Resolution, 2=Category
        reggex = {"~":"-", "@":":"}
        file = pd.DataFrame(pd.DataFrame(os.listdir(path)).replace(reggex,regex=True)[0].str.split(",",expand=True).sort_values(by=13,ascending=False)[columns_head])

        filterfile= file[
            (file[1]==datee) & ((file[7]==loginn) | (file[10]==loginn)) &
            (file[2]=="Schedule") & ((file[16]=="Done") | (file[16]=="Hide"))][:1]

    
        updatedshift =  filterfile[9].iloc[0] if filterfile[7].iloc[0] == loginn else filterfile[12].iloc[0]
        s = 11112
    
    except: updatedshift= None; s=None 

    return updatedshift , s

print(test()[1])







