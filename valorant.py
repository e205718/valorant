import random

AGENT = ['Brimstone', 'Viper' , 'Omen','Killjoy','Cypher','Sova','Sage','Phoenix','Jett','Reyna','Raze','Breach','Skye','Yoru','Astra','KayO']

DUELIST = ['Phoenix','Jett','Reyna','Raze','Yoru']  # 0      ロールナンバー
SENTINEL = ['Killjoy','Cypher' , 'Sage']            # 1
SMOKE = ['Brimstone', 'Viper' , 'Omen','Astra']     # 2
INISI = ['Sova','Breach','Skye','KayO'] 
           # 3
COMMAND_LIST = ["mapAgent","namAgent"]

async def mapAgent():
    mode = "true"
    map_name = input("\n マップ名を入力してください。\n Acent,Bind,Split,Haven,IceBox,Breeze,Fracture>>")
    while mode == "true":
        result = []
        rand1_2 = random.randint(1,2)
        if rand1_2 == 1 :
            rand_s = 2
        else :
            rand_s = 1

        if map_name == 'Acent':
            role_nam = [2,1,1,1]
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(random.sample(SMOKE,role_nam[2]))
            result.append(random.sample(INISI,role_nam[3]))
            mode = "False"   
        if map_name == 'Bind':
            role_nam = [2,1,1,1]
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(random.sample(SMOKE,role_nam[2]))
            result.append(random.sample(INISI,role_nam[3]))
            mode = "False"
        if map_name == 'Haven':
            role_nam = [2,1,1,1]
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(random.sample(SMOKE,role_nam[2]))
            result.append(random.sample(INISI,role_nam[3]))
            mode = "False"
        if map_name == 'Split':
            role_nam = [rand_1_2,1,rand_s,1]
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(random.sample(SMOKE,role_nam[2]))
            result.append(random.sample(INISI,role_nam[3]))
            mode = "False"
        if map_name == 'IceBox':
            role_nam = [2,1,1,1]
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(random.sample(SMOKE,role_nam[2]))
            result.append(random.sample(INISI,role_nam[3]))
            mode = "False"
        if map_name == 'Breeze':
            role_nam = [2,1,1,1]
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(SMOKE[1])
            result.append(random.sample(INISI,role_nam[3]))
            mode = "False"
        
        if map_name == 'Fracture':
            role_nam = [2,1,1,1]
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(random.sample(SMOKE,role_nam[2]))
            result.append(random.sample(INISI,role_nam[3]))
            mode = "False"
        return result


async def namAgent():
    role_nam = []
    result = []

    role_nam.append(int(input('duelistの数を入力（半角）>>>')))
    role_nam.append(int(input('sentinelの数を入力（半角）>>>')))
    role_nam.append(int(input('smokeの数を入力（半角）>>>')))
    role_nam.append(int(input('initiatorの数を入力（半角）>>>')))
    
    if sum(role_nam) == 5:
        result.append(random.sample(DUELIST,role_nam[0]))
        result.append(random.sample(SENTINEL,role_nam[1]))
        result.append(random.sample(SMOKE,role_nam[2]))
        result.append(random.sample(INISI,role_nam[3]))

    else :
        print("入力オーバーです。最初からやり直してね")

    return result 
async def help_com():
    return COMMAND_LIST
    
def main():
    mode = "true"
    while mode == "true":
        command = input("\nコマンドの入力(help):>>")
        if command == "help":
            help_com()
    
        elif command == "mapAgent":
            print(mapAgent())

        elif command == "namAgent":
            print(namAgent())
        
        elif command == "exit":
            print("終了します。")
            mode = "False"
        else:
            print("コマンドが間違っています。")
        

##print(mapAgent('Acent'))
