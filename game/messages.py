def noPermissionMessage():
    return "You have no permission to see this."


def notSharedLevel():
    return "This level is private. You can only see the public levels and the ones created by " \
           + "other users only if they share them with you."


""" Strings used in the scoreboard. """


def noPermissionTitle():
    return "No permission "


def noPermissionScoreboard():
    return "Scoreboard is only visible to students and teachers. Log in if you think you " + \
           "should be able to see it. "


def noDataToShow():
    return "There is no data to show. Please contact your administrator if this is unexpected. "


""" String messages used on the settings page. """


def shareTitle():
    return "Level Share"


def shareSuccessfulPerson(name, surname):
    return "You shared your level with {0} {1} successfully! ".format(name, surname)


def shareSuccessfulClass(className):
    return "You shared your level with class {0} successfully! ".format(className)


def shareUnsuccessfulPerson(name, surname):
    return "We were unable to find {0} {1}. Are you sure you got their name right?".format(name, surname)


def shareUnsuccessfulClass(className):
    return "We were unable to find class {0}. Are you sure you got it right?".format(className)


def chooseAvatar():
    return "Choose your avatar "


def uploadAvatar():
    return "...Or upload your own "


def noLevelsToShow():
    return "It seems that you have not created any levels. How about creating one now? "


def levelsMessage():
    return "All the levels you have created so far. Click on them to play them or share them " \
           + "with your friends. "


def sharedLevelsMessage():
    return "All the levels created by others that were shared with you. Click on them to " \
           + "play them"


def noSharedLevels():
    return "No one shared a level with you yet. "


""" Strings used in the class view. """


def chooseClass():
    return "Choose a class you want to see. "


def noPermission():
    return "You don't have permissions to see this. "












""" String messages used as level tips in the game view. """


def build_description(title, message):
    return "<b>" + title + "</b><br><br>" + message


def description_level_default():
    return "Write something. "  # TODO: Come up with something.


def description_overall():
    return "<i>Help the van deliver the order to the customers in the house.</i><br><br>"


def hint_level_default():
    message = "Think back to earlier levels. What did you learn? "
    return message


def title_level1():
    return "Can you help the van get to the house? "


def description_level1():
    message = "Choose the right blocks to tell the van where to go. <br> Drag the blocks under " \
          + " the 'Start' block to attach them. <br> Are you happy with your sequence? Then click " \
          + "'go'! "  # TODO: not direct control?
    return build_description(title_level1(), message)


def hint_level1():
    message = "Drag the <b>Move forwards</b> block so that it is under the <b>Start</b> " \
        + "block - close enough to be touching. "
    return message


def title_level2():
    return "This time the house is further away. "


def description_level2():
    message = "Can you help the van get there? <br> Like last time, drag the right blocks and " \
        + "attach them under the 'Start' block. <br> To remove a block, drag it back to the " \
        + "left of the screen or drop them in the bin. "
    return build_description(title_level2(), message)


def hint_level2():
    message = "A block can be placed next to or under another, like a jigsaw. A second <b>Move " \
        + "forwards</b> block can be placed under the first <b>Move forwards</b> block."
    return message


def title_level3():
    return "Can you make the van turn right? "


def description_level3():
    message = "This time, the van has to turn right to reach the house. Make sure you use the " \
        + "'turn right' block in your sequence. <br> Drag the blocks and attach them under the " \
        + "'Start' block like before. To remove a block, drag it back to the left of the screen. "
    return build_description(title_level3(), message)


def hint_level3():
    message = "A block can be placed next to another if the jigsaw pieces fit. A <b>Turn " \
        + "right</b> block can be placed under the first <b>Move forwards</b> block. "
    return message


def title_level4():
    return "You are getting good at this! Let's try turning left. "


def description_level4():
    message = "This time the van has to go left as well as right. Make sure you use the 'Turn " \
        + "left' block in your sequence. <br> Drag and attach the blocks like before."
    return build_description(title_level4(), message)


def hint_level4():
    message = " A <b>Turn left</b> block can be placed under the series of <b>Move forwards</b> " \
        + "block. "
    return message


def title_level5():
    return "Good work! You are ready for something harder. "


def description_level5():
    message = "You already know how to make the van turn left or right. This time the van has to " \
        + "make lots of turns to reach the house. <br> Drag and attach the blocks to make your " \
        + "sequence. "
    return build_description(title_level5(), message)


def hint_level5():
    message = "This road starts by curving to the <b>left</b>. Then it curves to the <b>right</b>. "
    return message


# Paulina's Creation
def title_level6():
    return "Well done! Let's use all three blocks. "


# Paulina's Creation
def description_level6():
    message = "This time the van has to go forward, left and right. <br> Drag and attach the " \
        + "blocks like before. "
    return build_description(title_level6(), message)


def hint_level6():
    message = "Follow the road round. Doing this with the arrows next to the <b>GO</b> button " \
        + "will drag the blocks into a sequence for you. "
    return message


# Paulina's Creation
def title_level7():
    return "This maze is more complicated. "


# Paulina's Creation
def description_level7():
    message = "Practise your newly acquired skills on this road by helping the driver to arrive " \
              + "at the house. "
    return build_description(title_level7(), message)


def hint_level7():
    message = "Follow the road round. Doing this with the arrows next to the <b>GO</b> button " \
        + "will drag the blocks into a sequence for you. "
    return message


def title_level8():
    return "The warehouse is not always in the same place. "


def description_level8():
    message = "The driver does not always start the journey by going to the right of the screen. "
    return build_description(title_level8(), message)


def hint_level8():
    message = "For you, it looks like the van is going down the screen. For the driver, il looks " \
        + "like it's going forwards."
    return message


def title_level9():
    return "Can you go from right to left? "


def description_level9():
    message = "Practise your new skills on this road by helping the driver to arrive at the house. "
    return build_description(title_level9(), message)


def hint_level9():
    message = "For you, it might look like the van needs to go to the left. But for the driver, " \
        + "it looks like the van needs to go forwards, then turn left. <br><br> Do you know " \
        + "which blocks to use to tell him how to do that? "
    return message


# Paulina's creation
def title_level10():
    return "Well done! How about another go? "


# Paulina's creation
def description_level10():
    message = "You've done beautifully so far. Try to get the driver to the destination in this " \
        + "maze now. "
    return build_description(title_level10(), message)


def hint_level10():
    message = "This map is not so complicated. Notice that for you the van needs to go up, but " \
        + "the driver actually needs to turn left. <br><br> Do you know which turn he's going to " \
        + "take next? "
    return message


def title_level11():
    return "Snail maze! "


def description_level11():
    message = "Uh oh, a tricky snail maze! Can you take the driver through it? "
    return build_description(title_level11(), message)


def hint_level11():
    message = "The maze looks a bit like a snail, doesn't it? That means that for most of time " \
        + "the van should only be going <b>forwards</b> and <b>left</b>. "
    return message


def title_level12():
    return "This maze is more complicated. "


def description_level12():
    message = "Congratulations, you should be now able to solve quite complex levels. <br><br> " \
        + "Here's one you can have a go at. "
    return build_description(title_level11(), message)


def hint_level12():
    message = "This maze might look much longer and more complicated, but it's not that hard. " \
        + "<br><br> Start by going forwards and right first."
    return message


# Paulina's Creation
def title_level13():
    return "Multiple routes"


# Paulina's Creation
def description_level13():
    message = "Very often there is more than one way of getting to the destination. In such " \
        + "cases, we tend to choose the ones that let us do that with as few steps as possible. " \
        + "<br><br> Help the van driver find the shortest route to the house. "
    return build_description(title_level13(), message)


# Paulina's Creation
def hint_level13():
    message = "The route that you probably want to take starts with the van turning left " \
        + "followed by turning right. Do you know what follows next? "
    return message


# Paulina's Creation
def title_level14():
    return "Can you spot the shortest route? "


# Paulina's Creation
def description_level14():
    message = "So many options to choose from! <br><br> Do you know which one to choose to let " \
        + "the driver reach the destination in the shortest way possible? "
    return build_description(title_level14(), message)


# Paulina's Creation
def hint_level14():
    message = "The middle route seems to be shortest path. Do you know what sequence of " \
        + "instructions will let the van driver take it? "



# Paulina's Creation
def title_level15():
    return "How about multiple deliveries? "


# Paulina's Creation
def description_level15():
    message = "Professional drivers tend to have a few houses to visit. To deliver to one of " \
        + "many destinations drive to it and append the <b>'deliver'</b> block. <br><br>" \
        + "Make sure you produce a program which lets the van travel the shortest route! "
    return build_description(title_level15(), message)


# Paulina's Creation
def hint_level15():
    message = "Drive to the house closer to the starting point first to make sure the van " \
        + "travels the shortest route possible. <br><br> Although the deliver instruction is not " \
        + "necessary in case of a single destination, we do need it in this map. <br><br> " \
        + "Once the van is at the home square, make it execute the '<b>deliver</b>' command. Do " \
        + "that for each house."


# Paulina's Creation
def title_level16():
    return "Even more destinations! "


# Paulina's Creation
def description_level16():
    message = "Well done! You have done great so far! Let's raise the bar and add another house " \
        + "to visit. "
    return build_description(title_level16(), message)


# Paulina's Creation
def hint_level16():
    message = "Although the deliver instruction is not necessary in case of a single destination, " \
        + " we need it now, with 2 extra houses to visit. <br><br> " \
        + "Once the van is at the home square, make it execute the '<b>deliver</b>' command. Do " \
        + "that for each house you visit."


# Paulina's Creation
def title_level17():
    return "House overload! "


# Paulina's Creation
def description_level17():
    message = "Well done, you're getting a hang of it! Can you do the same for even more houses? " \
        + "Don't forget to use the '<b>deliver</b>' block at each destination! "
    return build_description(title_level17(), message)


# Paulina's Creation
def hint_level17():
    message = "Test your application to make sure that the van travels the shortest distance " \
        + "possible to visit all the houses. "


# Paulina's Creation
def title_level18():
    return "Tangled! "


# Paulina's Creation
def description_level18():
    message = "Practise your new skills on this road by helping the driver to arrive at all of " \
        + " the houses. "
    return build_description(title_level18(), message)



# Paulina's Creation
def hint_level18():
    message = "To make sure your van picks the shortest route, first turn left. "


def title_level19():
    return "Repeating yourself is boring."


def description_level19():
    message = "Attach a block inside the '<b>Repeat</b>' block to make the van repeat it. <br> " \
        + "This means you can use one block instead of lots of blocks to do the same thing. <br> " \
        + "How many times do you want the block repeated? Type the number into the " \
        + "'<b>Repeat</b>' block. "
    return build_description(title_level19(), message)


def hint_level19():
    message = "A <b>Move forwards</b> block can be placed inside a <b>Repeat</b> block (to the " \
        + "right of the word 'Do'). <br><br> Don't forget to change the number of times you need " \
        + "to repeat. "
    return message


def title_level20():
    return "Use the 'Repeat' block to make your sequence simpler. "


def description_level20():
    message = "You drove the van down this road on Level 5. This time, use the 'Repeat' block to " \
              + "get the van to the house. This will make your sequence simpler than last time."
    return build_description(title_level20(), message)


# Paulina's Creation
def hint_level20():
    message = "This level can be broken down into three sets of: 'turn left, then turn right'. "
    return message


# Paulina's Creation
def title_level21():
    return "Four leaf clover."


# Paulina's Creation
def description_level21():
    message = "This path looks a bit like a four leaf clover. Can you take the driver through it? "
    return build_description(title_level21(), message)


# Paulina's Creation
def hint_level21():
    message = "This level can be broken down into sets of: move forwards, turn left, turn right, " \
        + "turn left. "
    return message


# Paulina's Creation
def title_level22():
    return "Quite long and complex. "


# Paulina's Creation
def description_level22():
    message = "An algorithm to help the driver reach the destination does not always get really " \
        + "simple, but it definitely can get shorter by using the repeat blocks. Are you up for " \
        + "this challenge? "
    return build_description(title_level22(), message)


# Paulina's Creation
def hint_level22():
    message = "Look at solution using simple move forwards, turn left and turn right blocks. Are " \
        + "any neighbouring instructions the same? Collapse them into one repeat! "
    return message


# Paulina's Creation
def title_level23():
    return "Sssssssssnake!"


# Paulina's Creation
def description_level23():
    message = "This path seems to be winding just like a snake! Can you find a nice and simple " \
        + "solution to lead the driver to the destination? "
    return build_description(title_level23(), message)


# Paulina's Creation
def hint_level23():
    message = "How about using repeat inside another repeat? <br><br> This level can be broken " \
        + "down into sets of a set of moves forwards, two turns left, set of moves forwards, two " \
        + "turns right."
    return message


def title_level24():
    return "The road is very long and very bendy."


def description_level24():
    message = "Wow! Look at that! It won't get more complicated than this, we promise."
    return build_description(title_level23(), message)

def hint_level24():
    message = "With all these twists and turns, you will have to think hard about what blocks to " \
        + "use. <br><br> Which block is first, and which blocks will keep the van going? <br><br>" \
        + "A Move forwards block can be placed inside a Repeat block (to the right of the word " \
        + "'Do'). <br><br> Don't forget to change the number of times you need to repeat. "
    return message


# Paulina's Creation
def title_level25():
    return "Waterfall."


# Paulina's Creation
def description_level25():
    message = "Since you did so well with the loops within loops (we call them 'nested loops')" \
        + "have a go at this level. "
    return build_description(title_level25(), message)


# Paulina's Creation
def hint_level25():
    message = "Most of the program will consist of sets of move forwards and a set of turn right " \
        + "and turn left."
    return message


# Paulina's Creation
def title_level26():
    return "Winter wonderland!"


# Paulina's Creation
def description_level26():
    message = "Notice the snow! You can create new levels with different 'themes' of backgrounds " \
        + "and decorations in the level editor. But first, try leading the van to the house! "
    return build_description(title_level26(), message)


# Paulina's Creation
def hint_level26():
    message = "Break the program into two repeats with a turn left in between them. "
    return message


# Paulina's Creation
def title_level27():
    return "Winter wonderland!"


# Paulina's Creation
def description_level27():
    message = ""
    return build_description(title_level27(), message)


# Paulina's Creation
def hint_level27():
    message = ""
    return message


# Paulina's Creation
def title_level28():
    return ""


# Paulina's Creation
def description_level28():
    message = ""
    return build_description(title_level28(), message)


# Paulina's Creation
def hint_level28():
    message = ""
    return message


def title_level29():
    return "No need for numbers. "


def description_level29():
    message = "Attach a block inside a 'Repeat until' block, and the van will keep repeating it. " \
              + "The van will not stop until it has reached the point you want it to stop. <br> " \
              + "You do not have to work out how many times the van should repeat your block. Instead, " \
              + "just tell the van to stop when it reaches the house. "
    return build_description(title_level29(), message)


def hint_level29():
    message = "This blocks should read like a sentence: '<b>Repeat</b> (these blocks) <b>until " \
        + "at house: move forwards</b>'."
    return message


def title_level30():
    return "Can you do that again? "


def description_level30():
    message = "Well done, you did it! Now have a go at using the 'Repeat until' block on a road " \
              + "with lots of turns. "
    return build_description(title_level30(), message)


def hint_level30():
    message = "This blocks should read like a sentence: '<b>Repeat</b> (these blocks) <b>until " \
        + "at house: turn left</b>, (then) <b>turn right</b>'."
    return message


# Paulina's Creation
def title_level31():
    return "Practice makes perfect. "


# Paulina's Creation
def description_level31():
    message = "Have another go to make sure you let your knowledge sink in. "
    return build_description(title_level31(), message)


# Paulina's Creation
def hint_level31():
    message = "This program can be broken into sets of <b>turn left, turn right and two moves " \
        + "forwards</b>. "
    return message


# Paulina's Creation
def title_level32():
    return "Until fever! "


# Paulina's Creation
def description_level32():
    message = "Good job! Can you help the driver reach the destination again? "
    return build_description(title_level32(), message)


# Paulina's Creation
def hint_level32():
    message = "This program is quite similar to the previous one you solved. Do you remember the " \
        + "solution you came up with back then? "


def title_level33():
    return "Now it's time to try the 'if' block. "


def description_level33():
    message = "Another way of telling the van what to do is to use the 'If' block . For example, " \
        + "you can tell the van to go forward if the road goes forward, or to turn left if the " \
        + "road goes forward, or to turn left if it goes left. <br> Try using the 'If block' and " \
        + "the 'Repeat' block together. <br> The 'Repeat' block will stretch if you attach the " \
        + "'If' block inside it. "
    return build_description(title_level33(), message)


def hint_level33():
    message = "'<b>If</b> a <b>road exists forwards</b> then <b>move forwards</b>'. This will " \
        + "need to be repeated to get to the house. "
    return message


# Paulina's Creation
def title_level34():
    return "Multiple 'if's"


# Paulina's Creation
def description_level34():
    message = "If statements are really useful when you have to make a decision based on some " \
        + "external factor. So, for example, when you have to decide which way to go based on " \
        + "what direction the road goes. If you attach multiple if statements, you can create " \
        + "a program which helps the driver go through a bendy path. "


# Paulina's Creation
def hint_level34():
    message = "At each step (we say: at each loop repetition or iteration) the driver faces a" \
        + "choice: he can can either move forwards or turn right. Append two 'if' blocks to " \
        + "mirror the situation. "
    return message


# Paulina's Creation
def title_level35():
    return "Let's put it all together!"


# Paulina's Creation
def description_level35():
    message = "You have discovered the magic of if statements. Can you make a program that makes " \
        + "use of all the move blocks (move forwards, turn left and turn right) to lead the " \
        + "driver to the house? "

# Paulina's Creation
def hint_level35():
    message = "At each step (we say: at each loop repetition or iteration) the driver faces a " \
        + "choice: he can either move forwards, turn left or turn right. Append three 'if' " \
        + "blocks to mirror the situation. "


# Paulina's Creation
def title_level36():
    return "If-else."


# Paulina's Creation
def description_level36():
    message = "You can also use the modified 'If' block to create choices. Click on the star on " \
        + "the if block to unwind the choices. Add 'else if' to the 'If' block so the van knows " \
        + "what to check if the first choice can't be done. <br> For example, " \
        + "tell the van to 'turn left if the road turns left'. Add 'else if the road exists " \
        + "right, turn right. This reduces amount of blocks used and makes sure at most one step " \
        + "is taken at each loop repetition. Such version of an algorithm is called a generic " \
        + "algorithm - it will work with most kinds of simple routes. "
    return build_description(title_level36(), message)


# Paulina's Creation
def hint_level36():
    message = "You can either solve this level similar to the way you've done the previous ones, " \
        + "or use the else if options. <br><br> If you choose to use the else if alternative, " \
        + "the program should consist of repeated block which reads like: if road exists " \
        + "forwards, move forwards, else if road exists left, turn left, else if road exists " \
        + "right, turn right."


# Paulina's Creation
def title_level37():
    return "A bit longer."


# Paulina's Creation
def description_level37():
    message = "Let's raise a bar a bit and help the travel a bit further. Notice that the length " \
        + "of the path no longer changes the length of the program! "
    return build_description(title_level36(), message)


# Paulina's Creation
def hint_level37():
    message = "Think back to the solutions you produced using if statements before."


def title_level38():
    return "Third time lucky! "


def description_level38():
    message = "Well done! You've got so far. Can you apply the knowledge you gained going " \
        + "through this part of the game to this level? "


def hint_level38():
    message = "Think back to the solutions you produced using if statements before."


# Paulina's Creation
def title_level39():
    return "Dead ends!"







def title_level15():
    return "This time use 'Repeat While'. "


def description_level15():
    message = "Last time you told the van to repeat a block until it reached the house. This " \
        + "time, tell the van to repeat the block while not at the house. This means it will " \
        + "stop when it does reach the house. <br> This is called a While Loop. The block is " \
        + "repeated while it is true that the van is not at the house. "
    return build_description(title_level15(), message)


def title_level16():
    return "Put the 'while loop' to the test. "


def description_level16():
    message = "The van is back at the bendy road. Can you use the 'Repeat while' block to make a " \
        + "While Loop? <br> Make the van repeat your While Loop while it is not at the house. " \
        + "This means you will have a short, simple sequence to make it reach the house. "
    return build_description(title_level16(), message)





def title_level18():
    return "Good work! What else can you do? "



def title_level19():
    return "What if you cannot see the road? "


def description_level19():
    message = "If you cannot see the road, you cannot see the choices to make. No problem! " \
        + "This is where 'If' and 'else' are useful. <br> You can tell the van to go one way if " \
        + "the road goes that way. If the road does not go that way, the van will do nothing. " \
        + "<br> Keep adding choice using 'else if' and the van will move when the program finds " \
        + "the right choice. <br> You can add as many 'else if' choices as you like. Add 'else' " \
        + "as your last choice so that the van knows what to do when the choices run out."
    return build_description(title_level19(), message)


def title_level20():
    return "Fantastic! Can you do it again? "


def description_level20():
    message = "Here is another road. It is even bendier than before, but you know lots of ways " \
        + "to get the van to the house. <br> Get the van to the house using what you have learnt. "
    return build_description(title_level20(), message)


#
# Paulina's happy creations
#
#
def title_level21():
    return "Junction time!"


def description_level21():
    message = "Have you noticed something different? Now you can solve mazes with junctions. " \
        + "This means you have more than one way to reach the destination. Do you accept the" \
        + "challenge? "
    return build_description(title_level21(), message)


def title_level22():
    return "Snail roundabout. "


def description_level22():
    message = "This maze does look like a snail a bit, doesn't it? Can you navigate the van " \
        + "to the destination having a knot on your way? Remember - the shorter the path, the " \
        + "better. "
    return build_description(title_level22(), message)


def title_level23():
    return "Great! Another try? "


def description_level23():
    message = "You've done fantastic job so far! Can you find the way to the house this time? " \
              + "There is more than one solution! "
    return build_description(title_level23(), message)


def title_level24():
    return "That's tangled up! "


def description_level24():
    message = "This sure is one complicated maze. Can you spot the shortest path? "
    return build_description(title_level24(), message)


def title_level25():
    return "Find the pattern in this chaos."


def description_level25():
    message = "This maze surely can be solved with the general algorithm. But watch out - the " \
        + "order in which you check for the instructions will matter in this case! "
    return build_description(title_level25(), message)


def title_level26():
    return "Congratulations! You've made it so far!"


def description_level26():
    message = "Let's now practise what you've learnt so far. Create a program which lets the " \
              + "driver reach the house in the shortest way. "
    return build_description(title_level26(), message)


def title_level27():
    return "Traffic lights!"


def description_level27():
    message = "Don't ignore the law. Don't let the van driver drive through the red lights. "
    return build_description(title_level27(), message)


def title_level28():
    return "Following procedure"


def description_level28():
    message = "Use procedures to find the destination."
    return build_description(title_level28(), message)


def title_level29():
    return "Threading your way"


def description_level29():
    message = "Try using multiple threads to get both vans to their destination"
    return build_description(title_level29(), message)


def title_level30():
    return "Title level 30"


def description_level30():
    message = ""
    return build_description(title_level30(), message)


def title_level31():
    return "Title level 31"


def description_level31():
    message = ""
    return build_description(title_level31(), message)


def title_level32():
    return "Title level 32"


def description_level32():
    message = ""
    return build_description(title_level32(), message)


def title_level33():
    return "Decision making"


def description_level33():
    message = "Head forwards if you can.  "
    return build_description(title_level33(), message)


def title_level34():
    return "Check for several things."


def description_level34():
    message = "See if you can move forwards, and then see if you can turn. "
    return build_description(title_level34(), message)


def title_level35():
    return "Look both ways"


def description_level35():
    message = "If you can drive forwards, drive forwards, or if you can drive " \
              + "right go right, or if you can drive left, drive left. "
    return build_description(title_level35(), message)


def title_level36():
    return "Drive where there's road"


def description_level36():
    message = "If you're able to drive in a direction, you should drive that way. "
    return build_description(title_level36(), message)


def title_level37():
    return "Title level 37"


def description_level37():
    message = ""
    return build_description(title_level37(), message)


def title_level38():
    return "Title level 38"


def description_level38():
    message = ""
    return build_description(title_level38(), message)


def title_level39():
    return "House at the end of the road"


def description_level39():
    message = ""
    return build_description(title_level39(), message)


def title_level40():
    return "Title level 40"


def description_level40():
    message = ""
    return build_description(title_level40(), message)


def title_level41():
    return "Title level 41"


def description_level41():
    message = ""
    return build_description(title_level41(), message)


def title_level42():
    return "Title level 42"


def description_level42():
    message = ""
    return build_description(title_level42(), message)


def title_level43():
    return "Title level 43"


def description_level43():
    message = "You should be really good at this by now. Can you manage this complicated route?"
    return build_description(title_level43(), message)


def title_level44():
    return "Simple traffic light."


def description_level44():
    message = "You have to wait at red traffic lights until they become green. "
    return build_description(title_level44(), message)


def title_level45():
    return "More traffic lights."


def description_level45():
    message = ""
    return build_description(title_level45(), message)


def title_level46():
    return "Traffic lights around a corner."


def description_level46():
    message = ""
    return build_description(title_level46(), message)


def title_level47():
    return "Lots of traffic lights."


def description_level47():
    message = ""
    return build_description(title_level47(), message)


def title_level48():
    return "Make a decision at the traffic lights."


def description_level48():
    message = ""
    return build_description(title_level48(), message)


def title_level49():
    return "Traffic lights everywhere."


def description_level49():
    message = ""
    return build_description(title_level49(), message)


#
# The end of Paulina's Happy Creation.
#
#













def hint_level6():
    message = "A <b>move forwards</b> block can be placed inside of the <b>repeat</b> block (to " \
              + "the right of the word 'do'). <br>Don't forget to change the number of times you need " \
              + "to repeat. "
    return message




def hint_level6():
    message = "This maze might look much longer and more complicated, but it's not that hard. " \
        + "<br><br> Start by going <b>forwards</b> and <b>right</b> first. "


def hint_level8():
    message = "The blocks should read like a sentence: <b>Repeat</b> (the following) <b>until at " \
              + "destination</b>: <b>move forwards</b>. "
    return message




def hint_level10():
    message = "With all these twists and turns, you will have to think hard about what blocks to " \
        + "use. <br><br> Which block is first, and which blocks will keep the van going? "
    return message







def hint_level14():
    message = "The blocks should read like a sentence: '<b>Repeat</b> (this block) <b>until " \
        + "at house: turn left</b>, (then) <b>turn right</b>'."
    return message


def hint_level15():
    message = "<b>While not</b> is like <b>until</b>. <br><br> The blocks should read like a " \
        + "sentence: '<b>Repeat</b> (these block) <b>until at house: move forwards</b>."
    return message


def hint_level16():
    message = ""
    return 





def hint_level18():
    message = "Check where the road is by using '<b>if-else</b>'. <br><br> You can make an '<b>" \
        + "if-else</b>' block by clicking on tge star of the '<b>if</b>' block and adding '<b>" \
        + "else</b>'. <br><br> If the road goes the same way you've put after '<b>if</b>' (we " \
        + "say 'if the conditions are true'), the van will follow those blocks. <br><br>" \
        + "If the road doesn't go the same way (we say 'the conditions are false', the van will " \
        + "follow the blocks after '<b>else</b>'. <br><br> <b>If</b> a <b>road exists left, turn " \
        + "left, else turn right</b>. "
    return message


def hint_level19():
    message = "We need to check where the road is using an 'if-else if' block. <br><br> You can " \
        + "make an '<b>if-else if</b>' block by clicking the star on the '<b>if</b>' block and " \
        + "adding the '<b>else if</b>'.If the first condition block is true (if the road goes " \
        + "the way you've put), the van follows the blocks after '<b>if</b>'. <br><br>" \
        + "If the second condition block is true (if the road doesn't go the way you've put), " \
        + "the van follows the blocks after '<b>else if</b>'. <br><br> <b>If</b> a <b>road " \
        + "exists left, turn left. Else if</b> a <b>road exists right, turn right, else move " \
        + "forwards.</b> "
    return message


def hint_level20():
    message = "We need to check where the road is using an '<b>if-else if</b>' block. <br><br> " \
        + "You can make an '<b>if-else if</b>' block by clicking the star on the '<b>if</b>' " \
        + "block and adding the '<b>else if</b>'. <br><br> If the first condition block is true " \
        + "(if the road goes the way you've put), the van follows the blocks after '<b>if</b>'. " \
        + "If the second condition block is true (if the road doesn't go the way you've put), " \
        + "the van follows the blocks after '<b>else if</b>'. <br><br> " \
        + "<b>If</> a <b>road exists left, turn left. Else if</b> a <b>road exists right, turn " \
        + "right, else move forwards</b>. "
    return message


def hint_level21():
    message = "We need to check where the road is using an '<b>if-else if</b>' block. <br><br> " \
        + "You can make an '<b>if-else if</b>' block by clicking the star on the '<b>if</b>' " \
        + "block and adding the '<b>else if</b>'. <br><br> If the first condition block is true " \
        + "(if the road goes the way you've put), the van follows the blocks after '<b>if</b>'. " \
        + "If the second condition block is true (if the road doesn't go the way you've put), " \
        + "the van follows the blocks after '<b>else if</b>'. <br><br> " \
        + "<b>If</> a <b>road exists left, turn left. Else if</b> a <b>road exists right, turn " \
        + "right, else move forwards</b>. "
    return message


def hint_level22():
    message = "Be careful about the order you put your '<b>if</b>' blocks in. <br><br> If you " \
        + "make the van check for a left turn first you might make the van go further than it " \
        + "needs to. "
    return message


def hint_level23():
    message = "Be careful about the order you put your '<b>if</b>' blocks in. <br><br> If you " \
        + "make the van check the road goes forwards, you might make the van go in a circle. "
    return message


def hint_level24():
    message = "This is a complicated maze! There are many paths, but one is definitely shorter " \
        + "than the others. Hint: try going right first. "
    return message


def hint_level25():
    message = "Do not use the solution you came up with earlier. Direct commands will work " \
        + "better here. "
    return message


def hint_level26():
    message = "Here you can use a mix of direct commands your algorithm to make sure your route " \
        + "is as short as possible. <br><br> You need to go forward then turn left. Then add a " \
        + "'<b>while not at destination</b>', '<b>if road exists forward go forward</b>' and " \
        + "'<b>else turn right</b>'"
    return message


def hint_level27():
    message = "Don't worry about the algorithm you've already come up with. Take the first turn " \
        + "left which has fewer traffic lights. <br><br> Once your van is right under the " \
        + "traffic lights, make it wait for a green light by adding '<b>while traffic light red" \
        + "</b>' '<b>do</b>' '<b>wait</b>' blocks."
    return message


def hint_level28():
    message = hint_level_default()
    return message


def hint_level29():
    message = hint_level_default()
    return message


def hint_level30():
    message = hint_level_default()
    return message


def hint_level31():
    message = hint_level_default()
    return message


def hint_level32():
    message = hint_level_default()
    return message


def hint_level33():
    message = hint_level_default()
    return message


def hint_level34():
    message = hint_level_default()
    return message


def hint_level35():
    message = hint_level_default()
    return message


def hint_level36():
    message = hint_level_default()
    return message


def hint_level37():
    message = hint_level_default()
    return message


def hint_level38():
    message = hint_level_default()
    return message


def hint_level39():
    message = hint_level_default()
    return message


def hint_level40():
    message = hint_level_default()
    return message


def hint_level41():
    message = hint_level_default()
    return message


def hint_level42():
    message = hint_level_default()
    return message


def hint_level43():
    message = hint_level_default()
    return message


def hint_level44():
    message = hint_level_default()
    return message


def hint_level45():
    message = hint_level_default()
    return message


def hint_level46():
    message = hint_level_default()
    return message


def hint_level47():
    message = hint_level_default()
    return message


def hint_level48():
    message = hint_level_default()
    return message


def hint_level49():
    message = hint_level_default()
    return message


def hint_level50():
    message = hint_level_default()
    return message
