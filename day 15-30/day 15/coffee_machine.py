from coffee_machine_data import MENU,resources

off=False
income=0

while not off:
    stop=False
    money=0
    drink=input("What would you like? (espresso/latte/cappuccino): ");

    if drink in MENU:
        for key in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][key] > resources[key]:
                print(f"Sorry there is not enough {key}")
                stop=True
                break
        if not stop:
            print("Please insert coins.")
            money=int(input("how many quarters? "))*0.25
            money+=int(input("how many dimes? "))*0.10
            money+=int(input("how many nickles? "))*0.05
            money+=int(input("how many pennies? "))*0.01
            
            if money>=MENU[drink]["cost"]:
                income+=MENU[drink]["cost"]
                for key in MENU[drink]["ingredients"]:
                    resources[key]-=MENU[drink]["ingredients"][key]
                print(f"Here is your {drink} enjoy")           
                if money>MENU[drink]["cost"]:
                    change=round(money-int(MENU[drink]["cost"]),2)
                    print(f"Here is your change {change}")
                    
            elif money<MENU[drink]["cost"]:
                print(f"Sorry thats not enough. ${money} refunded")
                
        
    elif drink=="report":
        for key in resources:
            print(key+":"+str(resources[key]))
        print("Money: "+str(income))
    elif drink=="off":
        print("It was lovely serving you.")
        off=True
        
                
    