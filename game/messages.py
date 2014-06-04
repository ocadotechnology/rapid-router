
""" Strings used in the class view. """

def chooseClass():
    return "Choose a class you want to see."

def noPermission():
    return "You don't have permissions to see this."


""" String messages used as level tips in the game view. """

def buttons():
    return "Use the buttons in the left bottom part of the screen to create a path that " \
        + "will lead the van to the destination."

def dragAndDrop():
    return "<br>Drag the blocks from the left to the white space and connect them with one " \
        + "another to create series of commands that will guide the driver to the destination. " \
        + "To remove an instruction place it back in the gray area. Remember to start from the " \
        + "<b>start block</b>."

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
        + "a program that guides the driver to the house."
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
