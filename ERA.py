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
        choice2()
    elif oldlady == 3:
        helpOldLady()
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
    messagebox.showinfo("You help the old lady",
                        "You extend your hand to help her up and hobble to the nearest sitting area"+\
                        "She is really greatful of your kind act in helping her. She then asks if you" +\
                        "would like to go grab a bite to eat for lunch that she will gladly pay for you" +\
                        "You kindly accept and drive with her to the nearest Cafe in town. During the hearty meal" +\
                        "she says 'I have something important for you. It's a treasure map that holds many"+\
                        "exciting treasures that a person as kind as you deserves to find and possess." +\
                        "I would like you to be the person to have this treasure.")

    messagebox.showinfo("Accept or Deny Map",
                            "While taking in what the old lady has just told you, you contemplate this idea of"+\
                            "seeking out this treasure. You must now choose whether to accept the treasure map" +\
                            "or decline the idea.")
    AcceptOrDenyMap =simpledialog.askinteger ( "Accept or Deny Map",
                                                "Press 1 to accept, or 2 to deny Map."
                                                "Choose Wisely...")
    if (AcceptOrDenyMap == 1):
        messagebox.showinfo(" AcceptOrDeny","The old lady tells you to first be aware of the horrid dragon lurking in the"+\
                            "Western and Eastern sides of where the treasure is located. So you must approach"+\
                            "it through the Southern or Northern side of it. Behind the map there is a code"+\
                            "to open the treasure box but it can only be seen under the moonlight. But be"+\
                            "aware you only get one shot to put in the right code otherwise the treasure box will"+\
                            "desintegrate and be gone until another 100 years. Now this dragon that lurks guarding the"+\
                            "treasure only sleeps every two weeks on a Wednesday and has eyes like a hawk. But there is the choice of battling"+\
                            "the dragon and if you choose to do that the riches become greater for you than before but it" +\
                            "is the much more deadly and fatal route to take for you must stab it in the heart.")
        
        fight()

    elif (AcceptOrDenyMap == 2):
        deny()

def deny():
    messagebox.showinfo("Deny", "The old lady's heart saddens knowing that she had so much faith in you, bids you goodbye"+\
                             "and you both go your seperate ways both full of emptiness and a sense of loss.The End.")
    root.destroy()
        
                             

def fight():                             
    FightOrNot = simpledialog.askinteger ( "Fight the dragon",
                                           "Press 1 to fight, or 2 to wait for dragon to fall asleep"
                                           " Take your pick....")

    if (FightOrNot == 1):
        messagebox.showinfo("Fight","You must physically and mentally prepare to fight this dreadful dragon. That night"+\
                            "you find the code under the moonlight and wake up early in the morning to sharpen your"+\
                            "sword and spear. As you walk down the long pathway in the hillside where the dragon lays" +\
                            "you can begin to smell the deadly smoke the dragon has blowed and you begin to feel stick to" +\
                            "your stomach. The feelings of doubt begin to haunt you, but the reassuring words of the old lady"+\
                            "begin to come to you and the deep faith the old lady has in you helps you continue to push on"+\
                            "You are now sweating vigorously because of the hot humid breath the dragon's fire has released")
        
        messagebox.showinfo("Fight", "You can see the dragon it is black like the night with a long red stripe down it's back it is so"+\
                            "large you feel yourself getting smaller by the second as you come from the South side of it just as the"+\
                            "old lady has told you too. However the dragon has sensed that there is someone there and is pacing back"+\
                            "and forth letting out fire every second all around him. You are now inside a ring of fire alone with"+\
                            "the horrid dragon. The dragon has now spotted you and is roaring at you in rage and fury. You attempt"+\
                            "to climb it's back and stab the dragon for support to get you higher up closer to the heart")
                             
        messagebox.showinfo("Fight","You can feel the burn of your cuts from the scaly skin of the dragon tearing into you and buckets of"+\
                            "sweat dripping down your entire body. You are now spinning in circles and feel yourself in a whirlwind"+\
                            "You are clinging on for dear life as your hands are bleeding their way closer to the heart. Everything"+\
                            "has now become a worldwind you smell burning skin, hair and blood and it's making you feel queasy yet you"+\
                            "are so close to heart of the dragon you can feel and hear it's thumping heartbeats.You place your bloody"+\
                            "hand on it's heart and then you stab it so hard that you feel your hand being thrusted inside the dragon"+\
                            "you feel yourself being flung outside of the ring of fire and hit the ground so hard you feel you've broken"+\
                            "some bones. You have done it..You have killed the dragon! You then limp over to the cave where it had been"+\
                            "hidden and admire the beauty glowing from the golden box. You then put in the code and open the treasure........")
        share()                 
                            
    elif (FightOrNot == 2):
        messagebox.showinfo("Wait", "It is a Wednesday morning and you must wait another two weeks for the dragon to sleep."+\
                            ".....TWO WEEKS LATER..you're a bit nervous but anxious to see this treausre it's been"+\
                            "lingering on your mind for the past two weeks. You then finally start walking towards the"+\
                            "dragon making sure to come at it towards the Southern side. You then see the wild beast"+\
                            "breathing in and out the deadly smoke it produces. You walk as quietly as possible and make sure"+\
                            "to follow the instruction the old lady has told you. You then see the brown box, put the code in and"+\
                            "open the treasure......")

        share()

def share():
    ShareorKeep = simpledialog.askinteger( "Share or Keep",
                                            "Would you like to publically share your riches to the world or keep your finding to yourself"
                                            "Press 1 to keep findings to yourself, or 2 to share to the public"
                                            "Think wisely...")
    if (ShareorKeep == 1):
        messagebox.showinfo("Keep", "So since you have decided to keep to yourself you decide to write a novel on the journey"+\
                            "taken to get this treasure. You have decided that by keeping it to yourself it will be a family secret for your future "+\
                            "children and future descendants to enjoy and have as a family heirloom. You are content with your decision, because it"+\
                            "brings a sort of peace and content to yourself.")
    elif (ShareorKeep == 2):
        messagebox.showinfo("Share", "Since you've chosen to share with the public, there are now news reporters at your front door"+\
                            "throwing tons of questions at you on how you got the treasure and where the treasure is now...you're a bit"+\
                            "overwhelmed by all the publicity that you're getting, but now you've become a bit famous and you seem to be"+\
                            "enjoying yourself......at the present moment....")

        


                             
                            
                
        
                             
                            
                        







############################# Main ##############################################
intro()

root.destroy()








    
