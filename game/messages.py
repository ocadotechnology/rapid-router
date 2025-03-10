from builtins import str


def video_link(url, border):
    return (
        "<div class='popup_video'>"
        "<iframe "
        + "src="
        + str(url)
        + "?rel=0"
        + "' frameborder='"
        + str(border)
        + "' allowfullscreen class='video'></iframe><br></div>"
    )


def play_button_icon_url():
    return '<img src="/static/game/image/icons/play.svg" alt="Play icon">' "<b>Play</b>"


def step_button_icon_url():
    return (
        '<img src="/static/game/image/icons/step.svg" alt="Step button" '
        '" style="width: 4%;">'
    )


def if_else_icon_url():
    return (
        '<img src="/static/game/image/icons/if_else.svg" alt="If Else button" '
        '" style="width: 4%;">'
    )


def if_else_example_url():
    return '<img src="/static/game/image/if_else_example.png" alt="If Else example">'


def not_shared_level():
    return (
        "This level is private. You can only see the public levels and the ones "
        "created by other users only if they share them with you."
    )


""" Strings used in the scoreboard. """


def no_permission_title():
    return "No permission"


def no_permission_scoreboard():
    return (
        "Scoreboard is only visible to school students and teachers. Log in if you "
        "think you should be able to see it."
    )


""" Strings used on the level moderation page. """


def no_permission_level_moderation_title():
    return "No permission"


def no_permission_level_moderation_page():
    return (
        "Level moderation is only visible to teachers. Log in if you "
        "think you should be able to see it."
    )


def no_permission_level_moderation_class():
    return (
        "You do not teach this class. Please contact your administrator if this "
        "is unexpected."
    )


def no_data_to_show_level_moderation():
    return (
        "You have not created any classes and therefore is no data to show. "
        "Please contact your administrator if this is unexpected."
    )


""" String messages used as level tips in the game view. """


def title_night_mode():
    return "Can you find your way in the dark?"


def build_description(title, message):
    return f"<b>{title}</b><br><br>{message}"


# RAPID ROUTER


def title_level1():
    return "Can you help the van get to the house?"


def description_level1():
    message = (
        f"Choose the right blocks to tell the van where to go. <br> Drag the "
        f"blocks under the <b>Start</b> block to attach them. <br> To remove a "
        f"block, drag it into the bin in the bottom right of the screen. "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level1(), message)


def hint_level1():
    return (
        "Try dragging a move forwards block onto the <b>Start</b> block. Then click "
        "the <b>Start</b> block."
    )


def title_level2():
    return "This time the house is further away"


def description_level2():
    message = (
        f"A block can be placed next to or under another, like a jigsaw. A second "
        f"<b>Move forwards</b> block can be placed under the first <b>Move "
        f"forwards</b> block. <br> To remove a block, drag it back to the "
        f"left of the screen or drop it in the bin. <br> When you are happy with "
        f"your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level2(), message)


def hint_level2():
    return (
        "Now there is further to go. How many times do you need to move forwards this "
        "time?"
    )


def title_level3():
    return "Can you make the van turn right?"


def description_level3():
    message = (
        f"This time, the van has to turn right to reach the house. Make sure you use "
        f"the <b>Turn right</b> block in your sequence. <br> Drag the blocks "
        f"and attach them under the <b>Start</b> block like before. To remove a "
        f"block, drag it back to the left of the screen or drop it in the bin. "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level3(), message)


def hint_level3():
    return "Now you need to make a turn. Which way do you need to go?"


def title_level4():
    return "You are getting good at this! Let's try turning left"


def description_level4():
    message = (
        f"This time the van has to go left. Make sure you use the <b>Turn left</b> "
        f"block in your sequence. <br> Drag and attach the blocks like before. "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level4(), message)


def hint_level4():
    return (
        "You’re doing really well! This time you need to go a bit further and turn the "
        "other way. Count the number of blocks you need to move."
    )


def title_level5():
    return "Good work! You are ready for something harder"


def description_level5():
    message = (
        f"You already know how to make the van turn left or right. This time "
        f"the van has to make lots of turns to reach the house. <br> Drag and "
        f"attach the blocks to make your sequence."
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level5(), message)


def hint_level5():
    return (
        "There are more turns to make this time. Try building your solution up block "
        "by block. Which way do you need to turn first?"
    )


def title_level6():
    return "Well done! Let's use all three blocks"


def description_level6():
    message = (
        f"This time the van has to <b>Move forwards</b>, <b>Turn left</b> and "
        f"<b>Turn right</b>. <br><br> Drag and attach the blocks like before. "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level6(), message)


def hint_level6():
    return (
        "You’ve done really well to get this far! Now you need to travel further but "
        "include some turns. Check which direction you need to turn and count the "
        "number of blocks you need to travel."
    )


def title_level7():
    return "This road is more complicated"


def description_level7():
    message = (
        f"Practise your new skills on this road by helping the driver to arrive at "
        f"the house. <br> When you are happy with your sequence, press "
        f"{play_button_icon_url()}!"
    )
    return build_description(title_level7(), message)


def hint_level7():
    return (
        "This road is more complicated but you can do this! Start with just a few "
        "blocks and try that, then add more blocks and check it again."
    )


def title_level8():
    return "The warehouse is not always in the same place"


def description_level8():
    message = (
        f"This time the warehouse is somewhere else on the screen but you still need "
        f"to use the <b>Move forwards</b> block. <br> Can you use the <b>Move "
        f"forwards</b> block correctly even when it looks like the van goes in a "
        f"different direction? "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level8(), message)


def hint_level8():
    return (
        "The warehouse is in a different place now but don’t let that confuse you! "
        "Which way do you need to go first? Imagine you are driving the van."
    )


def title_level9():
    return "Can you go from right to left?"


def description_level9():
    message = (
        f"Practise your new skills on this road by helping the driver to arrive "
        f"at the house. "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level9(), message)


def hint_level9():
    return "Try counting the blocks before the turn. Which way do you need to go?"


def title_level10():
    return "Well done! How about another go?"


def description_level10():
    message = (
        f"You've done really well so far. Try to get the van to the house. "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level10(), message)


def hint_level10():
    return (
        "You need to make a turn as soon as you leave the warehouse. Which way do you "
        "need to go? If you get stuck, don’t forget to count the blocks and check "
        "which way you need to turn each time."
    )


def title_level11():
    return "Snail maze!"


def description_level11():
    message = (
        f"Uh oh, a tricky snail maze! Can you take the van through it? "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level11(), message)


def hint_level11():
    return (
        "The warehouse is in a different place again so check which way you need to "
        "go. If you get stuck, remember that you can just add a few blocks and run "
        "the program and then add a few more and try again."
    )


def title_level12():
    return "This road is more complicated"


def description_level12():
    message = (
        f"Good work, by now you are able to solve quite complicated levels. Prove "
        f"your skills! "
        f"<br> When you are happy with your sequence, press {play_button_icon_url()}!"
    )
    return build_description(title_level12(), message)


def hint_level12():
    return (
        "You have learned a lot in these levels. Here’s a route to really test your "
        "skills. Try counting the number of straight sections and then add the "
        "curves in slowly. You can run the program before it is complete and then "
        "add to it. That can be easier than adding lots of blocks at once. Good luck!"
    )


def title_level13():
    return "Multiple routes"


def description_level13():
    message = (
        f"Often there is more than one way to get to the house. The route that needs "
        f"the fewest directions is usually best. <br> Help the van find the "
        f"shortest route to the house. <br> You can press the {play_button_icon_url()} "
        f"button to start the van."
    )
    return build_description(title_level13(), message)


def hint_level13():
    return (
        "There are a few different ways of getting to the house in these levels. Can "
        "you find the shortest route? Try counting the blocks if you’re not sure. "
        "That’s the way to get the best score on these levels. "
    )


def title_level14():
    return "Can you spot the shortest route?"


def description_level14():
    message = (
        "So many options to choose from! <br> Do you know which is the shortest "
        "route to get the van to house?"
    )
    return build_description(title_level14(), message)


def hint_level14():
    return (
        "This one is a bit trickier. There are lots of different ways you could go but "
        "there is no point wasting fuel! If you take one of the longer routes, you "
        "won’t get such a good algorithm score."
    )


def title_level15():
    return "What if there is more than one delivery?"


def description_level15():
    message = (
        "Our vans often need to go to more than one house. To make the van deliver "
        "to a house use the <b>Deliver</b> block. <br> Make sure your sequence "
        "gets the van to travel the shortest route!"
    )
    return build_description(title_level15(), message)


def hint_level15():
    return (
        "On this level, there are two houses to deliver to. Which one are you going to "
        "go to first? Make sure you add a <b>Deliver</b> block for each house, you "
        "don’t want to forget anyone’s shopping!"
    )


def title_level16():
    return "This time there are even more houses"


def description_level16():
    message = (
        "Well done! You have done really well to get so far - let's take it to the "
        "next level and add another house. <br> Can you work out the shortest, "
        "most efficient route to each house?"
    )
    return build_description(title_level16(), message)


def hint_level16():
    return (
        f"Now there is another house to deliver to! Make sure you take the shortest "
        f"route and add a <b>Deliver</b> block for each house. You might find it "
        f"easier to add a small amount of code at a time and test it. You can even "
        f"use the <b>Step</b> button {step_button_icon_url()} to try each block in "
        f"your program."
    )


def title_level17():
    return "House overload!"


def description_level17():
    message = (
        "Well done, you're getting a hang of it! Can you do the same for even more "
        "houses?<br> Don't forget to use the <b>Deliver</b> block at each house."
    )
    return build_description(title_level17(), message)


def hint_level17():
    return (
        "You have four houses to deliver to now. Have you noticed that the red box "
        "turns green when you have delivered the shopping? Your programs are "
        "starting to get quite long now. Add a few blocks and then test your code. "
        "It is easier to spot errors that way. Good luck!"
    )


def title_level18():
    return "This one is quite a tangle"


def description_level18():
    message = (
        "Practise your new skills on this road by getting the van to <b>Deliver</b> "
        "to each of the houses."
    )
    return build_description(title_level18(), message)


def hint_level18():
    return (
        "You have reached the last route in this section, and it is quite complicated! "
        "Check which direction you need to turn and build up your code slowly. Maybe "
        "try to get to one house at a time and then add more code for the next one. "
        "Don’t miss a house off!"
    )


def title_level19():
    return "Repeating yourself is boring"


def description_level19():
    message = video_link(
        "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2FPucDWuRfzuTxeLI6IHRx%2FMahana%20explains%20repeat%20functions.mp4?alt=media&token=361c8495-dc7d-4e18-9a7f-4c07c3fd303d",
        0,
    )
    message += (
        "<div class='popup_message'>"
        "Attach a block inside the <b>Repeat</b> block to make the van repeat "
        "that instruction. <br> This means you can use one block instead of lots "
        "of blocks to do the same thing over and over again. <br> How many times "
        "do you want the instruction repeated? Type the number into the "
        "<b>Repeat</b> block. <br> The repeated sets of blocks make a 'loop'.  "
        "<br><br> When you are ready, press <b>Play</b>!"
        "</div>"
    )
    return build_description(
        title_level19(), f"<div class='main_popup_container'>{message}</div>"
    )


def hint_level19():
    return (
        "You have seen this route before! This time you are going to use a "
        "<b>Repeat</b> block so that you don’t need to have several "
        "<b>Move forwards</b> blocks. How many do you need?"
    )


def title_level20():
    return "Use the <b>repeat</b> block to make your sequence shorter and simpler"


def description_level20():
    message = (
        "You drove the van down this road on Level 5. This time, use the "
        "<b>Repeat</b> block to get the van to the house. <br> This will make "
        "your sequence shorter and simpler than last time."
    )
    return build_description(title_level20(), message)


def hint_level20():
    return (
        "This is another route you have seen before. Instead of having lots of left "
        "and right blocks, can you find a pattern and put them inside a "
        "<b>Repeat</b> block? How many times do you need to repeat them?"
    )


def title_level21():
    return "Four leaf clover"


def description_level21():
    message = (
        "This path looks a bit like a four leaf clover. Can you take the driver "
        "through it?"
    )
    return build_description(title_level21(), message)


def hint_level21():
    return (
        "Here is a challenge for you! Can you find a pattern to put in the "
        "<b>Repeat</b> block? If you’re not sure, try doing your program without the "
        "repeat and then looking for the pattern. You could use a piece of paper to "
        "write the route down if that helps."
    )


def title_level22():
    return "Now things are getting quite long and complicated"


def description_level22():
    message = (
        "An algorithm (a set of instructions in a particular order) to get the van "
        "to the house might not be very simple, but it can be made shorter by "
        "using the <b>Repeat</b> blocks. <br> Are you up for this challenge?"
    )
    return build_description(title_level22(), message)


def hint_level22():
    return (
        "Instead of having lots of<b>Move forwards</b> blocks, try putting them in "
        "<b>Repeat</b> blocks when you can. This is quite a complicated route so try "
        "building up your solution slowly. If you get in a muddle, try starting "
        "again and just doing a bit of the route at a time."
    )


def title_level23():
    return "Sssssssssnake!"


def description_level23():
    message = (
        "This road seems to be winding just like a snake! Can you find a nice and "
        "simple route to get the van to the house?"
    )
    return build_description(title_level23(), message)


def hint_level23():
    return (
        "Don’t rush into this one. Try counting the straights and using a"
        "<b>Repeat</b> block for those. Then make the turn and do the same. Run the "
        "code each time."
    )


def title_level24():
    return "The road is very long and very bendy"


def description_level24():
    message = "Wow! Look at that! It won't get more complicated than this, we promise."
    return build_description(title_level24(), message)


def hint_level24():
    return (
        "This is as complicated as they get so don’t worry! Try writing down the turns "
        "to get you up to the straight bit. Can you see a pattern?"
    )


def title_level25():
    return "Waterfall level"


def description_level25():
    message = "Since you did so well with the repeat loops, have a go at this level."
    return build_description(title_level25(), message)


def hint_level25():
    return (
        "The solution to this route is quite short but you will need to find the "
        "pattern! Try solving it without loops or writing down the steps on paper. "
        "Then look for a pattern to repeat. You can do this!"
    )


def title_level26():
    return "Winter wonderland!"


def description_level26():
    message = (
        "Notice the snow! You can create new levels with different 'themes' of "
        "backgrounds and decorations in the Level Editor. But first, try getting "
        "the van to the house!"
    )
    return build_description(title_level26(), message)


def hint_level26():
    return (
        "This route is much simpler, don’t let the snow distract you! How many "
        "straights are there before the turn? How many straights after the turn?"
    )


def title_level27():
    return "Farmyard"


def description_level27():
    message = (
        "What a muddy road! Can you help Dee find her way from the barn to the "
        "house?"
    )
    return build_description(title_level27(), message)


def hint_level27():
    return (
        "Here is another type of route. This time you have a muddy road and some "
        "farmland. The pattern is not that easy to find straightaway. Try writing "
        "out the instructions without the <b>Repeat</b> block and then try to find "
        "the best pattern you can."
    )


def title_level28():
    return "The big city"


def description_level28():
    message = (
        "Can you get the van from the warehouse to the house? Don't stop at any "
        "shops on the way!"
    )
    return build_description(title_level28(), message)


def hint_level28():
    return (
        "This time you’re in a town and you need to deliver to the blue house at the "
        "end of the route. Don’t get distracted along the way. To get the best "
        "route, you need to put a <b>Repeat</b> block inside another <b>Repeat</b> "
        "block. These levels are not so simple so write down the route and then look "
        "for patterns."
    )


def title_level29():
    return "No need for numbers"


def description_level29():
    message = video_link(
        "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2FmUm2VB4N62Opk2CezOFR%2FAna%20discusses%20repeat%20until%20and%20repeat%20while%20functions.mp4?alt=media&token=1add73b1-9e21-4cdb-876d-31495012bb50",
        0,
    )
    message += (
        "<div class='popup_message'>"
        "Drag a block inside a <b>Repeat until</b> block to make the van repeat an "
        "instruction. <br> Attach a 'condition' so the van knows when to stop "
        "repeating the instruction. <br> Here, you want the van to repeat your "
        "instruction until it is at the destination. <br> Doing this means "
        "you don't have to work out how many times the van should repeat your "
        "instruction."
        "</div>"
    )
    return build_description(
        title_level29(), f"<div class='main_popup_container'>{message}</div>"
    )


def hint_level29():
    return (
        "You’ve seen this route before! This time you are not counting repetitions, "
        "your loop is going to repeat the <b>Move forwards</b> block until you reach "
        "your destination."
    )


def title_level30():
    return "Can you do that again?"


def description_level30():
    message = (
        "Well done, you did it! Now have a go at using the <b>Repeat until</b> block "
        "on a road with lots of turns."
    )
    return build_description(title_level30(), message)


def hint_level30():
    return (
        "This is another route you have seen before. Last time you counted how many "
        "times your instructions were repeated. This time, your program is going to "
        "repeat your commands until you reach the destination. What do you need to "
        "repeat?"
    )


def title_level31():
    return "Practice makes perfect"


def description_level31():
    message = "Have another go to make sure you have got the hang of it."
    return build_description(title_level31(), message)


def hint_level31():
    return (
        "If you look at this route, do you notice that the shape of the road repeats? "
        "Can you put the instructions in a loop?"
    )


def title_level32():
    return "Uh oh, it's <b>until</b> fever!"


def description_level32():
    message = "Good job! Can you help the driver reach the destination again?"
    return build_description(title_level32(), message)


def hint_level32():
    return (
        "What about this road, can you see a repeating pattern? Maybe write down the "
        "instructions without a loop to solve this route and then look for the "
        "pattern."
    )


def title_level33():
    return "Now it's time to try the <b>if</b> block"


def description_level33():
    message = video_link(
        "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2F8A63G0OQlNdxMpvLuK9j%2FChris%20and%20Matt%20introduce%20if%20statements.mp4?alt=media&token=6fc94e71-a8b1-43a4-aadd-63fcf3b5788c",
        0,
    )
    message += (
        "<div class='popup_message'>"
        "Another way of telling the van what to do is to use the <b>If</b> block. "
        "For example, <b>If</b> the <b>road exists forwards do</b> <b>Move "
        "forwards</b>. <br> This is called an 'if statement'. <br> Try "
        "using the <b>If</b> block and the <b>Repeat</b> block together. <br> "
        "The <b>Repeat</b> block will stretch if you attach the <b>If</b> block "
        "inside it."
        "</div>"
    )
    return build_description(
        title_level33(), f"<div class='main_popup_container'>{message}</div>"
    )


def hint_level33():
    return (
        "You could solve this with the same code you used on level 29 but the "
        "instructions for this level introduced the <b>If</b> block. To get full "
        "marks on this level, you will need to use an <b>If</b> block."
    )


def title_level34():
    return "Multiple <b>if</b>s"


def description_level34():
    message = (
        "It can be handy to use <b>If</b> to give your van choices, so you don't "
        "have to give the van new instructions at every step. <br> For "
        "example: Tell the van <b>If</b> the <b>road exists forwards do Move "
        "forwards,</b> but <b>If</b> the <b>road exists left do Turn left</b>. "
        "<br> The van will choose correctly from the <b>Move forwards</b> and "
        "<b>Turn left</b> instructions depending on the road. <br> Use an 'if "
        "statement' in a 'loop' to drive the van down this bendy road."
    )
    return build_description(title_level34(), message)


def hint_level34():
    return (
        "This route looks complicated, but you can solve it without counting blocks. "
        "You are going to use a <b>Repeat until</b> block again and <b>If</b> blocks "
        "to help the driver check the road ahead so they can decide which way to go. "
        "What are the possible directions on this route?"
    )


def title_level35():
    return "Let's put it all together!"


def description_level35():
    message = (
        "You have discovered the magic of 'if statements'. Can you make a program "
        "that uses <b>Move forwards</b>, <b>Turn left</b> and <b>Turn right</b> "
        "to get the van to the house."
    )
    return build_description(title_level35(), message)


def hint_level35():
    return (
        "For this route you need to go straight, turn left and turn right so you will "
        "need to make your <b>if</b> statement more complex. To make your code as "
        "fast as possible, think about which you need to do most. It is less "
        "efficient to ask if you need to turn left first if most of the time you "
        "want to go straight, for example."
    )


def title_level36():
    return "What else? <b>If-else</b>, that's what!"


def description_level36():
    message = video_link(
        "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2FsxMatN6zCvgFag8YDvK4%2FHelen%20explains%20if_else%20statements.mp4?alt=media&token=1051ab04-b02d-4b75-8278-2b63216b2985",
        0,
    )
    message += (
        f"<div class='popup_message'>"
        f"You can change the <b>if</b> block to make more choices. Click on the"
        f" {if_else_icon_url()} to add <b>else if</b>."
        f"<br>"
        f"This will tell the van what to do if the first <b>if</b> direction"
        f" can't be done."
        f"<br>"
        f"You can also add an <b>else</b> block to tell the van what to do if"
        f" none of the conditions match."
        f"<br>"
        f"{if_else_example_url()}"
        f"<br>"
        f"This is a general algorithm, it can be used for lots of different routes!"
        f"</div>"
    )
    return build_description(
        title_level36(), f"<div class='main_popup_container'>{message}</div>"
    )


def hint_level36():
    return (
        "This route is quite different from the last one but is the solution very "
        "similar?"
    )


def title_level37():
    return "A bit longer"


def description_level37():
    message = (
        "Let's see if we can go further - this road is longer. Notice that the "
        "length of the road does not change the length of your program!"
    )
    return build_description(title_level37(), message)


def hint_level37():
    return (
        "This route is longer and a different shape again but does your last solution "
        "help? Are you noticing a pattern here?"
    )


def title_level38():
    return "Where did the cows come from?"


def description_level38():
    message = (
        "Well done! You've got so far."
        "<br>"
        "Can you apply the knowledge you gained going through this part of the "
        "game to this level? This time there are some hidden cows that you "
        "need to get out of the road! Can you work out what to do?"
        "<br><br>"
        "Hint: Cows don't like noise"
    )
    return build_description(title_level38(), message)


def hint_level38():
    return (
        "This is a really long route. With a counted loop, your program would "
        "be quite long but is this program going to be any longer than your "
        "solution to the last level?"
        "<br><br>"
        "Hint: Cows don't like noise"
    )


def title_level39():
    return "Dead ends!"


def description_level39():
    message = (
        "It looks like the cows have escaped when you get to the side roads, "
        "so be careful not to hit them!"
        "<br><br>"
        "Hint: Cows don't like noise"
    )
    return build_description(title_level39(), message)


def hint_level39():
    return (
        "You'll need to modify your general algorithm here so you can get back "
        "on track if you hit a dead end."
        "<br><br>"
        "Hint: Cows don't like noise"
    )


def title_level40():
    return "Adjust your previous solution"


def description_level40():
    message = (
        "Can you think of a way you could change the 'general algorithm' you have "
        "implemented earlier to make sure the van driver reaches the house having "
        "travelled the shortest route?"
    )
    return build_description(title_level40(), message)


def hint_level40():
    return (
        "With this route, only ask questions about the directions you actually need to "
        "go."
    )


def title_level41():
    return "Decision time"


def description_level41():
    message = (
        "Do you think changes to the 'general algorithm' will help the van find the "
        "shortest route? <br> Or do you have to come up with a different "
        "solution? <br> Time to make a decision..."
    )
    return build_description(title_level41(), message)


def hint_level41():
    return (
        "This is a short route and you can choose either route. Can you use an "
        "algorithm you have used before?"
    )


def title_level42():
    return "What do you think this time?"


def description_level42():
    message = (
        "Can you use the 'general algorithm' here? <br> Can it be changed so that "
        "it finds a shorter route, or will you need a new solution?"
    )
    return build_description(title_level42(), message)


def hint_level42():
    return (
        "You have been using a similar solution to lots of levels in this section, but "
        "does that help you now? Can you use a general set of instructions or do you "
        "need to write a specific solution for this one?"
    )


def title_level43():
    return "Good work! What else can you do?"


def description_level43():
    message = (
        "You should be really good at this by now. Can you manage this complicated "
        "road?"
    )
    return build_description(title_level43(), message)


def hint_level43():
    return (
        "Your general solution might not help you here. See if you need to use some "
        "counted loops for this one."
    )


def title_level44():
    return "Oh no! Traffic lights!"


def description_level44():
    message = video_link(
        "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2FVDmgFe1LBpTpWI2b9EVN%2FWill%20discusses%20variables.mp4?alt=media&token=3fb3c5ca-f0d7-4f98-9274-5c4db8f64eac",
        0,
    )
    message += (
        "<div class='popup_message'>"
        "The light varies from red to green. <br>"
        "The van must check which colour the traffic light is when it reaches them "
        "- if it goes past a red light it will break the Highway Code."
        "<br> Here, you want the van to repeat the wait instruction while the traffic light is red. "
        "Drag a block inside a <b>Repeat while</b> block to make the van repeat an instruction. "
        "<br> Attach a 'condition' so the van knows when to repeat the instruction."
        "</div>"
    )
    return build_description(
        title_level44(), f"<div class='main_popup_container'>{message}</div>"
    )


def hint_level44():
    return (
        "This route is very similar to one you’ve seen before but do you notice the "
        "traffic light? If the traffic light is red, you will need to wait."
    )


def title_level45():
    return "Green for go, red for wait"


def description_level45():
    message = (
        "Can you write a program so the van moves forwards on a green light but "
        "waits at a red light?"
    )
    return build_description(title_level45(), message)


def hint_level45():
    return (
        "This route is longer and there are two sets of traffic lights. Does it make "
        "any difference to your solution?"
    )


def title_level46():
    return "Well done - you've made it really far!"


def description_level46():
    message = (
        "Let's practise what you've learnt so far. <br> Don't forget to add a "
        "turn and to make the van wait at a traffic light."
    )
    return build_description(title_level46(), message)


def hint_level46():
    return (
        "In this level there is a left turn as well. Can you extend your solution to "
        "the last level to allow for that?"
    )


def title_level47():
    return "What a mess! But can you spot a route?"


def description_level47():
    message = (
        "Put your knowledge to test. Create an algorithm to lead the van to the "
        "house. <br> Don't forget to add a turn block and this time, you "
        "need to avoid cows instead of waiting at traffic lights."
    )
    return build_description(title_level47(), message)


def hint_level47():
    return (
        "This route is similar to the last one but the turn is in a different "
        "direction, and there are now cows instead of traffic lights!!"
        "<br><br>"
        "Do you remember what to do?"
    )


def title_level48():
    return "Put all that hard work to the test"


def description_level48():
    message = (
        "Congratulations - you've made it really far! <br> Can you create a solution that will deliver to all of the "
        "houses in the most efficient way?"
    )
    return build_description(title_level48(), message)


def hint_level48():
    return (
        "You need to check: "
        "<ul><li> if the lights are red </li>"
        "<li> if the road exists left </li>"
        "<li> if the road exists forward </li>"
        "<li> if the road exists right </li>"
        "<li> if it is a dead end </li></ul>"
        "Make sure you put the checks in the right order. You will need to repeat this for every house and deliver."
    )


def title_level49():
    return "Amazing! Have another go!"


def description_level49():
    message = (
        "Can you change the 'general algorithm' you created before to make the van "
        "take the shortest route to the destination?"
    )
    return build_description(title_level49(), message)


def hint_level49():
    return (
        "Can you use your general algorithm to get to the house? What if you think "
        "about the order of the instructions? Of course you must obey the traffic "
        "lights but if you come to a junction, do you want to prioritise turning "
        "left, right or going straight?"
    )


def title_level50():
    return "Light maze"


def description_level50():
    message = (
        "Well this is tricky. Look at all those lights! <br> Can you find the "
        "shortest route to the destination? It would be good if the van doesn't "
        "have to wait at too many lights."
    )
    return build_description(title_level50(), message)


# TODO: Update when we update the solution and new text is provided
def hint_level50():
    return (
        "Don't worry about the algorithm you've already come up with. Take the "
        "first turn left which has fewer traffic lights. <br><br> Once your van "
        "is right under the traffic lights, make sure it waits for a green "
        "light."
    )


def title_level51():
    return "Back to basics with a twist"


def description_level51():
    message = (
        "Can you come up with a solution to this level using the limited number of blocks "
        "we provide at the start?"
    )
    return build_description(title_level51(), message)


def hint_level51():
    return (
        "In these levels, the blocks you can use are limited. Can you use the provided "
        "blocks to get to the house? If you run out blocks, check that you are "
        "taking the shortest route."
    )


def title_level52():
    return "A bit more tricky"


def description_level52():
    message = (
        "Well done so far! Can you find a solution to this road? You have to move forward, "
        "but you have no forward block to use. Do you know how to help the van get to "
        "the destination?"
    )
    return build_description(title_level52(), message)


def hint_level52():
    return (
        "You can’t use the shortest route here because you don’t have a "
        "<b>Move forwards</b> block. What can you do instead?"
    )


def title_level53():
    return "Choose your blocks wisely"


def description_level53():
    message = (
        "Can you find the shortest route? Use your blocks carefully and don't forget "
        "the <b>repeat</b> loop."
    )
    return build_description(title_level53(), message)


def hint_level53():
    return (
        "You must take the shortest route here otherwise you will run out of blocks. "
        "You must also use the loops to help you."
    )


def title_level54():
    return "Round and round"


def description_level54():
    message = (
        "Can you find the shortest route? Use your blocks carefully and don't forget "
        "the <b>repeat</b> loop."
    )
    return build_description(title_level54(), message)


def hint_level54():
    return (
        "You don’t have a <b>Move forwards</b> block. Can you use the loops to get to "
        "the house? You might need to put one loop inside another loop..."
    )


def title_level55():
    return "Wonky fish!"


def description_level55():
    message = "Use <b>repeat until</b> and the <b>if</b> statement to find your way around the Wonky Fish."
    return build_description(title_level55(), message)


def hint_level55():
    return (
        "In this level, you need to combine a <b>Repeat</b> block with an <b>If</b> "
        "block. Can you find the pattern that will get you to the house?"
    )


def title_level56():
    return "Concrete wasteland"


def description_level56():
    message = (
        "Use <b>repeat until</b> and the <b>if</b> statement to find your way around "
        "the Concrete Wasteland"
    )
    return build_description(title_level56(), message)


def hint_level56():
    return (
        "Think about which turns you need to make to get to the destination. Which way "
        "do you go most often?"
    )


def title_level57():
    return "This is <b>not</b>... the same"


def description_level57():
    message = (
        "Like <b>repeat until</b>, <b>repeat while</b> is the opposite. Here, you want "
        "the van to repeat your instructions while it is not at the destination.<br>"
        "Doing this means you don't have to work out how many times the van should "
        "repeat your instructions."
    )
    return build_description(title_level57(), message)


def hint_level57():
    return (
        "This time you have a <b>Repeat while</b> block. This is different from the "
        "<b>Repeat until</b> you have used before. What needs to change in your code?"
    )


def title_level58():
    return "Snow snake"


def description_level58():
    message = (
        "Combining what you have just learnt using <b>repeat while</b> with the repeat "
        "loop, can you find your way around the snow snake?"
    )
    return build_description(title_level58(), message)


def hint_level58():
    return (
        "In this example, you only have four counted loop blocks. How can you use them "
        "to get to the destination?"
    )


def title_level59():
    return "Tricky turnaround"


def description_level59():
    message = "Use your blocks carefully not forgetting the <b>turnaround</b>."
    return build_description(title_level59(), message)


def hint_level59():
    return (
        "In this level, there is no <b>Move forwards</b> block. How can you use the "
        "loop, <b>Turn left</b> and <b>Turn around</b> blocks to get to the house? "
        "Try using the blocks without the loop and see where that takes you. Would "
        "repeating that help?"
    )


def title_level60():
    return "Right around the block"


def description_level60():
    message = "Can you find your way around this puzzle?"
    return build_description(title_level60(), message)


def hint_level60():
    return (
        "Can you see a pattern in this route? Use that to create a loop. When you have "
        "done that, what is left to do?"
    )


def title_level61():
    return "Can you create the 'Wiggle' procedure?"


def description_level61():
    message = (
        "Procedures are groups of instructions that can be executed multiple times "
        "without being rewritten. For example, if you want to instruct the van to "
        "follow a repeated pattern in the road, you can create a specific procedure. "
        "To create a procedure, simply choose the correct blocks and put them in the "
        "right order inside the <b>Define do</b> block. Once you have done that, give "
        "it a name eg wiggle.<br>Now you're ready! Attach the <b>Call</b> block where "
        "you want your 'wiggle' procedure to be executed. Don't forget to put the name in it!"
    )
    return build_description(title_level61(), message)


def hint_level61():
    return (
        "The instructions asked you to create a procedure called ‘wiggle’. This "
        "procedure should make the moves to manage the bends in the road. You will "
        "need to call this procedure from the main program."
    )


def title_level62():
    return "Lots of traffic lights!"


def description_level62():
    message = "Create a procedure which tells the van to wait until the traffic lights are green."
    return build_description(title_level62(), message)


def hint_level62():
    return (
        "Can you create a procedure that just deals with traffic lights? Call it "
        "‘lights’ and call it from the main program whenever you need it. Don’t "
        "worry if you don’t use the <b>Repeat block</b> in the program."
    )


def title_level63():
    return "Wiggle wiggle"


def description_level63():
    message = (
        "Can you find the repeating pattern here and create a new 'wiggle' procedure? "
        "And do the Wiggle Wiggle!"
    )
    return build_description(title_level63(), message)


def hint_level63():
    return (
        "In this level, you should notice a repeated turn in the road. Can you create "
        "a ‘wiggle’ procedure and call it whenever you need it from the main "
        "program? If you can’t find the repeated pattern, try writing the route out "
        "in full and looking at your instructions."
    )


def title_level64():
    return "Muddy patterns with Phil"


def description_level64():
    message = (
        "Can you spot a pattern here? Create several procedures, it can save time when "
        "writing a program. Don't forget to clearly name your procedures and then call them."
    )
    return build_description(title_level64(), message)


def hint_level64():
    return (
        "Try to create two procedures to help you here. Then call them as you need "
        "them from the main procedure. You could use one procedure to deal with each "
        "of the turn patterns in the route."
    )


def title_level65():
    return "Complicated roads"


def description_level65():
    message = (
        "This road might be a bit more complicated, but the procedures you could come up "
        "with are quite simple. Have a go and find out yourself!"
    )
    return build_description(title_level65(), message)


def hint_level65():
    return (
        "This route involves using the main program to deal with the main route and "
        "using procedures to deal with the turns in the road. You could try creating "
        "the route without procedures and then looking for a pattern to move into a "
        "procedure."
    )


def title_level66():
    return "Dee's snowy walk"


def description_level66():
    message = "Did you know procedures can call other procedures?"
    return build_description(title_level66(), message)


def hint_level66():
    return (
        "In this example, you can write a procedure that calls another procedure. Look "
        "for certain actions that are repeated and try to put them in procedures."
    )


def title_level67():
    return "Crazy farm"


def description_level67():
    message = "This one will really test what you have learnt."
    return build_description(title_level67(), message)


def hint_level67():
    return (
        "In this level, try to find several patterns and put them in procedures. How "
        "about starting with a wiggle?"
    )


def title_level68():
    return "T - time"


def description_level68():
    message = "Can you find the shortest route?"
    return build_description(title_level68(), message)


def hint_level68():
    return (
        "You have limited blocks again here. How can you get to the house without a "
        "counted loop?"
    )


def title_level69():
    return "Duck pond dodge"


def description_level69():
    message = "Can you find the shortest route?"
    return build_description(title_level69(), message)


def hint_level69():
    return (
        "In this level, you need a loop inside another loop. When you are able to go "
        "forwards, you should keep going. When you can no longer go forwards, you "
        "need to turn and then try to go forwards again.<br><br>Hint: The traffic "
        "lights are a bit of a distraction and you don’t need to worry about them!"
    )


def title_level70():
    return "Winter wonderland"


def description_level70():
    message = "Can you find the shortest route?"
    return build_description(title_level70(), message)


def hint_level70():
    return (
        "You don’t have any <b>Move forwards</b> blocks here. How can you use a loop "
        "and the turn blocks to get to the house?"
    )


def title_level71():
    return "Frozen challenge"


def description_level71():
    message = "Can you find the shortest route?"
    return build_description(title_level71(), message)


def hint_level71():
    return (
        "In this level, most of the time you want to <b>Move forwards</b> and then "
        "<b>turn right</b>. However, there is an occasion when you don’t want to do "
        "that."
    )


def title_level72():
    return "Can Wes find his lunch?"


def description_level72():
    message = "Can you find the shortest route?"
    return build_description(title_level72(), message)


def hint_level72():
    return (
        "In this level, you want to <b>Move forwards</b> most of the time. When do you "
        "need to turn?"
    )


def title_level73():
    return "Traffic light freeze up!"


def description_level73():
    message = "Can you find the shortest algorithm?"
    return build_description(title_level73(), message)


def hint_level73():
    return (
        "You don’t have the blocks to check if you are at the destination. What can "
        "you use instead?  Don’t forget to deal with the traffic lights!"
    )


def title_level74():
    return "Pandemonium"


def description_level74():
    message = "Can you find the shortest route?"
    return build_description(title_level74(), message)


def hint_level74():
    return (
        "You only have one <b>Repeat</b> block here so make the most of it! You can "
        "use procedures to repeat code by just calling the procedure again."
    )


def title_level75():
    return "Kirsty's maze time"


def description_level75():
    message = "Can you find the shortest route?"
    return build_description(title_level75(), message)


def hint_level75():
    return (
        "You need to look for the shortest route here and then use loops inside loops "
        "to get you there. Good luck!"
    )


def title_level76():
    return "Cannot turn left!"


def description_level76():
    message = "Can you find the shortest route?"
    return build_description(title_level76(), message)


def hint_level76():
    return (
        "This van driver is going to have to take quite a circuitous route to make "
        "their delivery. You don’t have any left turns!"
    )


def title_level77():
    return "G force"


def description_level77():
    message = "Can you get the van to the house?"
    return build_description(title_level77(), message)


def hint_level77():
    return (
        "You don’t have any loops here but you can make a subroutine. You know that a "
        "subroutine can call another subroutine but did you know that a subroutine "
        "can call itself?"
    )


def title_level78():
    return "Wandering Phil"


def description_level78():
    message = "Can you get Phil to the house?"
    return build_description(title_level78(), message)


def hint_level78():
    return (
        "You really need to put together everything you have learned for this tricky "
        "level. You need to combine checking for being at the destination with "
        "checking for a dead end and which roads are available. Good luck!"
    )


def title_level79():
    return "Muddy mayhem"


def description_level79():
    message = "Can you find the shortest route?"
    return build_description(title_level79(), message)


def hint_level79():
    return (
        "This is the last of the levels in this section and you will have to put "
        "together everything you have learned! You don’t have any <b>Repeat</b> "
        "blocks so you need to use a procedure that calls itself and also checks "
        "which roads are available."
    )


# Legacy RR levels, still referenced in some Python Den levels
# --- Introduction to Python levels ---

INTRO_HINT = (
    "If you're stuck, you can learn more about the use of Blockly and Python on "
    "<a href='https://docs.codeforlife.education/rapid-router' target='_blank'>our documentation site</a>."
    "<br /><br />To learn more about Python in general, check this "
    "<a href='https://wiki.python.org/moin/BeginnersGuide' target='_blank'>Beginner's Guide to Python</a>."
)


def title_level80():
    return "Here's Python!"


def description_level80():
    message = video_link(
        "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2FhwOkHWSHqONf5lm7vbc4%2FCode%20for%20Life_%20Python.mp4?alt=media&token=8b47268c-91ea-4315-80e8-05c40d84372c",
        0,
    )
    message += (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Can you tell which Python statement matches which block?"
    )
    return build_description(
        title_level80(), f"<div class='main_popup_container'>{message}</div>"
    )


def hint_level80():
    return (
        "This route is quite simple and you have seen it before. Just drag the blocks "
        "as you normally would but notice what is happening in the Python code…"
    )


def title_level81():
    return "Matching Blockly"


def description_level81():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Can you tell which Python statement matches which block?"
    )
    return build_description(title_level81(), message)


# TODO: Update once we've renamed v to my_van
def hint_level81():
    return INTRO_HINT


def title_level82():
    return "Don't forget to find the shortest route"


def description_level82():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Can you tell which Python statement matches which block?"
    )
    return build_description(title_level82(), message)


def hint_level82():
    return (
        "You can’t edit the Python program yet but have a look at it as you add new "
        "blocks to your code. Notice that each command to the van ends with round "
        "brackets (). These are important, they tell Python that you are giving a "
        "command."
    )


def title_level83():
    return "Repeating yourself in Python looks different"


def description_level83():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Try adding a <b>repeat</b> block and watch what happens in Python."
    )
    return build_description(title_level83(), message)


# TODO: Update once we change the solution for this level
def hint_level83():
    return INTRO_HINT


def title_level84():
    return "<b>Repeat</b> and watch"


def description_level84():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Try adding a <b>repeat</b> block and watch what happens in Python."
    )
    return build_description(title_level84(), message)


# TODO: Update once we change the solution for this level
def hint_level84():
    return INTRO_HINT


def title_level85():
    return "Looks easy but use <b>repeat until</b> and see what happens?"


def description_level85():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Try adding a <b>repeat</b> until block and watch what "
        "happens in Python."
    )
    return build_description(title_level85(), message)


# TODO: For levels 85 - 109: the new hint text has not yet been provided.
def hint_level85():
    return INTRO_HINT


def title_level86():
    return "See what the <b>if</b> blocks looks like in Python"


def description_level86():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Try adding an <b>if</b> block and watch what happens in Python."
    )
    return build_description(title_level86(), message)


def hint_level86():
    return INTRO_HINT


def title_level87():
    return "Don't forget to use <b>else if</b>"


def description_level87():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Try adding an <b>if</b> block and watch what happens in "
        "Python particularly with <b>else if</b> and <b>else</b> statements."
    )
    return build_description(title_level87(), message)


def hint_level87():
    return INTRO_HINT


def title_level88():
    return "See what happens when you add traffic lights"


def description_level88():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Try adding an <b>if</b> block and watch what happens in "
        "Python particularly with <b>else if</b> and <b>else</b> statements."
    )
    return build_description(title_level88(), message)


def hint_level88():
    return INTRO_HINT


def title_level89():
    return "Watch carefully as you have another go"


def description_level89():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "programming language. Try adding an <b>if</b> block and watch what happens in "
        "Python particularly with <b>else if</b> and <b>else</b> statements."
    )
    return build_description(title_level89(), message)


def hint_level89():
    return INTRO_HINT


def title_level90():
    return "Have a go at procedures - what do they look like in Python?"


def description_level90():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "language. Try adding a procedure and watch what happens in Python."
    )
    return build_description(title_level90(), message)


def hint_level90():
    return (
        "Don't forget to name your procedure and see what happens in Python. "
        + INTRO_HINT
    )


def title_level91():
    return "Put it all together"


def description_level91():
    message = (
        "As you create your program using Blockly, see what it looks like in the Python "
        "language. Try adding a procedure and watch what happens in Python."
    )
    return build_description(title_level91(), message)


def hint_level91():
    return (
        "Don't forget to name your procedure and see what happens in Python. "
        + INTRO_HINT
    )


# --- Start of Python levels ---

PYTHON_HINT = (
    "<br /><br />Check our documentation site, to see "
    "<a href='https://code-for-life.gitbook.io/rapid-router/rapid-router-python-commands' target='_blank'>the full list of commands</a>."
    "<br /><br />To learn more about Python in general, check this "
    "<a href='https://wiki.python.org/moin/BeginnersGuide' target='_blank'>Beginner's Guide to Python</a>."
)


def title_level92():
    return "Start with the basics, <b>forward</b>, <b>left</b> and <b>right</b>"


def description_level92():
    message = (
        "Now you are coding in Python! This is what real developers do!! To start you off, "
        "the van object has been created for you already. Under this you need to add the "
        "correct Python statements to instruct the van to drive to the destination."
    )
    return build_description(title_level92(), message)


def commands_level92():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level92():
    return (
        "Try using the following commands:<br><pre>my_van.move_forwards()<br>my_van.turn_left()"
        "<br>my_van.turn_right()</pre>" + PYTHON_HINT
    )


def title_level93():
    return "Keep it simple"


def description_level93():
    message = (
        "Try this road. Under the van object you need to add the correct Python statements "
        "to instruct the van to drive to the destination."
    )
    return build_description(title_level93(), message)


def commands_level93():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level93():
    return (
        """Try using the following commands:
<pre>my_van.move_forwards()
my_van.turn_left()
my_van.turn_right()</pre>"""
        + PYTHON_HINT
    )


def title_level94():
    return "Take the shortest route"


def description_level94():
    message = (
        "You're getting good at this! Can you drive the van along this road using the "
        "correct Python statements."
    )
    return build_description(title_level94(), message)


def commands_level94():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level94():
    return (
        """Try using the following commands:
<pre>my_van.move_forwards()
my_van.turn_left()
my_van.turn_right()</pre>"""
        + PYTHON_HINT
    )


def title_level95():
    return "Count and repeat"


def description_level95():
    message = (
        "Now try to use a <b>repeat</b> loop to solve this level. Look back at level 83 "
        "to see what this could look like in Python."
    )
    return build_description(title_level95(), message)


def commands_level95():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level95():
    return (
        """To repeat some statements a set number of times you can use something like the following:
<pre>for count in range(3):
    my_van.turn left
    print count</pre>
The print statement will output the value of count to the console."""
        + PYTHON_HINT
    )


def title_level96():
    return "Count and repeat is easy"


def description_level96():
    message = (
        "Now try to use a <b>repeat loop</b> to solve this level. Look back at level 83 "
        "to see what this could look like in Python. This time you could use 2 loops, "
        "1 for each straight piece of road."
    )
    return build_description(title_level96(), message)


def commands_level96():
    return "<b>Movement</b>" + "<br>my_van.move_forwards()" + "<br>my_van.turn_left()"


def hint_level96():
    return (
        """To repeat some statements a set number of times you can use something like the following:
<pre>for count in range(3):
    my_van.turn left
    print count</pre>
The print statement will output the value of count to the console."""
        + PYTHON_HINT
    )


def title_level97():
    return "Loop the loop"


def description_level97():
    message = (
        "Now try to use a loop within a loop, known as a 'nested loop'. Look back at level "
        "84 to see what this could look like in Python."
    )
    return build_description(title_level97(), message)


def commands_level97():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level97():
    return (
        """To repeat within a repeats a set number of times you can use something like the following:
<pre>for i in range(3):
    for j in range(5):
        my_van.turn left
        print count</pre>
The print statement will output the value of count to the console."""
        + PYTHON_HINT
    )


def title_level98():
    return "Repeat and check"


def description_level98():
    message = (
        "Try to solve this level by repeatedly moving until the van is at the destination. "
        "Also, check whether the van can move forward or else must turn left. Now try and "
        "write the Python code. Look back at level 86 to give you an idea of what this "
        "could look like."
    )
    return build_description(title_level98(), message)


def commands_level98():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.at_destination()"
        + "<br>my_van.is_road_forward()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level98():
    return (
        """To repeat while a condition is met you can use something like the following:
<pre>while not my_van.at_destination():
    my_van.move_forwards()</pre>
To check whether a condition is met you can use something like the following:
<pre>if my_van.is_road_forward():
    my_van.move_forwards()</pre>
You may also need to use the <b>else</b> statement."""
        + PYTHON_HINT
    )


def title_level99():
    return "Find a general solution"


def description_level99():
    message = (
        "Now try using what you have just learnt to solve this level. You could also try "
        "using the <b>if</b>, <b>elif</b> and <b>else</b> statements. Look back at level "
        "86 to give you an idea of what this could look like."
    )
    return build_description(title_level99(), message)


def commands_level99():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.at_destination()"
        + "<br>my_van.is_road_right()"
        + "<br>my_van.is_road_left()"
        + "<br>my_van.is_road_forward()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level99():
    return (
        """To repeat while a condition is met you can use something like the following:
<pre>while not my_van.at_destination():
    my_van.move_forwards()</pre>
To check whether a condition is met you can use something like the following:
<pre>if my_van.is_road_forward():
    my_van.move_forwards()</pre>
You may also need to use the <b>elif</b> and <b>else</b> statements."""
        + PYTHON_HINT
    )


def title_level100():
    return "Watch out for the dead end!"


def description_level100():
    message = (
        "Practice your new Python skills on this road to get the van to the destination. "
        "Look back at level 88 for a dead end check."
    )
    return build_description(title_level100(), message)


def commands_level100():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.at_destination()"
        + "<br>my_van.is_road_forward()"
        + "<br>my_van.is_road_right()"
        + "<br>my_van.is_road_left()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level100():
    return (
        "Try using<br><pre>if my_van.at_dead_end():</pre><br>to check if the van is at a dead end."
        + PYTHON_HINT
    )


def title_level101():
    return "Function or junction?"


def description_level101():
    message = (
        "Try defining your own procedure to solve this level. In Python procedures are "
        "generally called functions. Look back at level 90 for an example of how to "
        "define a function in Python."
    )
    return build_description(title_level101(), message)


def commands_level101():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level101():
    return (
        """To define a function in Python you could do something like:
<pre>def my_function():
    print 'test'</pre>
To call a defined function you could do something like:
<pre>my_function()</pre>
Remember, you must define a function before you call it."""
        + PYTHON_HINT
    )


def title_level102():
    return "Watch for the patterns"


def description_level102():
    message = (
        "For this level try defining more than one function. Try to look for a repeating "
        "pattern to simplify your program."
    )
    return build_description(title_level102(), message)


def commands_level102():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level102():
    return (
        """To define a function in Python you could do something like:
<pre>def my_function():
    print 'test'</pre>
To call a defined function you could do something like:
<pre>my_function()</pre>"""
        + PYTHON_HINT
    )


def title_level103():
    return "Patterns within patterns"


def description_level103():
    message = (
        "For this level try to define 2 or more functions where inside one function you "
        "call another function."
    )
    return build_description(title_level103(), message)


def commands_level103():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level103():
    return (
        """To define a function that calls another function you could do something like:
<pre>def my_function():
    print 'test'

def my_other_function():
    for i in range(3):
        my_function()

my_other_function()</pre>"""
        + PYTHON_HINT
    )


def title_level104():
    return "Can you see the repeating pattern?"


def description_level104():
    message = (
        "For this level try to define 2 or more functions where inside one function you "
        "call another function."
    )
    return build_description(title_level104(), message)


def commands_level104():
    return (
        "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
    )


def hint_level104():
    return (
        """To define a function that calls another function you could do something like:
<pre>def my_function():
    print 'test'

def my_other_function():
    for i in range(3):
        my_function()

my_other_function()</pre>"""
        + PYTHON_HINT
    )


def title_level105():
    return "Find the shortest route"


def description_level105():
    message = (
        "For this level try to implement a general algorithm. Keep the van going until it "
        "arrives at the destination, checking for traffic lights and junctions."
    )
    return build_description(title_level105(), message)


def commands_level105():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
        + "<br>my_van.wait()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.is_road_forward()"
        + "<br>my_van.is_road_left()"
        + "<br>my_van.at_red_traffic_light()"
        + "<br>my_van.at_destination()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level105():
    return (
        "For this you will have to use a combination of the <b>while</b> and <b>if</b> statements."
        + PYTHON_HINT
    )


def title_level106():
    return "Spiral and add"


def description_level106():
    message = (
        "For this level the van needs to travel in a spiral. The number of grid squares the "
        "van has to move keeps increasing by 1 on each turn. To do this you can have a loop "
        "that makes use of a variable to track the length of the road you need to travel "
        "after each turn."
    )
    return build_description(title_level106(), message)


def commands_level106():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_right()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.at_destination()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level106():
    return (
        """To use a variable to store the number of grid squares the van has to move you can do something like the following:
<pre>count = 1
while not my_van.at_destination():
    # Do something
    print(count)
    count = count + 1</pre>
Variables can be used in place of fixed values when calling functions. For example to repeat something <strong>number</strong> times you can do something like the following:
<pre>for count in range(number):</pre>"""
        + PYTHON_HINT
    )


def title_level107():
    return "Spiral and double"


def description_level107():
    message = (
        "For this level try something similar to what you have just learnt. This time "
        "the straight sections of road are doubling in length after each turn."
    )
    return build_description(title_level107(), message)


def commands_level107():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.at_destination()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level107():
    return (
        "To double the value of a variable you can do something like the following:<br><pre>number *= 2</pre>"
        + PYTHON_HINT
    )


def title_level108():
    return "Think less"


def description_level108():
    message = "This time the straight sections of road decrease in length by 2 after each turn."
    return build_description(title_level108(), message)


def commands_level108():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_left()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.at_destination()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level108():
    return (
        "To decrease the value of a variable by an amount you can do something like the "
        "following:<br><pre>count = count - 5</pre>" + PYTHON_HINT
    )


def title_level109():
    return "Spiral challenge!"


def description_level109():
    message = (
        "For this challenge, the straight line sections of road start off increasing "
        "by 1 after each turn and then switch to dividing by 2 with a twist!"
    )
    return build_description(title_level109(), message)


def commands_level109():
    return (
        '<div class="row">'
        + '<div class="large-4 columns">'
        + "<b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_right()"
        + "<br>my_van.turn_left()</div>"
        + '<div class="large-4 columns">'
        + "<b>Position</b>"
        + "<br>my_van.at_destination()</div>"
        + '<div class="large-4 columns"></div></div>'
    )


def hint_level109():
    return (
        "To halve the value of a variable you can do something like the following:<br><pre>number /= 2</pre>"
        + PYTHON_HINT
    )


# PYTHON DEN

# Episode 12, Levels 110 - 122
(
    title_level1001,
    description_level1001,
    hint_level1001,
) = (
    lambda: "Here's Python",
    lambda: build_description(
        title_level1001(),
        "As you create your program using Blockly, see what it looks like in the Python programming language. Can you tell which Python statement matches which block?",
    ),
    lambda: "This is a deliberately simple level. What you need to focus on is the Python code that is being generated for the blocks you join.",
)

(
    title_level1002,
    description_level1002,
    hint_level1002,
) = (
    lambda: "Matching Blockly",
    lambda: build_description(
        title_level1002(),
        "As you create your program using Blockly, see what it looks like in the Python programming language. Can you tell which Python statement matches which block?",
    ),
    lambda: "This is a deliberately simple level. What you need to focus on is the Python code that is being generated for the blocks you join.",
)

(
    title_level1003,
    description_level1003,
    hint_level1003,
) = (
    lambda: "Don't forget to find the shortest route",
    lambda: build_description(
        title_level1003(),
        "As you create your program using Blockly, see what it looks like in the Python programming language. Can you tell which Python statement matches which block?"
        "<br><br>"
        "Don't forget to find the shortest route!",
    ),
    lambda: "Pay close attention to the spelling of the Python commands, the use of the dot and the round brackets.",
)

(
    title_level1004,
    description_level1004,
    hint_level1004,
    commands_level1004,
) = (
    lambda: "Where did the blocks go?",
    lambda: build_description(
        title_level1004(),
        "Can you remember how the Python was formed under the blocks in the previous levels? Take a look in the Py Commands for a quick reminder.",
    ),
    lambda: "Now it is your turn, you can click on the Py commands button for a reminder of the Python commands that you can use.",
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(
    title_level1005,
    description_level1005,
    hint_level1005,
    commands_level1005,
) = (
    lambda: "Tree snake",
    lambda: build_description(
        title_level1005(),
        "This route is just a bit longer. Make sure you type the Python code accurately!",
    ),
    lambda: "The most common errors here are missing the round brackets at the end of the commands or mistyping the commands, e.g. use my_van.move_fowards() and not my_van.move_foward()",
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(
    title_level1006,
    description_level1006,
    hint_level1006,
    commands_level1006,
) = (
    lambda: "Which way to turn? This way or that way?",
    lambda: build_description(
        title_level1006(),
        "Try to find the shortest route using Python code only. You are getting really good at this!",
    ),
    lambda: "If you are stuck on this one, check that you are using the Python commands accurately. Click the Py Commands button to help you.",
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(
    title_level1007,
    description_level1007,
    hint_level1007,
) = (
    lambda: "In a <b>while</b>, crocodile!",
    lambda: build_description(
        title_level1007(),
        "<div class='main_popup_container'>"
        "<div class='popup_message'>"
        "Try to build up the blocks using a while loop to solve this one. Make sure that you count carefully."
        "<br><br><br><br><br><br><br><br>Watch this video for more details: <br>"
        "</div>"
        f"{video_link("https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2F3ojsv3EPh8qREqYMJBqo%2FPython%20Den%20Variable%20blocks%20demo.mp4?alt=media&token=192e4448-f16b-497f-b0d3-18163fd7d1d7", 0)}"
        "</div>",
    ),
    lambda: "<div class='main_popup_container'>"
    "<div class='popup_message'>"
    "Make sure that you are using the right blocks here. You must use the pink block for variables and the dark blue number block for values."
    "<br><br><br><br><br><br><br><br>Watch the video here if you are unsure.<br>"
    "</div>"
    f"{video_link("https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdCZE3FuBgH5fHsGocKGv%2Fuploads%2F3ojsv3EPh8qREqYMJBqo%2FPython%20Den%20Variable%20blocks%20demo.mp4?alt=media&token=192e4448-f16b-497f-b0d3-18163fd7d1d7", 0)}"
    "</div>",
)

(
    title_level1008,
    description_level1008,
    hint_level1008,
) = (
    lambda: "Wiggle <b>while</b> you work",
    lambda: build_description(
        title_level1008(),
        "Now look at the Python code for that while loop you created. Can you match the blocks to the Python? What do you notice about the Python code?",
    ),
    lambda: "If you cannot solve this one, try creating a solution without a while loop and then looking for what is repeated...",
)

(
    title_level1009,
    description_level1009,
    hint_level1009,
) = (
    lambda: "This way, that way, forwards...",
    lambda: build_description(
        title_level1009(),
        "Think carefully about this one. It might be that some code is inside a loop and some code is not…",
    ),
    lambda: "You can solve this in stages. Try moving to the start of the repeated section, then adding the loop and then finishing it off.",
)

(
    title_level1010,
    description_level1010,
    hint_level1010,
    commands_level1010,
) = (
    lambda: "Four leaf clover",
    lambda: build_description(
        title_level1010(),
        "Look for a pattern and then count how many times it repeats. Good luck!",
    ),
    lambda: "If you cannot solve this one, try creating a solution without a while loop and then looking for what is repeated...",
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(
    title_level1011,
    description_level1011,
    hint_level1011,
    commands_level1011,
) = (
    lambda: "Pond life",
    lambda: build_description(
        title_level1011(),
        "There is a pattern of moves in this one too. Can you spot it?",
    ),
    lambda: "What if you go down the middle section?",
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(
    title_level1012,
    description_level1012,
    hint_level1012,
    commands_level1012,
) = (
    lambda: "Farmyard overdrive",
    lambda: build_description(
        title_level1012(),
        "Look for a pattern before you type any code. You can solve this one with a counted loop…",
    ),
    lambda: "Try that middle route...",
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(
    title_level1013,
    description_level1013,
    hint_level1013,
    commands_level1013,
) = (
    lambda: "Snnnaaaake reflection",
    lambda: build_description(
        title_level1013(),
        "The solution to this one is just a bit longer. Build it up slowly. Good luck!",
    ),
    lambda: "Don't try to solve this in one go. Work out the pattern for the top route and check that works. Then move on to the next part...",
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(
    title_level1014,
    description_level1014,
    hint_level1014,
) = (
    lambda: "Too many cows",
    lambda: build_description(
        title_level1014(),
        "This is a nice long straight road, but there are cows about!",
    ),
    lambda: "Make sure you sound the horn to get the cows off the road.",
)

(
    title_level1015,
    description_level1015,
    hint_level1015,
) = (
    lambda: "Stepping it up",
    lambda: build_description(
        title_level1015(), "There are some bends in this road. Be careful!"
    ),
    lambda: "What do you need to count, how many times you move or how many times you move forwards?",
)

(title_level1016, description_level1016, hint_level1016, commands_level1016) = (
    lambda: "Cows on the stairs",
    lambda: build_description(
        title_level1016(),
        "Oh no! The farmer seems to have let their cows out again. Be careful.",
    ),
    lambda: "Look for a pattern here...",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()</div>"
    + "</div>"
    + '<div class="row">'
    + '<div class="large-4 columns">'
    + "<p><b>Animals</b>"
    + "<br>my_van.is_animal_crossing()"
    + "<br>my_van.sound_horn()</div>"
    + "</div>",
)

(title_level1017, description_level1017, hint_level1017, commands_level1017) = (
    lambda: "Try stepping in Python!",
    lambda: build_description(
        title_level1017(),
        "Keep going, you're getting the hang of the Python code.",
    ),
    lambda: "So you are going forward unless...?",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_left()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(title_level1018, description_level1018, hint_level1018, commands_level1018) = (
    lambda: "A long and winding road",
    lambda: build_description(title_level1018(), "Oh dear, you might get a bit dizzy!"),
    lambda: "What are you counting here, straight roads or bends?",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_left()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(
    title_level1019,
    description_level1019,
    hint_level1019,
) = (
    lambda: "Try this level... or <b>else</b>!",
    lambda: build_description(
        title_level1019(),
        "Have you noticed that there are more roads ahead than turns? Try checking if there is a road ahead and then otherwise making the turns you need...",
    ),
    lambda: "Remember to use if..else",
)

(title_level1020, description_level1020, hint_level1020, commands_level1020) = (
    lambda: "Now try one in Python!",
    lambda: build_description(
        title_level1020(), "Use if..else in Python for this level"
    ),
    lambda: "Don't get distracted by the other roads. Look for a pattern you can repeat.",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_left()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(title_level1021, description_level1021, hint_level1021, commands_level1021) = (
    lambda: "What if there are multiple houses?",
    lambda: build_description(
        title_level1021(),
        "This is a really busy road. Make sure that you don't miss any of the houses.",
    ),
    lambda: "Did you get the last house? Think about what value the loop counter will have at that point in your code...",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()"
    + "<br>my_van.deliver()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_left()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(
    title_level1022,
    description_level1022,
    hint_level1022,
) = (
    lambda: "Count and check",
    lambda: build_description(
        title_level1022(), "There are lots of turns here, don't get distracted."
    ),
    lambda: "Think about the order of the questions you ask using your if and elif statements.",
)

(
    title_level1023,
    description_level1023,
    hint_level1023,
) = (
    lambda: "Another twisty trip",
    lambda: build_description(title_level1023(), "Don't go the long way around!"),
    lambda: "Think carefully about the order in which you ask questions in your if..else if block",
)

(title_level1024, description_level1024, hint_level1024, commands_level1024) = (
    lambda: "Give Python a go!",
    lambda: build_description(
        title_level1024(), "Look carefully for the shortest route."
    ),
    lambda: "Think carefully about the order in which you ask questions in your if..elif statements.",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_forward()"
    + "<br>my_van.is_road_left()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(title_level1025, description_level1025, hint_level1025, commands_level1025) = (
    lambda: "Now we've added a traffic light",
    lambda: build_description(
        title_level1025(), "Look carefully for the shortest route."
    ),
    lambda: "Think carefully about the order in which you ask questions in your if..elif statements. Don't forget the traffic lights.",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()"
    + "<br>my_van.wait()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_forward()"
    + "<br>my_van.is_road_left()"
    + "<br>my_van.at_red_traffic_light()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(
    title_level1026,
    description_level1026,
    hint_level1026,
) = (
    lambda: title_level85(),
    lambda: description_level85(),
    lambda: hint_level85(),
)

(
    title_level1027,
    description_level1027,
    hint_level1027,
) = (
    lambda: "Full steam ahead",
    lambda: build_description(
        title_level1027(), "Just keep going until you get there..."
    ),
    lambda: "You might find that the solution to this level is quite familiar...",
)

(
    title_level1028,
    description_level1028,
    hint_level1028,
) = (
    lambda: "Another staircase...",
    lambda: build_description(
        title_level1028(),
        "Well done, you did it! Now have a go at using the <b>Repeat while</b> block on a road with lots of turns.",
    ),
    lambda: "This is another route you have seen before. Last time you counted how many times your instructions were repeated. This time, your program is going to repeat your commands until you reach the destination. What do you need to repeat?",
)

(
    title_level1029,
    description_level1029,
    hint_level1029,
) = (
    lambda: title_level1010(),
    lambda: description_level1010(),
    lambda: hint_level1010(),
)

(title_level1030, description_level1030, hint_level1030, commands_level1030) = (
    lambda: title_level84(),
    lambda: build_description(
        title_level1030(),
        "Well done, you did it! Now have a go at coding with Repeats in Python only.",
    ),
    lambda: hint_level84(),
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.at_destination()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(
    title_level1031,
    description_level1031,
    hint_level1031,
) = (
    lambda: title_level34(),
    lambda: description_level34(),
    lambda: hint_level34(),
)

(
    title_level1032,
    description_level1032,
    hint_level1032,
) = (
    lambda: "Something isn't <b>right</b>",
    lambda: build_description(
        title_level1032(),
        "You don't have a right turn block here, so plan your route carefully.",
    ),
    lambda: "Think carefully about the order in which you ask questions in your if-statement here...",
)

(title_level1033, description_level1033, hint_level1033, commands_level1033) = (
    lambda: "Looking both ways",
    lambda: build_description(title_level1033(), "Can you find the shortest route?"),
    lambda: "In this level, you want to check for a left turn first. If there is no left turn, turn right. Keep in mind what that looks like in Python.",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_left()"
    + "<br>my_van.at_destination()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(title_level1034, description_level1034, hint_level1034, commands_level1034) = (
    lambda: "The pond is nice but out of the way",
    lambda: build_description(
        title_level1034(),
        "Can you find the shortest route? Don't take the scenic route.",
    ),
    lambda: "Just look for the simplest route to the house.",
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_right()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.is_road_right()"
    + "<br>my_van.at_destination()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(
    title_level1035,
    description_level1035,
    hint_level1035,
) = (
    lambda: title_level99(),
    lambda: build_description(
        title_level99(),
        "Now try using what you have just learnt to solve this level. You could also try using the if, elif and else statements.",
    ),
    lambda: hint_level99(),
)

(
    title_level1036,
    description_level1036,
    hint_level1036,
) = (
    lambda: title_level38(),
    lambda: description_level38(),
    lambda: hint_level38(),
)

(title_level1037, description_level1037, hint_level1037, commands_level1037) = (
    lambda: title_level100(),
    lambda: build_description(
        title_level100(),
        "Practice your new Python skills on this road to get the van to the destination.",
    ),
    lambda: hint_level100(),
    lambda: commands_level100(),
)

(title_level1038, description_level1038, hint_level1038, commands_level1038) = (
    lambda: title_level39(),
    lambda: description_level39(),
    lambda: hint_level39(),
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_around()"
    + "<br>my_van.turn_right()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.at_destination()"
    + "<br>my_van.is_road_forward()"
    + "<br>my_van.at_dead_end()</div>"
    + '<div class="large-4 columns"></div></div>'
    + '<div class="row">'
    + '<div class="large-4 columns">'
    + "<p><b>Animals</b>"
    + "<br>my_van.is_animal_crossing()"
    + "<br>my_van.sound_horn()</div>"
    + "</div>",
)

(title_level1039, description_level1039, hint_level1039, commands_level1039) = (
    lambda: title_level47(),
    lambda: build_description(
        title_level47(),
        "Put your knowledge to test. Create an algorithm to lead the van to the house. Don't forget to turn and avoid the cows.",
    ),
    lambda: hint_level47(),
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.at_destination()"
    + "<br>my_van.is_road_forward()</div>"
    + '<div class="large-4 columns"></div></div>'
    + '<div class="row">'
    + '<div class="large-4 columns">'
    + "<p><b>Animals</b>"
    + "<br>my_van.is_animal_crossing()"
    + "<br>my_van.sound_horn()</div>"
    + "</div>",
)

(title_level1040, description_level1040, hint_level1040, commands_level1040) = (
    lambda: title_level48(),
    lambda: description_level48(),
    lambda: hint_level48(),
    lambda: '<div class="row">'
    + '<div class="large-4 columns">'
    + "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_around()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()"
    + "<br>my_van.wait()"
    + "<br>my_van.deliver()</div>"
    + '<div class="large-4 columns">'
    + "<b>Position</b>"
    + "<br>my_van.at_red_traffic_light()"
    + "<br>my_van.at_destination()"
    + "<br>my_van.is_road_forward()"
    + "<br>my_van.is_road_left()"
    + "<br>my_van.is_road_right()"
    + "<br>my_van.at_dead_end()</div>"
    + '<div class="large-4 columns"></div></div>',
)

(
    title_level1041,
    description_level1041,
    hint_level1041,
) = (
    lambda: title_level83(),
    lambda: description_level83(),
    lambda: hint_level83(),
)

(title_level1042, description_level1042, hint_level1042, commands_level1042) = (
    lambda: title_level95(),
    lambda: build_description(
        title_level95(),
        "Now try to use a <b>repeat</b> loop to solve this level. Look back at level 41 to see what this could look like in Python.",
    ),
    lambda: hint_level95(),
    lambda: commands_level95(),
)

(title_level1043, description_level1043, hint_level1043, commands_level1043) = (
    lambda: title_level96(),
    lambda: build_description(
        title_level96(),
        "Now try to use a <b>repeat</b> loop to solve this level. Look back at level 41  to see what this could look like in Python. This time you could use 2 loops, 1 for each straight piece of road.",
    ),
    lambda: hint_level96(),
    lambda: commands_level96(),
)

(
    title_level1044,
    description_level1044,
    hint_level1044,
) = (
    lambda: title_level84(),
    lambda: description_level84(),
    lambda: hint_level84(),
)

(title_level1045, description_level1045, hint_level1045, commands_level1045) = (
    lambda: title_level97(),
    lambda: build_description(
        title_level97(),
        "Now try to use a loop within a loop, known as a 'nested loop'. Look back at level 44 to see what this could look like in Python.",
    ),
    lambda: hint_level97(),
    lambda: commands_level97(),
)

(title_level1046, description_level1046, hint_level1046, commands_level1046) = (
    lambda: title_level106(),
    lambda: description_level106(),
    lambda: hint_level106(),
    lambda: commands_level106(),
)

(title_level1047, description_level1047, hint_level1047, commands_level1047) = (
    lambda: title_level107(),
    lambda: description_level107(),
    lambda: hint_level107(),
    lambda: commands_level107(),
)

(title_level1048, description_level1048, hint_level1048, commands_level1048) = (
    lambda: title_level108(),
    lambda: description_level108(),
    lambda: hint_level108(),
    lambda: commands_level108(),
)

(title_level1049, description_level1049, hint_level1049, commands_level1049) = (
    lambda: title_level109(),
    lambda: description_level109(),
    lambda: hint_level109(),
    lambda: commands_level109(),
)

(
    title_level1050,
    description_level1050,
    hint_level1050,
) = (
    lambda: title_level61(),
    lambda: description_level61(),
    lambda: hint_level61(),
)

(
    title_level1051,
    description_level1051,
    hint_level1051,
) = (
    lambda: title_level62(),
    lambda: description_level62(),
    lambda: hint_level62(),
)

(title_level1052, description_level1052, hint_level1052, commands_level1052) = (
    lambda: title_level63(),
    lambda: description_level63(),
    lambda: hint_level63(),
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(title_level1053, description_level1053, hint_level1053, commands_level1053) = (
    lambda: title_level64(),
    lambda: description_level64(),
    lambda: hint_level64(),
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(title_level1054, description_level1054, hint_level1054, commands_level1054) = (
    lambda: title_level65(),
    lambda: description_level65(),
    lambda: hint_level65(),
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(title_level1055, description_level1055, hint_level1055, commands_level1055) = (
    lambda: title_level66(),
    lambda: description_level66(),
    lambda: hint_level66(),
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(title_level1056, description_level1056, hint_level1056, commands_level1056) = (
    lambda: title_level67(),
    lambda: description_level67(),
    lambda: hint_level67(),
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(title_level1057, description_level1057, hint_level1057, commands_level1057) = (
    lambda: "Have a go at procedures",
    lambda: build_description(
        title_level1057(),
        "Try adding a procedure and watch what happens in Python.",
    ),
    lambda: hint_level90(),
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(title_level1058, description_level1058, hint_level1058, commands_level1058) = (
    lambda: title_level91(),
    lambda: build_description(
        title_level1058(),
        "Try adding a procedure and watch what happens in Python.",
    ),
    lambda: hint_level91(),
    lambda: "<b>Movement</b>"
    + "<br>my_van.move_forwards()"
    + "<br>my_van.turn_left()"
    + "<br>my_van.turn_right()",
)

(title_level1059, description_level1059, hint_level1059, commands_level1059) = (
    lambda: title_level101(),
    lambda: build_description(
        title_level101(),
        "Try defining your own procedure to solve this level. In Python procedures are generally called functions. Look back at the previous levels for examples of how to define a function in Python.",
    ),
    lambda: hint_level101(),
    lambda: commands_level101(),
)

(title_level1060, description_level1060, hint_level1060, commands_level1060) = (
    lambda: title_level102(),
    lambda: description_level102(),
    lambda: hint_level102(),
    lambda: commands_level102(),
)


# Episode titles
def get_episode_title(episode_id):
    episode_titles = {
        1: "Getting Started",
        2: "Shortest Route",
        3: "Loops and Repetitions",
        4: "Loops with Conditions",
        5: "If... Only",
        6: "Traffic Lights",
        7: "Limited Blocks",
        8: "Procedures",
        9: "Blockly Brain Teasers",
        10: "Introduction to Python",
        11: "Python",
        12: "Counted Loops Using While",
        13: "Selection in a Loop",
        14: "Indeterminate Loops",
        15: "For Loops",
        16: "Output, Operators, and Data",
        17: "Variables, Input, and Casting",
        18: "Selection",
        19: "Complex Selection",
        20: "String Manipulation",
        21: "Lists",
        22: "Procedures",
        23: "2D Lists",
        24: "Procedures and Functions",
    }

    return episode_titles[episode_id]
