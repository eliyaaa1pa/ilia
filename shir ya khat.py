username = input("lotfan shomare daneshjooi khod ra vared konid:")
while username != ("99123047"):
    print("shomare daneshjooi ghalat mibashad")
    username = input("lotfan shomare daneshjooi khod ra vared konid:")
print("shomare daneshjooi sahih mibashad")
password = input("lotfan Code melli khod ra varedkonid:")
while password != ("0024135942"):
    print("code melli ghalat ast")
    password = input("lotfan Code melli khod ra varedkonid")
print("code melli sahih mibashad")
print("khosh amadid")
emtiaz_player1 = 0
emtiaz_player2 = 0
while True :
    player_1 = input("lotfan entekhab konid : shir ya khat ?")
    player_1 = str.lower(player_1)
    if player_1 == "shir":
        print("player_1 : shir")
    elif player_1 == "khat":
        print("player_1 : khat ")
    else:
        print("entekhab shoma ghalat mibashad")
        player_1 = input("lotfan entekhab konid : shir ya khat ?")
    
    import random as rn
    randint = rn.randint(1 , 3)
    player_2 = randint
    if player_2 == 1:
        print("player_2 : shir")
    if player_2 ==2:
        print("player_2 : khat ")
    if player_1 == "shir" and player_2 == 1:
        print("barande : player_1")
        emtiaz_player1 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "shir" and player_2 == 2 :
        print("barande : player_2")
        emtiaz_player2 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "kaht" and player_2 == 1 :
        print("barande : player_2")
        emtiaz_player2 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    elif player_1 == "khat" and player_2 == 2 :
        print("barande : player_1")
        emtiaz_player1 += 1
        print("emtiaz_player1 =",emtiaz_player1)
        print("emtiaz_player2 =",emtiaz_player2)
    if emtiaz_player1 == 3 :
        print("Shoma barande shodid")
        break
    if emtiaz_player2 == 3 :
        print("Game Over")
        break