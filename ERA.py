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








    
