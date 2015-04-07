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
                            " remember if you should go striaght, left or right.")

    leftorright= simpledialog.askinteger ("Left or Right?",
                             " Press 1 for right, or 2 for left, or 3 for striaght.")

    if leftorright ==1:
        right()
    elif leftorright ==2:
        left()
    elif leftorright ==3:
        striaght()
    
def right():
    messagebox.showinfo(" Right",
                        " You try to remember, adn you're fairly certain the map said to go right."+\
                        " You turn right, and after a bit of walking, you come to a dungeon, just like"+\
                        " the one the map described! You go down into the dungeon, and trip on a rock."+\
                        " You tumble down into a giant open room with a sleeping dragon, which is now awake"+\
                        " because of you. The giant dragon stands up and prepares to attack.")

    dragonhp = random.randint (15,50)
    dragondmg = random.randint (5, 15)
    playerhealth = random.randint (20, 30)
    playerdamage = random.randint (5, 25)
    while playerhealth >= 0 or dragonhp >= 0:
        attack = simpledialog.askinteger (" Press 1 to attack.",
                                                  " To attack, press 1. " )
        


        if attack == 1:
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
                                " you dead, so close to the treasure.")
        root.destroy()
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
        root.destroy()
                
                                
                                     
                                



def left():
    messagebox.showinfo(" Left",
                             " You begin walking left. You walk for an hour or so with no signs of the dungeon the"+\
                             " map described. You do however come across an old house hidden in the woods. You are"+\
                             " tired and hungry, and decide to see if who ever is inside will help you. You walk in"+\
                             " and don't see anyone. You call out, and hear no response. Suddenly, the door slams"+\
                             " behind you, and you hear an old lady cackling. You see a figure step out of the shadows"+\
                             " and yuo recognize it as the old lady you stole from, except now, she is dressed in witch"+\
                             " clothes. Turns out she is actually a powerful caster, and she's very mad at you. You see"+\
                             " a fireball begin to burn in her hand, and she prepares to attack.")
                             
        
    witchhp = random.randint (20,25)
    witchdmg = random.randint (3, 20)
    playerhealth = random.randint (20, 30)
    playerdamage = random.randint (5, 25)
    while playerhealth >= 0 or witchhp >= 0:
        attack = simpledialog.askinteger (" Press 1 to attack.",
                                                  " To attack, press 1. " )
        


        if attack == 1:
            witchhp -= playerdamage
            playerhealth -= witchdmg
            messagebox.showinfo ("Witch Battle",
            "You took {} damage.".format(witchdmg) +\
            "Your health is now: {}".format(playerhealth)+\
            "The witch has {} health" .format(witchhp))
            if playerhealth <= 0 or witchhp <= 0:
                break 

    if playerhealth <= 0:
        messagebox.showinfo("You died",
                                "The old lady laughs ss you fall dead to teh floor."+\
                                " 'Thats what you deserve for stealing from old ladies."+\
                                " Now you'll never do it again. Tehehehehe' she says as"+\
                                " she loots your dead body.")
        root.destroy()
    elif playerhealth >= 1:
        messagebox.showinfo (" You won ",
                                 " Somehow, you managed to kill the old lady.")

        messagebox.showinfo (" You kill the old lady...",
                                     " The witch falls dead at you feet, and you proceed to loot"+\
                                     " her house. You really didn't learn anything did you?")
        root.destroy()


    
def striaght():
    messagebox.showinfo (" Striaght",
                         " You're pretty sure the map said to keep going forward."+\
                         " You walk for what seems like hours with no sign of the"+\
                         " dungeon. You keep walking, and you start to get the feeling"+\
                         " that you're being followed. You turn around, and see a huge"+\
                         " owl bear in a tree behind you! It jumps down and prepares to"+\
                         " fight.")

          
    owlhp = random.randint (10,25)
    owldmg = random.randint (1, 12)
    playerhealth = random.randint (20, 30)
    playerdamage = random.randint (5, 25)
    while playerhealth >= 0 or owlhp >= 0:
        attack = simpledialog.askinteger (" Press 1 to attack.",
                                             " To attack, press 1. " )
        


        if attack == 1:
            owlhp -= playerdamage
            playerhealth -= owldmg
            messagebox.showinfo ("OWLBEAR Battle",
            "You took {} damage.".format(owldmg) +\
            "Your health is now: {}".format(playerhealth)+\
            "The owl bear has {} health" .format(owlhp))
            if playerhealth <= 0 or owlhp <= 0:
                break 

    if playerhealth <= 0:
            messagebox.showinfo("You died",
                                " The owl bear chirps in happiness as you fall to the floor"+\
                                " It calls out, and a bunch of cute little owl bear babies"+\
                                " fall down from their nest and start to eat you.")
                            
            root.destroy()
    elif playerhealth >= 1:
            messagebox.showinfo (" You won ",
                                 " You manage to scare the owlbear away, and watch has it climbs back up."+\
                                 " its tree. You realize you chose the wrong way, and that it would be best"+\
                                 " to just head back to town. You head back, and try to sneak to your house, "+\
                                 " but sadly the town guards see you. They arrest you for being a jerk and for"+\
                                 " stealing. You slowly rot away in the town prison for the rest of your life. "+\
                                 " No one comes to visit you, except the old lady, who comes by once in awhile"+\
                                 " to laugh.")
            root.destroy()



    



############################## Alexis' Function #################################
def choice2():
    choice = messagebox.showinfo("You walk past her",
                                     " Trying to avoid eye contact with the old lady you quickly"+\
                                     "  pull your hand up to your face and sheild your view of her as"+
                                     " you walk past her, leaving her struggling to get up. After crossing"+\
                                     " the street you look to where the old lady was still attempting to get"+\
                                     " to her feet and think about going back to help her.")

    messagebox.showinfo ("Help or Leave",
                             "As you sit there the old lady glances across the steet and notices you."+\
                             "You are left with the choice to either go and help her up or turn "+\
                             "around and leave her in the street.")
        
    leaveorhelp = simpledialog.askinteger ( "Help or Leave",
                                              "Press 1 to help, or 2 to leave."
                                              "You decide to...")
                              

                         
    if (leaveorhelp == 1):
        messagebox.showinfo("Change of Heart",
                            "You feel bad for leaving the old lady laying in  the street"+\
                            "and you go back to help her up. She struggles for a momnet but"+\
                            "seems alright when she finally gets to her feet.'Why thank you"+\
                            "young traveler, I would have never been able to get up all by my"+\
                            "self. I appreciate your assistance!'she says while fishing around"+\
                            "in her purse. After a moment she pulls out an old tatterd look paper"+\
                            "and places it in your hand.'I think you deserve this for your good deed"+\
                            "today,it is very fragile but of great importance! Do not loose this and"+\
                            "make sure you are well prepared before setting off. Have a nice day now.'"+\
                            "She takes off down the street as you stare at the paper in your hand.")
        messagebox.showinfo()

    elif (leaveorhelp == 2):
        messagebox.showinfo("The End",
                            "You chose ok2.  THE END")
        
    else:
        choice2()




############################## Evelyn's Function ################################
def helpOldLady():
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
        helpOldLady()






############################# Main ##############################################
intro()

root.destroy()








    
