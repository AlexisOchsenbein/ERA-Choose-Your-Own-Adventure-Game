#ERA.py
#by Evelyn, Rachel, Alexis
#Code for the choose your own adventure game, ERA.

### Import Statements ###
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import random
root = Tk()
w = Label(root, text="ERA")
w.pack()


        

def intro():
    """Start of the story"""
    messagebox.showinfo ("Old Lady",
                         " You're walking down the street and you see a sweet "+\
                         "old lady trip and fall on her face.")
    oldlady = simpledialog.askinteger (" Please type the number corresponding to your desired class.",
                                    " To steal her purse while she's down, press 1 " +\
                                    " To mind your own buissness and walk past, press 2. " +\
                                    " To help her up, press 3.")


    if oldlady == 1:
        choice1()
    elif oldlady == 2:
        choice2()
    elif oldlady == 3:
        choice3()
    else:
        intro()

############################### Rachel's Function ###############################
def choice1():
    choice = messagebox.showinfo ("You steal her purse",
                             " You run by and snatch her purse as she struggles to get up."+\
                             " You hear her cursing at you as you run off into the near by forest."+\
                             " You feel you aren't begin chased, and begin rooting through her purse."+\
                             " Inside you find nothing but a bunch of old lady stuff, until a ragged old"+\
                             " paper catches your eye. You unfold it and see that it is a treasure map!"+\
                             " The treasure seems to be somewhere in the forest you're in now, so you set"+\
                             " off to find it.")
   

    messagebox.showinfo ("The Forest",
                             " As you're reading the map, you here voices behind you."+\
                             " 'That way! Into the forest!' you here and old lady shout."+\
                             " 'Okay mam we will get your purse back for you.' a deeper, younger"+\
                             " voice says. You get scared and run off further into the forest. Your"+\
                             " bad karma catches up to you, as you find yourself tripping into a river"+\
                             " you forgot was there. You make it to the other side, but part of the map"+\
                             " is ruined.")
    messagebox.showinfo(" Lost",
                            " You walk for a couple hours, trying to remember all of the map"+\
                            " you can, and have been successful so far, until now. You don't"+\
                            " remember if you should go left or right.")

    leftorright= simpledialog.askinteger ("Left or Right?",
                             " Press 1 for right, or 2 for left.")

    if leftorright ==1:
        Rchoice1()
    elif leftorright ==2:
        Rchoice2()

def Rchoice1 ():
    messagebox.showinfo(" Right",
                        " You try to remember, and you're fairly certain the map said to go right."+\
                        " You turn right, and after a bit of walking, you come to a dungeon, just like"+\
                        " the one the map described! You go down into the dungeon, and trip on a rock."+\
                        " You tumble down into a giant open room with a sleeping dragon, which is now awake"+\
                        " because of you. The giant dragon stands up and prepares to attack.")
           
            
    attack = simpledialog.askinteger (" Press 1 to attack.",
                                      " To attack, press 1. ") 
    if attack ==1:                
        dragonhp = random.randint (15,50)
        dragondmg = random.randint (5, 15)
        playerhealth = random.randint (20, 30)
        playerdamage = random.randint (5, 25)
        while playerhealth >= 0 or dragonhp >= 0:
            dragonhp -= playerdamage
            playerhealth -= dragondmg
            messagebox.showinfo ("Dragon Battle",
            "You took {} damage.".format(dragondmg) +\
            "Your health is now: {}".format(playerhealth)+\
            "The dragon has {} health" .format(dragonhp))
            if playerhealth <= 0 or dragonhp <= 0:
                break 

    if playerhealth <= 0:
        messagebox.showinfo("You died",
                                "The dragon burnt you with his firey breath, leaving"+\
                                " you dead on the floor, so close to the treasure.")

    elif playerhealth <= 0 and dragonhp <= 0:
        messagebox.showinfo("You both died",
                                " You both fall dead to the floor. You didn't live, but"+\
                                " you're happy that you killed the dragon too. In your last moment"+\
                                " of life, as the dragon's flames consume you, you see the"+\
                                " old woman run in, activate a hidden door on the wall, revealing the."+\
                                " treasure. She grabs as much as she can carry, and runs out with, smiling"+\
                                "  and thanking you as she runs past.")                           
        root.destroy
    elif playerhealth >= 1:
        messagebox.showinfo (" You won ",
                                 " Somehow, you managed to slay the dragon.")

        messagebox.showinfo (" You find the treasure...",
                                     " You slay the dragon, and you see part of the wall"+\
                                     " slide down behind it. You run in and see a huge treause"+\
                                     " chest, filled with gold and gems. You begin grabbing as many"+\
                                     " as you can carry. Suddenly, you see the old lady burst into"+\
                                     " the room. She runs in, trips you, and steals all of the treasure"+\
                                     " 'See!? How does it feel huh??? Not very good! Thats what you deserve'."+\
                                     " she shouts at you as she runs away laughing, leaving you on the ground"+\
                                     " with nothing.")
        root.destroy

                
                                
                                     
       
                                


    
def Rchoice2 ():
    messagebox.showinfo(" Left",
                             " You begin walking left. You walk for an hour or so with no signs of the dungeon the"+\
                             " map described. You do however come across an old house hidden in the woods. You are"+\
                             " tired and hungry, and decide to see if who ever is inside will help you. You walk in"+\
                             " and don't see anyone. You call out, and hear no response. Suddenly, the door slams"+\
                             " behind you, and you hear an old lady cackling. You see a figure step out of the shadows"+\
                             " and yuo recognize it as the old lady you stole from, except now, she is dressed in witch"+\
                             " clothes. Turns out she is actually a powerful caster, and she's very mad at you. You see"+\
                             " a fireball begin to burn in her hand, and she prepares to attack.")
                             
     
    lastbattle()


def lastbattle ():
    witchhp = random.randint (20,25)
    witchdmg = random.randint (3, 20)
    playerhealth2 = random.randint (20, 30)
    playerdamage2 = random.randint (5, 25)
    while playerhealth2 >= 0 or witchhp >= 0:
        attack = simpledialog.askinteger (" Press 1 to attack.",
                                            " To attack, press 1. " )
        


        if attack == 1:
            witchhp -= playerdamage2
            playerhealth2 -= witchdmg
            messagebox.showinfo ("Witch Battle",
            "You took {} damage.".format(witchdmg) +\
            "Your health is now: {}".format(playerhealth2)+\
            "The witch has {} health" .format(witchhp))
        if playerhealth2 <= 0 or witchhp <= 0:
            break 

    if playerhealth2 <= 0:
        messagebox.showinfo("You died",
                                "The old lady laughs as you fall dead to teh floor."+\
                                " 'Thats what you deserve for stealing from old ladies."+\
                                " Now you'll never do it again. Tehehehehe' she says as"+\
                                " she loots your dead body.")
        root.destroy()

    

    elif playerhealth2 >= 1:
        messagebox.showinfo (" You won ",
                                 " Somehow, you managed to kill the old lady.")

        messagebox.showinfo (" You kill the old lady...",
                                     " The witch falls dead at you feet, and you proceed to loot"+\
                                     " her house. You really didn't learn anything did you?")
        root.destroy

                

    
                        
    
    



############################## Alexis' Function #################################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right1.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok2.  THE END")
    elif (choice == 3):
        messagebox.showinfo("The End",
                            "You chose ok3.  THE END")
        
    else:
        choice2()




############################## Evelyn's Function ################################
def choice3():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right1.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok2.  THE END")
    elif (choice == 3):
        messagebox.showinfo("The End",
                            "You chose ok3.  THE END")
        
    else:
        choice1()






############################# Main ##############################################
intro()

root.destroy()








    
