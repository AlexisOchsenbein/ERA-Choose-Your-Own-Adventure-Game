#ERA.py
#by Evelyn, Rachel, Alexis
#Code for the choose your own adventure game, ERA.

### Import Statements ###
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

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
        ignoreOldLady()
    elif oldlady == 3:
        choice3()
    else:
        intro()

############################### Rachel's Function ###############################
def choice1():
    choice = messagebox.showinfo ("You steal her purse",
                             " You run by and snatch her purse as she struggles to get up."+\
                             " You hear her cursing at you as you run off into the near by forest."+\
                             " You feel you aren't bein chased, and begin rooting through her purse."+\
                             " Inside you find nothing but a bunch of old lady stuff, until a ragged old"+\
                             " paper catches your eye. You unfold it and see that it is a treasure map!"+\
                             " The treasure seems to be somewhere in the forest you're in now, so you set"+\
                             " off to find it.")
   

    messagebox.showinfo ("The Forest",
                             " As you're reading the map, you here voices behind you."+\
                             " 'That way! Into the forest!' you here and old lady shout."+\
                             " 'Okay mam we will get your purse back for you.' a deeper, younger"+\
                             " voice says. You get scared and run off further into the forest. Your"+\
                             " bad karma catches up to you, as you find yurself tripping into a river"+\
                             " you forgot was there. You make it to the other side, but part of the map"+\
                             " is ruined.")
    messagebox.showinfo(" Lost",
                            " You walk for a couple hours, trying to remember all of the map"+\
                            " you can, and have been successful so far, until now. You don't"+\
                            " remember if you should go left or right.")

    leftorright= simpledialog.askinteger ("Left or Right?",
                             " Press 1 for right, or 2 for left.")

    if leftorright ==1:
         Rchoice1 
    elif leftorright ==2:
         Rchoice2
    



############################## Alexis' Function #################################
def ignoreOldLady():
    """Ignore Helping the old lady"""
    choice = messagebox.showinfo("Walk Past Her",
                                     " Trying to avoid eye contact with the old lady you quickly"+\
                                     "  pull your hand up to your face and sheild your view of her as"+
                                     " you walk by, leaving her struggling to get up. After crossing"+\
                                     " the street you look to where the old lady was still attempting to get"+\
                                     " to her feet and think about going back to help her.")

    messagebox.showinfo ("Help or Leave",
                             "As you sit there the old lady glances across the steet and notices you."+\
                             " You are left with the choice to either go and help her up or turn "+\
                             " around and leave her in the street.")
        
    leaveorhelp = simpledialog.askinteger ( "Help or Leave",
                                              "Press 1 to help, or 2 to leave."
                                              "You decide to...")
                              

                         
    if (leaveorhelp == 1):
        messagebox.showinfo("Change of Heart",
                            "You feel bad for leaving the old lady laying in  the street"+\
                            "and you go back to help her up. She struggles for a moment but"+\
                            " seems alright when she finally gets to her feet.'Why thank you"+\
                            " young traveler, I would have never been able to get up all by my"+\
                            " self. I appreciate your assistance!'she says while fishing around"+\
                            " in her purse. After a moment she pulls out an old tatterd look paper"+\
                            " and places it in your hand.'I think you deserve this for your good deed"+\
                            " today,it is very fragile but of great importance! Do not loose this and"+\
                            " make sure you are well prepared before setting off. Have a nice day now.'"+\
                            " She takes off down the street as you stare at the paper in your hand.")
        
        messagebox.showinfo("The Map",
                            "You unfold the paper in your hand very carefully. Finally "+\
                            " opening the entire paper you realize this is a treasure map!"+\
                            " As you study the map you think back to what the old lady had said."+\
                            " 'She said something about being well prepaired.' You can either "+\
                            " prepare yourself first (1) or try to go without any supplies (2).")
        
        getting_ready = simpledialog.askinteger("Getting Ready",
                               "Supplies(1), Empty Handed(2)"+\
                               "You decide to...")
        
        

    elif (leaveorhelp == 2):
        messagebox.showinfo("Ignore Her",
                            " You decide she dosent need your help and walk away."+\
                            " You walk around town and look through the shops, forgetting"+\
                            " about the old lady. Eventually you get bored and go home to"+\
                            " live out your boring life. THE END.")
        root.destroy()
                                            ###WHY ERROR WHEN ENDDING leaveorhelp == 2 ?###
        
    else:
        ignoreOldLady()

    if getting_ready == 1:
        Prepaired()
        

    elif getting_ready == 2:
        Unprepaired()

    else:
        ignoreOldLady()
        

def Prepaired():
    """Prepairing for battle"""
    gold = 10
    
    messagebox.showinfo("Gearing Up",
                        "You walk into town while counting your money."+\
                        "You count out 10 gold as you walk into the town square."+\
                        "Looking around you decide to go into the blacksmith." )
    
    messagebox.showinfo("Blacksmith",
                        "You walk into the store and are welcomed in by the shopkeeper."+\
                        " 'What can i get for you today?' You think for a momment and decide"+\
                        " to purchase... A Sword(1), Chestplate(2), or both the Sword and Chestplate(3).")
    
    purchase = simpledialog.askinteger("Purchase",
                            "Sword (1) cost 5 gold, Chestplate(2) cost 5 gold, Both(3) cost 10 gold,"+\
                            "You decide to purchase...")
    if purchase == 1:
        gold = gold - 5

        messagebox.showinfo("This Will Do.",
                            "Now that you've got your sword you set of in the direction" +\
                            " that the map specifies.")
    elif purchase == 2:
        gold = gold - 5

        messagebox.showinfo("Protected.",
                            "Now that you can almost gurantee you most likely won't"+\
                            " get stabed through the chest you feel safe enough to set"+\
                            " of into the direction the map specifies.")
    elif purchase == 3:
        gold = gold - 10

        messagebox.showinfo("Let's Go!",
                            "Now that you're looking good but broke you set off in the"+\
                            "direction the map specifies with your sword and chestplate.")
    else:
        Prepaired()

        messagebox.showinfo("Bear,",
                            "As you walk through the forest following the map you run into an angry"+\
                            " bear")
    


def Unprepaired():
    """Going to die"""
    messagebox.showinfo("Unsafe",
                        "You decide not to take the old ladys warning and figure you"+\
                        
                        " can handle whatever it is this old lady is so affraid of, besides"+\
                        " its probably not that big of a deal anyways.")
    messagebox.showinfo("Fight!",
                        "As you walk along the trail paying close attention to the map,"+\
                        " you hear a low angry growl...You slowly peek up from the map"+\
                        " and see a very angry looking mother bear.")

    messagebox.showinfo("Died,",
                        "You are now looking right into the bears eyes and"+\
                        " she dosent look like she's going to let you go without"+\
                        " a fight. About this time you really regret not buying anything"+\
                        " to protect yourself back at the store. The Mother bear stands up and"+\
                        " takes you out with one big swipe of her claw and rips open your chest."+\
                        " Your body is left in the forest to be eaten by the bear cubs and any other"+\
                        " critter that walks by your corpse."+\
                        " THE END.")

                            ### Why errror when ending def Unprepaired? ###
root.destroy()
    

    
    
    
        
        






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








    
