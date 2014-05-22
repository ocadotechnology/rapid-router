def buttons():
    return "Use the buttons in the left bottom part of the screen to create a path that will lead "
    + "the van to the destination. "

def dragAndDrop():
    return "Drag the blocks from the left to the white space and connect them with one another "
    + "to create series of commands that will guide the driver to the destination. "
    + "To remove an instruction place it back in the gray area. Remember to start from the "
    + "start block."

def description_overall():
    return "Help the van deliver the order to the customers in the house. "

def description_level1():
    return description_overall() + buttons()

def description_level2():
    message = "To connect two instructions stack them together on the white space. "
    return message + description_overall() + dragAndDrop()

def description_level3():
    message = "Turn right lets the driver know he has to turn right. "
    return message + description_overall() + dragAndDrop()

def description_level4():
    message = "Turning only right is really boring. Lets add turning left as well. Now you can " \
        + "also use Turn Left command. "
    return message + description_overall()

def description_level5():
    message = "Now you are ready for more complex paths. "
    return message + description_overall()

def description_level6():
    message = "Manualy adding repeating instructions is boring. Thats why there is a repeat " \
    + "block. Repeat block executes the instructions attached inside it specified amount of " \
    + "times. Type into the light green box in the block a number of repetitions. "
    return message + description_overall()

def description_level7():
    message = "This road looks quite familiar, doesnt it? Use the repeat block to simplify " \
    + "your program which guides the driver."
    return message + description_overall()

def description_level8():
    message = "While and Until block is quite similar to the repeat one. But instead of " \
    + "specifying exact amount of repetitions, we append a condition. The blocks inside the " \
    + "while or until loops will be executed as long as the condition is true. " \
    + "Change the while block to the until and append the at destination condition. " \
    + "Use the modifed set of blocks to create a program that guides the driver to the house. "
    return message + descripton_overall()

def description_level9():
    message = "Use the Until block together with the at destination condition to guide the van " \
    + "to the destination."
    return message + description_overall()

def description_level10():
    message = "Usually there is no such thing as until. A while block with a negated condition " \
    + "can be used to achieve the same result. Use the not block to reverse the condition. " 
    return message + description_overall()

def description_level11():
    message = "Use the while block to create a simpler program to guide the van. "
    return message + description_overall()

def description_level12():
    message = "In this lesson, we have a look at the if statement. If statements are used when " \
    + "we want a set of commands to be executed only if a condition holds. For example, if " \
    + "there is a turn right, turn right. If the condition is false, the block is omitted. " \
    + "Use the if block to create a path for the driver to reach the destination. "
    return message + description_overall()

def description_level13():
    message = "The if statement often is used with the else clause. If the condition is true, " \
    + "the block in the if gap is executed, otherwise the one following else is. " \
    + "Use an if block together with else one to create a path for the driver. " 
    return message + description_overall()

def description_level14():
    message = "Quite often we need to check more than one condition to know how to behave - " \
    + "there might not be a turn right, but we still dont know whether we can go forwards or " \
    + "we have to turn left first. Hence, we can append else if blocks to the if " \
    + "statement. Use the if together with else if and else to guide the driver " \
    + "to the customer."
    return message + description_overall()

def description_level15():
    message = "Now you are ready! Use all your knowledge and the newly added conditions to guide " \
    + "the van to the house."
    return message + description_overall()
