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


#Sword"
    if purchase == 1:
        gold = gold - 5

        messagebox.showinfo("This Will Do.",
                            "Now that you've got your sword you set of in the direction" +\
                            " that the map specifies.")
        
        messagebox.showinfo("Bear,",
                            "As you walk through the forest following the map you run into an angry"+\
                            " bear. She dosent look like she is going to let you go without a fight."+\
                            " Normaly you would run away from this situation but since you bought this sword"+\
                            " you feel pretty confident and decide to fight the bear.")

        
        messagebox.showinfo("Die.",
                            "As you swing the sword at the bear you manage to get a few good cuts in."+\
                            " After you balance yourself out again you look up at the bear to see the damage"+\
                            " you did. Looking at the bear you see it hasnt moved since you got there and is not"+\
                            " amussed with your attempt at defeating it.The  bear stands up and"+\
                            " takes you out with one big swipe of its claw and rips open your chest."+\
                            " Your body is left on the forest floor to be eaten by the bear cubs and any other"+\
                            " critter that walks by your lifeless body. Well at least you tried your best,"+\
                            " and hey now someone gets a free sword."+\
                            " THE END.")

        





#Chestplate#      
    elif purchase == 2:
        gold = gold - 5

        messagebox.showinfo("Protected.",
                            "Now that you can almost gurantee you most likely won't"+\
                            " get stabed through the chest you feel safe enough to set"+\
                            " of into the direction the map specifies.")
        
        messagebox.showinfo("Bear,",
                            "As you walk through the forest following the map you run into an angry"+\
                            " bear. She dosent look like she is going to let you go without a fight" +\
                            " Since you didnt buy a weapon to fight with you dont really know how your"+\
                            " going to get out of this besides running away. So you turn around as quickly"+\
                            " as you can and the bear swipes at your back making a loud clashing noise. She hit"+\
                            " the chestplate! As you continue running along deeper into the forest you notice the"+\
                            " bear is gone and you dropped the map ahwile ago while fleeing. As you come to a stop and"+\
                            " realize you're completly lost and have no idea where you are, you sit down next to the closest tree."+\
                            " You are completly exausted and start to fall asleep, but as you do you here a low growl."+\
                            " To tierd to get up you pass out and are ripped apart in your sleep by the bear."+\
                            " THE END.")

#Sword and Chestplate#         
    elif purchase == 3:
        gold = gold - 10

        messagebox.showinfo("Let's Go!",
                            "Now that you're looking good but broke you set off in the"+\
                            "direction the map specifies with your sword and chestplate.")

        messagebox.showinfo("Bear",
                            "As you walk through the forest following your map you run into"+\
                            " an angry looking bear. The bear dosent look like its going to let you"+\
                            " go without a fight. Not fearing the callange you pull out your sword and"+\
                            " aim for the bears heart.")
        messagebox.showinfo("Kill",
                            "You  swing the sword twords the bears heart and hit right on."+\
                            " The bear falls over and lets out a loud roar, knowing that it isnt going"+\
                            " to get back up you continue on your journy, paying close attention to the map.")
        Hero()

        
        




        
    else:
        Prepaired()


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

    

def Hero():
    """ The Choice Where you live """
    
    messagebox.showinfo("Hero",
                        "You follow the map for a long while and end up at a large"+\
                        " cave. You attempt to peer inside but you are only meet with"+\
                        " darkness. ")
    
    messagebox.showinfo("Hero",
                        "You decide you have to go into the cave if you have already traveled"+\
                        " this far. As you walk in you hear a strange noise...")
    messagebox.showinfo("Dragon",
                        "As your eyes ajust to the dim light coming from deeper within the cave,"+\
                        " you are frozen in place by the sight of a dragon... Sitting ontop of all"+\
                        " this gold! Now you have to decide. Try to fight the dragon for the gold(1) or"+\
                        " sneak past it and try to collect as much as you can before he wakes up and you"+\
                        " escape(2).")
    sneak_or_steal = simpledialog.askinteger("Fight OR Flight",
                                             "1 for fighting the dragon or 2 for sneaking."+\
                                             " you decide to...")
    if sneak_or_steal == 1:
        messagebox.showinfo("Fight",
                            "You decide to walk strait up to the dragon and announce your"+\
                            " here. He slowly starts to get up looking strait at you. When the"+\
                            " dragon is almost fully standing you charge at it with your sword."+\
                            " The dragon suffers a massive cut right to the belly but continues to fight you.")
        dragon_Fight()
        
        

    elif sneak_or_steal == 2:
        messagebox.showinfo("Sneak",
                            "As you try your best to sneak around the dragon,"+\
                            " your sword scratchs the ground behind the beast and it"+\
                            " wake up. You try to find a place to hide but its to late."+\
                            " the dragon turns around and blasts you with fire. You are"+\
                            " now super crispy (and also dead) and the dragon returns to rest."+\
                            " THE END.")

def dragon_Fight():
    """ Fighting the dragon """
    
    dragon_hp = random.randint (50,150)
    dragon_dmg = random.randint (5,50)
    hero_hp = random.randint (100,200)
    hero_dmg = random.randint (25,50)

    while hero_hp >= 0 or dragon_hp >=0:
        attack = simpledialog.askinteger("Attack.",
                                         " Press 1 to attack dragon.")


        if attack == 1:
            dragon_hp -= hero_dmg
            hero_hp -= dragon_dmg
            messagebox.showinfo("Dragon Fight",
                                " You took {} damage.".format(dragon_dmg)+\
                                " Your health is now {}.".format(hero_hp)+\
                                " The dragon has {}.".format(dragon_hp))

        if hero_hp <= 0 or dragon_hp <= 0:
            break
        if hero_hp <= 0:
            messagebox.showinfo("Died",
                                "As hard as you tried the dragon still manages to kill you."+\
                                " You have died. THE END.")
        elif hero_hp >=1:
                messagebox.showinfo("Won",
                                    "You kill the dragon and all the treasure is now yours."+\
                                    " The End.")

                
        
    
    
    
        
        






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








    
