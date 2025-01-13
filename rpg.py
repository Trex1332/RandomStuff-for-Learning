#player

class player():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        self.weapons = {}
        self.potion = 1
        self.gold = 10

class monster():
    def __init__(self,name,hp,damage,gold):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.gold = gold

name = input("name please: " )

player1 = player(name,10)
rat = monster("rat",5,2,200)

player1.weapons["Sword"] = 10

print(player1.weapons)

def shop():
    choice = int(input("what do you want: 1.Health potion, 2.Upgrade sword "))
    if choice == 1:
        if player1.gold <= 10:
            player1.potion +=1
        else:
            print("Not Enough Gold")
    elif choice == 2:
        if player1.gold >= 100:
            player1.weapons["Sword"] += 10
            print(player1.weapons)
        else:
            print("Not Enough Gold")


def adventure():
    print(f"you see a {rat.name}")
    rat.hp = 5
    while rat.hp >= 0:
        choice = int(input("1.Attack, 2.Heal, 3.Run "))
        if choice == 1:
            rat.hp -= player1.weapons["Sword"]
        elif choice == 2:
            if player1.potion >=0:
                player1.hp += 10
                player1.potion -=1
            else:
                print("no Potions")
        elif choice == 2:
            break
        if rat.hp <= 0:
            print(f"rat killed heres {rat.gold} gold")
            player1.gold += rat.gold
            break
    

        print("ratattack -2 hp")
        player1.hp -= rat.damage
        print(player1.hp)
        if player1.hp <= 0:
            print("died")
            break
    
    
        

while player1.hp >= 0:
    choice = int(input("1.Inventory, 2.Adventure, 3.Shop "))
    if choice == 3:
        shop()
    elif choice == 2:
        adventure()




