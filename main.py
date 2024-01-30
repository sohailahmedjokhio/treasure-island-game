print('''
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  \
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::''        :: :     ""--.._
                  '__..-''           __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a crossroad. where do you want to go? Type 'left' or 'right'")
action1 = input().lower()
if action1 == "left":
    print(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across."
    )
    action2 = input().lower()
    if action2 == "wait":
        print(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?"
        )
        action3 = input().lower()
        if action3 == "yellow":
            print("Congratulations, You Win.")
        elif action3 == "red":
            print("Burned by fire.")
            print("Game Over.")
        else:
            print("Eaten by beasts.")
            print("Game Over.")
    else:
        print("Attacked by trout.")
        print("Game Over")
else:
    print("Fall into a Hole.")
    print("Game Over")
