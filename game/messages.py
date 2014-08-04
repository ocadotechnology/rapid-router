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


def title_level_default():
    return "Well done! Try solving this one! "


def description_level_default():
    return "Look at this maze! Can you find a way to lead the driver to the house with the " \
        + "shortest route possible? "
    return build_description(title_level_default(), message)


def hint_level_default():
    message = "Think back to earlier levels. What did you learn? "
    return message


def title_level1():
    return "Can you help the van get to the house? "


def description_level1():
    message = "Choose the right blocks to tell the van where to go. <br> Drag the blocks under " \
        + " the 'Start' block to attach them. <br> Are you happy with your sequence? Then " \
        + "click 'go'! "  # TODO: not direct control?
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


def title_level6():
    return "Well done! Let's use all three blocks. "


def description_level6():
    message = "This time the van has to go forward, left and right. <br> Drag and attach the " \
        + "blocks like before. "
    return build_description(title_level6(), message)


def hint_level6():
    message = "Follow the road round. Doing this with the arrows next to the <b>GO</b> button " \
        + "will drag the blocks into a sequence for you. "
    return message


def title_level7():
    return "This maze is more complicated. "


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


def title_level10():
    return "Well done! How about another go? "


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


def title_level13():
    return "Multiple routes"


def description_level13():
    message = "Very often there is more than one way of getting to the destination. In such " \
        + "cases, we tend to choose the ones that let us do that with as few steps as possible. " \
        + "<br><br> Help the van driver find the shortest route to the house. "
    return build_description(title_level13(), message)


def hint_level13():
    message = "The route that you probably want to take starts with the van turning left " \
        + "followed by turning right. Do you know what follows next? "
    return message


def title_level14():
    return "Can you spot the shortest route? "


def description_level14():
    message = "So many options to choose from! <br><br> Do you know which one to choose to let " \
        + "the driver reach the destination in the shortest way possible? "
    return build_description(title_level14(), message)


def hint_level14():
    message = "The middle route seems to be shortest path. Do you know what sequence of " \
        + "instructions will let the van driver take it? "
    return message


def title_level15():
    return "How about multiple deliveries? "


def description_level15():
    message = "Professional drivers tend to have a few houses to visit. To deliver to one of " \
        + "many destinations drive to it and append the <b>'deliver'</b> block. <br><br>" \
        + "Make sure you produce a program which lets the van travel the shortest route! "
    return build_description(title_level15(), message)


def hint_level15():
    message = "Drive to the house closer to the starting point first to make sure the van " \
        + "travels the shortest route possible. <br><br> Although the deliver instruction is not " \
        + "necessary in case of a single destination, we do need it in this map. <br><br> " \
        + "Once the van is at the home square, make it execute the '<b>deliver</b>' command. Do " \
        + "that for each house."
    return message


def title_level16():
    return "Even more destinations! "


def description_level16():
    message = "Well done! You have done great so far! Let's raise the bar and add another house " \
        + "to visit. "
    return build_description(title_level16(), message)


def hint_level16():
    message = "Although the deliver instruction is not necessary in case of a single destination, " \
        + " we need it now, with 2 extra houses to visit. <br><br> " \
        + "Once the van is at the home square, make it execute the '<b>deliver</b>' command. Do " \
        + "that for each house you visit."
    return message


def title_level17():
    return "House overload! "


def description_level17():
    message = "Well done, you're getting a hang of it! Can you do the same for even more houses? " \
        + "Don't forget to use the '<b>deliver</b>' block at each destination! "
    return build_description(title_level17(), message)


def hint_level17():
    message = "Test your application to make sure that the van travels the shortest distance " \
        + "possible to visit all the houses. "
    return message


def title_level18():
    return "Tangled! "


def description_level18():
    message = "Practise your new skills on this road by helping the driver to arrive at all of " \
        + " the houses. "
    return build_description(title_level18(), message)


def hint_level18():
    message = "To make sure your van picks the shortest route, first turn left. "
    return message


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


def hint_level20():
    message = "This level can be broken down into three sets of: 'turn left, then turn right'. "
    return message


def title_level21():
    return "Four leaf clover."


def description_level21():
    message = "This path looks a bit like a four leaf clover. Can you take the driver through it? "
    return build_description(title_level21(), message)


def hint_level21():
    message = "This level can be broken down into sets of: move forwards, turn left, turn right, " \
        + "turn left. "
    return message


def title_level22():
    return "Quite long and complex. "


def description_level22():
    message = "An algorithm to help the driver reach the destination does not always get really " \
        + "simple, but it definitely can get shorter by using the repeat blocks. Are you up for " \
        + "this challenge? "
    return build_description(title_level22(), message)


def hint_level22():
    message = "Look at solution using simple move forwards, turn left and turn right blocks. Are " \
        + "any neighbouring instructions the same? Collapse them into one repeat! "
    return message


def title_level23():
    return "Sssssssssnake!"


def description_level23():
    message = "This path seems to be winding just like a snake! Can you find a nice and simple " \
        + "solution to lead the driver to the destination? "
    return build_description(title_level23(), message)


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


def title_level25():
    return "Waterfall."


def description_level25():
    message = "Since you did so well with the loops within loops (we call them 'nested loops')" \
        + "have a go at this level. "
    return build_description(title_level25(), message)


def hint_level25():
    message = "Most of the program will consist of sets of move forwards and a set of turn right " \
        + "and turn left."
    return message


def title_level26():
    return "Winter wonderland!"


def description_level26():
    message = "Notice the snow! You can create new levels with different 'themes' of backgrounds " \
        + "and decorations in the level editor. But first, try leading the van to the house! "
    return build_description(title_level26(), message)


def hint_level26():
    message = "Break the program into two repeats with a turn left in between them. "
    return message


def title_level27():
    return "Winter wonderland!"


def description_level27():
    message = ""
    return build_description(title_level27(), message)


def hint_level27():
    message = ""
    return message


def title_level28():
    return ""


def description_level28():
    message = ""
    return build_description(title_level28(), message)


def hint_level28():
    message = ""
    return message


def title_level29():
    return "No need for numbers. "


def description_level29():
    message = "Attach a block inside a 'Repeat until' block, and the van will keep repeating it. " \
              + "The van will not stop until it has reached the point you want it to stop. <br> " \
              + "You do not have to work out how many times the van should repeat your block. " \
              + "Instead, just tell the van to stop when it reaches the house. "
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


def title_level31():
    return "Practice makes perfect. "


def description_level31():
    message = "Have another go to make sure you let your knowledge sink in. "
    return build_description(title_level31(), message)


def hint_level31():
    message = "This program can be broken into sets of <b>turn left, turn right and two moves " \
        + "forwards</b>. "
    return message


def title_level32():
    return "Until fever! "


def description_level32():
    message = "Good job! Can you help the driver reach the destination again? "
    return build_description(title_level32(), message)


def hint_level32():
    message = "This program is quite similar to the previous one you solved. Do you remember the " \
        + "solution you came up with back then? "
    return message


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


def title_level34():
    return "Multiple 'if's"


def description_level34():
    message = "If statements are really useful when you have to make a decision based on some " \
        + "external factor. So, for example, when you have to decide which way to go based on " \
        + "what direction the road goes. If you attach multiple if statements, you can create " \
        + "a program which helps the driver go through a bendy path. "
    return build_description(title_level34(), message)


def hint_level34():
    message = "At each step (we say: at each loop repetition or iteration) the driver faces a" \
        + "choice: he can can either move forwards or turn right. Append two 'if' blocks to " \
        + "mirror the situation. "
    return message


def title_level35():
    return "Let's put it all together!"


def description_level35():
    message = "You have discovered the magic of if statements. Can you make a program that makes " \
        + "use of all the move blocks (move forwards, turn left and turn right) to lead the " \
        + "driver to the house? "
    return build_description(title_level35(), message)


def hint_level35():
    message = "At each step (we say: at each loop repetition or iteration) the driver faces a " \
        + "choice: he can either move forwards, turn left or turn right. Append three 'if' " \
        + "blocks to mirror the situation. "
    return message


def title_level36():
    return "If-else."


def description_level36():
    message = "You can also use the modified 'If' block to create choices. Click on the star on " \
        + "the if block to unwind the choices. Add 'else if' to the 'If' block so the van knows " \
        + "what to check if the first choice can't be done. <br> For example, " \
        + "tell the van to 'turn left if the road turns left'. Add 'else if the road exists " \
        + "right, turn right. This reduces amount of blocks used and makes sure at most one step " \
        + "is taken at each loop repetition. Such version of an algorithm is called a generic " \
        + "algorithm - it will work with most kinds of simple routes. "
    return build_description(title_level36(), message)


def hint_level36():
    message = "You can either solve this level similar to the way you've done the previous ones, " \
        + "or use the else if options. <br><br> If you choose to use the else if alternative, " \
        + "the program should consist of repeated block which reads like: if road exists " \
        + "forwards, move forwards, else if road exists left, turn left, else if road exists " \
        + "right, turn right."
    return message


def title_level37():
    return "A bit longer."


def description_level37():
    message = "Let's raise a bar a bit and help the travel a bit further. Notice that the length " \
        + "of the path no longer changes the length of the program! "
    return build_description(title_level37(), message)


def hint_level37():
    message = "Think back to the solutions you produced using if statements before."
    return message


def title_level38():
    return "Third time lucky! "


def description_level38():
    message = "Well done! You've got so far. Can you apply the knowledge you gained going " \
        + "through this part of the game to this level? "
    return build_description(title_level38(), message)


def hint_level38():
    message = "Think back to the solutions you produced using if statements before."
    return message


def title_level39():
    return "Dead ends! "


def description_level39():
    message = "The generic algorithms tend to work in many situations, but sometimes they need " \
        + "some sort of an adjustment to perform the best. Do you know how to create your " \
        + "solution to make sure the van is not trapped in an infinite loop and that it travels " \
        + " the shortest distance possible? "
    return build_description(title_level39(), message)


def hint_level39():
    message = "The generic solution with a check for a dead end as well as the checks for " \
        + "conditions you already know will work in this case, but will not produce the shortest " \
        + "path. Do you know why? "
    return message


def title_level40():
    return "Adjust your previous solution."


def description_level40():
    message = "Can you think of a way you could change the generic algorithm you have " \
        + "implemented earlier to make sure the van driver reaches the house having travelled " \
        + "shortest route? "
    return build_description(title_level40(), message)


def hint_level40():
    message = "If you rearrange the checks for existing roads so that you check if you can turn " \
        + "right before you check for a road ahead of you, will be able to reach the destination " \
        + "using the generic algorithm! "
    return message


def title_level41():
    return "Generic or not? "


def description_level41():
    message = "Do you think you can adjust the generic algorithm to help the driver deliver to " \
        + "the house in an efficient way? Or do you have to come up with a different solution? "
    return build_description(title_level41(), message)


def hint_level41():
    message = "If you were thinking that the general algorithm would be useful in this case - " \
        + "you were right! If you move a check for a turn to be done before you check for the " \
        + "existence of the road forwards - you will come up with the perfect solution. <br><br>" \
        + "Notice that it doesn't matter which turn you check for as first - it will change the " \
        + "the route but provide you with the same score! "
    return message


def title_level42():
    return "Tinker, tailor"


def description_level42():
    message = "Can you try the generic algorithm in this case? Can you think of a way to adjust " \
        + "it or do you see another way of solving this puzzle? "
    return build_description(title_level42(), message)


def hint_level42():
    message = "In this case, generic algorithm cannot be adjusted by simply reshuffling the " \
        + "condition checks. How about creating a straightforward solution without if statements " \
        + "that will help the driver reach the house? "
    return message


def title_level43():
    return "Good work! What else can you do? "


def description_level43():
    message = "You should be really good at this by now. Can you manage this complicated route? "
    return build_description(title_level43(), message)


def hint_level43():
    message = "This route cannot be solved by a generic algorithm. Can you solve it without if " \
        + "statements? Remember to choose the shortest path an algorithm which is as short as " \
        + "possible. "
    return message


def title_level44():
    return "Uh oh... Traffic lights! "


def description_level44():
    message = "Don't break the law. The van must not go through a red light. <br><br>" \
        + "When the van gets to the traffic lights make it wait while the light is red."
    return build_description(title_level44(), message)


def hint_level44():
    message = "Don't worry about the algorithm you've already come up with. Just go forwards! " \
        + "<br><br> Once your van is right under the traffic lights, make it wait for a green " \
        + "light by adding 'wait' blocks. "
    return message


def title_level45():
    return "Generic lights! "


def description_level45():
    message = "Now we're working towards incorporating the lights into the generic algorithm. " \
        + "Can you write a program lets the van either move forwards or wait on the red light? "
    return build_description(title_level45(), message)


def hint_level45():
    message = "You can use an if statement and check if the light is red. If it is, wait, else " \
        + "move forwards. Remember to repeat that until you get to the destination! "
    return message


def title_level46():
    return "Congratulations - you've made it really far!"


def description_level46():
    message = "Let's practise what you've learnt so far. Create a program which gets the van to " \
        + "the house in the shortest way. "
    return build_description(title_level46(), message)


def hint_level46():
        message = "Be careful about the order you put your 'if' blocks in. <br><br> " \
            + "If you make the van check the road goes forwards, you might break the road code."
        return message


def title_level47():
    return "Find the pattern in all this mess. "


def description_level47():
    message = "Put your knowledge to test.  Create an algorithm to lead the driver to the house"
    return build_description(title_level47(), message)


def hint_level47():
    message = "Use an if statement and check if the light is red. If it is, wait, else if road " \
        + "exists forwards, move forwards, else turn right. <br><br> " \
        + "Remember to repeat that until you get to the destination! "
    return message


def title_level48():
    return "Full generic. "


def description_level48():
    message = "Congratulations - you've made it really far! Can you create a full generic " \
        + "algorithm that could help the van reach the destination in the shortest way? "
    return build_description(title_level48(), message)


def hint_level48():
    message = "You need to check if the light is red, if the road exists right, if the road " \
        + "exists forwards, if the road exists left and if it is a dead end. In that order! Do " \
        + "you know how to fill in the gaps to guide the van's behaviour in each of the " \
        + "conditions? "
    return message


def title_level49():
    return "Amazing! Have another go! "


def description_level49():
    message = "Can you think of a way you could change the generic algorithm you have " \
        + "implemented earlier to make sure the van driver reaches the house having travelled " \
        + "shortest route? "
    return build_description(title_level49(), message)


def hint_level49():
    message = "You need to check if the light is red, if the road exists left, if the road " \
        + "exists forwards or if the road exists right. You can also check if it is a dead end. " \
        + "Why is it optional? Do you know how to fill in the gaps to guide the van's behaviour " \
        + "in each of the conditions? "
    return message


def title_level50():
    return "So many traffic lights! "


def description_level50():
    message = "Well that's what you can call a light maze! Can you find the most efficient route " \
        + "that will lead the van driver to the house? You might want to take the route which " \
        + "has fewer traffic lights. "
    return build_description(title_level50(), message)


def hint_level50():
    message = "Don't worry about the algorithm you've already come up with. Take the first turn " \
        + "left which has fewer traffic lights. <br<br> Once your van is right under the traffic " \
        + "lights, make it wait for a green light by adding '<b>while traffic light red</b>' " \
        + "'<b>do</b>' '<b>wait</b>' blocks. "
    return message
