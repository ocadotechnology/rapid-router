""" Strings used in the scoreboard. """

def noPermissionTitle():
    return "No permission "

def noPermissionScoreboard():
    return "Scoreboard is only visible to students and teachers. Log in if you think you " + \
        "should be able to see it. "


""" String messages used on the settings page. """

def shareTitle():
    return "Level Share"

def shareSuccessful(name, surname):
    return "You shared your level with {0} {1} successfully! ".format(name, surname)

def shareUnsuccessful(name, surname):
    return "We were unable to find {0} {1}. Are you sure you got their name " \
        + "right?".format(name, surname)

def chooseAvatar():
    return "Choose your avatar "

def uploadAvatar():
    return "...Or upload your own "

def noLevelsToShow():
    return "It seems that you have not created any levels. How about creating one now? "

def levelsMessage():
    return "All the levels you have created so far. Click on them to play them or share them " \
        + "with your friends. "

def noSharedLevels():
    return "No one shared a level with you yet. "


""" Strings used in the class view. """

def chooseClass():
    return "Choose a class you want to see. "

def noPermission():
    return "You don't have permissions to see this. "


""" String messages used as level tips in the game view. """

def buttons():
    return "Use the buttons in the bottom right part of the screen to create a path that " \
        + "will lead the van to the destination. "

def dragAndDrop():
    return "<br>Drag the blocks from the left to the white space and connect them with one " \
        + "another to create series of commands that will guide the driver to the destination. " \
        + "To remove an instruction place it back in the gray area. Remember to start from the " \
        + "<b>start block</b>. "

def description_level_default():
    return description_overall() + dragAndDrop()

def description_overall():
    return "<i>Help the van deliver the order to the customers in the house.</i><br><br>"

def description_level1():
    return description_overall() + buttons()

def description_level2():
    message = "To connect two instructions stack them together on the white space. "
    return description_overall() + message + dragAndDrop()

def description_level3():
    message = "<b>Turn right</b> lets the driver know he has to turn right. "
    return description_overall() + message + dragAndDrop()

def description_level4():
    message = "Turning only right is really boring. Let's add turning left as well. Now you can " \
        + "also use <b>Turn Left</b> command. "
    return description_overall() + message

def description_level5():
    message = "Now you are ready for more complex paths! <br><br>"
    return message + description_overall()

def description_level6():
    message = "Manually adding repeating instructions is boring. That's why there is a " \
        + "<b>repeat</b> block. <b>Repeat</b> block executes the instructions attached inside it " \
        + "specified amount of times. Type into the light green box in the block a number of " \
        + "repetitions. "
    return description_overall() + message

def description_level7():
    message = "This road looks quite familiar, doesn't it? <br> Use the <b>repeat</b> " \
        + "block to simplify your program which guides the driver. "
    return description_overall() + message

def description_level8():
    message = "<b>While</b> and <b>until</b> blocks are quite similar to the repeat one. But " \
        + "instead of specifying exact amount of repetitions, we append a condition. The blocks " \
        + "inside the <b>while</b> or <b>until</b> loops will be executed as long as the " \
        + "condition is true.<br> Change the <b>while</b> block to the <b>until</b> and add " \
        + "the <b>at destination</b> condition. <br> Use the modified set of blocks to create " \
        + "a program that guides the driver to the house. "
    return description_overall() + message

def description_level9():
    message = "Use the <b>until</b> block together with the <b>at destination</b> condition " \
        + "to guide the van to the destination. "
    return description_overall() + message

def description_level10():
    message = "Usually there is no such thing as <b>until</b>. A <b>while</b> block with " \
        + "a negated condition can be used to achieve the same result. <br> Use the <b>not</b> " \
        + "block to reverse the condition. "
    return description_overall() + message

def description_level11():
    message = "Use the <b>while</b> block to create a simpler program to guide the van. "
    return description_overall() + message

def description_level12():
    message = "In this level, we have a look at the <b>if</b> statement. <br> <b>If</b> " \
        + "statements are used when we want a set of commands to be executed only if a condition " \
        + "holds. For example, 'if there is a turn right, turn right'. If the condition " \
        + "is false, the block is omitted. <br> Use the <b>if</b> block to create a path " \
        + "for the driver to reach the destination. "
    return description_overall() + message

def description_level13():
    message = "The <b>if</b> statement is often used with the <b>else</b> clause. " \
        + "If the condition is true, the block in the <b>if</b> gap is executed, otherwise " \
        + "the one following <b>else</b> is. <br> Use an <b>if</b> block together with " \
        + "<b>else</b> one to create a path for the driver. "
    return description_overall() + message

def description_level14():
    message = "Quite often we need to check more than one condition to know how to behave - " \
        + "there might not be a turn right, but we still don't know whether we can go forwards " \
        + "or we have to turn left first. Hence, we can append <b>else if</b> blocks " \
        + "to the <b>if</b> statement. <br> Use the <b>if</b> together with <b>else if</b> " \
        + "and else to guide the driver to the customer. "
    return description_overall() + message

def description_level15():
    message = "Now you are ready! <br> Use all your knowledge and the newly added conditions " \
        + "to guide the van to the house. "
    return description_overall() + message

def description_level16():
    message = "zomg! Junctions! "
    return description_overall() + message

def description_level17():
    message = "zomg! Loops! "
    return description_overall() + message

def description_level18():
    message = "zomg! Non-trivial loops! "
    return description_overall() + message

def description_level19():
    message = "Have fun! "
    return description_overall() + message

def description_level20():
    message = "Non-trivial loops??!? "
    return description_overall() + message

def description_level21():
    message = "zomg! I don't even know what to say! "
    return description_overall() + message

def hint_level_default():
    message = "There is no specific information I can give for this level.<br>Do your best to " \
        + "remember some of the things you have learnt in the previous levels. "
    return message

def hint_level1():
    message = "Drag and drop the <b>move forwards</b> block so that it is under the <b>start</b> " \
        + "block - close enough to be touching. "
    return message

def hint_level2():
    message = "A block can be placed next to another if the jigsaw pieces fit. A second <b>move " \
        + "forwards</b> block can be placed under the first <b>move forwards</b> block. "
    return message

def hint_level3():
    message = "A block can be placed next to another if the jigsaw pieces fit. A <b>turn " \
        + "right</b> block can be placed under the first <b>move forwards</b> block. "
    return message

def hint_level4():
    message = "This road starts by curving to the <b>left</b>. Then it curves to the <b>right</b>. "
    return message

def hint_level5():
    message = "Follow the road round. Doing this with the arrows next to the <b>GO</b> button " \
        + "will produce the instructions for you! "
    return message

def hint_level6():
    message = "A <b>move forwards</b> block can be placed inside of the <b>repeat</b> block (to " \
        + "the right of the word 'do'). <br>Don't forget to change the number of times you need " \
        + "to repeat. "
    return message

def hint_level7():
    message = "This level can be broken down into 3 sets of: 'turn left, then turn right'. "
    return message

def hint_level8():
    message = "The blocks should read like a sentence: <b>Repeat</b> (the following) <b>until at " \
        + "destination</b>: <b>move forwards</b>. "
    return message

def hint_level9():
    message = "The blocks should read like a sentence: <b>Repeat</b> (the following) <b>until at " \
        + "destination</b>: <b>turn left</b>, (then) <b>turn right</b>. "
    return message

def hint_level10():
    message = "<b>while not</b> is the same as <b>until</b>. <br>The blocks should read like a " \
        + "sentence: <b>Repeat</b> (the following) <b>while not at destination</b>: <b>move " \
        + "forwards</b>. "
    return message

def hint_level11():
    message = "<b>while not</b> is the same as <b>until</b>. <br>The blocks should read like a " \
        + "sentence: <b>Repeat</b> (the following) <b>while not at destination</b>: <b>turn " \
        + "left</b>, (then) <b>turn right</b>. "
    return message

def hint_level12():
    message = "<b>if</b> a <b>road exists forwards</b> then <b>move forwards</b>. This "\
        + "instruction will need to be repeated to get to the destination. "
    return message

def hint_level13():
    message = "We need to check where the road is using an <b>if-else</b> block. <br>You can " \
        + "create an <b>if-else</b> block by clicking the star on the <b>if</b> block, and " \
        + "adding the <b>else</b> clause. <br>If the condition block is true, the blocks after " \
        + "<b>if</b> are executed, otherwise the blocks after <b>else</b> are. <br><b>if</b> a " \
        + "<b>road exists left</b>, <b>turn left</b>. <b>else</b> (otherwise) <b>turn right</b>. "
    return message

def hint_level14():
    message = "We need to check where the road is using an <b>if-else if</b> block. <br>You can " \
        + "create an <b>if-else if</b> block by clicking the star on the <b>if</b> block, and " \
        + "adding the <b>else if</b> clause. <br>If the first condition block is true, the " \
        + "blocks after <b>if</b> are executed, otherwise if the second condition block is true, " \
        + "the blocks after <b>else if</b> are executed. <br><b>if</b> a <b>road exists " \
        + "left</b>, <b>turn left</b>. <b>else if a road exists right</b>, <b>turn right</b>. " \
        + "<b>else move forwards</b>. "
    return message

def hint_level15():
    message = hint_level_default()
    return message

def hint_level16():
    message = "<b>If</b> the road <b>is a dead end</b>, you will need to <b>turn around</b>. "
    return message

def hint_level17():
    message = hint_level_default()
    return message

def hint_level18():
    message = hint_level_default()
    return message

def hint_level19():
    message = hint_level_default()
    return message

def hint_level20():
    message = hint_level_default()
    return message

def hint_level21():
    message = hint_level_default()
    return message
