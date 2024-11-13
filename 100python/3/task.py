print("""
                                  _
                               _ooOoo_
                              o8888888o
                              88" . "88
                              (| -_- |)
                              O\  =  /O
                           ____/`---'\____
                         .'  \\\\|     |//  `.
                        /  \\\\|||  :  |||//  \\
                       /  _||||| -:- |||||_  \\
                       |   | \\\\\  -  /'| |   |
                       | \_|  `\`---'//  |_/ |
                       \  .-\__ `-. -'__/-.  /
                     ___`. .'  /--.--\  `. .'___
                  ."" '<  `.___\_<|>_/___.' _> \"".
                 | | :  `- \`. ;`. _/; .'/ /  .' ; |
                 \  \ `-.   \_\_`. _.'_/_/  -' _.' /
       ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
                               `=--=-'                   
      """)
print("So you want to find your peace ?")
print("Make the Right choice and you might just find it")
foot = input("So you just woke up Which leg should you start the day with ? Left or Right ? ")
if foot.lower() == "right" :
    print("Well played, you can keep going !")
    drink = input("Which drink would you start your day with ? Coffee, tea or something else ? ")
    if drink.lower() == "coffee" :
        print("Stop lying to yourself !")
    elif drink.lower() == "tea" :
        print("This is good, but you can be great !")
    else :
        print("Well played, the end is nigh")
        start = input("What will you start your day with ? Nothing, Play or Work ? ")
        if start.lower() == "nothing" :
            print("Sadly, life ain't that easy")
        elif start.lower() == "work" :
            print("Good job, have a good day")
        else :
            print("...")
else :
    print("Has this ever worked for you ?")
