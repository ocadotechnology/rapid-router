# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from django.utils.translation import ugettext


def youtubeLink(width, height, url, border):
    return "<iframe width='" + str(width) + "' height='" + str(height) + "' src='" + str(url) \
           + "?rel=0" + "' frameborder='" + str(border) \
           + "' allowfullscreen class='video'></iframe><br>"


def noPermissionMessage():
    return ugettext("You have no permission to see this.")


def notSharedLevel():
    return ugettext("This level is private. You can only see the public levels and the ones "
                    + "created by other users only if they share them with you.")


""" Strings used in the scoreboard. """


def noPermissionTitle():
    return ugettext("No permission ")


def noPermissionScoreboard():
    return ugettext("Scoreboard is only visible to school students and teachers. Log in if you "
                    + "think you should be able to see it. ")


def noDataToShow():
    return ugettext("There is no data to show. Please contact your administrator if this is "
                    + "unexpected. ")


""" Strings used on the level moderation page. """


def noPermissionLevelModerationTitle():
    return ugettext("No permission ")


def noPermissionLevelModerationPage():
    return ugettext("Level moderation is only visible to teachers. Log in if you "
                    + "think you should be able to see it. ")


def noPermissionLevelModerationClass():
    return ugettext("You do not teach this class. Please contact your administrator if this "
                    + "is unexpected.")


def noPermissionLevelModerationStudent():
    return ugettext("You do not teach this student. Please contact your administrator if this "
                    + "is unexpected.")


def noDataToShowLevelModeration():
    return ugettext("You have not created any classes and therefore is no data to show. " +
                    "Please contact your administrator if this is unexpected.")


""" String messages used on the settings page. """


def shareTitle():
    return ugettext("Level Share")


def shareSuccessfulPerson(name, surname):
    return ugettext("You shared your level with {0} {1} successfully! ".format(name, surname))


def shareSuccessfulClass(className):
    return ugettext("You shared your level with class {0} successfully! ".format(className))


def shareUnsuccessfulPerson(first_name, last_name):
    return ugettext("We were unable to find %(name)s %(surname)s. "
                    % {'name': first_name, 'surname': last_name}
                    + "Are you sure you got their name right?")


def shareUnsuccessfulClass(className):
    return ugettext("We were unable to find class %(class)s. Are you sure you got it right?"
                    % {'class': className})


def noLevelsToShow():
    return ugettext("It seems that you have not created any levels. How about creating one "
                    + "now? ")


def levelsMessage():
    return ugettext("All the levels you have created so far. Click on them to play them or "
                    + "share them with your friends. ")


def sharedLevelsMessage():
    return ugettext("All the levels created by others that were shared with you. Click on "
                    + "them to play them")


def noSharedLevels():
    return ugettext("No one shared a level with you yet. ")


""" Strings used in the class view. """


def chooseClass():
    return ugettext("Choose a class you want to see. ")


def noPermission():
    return ugettext("You don't have permissions to see this. ")


"""
"""
""" String messages used as level tips in the game view.
"""
"""
"""

def title_night_mode():
    return 'Can you find your way in the dark?'

def build_description(title, message):
    return "<b>" + title + "</b><br><br>" + message


def title_level_default():
    return ugettext(" ")


def description_level_default():
    message = ugettext("Can you find the shortest route? ")
    return message


def hint_level_default():
    message = ugettext("Think back to earlier levels. What did you learn? ")
    return message


def title_level1():
    return ugettext("Can you help the van get to the house? ")


def description_level1():
    message = ugettext("Choose the right blocks to tell the van where to go. <br> Drag the "
                       + "blocks under the <b>Start</b> block to attach them. <br> To remove a "
                       + "block, drag it into the bin in the bottom right of the screen. "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level1(), message)


def hint_level1():
    message = ugettext("Drag the <b>Move forwards</b> block so that it is under the <b>Start</b> "
                       + "block - close enough to be touching. <br><br>"
                       + "Clicking on the arrows next to the <b>Go</b> button will also drag the "
                       + "blocks into a sequence for you. <br><br>"
                       + "Don't forget to press <b>Go</b> when you are done. ")
    return message


def title_level2():
    return ugettext("This time the house is further away. ")


def description_level2():
    message = ugettext("A block can be placed next to or under another, like a jigsaw. A second "
                       + "<b>Move forwards</b> block can be placed under the first <b>Move "
                       + "forwards</b> block. <br> To remove a block, drag it back to the "
                       + "left of the screen or drop it in the bin. <br> When you are happy with "
                       + "your sequence, press <b>Go</b>! ")
    return build_description(title_level2(), message)


def hint_level2():
    message = ugettext("A second <b>Move forwards</b> block can be placed under the first <b>Move "
                       + "forwards</b> block. <br><br>"
                       + "The arrows next to the <b>Go</b> button will drag the blocks into a "
                       + "sequence for you. ")
    return message


def title_level3():
    return ugettext("Can you make the van turn right? ")


def description_level3():
    message = ugettext("This time, the van has to turn right to reach the house. Make sure you use "
                       + "the <b>Turn right</b> block in your sequence. <br> Drag the blocks "
                       + "and attach them under the <b>Start</b> block like before. To remove a "
                       + "block, drag it back to the left of the screen or drop it in the bin. "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level3(), message)


def hint_level3():
    message = ugettext("A <b>Turn right</b> block can be placed under the first <b>Move "
                       + "forwards</b> block. <br><br> The arrows next to the <b>Go</b> button "
                       + "will drag the blocks into a sequence for you. ")
    return message


def title_level4():
    return ugettext("You are getting good at this! Let's try turning left. ")


def description_level4():
    message = ugettext("This time the van has to go left. Make sure you use the <b>Turn left</b> "
                       + "block in your sequence. <br> Drag and attach the blocks like before. "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level4(), message)


def hint_level4():
    message = ugettext("A <b>Turn left</b> block can be placed under a series of <b>Move "
                       + "forwards</b> blocks. <br> The arrows next to the <b>Go</b> button will "
                       + "drag the blocks into a sequence for you. ")
    return message


def title_level5():
    return ugettext("Good work! You are ready for something harder. ")


def description_level5():
    message = ugettext("You already know how to make the van turn left or right. This time "
                       + "the van has to make lots of turns to reach the house. <br> Drag and "
                       + "attach the blocks to make your sequence."
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level5(), message)


def hint_level5():
    message = ugettext("This road starts by curving to the <b>left</b>. Then it curves to the "
                       + "<b>right</b>. <br><br> The arrows next to the <b>Go</b> button will drag "
                       + "the blocks into a sequence for you. ")
    return message


def title_level6():
    return ugettext("Well done! Let's use all three blocks. ")


def description_level6():
    message = ugettext("This time the van has to <b>Move forwards</b>, <b>Turn left</b> and "
                       + "<b>Turn right</b>. <br><br> Drag and attach the blocks like before. "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level6(), message)


def hint_level6():
    message = ugettext("Follow the road around. How many <b>Move forwards</b> do you need? <br><br>"
                       + "The arrows next to the <b>Go</b> button will drag the blocks into a "
                       + "sequence for you. ")
    return message


def title_level7():
    return ugettext("This road is more complicated. ")


def description_level7():
    message = ugettext("Practise your new skills on this road by helping the driver to arrive at "
                       + "the house. <br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level7(), message)


def hint_level7():
    message = ugettext("Follow the road around. Don't forget to <b>Turn left</b> first. <br><br>"
                       + "The arrows next to the <b>Go</b> button will drag the blocks into a "
                       + "sequence for you.")
    return message


def title_level8():
    return ugettext("The warehouse is not always in the same place. ")


def description_level8():
    message = ugettext("This time the warehouse is somewhere else on the screen but you still need "
                       + "to use the <b>Move forwards</b> block. <br> Can you use the <b>Move "
                       + "forwards</b> block correctly even when it looks like the van goes in a "
                       + "different direction? "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level8(), message)


def hint_level8():
    message = ugettext("On screen, the van looks like it follows the road down. If you were in the "
                       + "van, it would look like you should <b>Move forwards</b>, then <b>Turn "
                       + "right</b>. ")
    return message


def title_level9():
    return ugettext("Can you go from right to left? ")


def description_level9():
    message = ugettext("Practise your new skills on this road by helping the driver to arrive "
                       + "at the house. "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level9(), message)


def hint_level9():
    message = ugettext("How many times do you have to <b>Move forwards</b> before you "
                       + "<b>Turn left</b>? ")
    return message


def title_level10():
    return ugettext("Well done! How about another go? ")


def description_level10():
    message = ugettext("You've done really well so far. Try to get the van to the house. "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level10(), message)


def hint_level10():
    message = ugettext("This map is not so hard. Notice that to you it looks like the road goes "
                       + "up, but if you were in the in the van, you would see the road goes "
                       + "right. <br><br> Do you know which turn the van will take next? <br><br> "
                       + "The arrows next to the <b>Go</b> button will drag the blocks into a "
                       + "sequence for you. ")
    return message


def title_level11():
    return ugettext("Snail maze! ")


def description_level11():
    message = ugettext("Uh oh, a tricky snail maze! Can you take the van through it? "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level11(), message)


def hint_level11():
    message = ugettext("The maze looks a bit like a snail, doesn't it? That means that for most of "
                       + "the time the van should only <b>Move forwards</b> and <b>Turn right</b>. "
                       + "<br><br> The arrows next to the <b>Go</b> button will drag the blocks "
                       + "into a sequence for you. ")
    return message


def title_level12():
    return ugettext("This road is more complicated. ")


def description_level12():
    message = ugettext("Good work, by now you are able to solve quite complicated levels. Prove "
                       + "your skills! "
                       + "<br> When you are happy with your sequence, press <b>Go</b>! ")
    return build_description(title_level12(), message)


def hint_level12():
    message = ugettext("This road might look much longer and more complicated, but it's not that "
                       + "hard. <br> Start by using <b>Move forwards</b> a few steps and <b>Move "
                       + "left</b>. ")
    return message


def title_level13():
    return ugettext("Multiple routes")


def description_level13():
    message = ugettext("Often there is more than one way to get to the house. The route that needs "
                       + "the fewest directions is usually best. <br> Help the van find the "
                       + "shortest route to the house. <br> You can press the <b>Go</b> or "
                       + "<b>Play</b> buttons to start the van. ")
    return build_description(title_level13(), message)


def hint_level13():
    message = ugettext("Try taking the route that starts by turning left then turns right. Do you "
                       + "know what follows next? ")
    return message


def title_level14():
    return ugettext("Can you spot the shortest route? ")


def description_level14():
    message = ugettext("So many options to choose from! <br> Do you know which is the shortest "
                       + "route to get the van to house? ")
    return build_description(title_level14(), message)


def hint_level14():
    message = ugettext("The middle route seems to be shortest. Do you know what sequence of "
                       + "instructions will make the van follow it?")
    return message


def title_level15():
    return ugettext("What if there is more than one delivery? ")


def description_level15():
    message = ugettext("Our vans often need to go to more than one house. To make the van deliver "
                       + "to a house use the <b>Deliver</b> block. <br> Make sure your sequence "
                       + "gets the van to travel the shortest route! ")
    return build_description(title_level15(), message)


def hint_level15():
    message = ugettext("Make the van turn left and go directly to the closest house first. This is "
                       + "the shortest route. <br><br> The <b>Deliver</b> block is not needed when "
                       + "the van is only going to one house, but you need it when the van is "
                       + "going to two or more houses. <br><br> Use the <b>Deliver</b> block every "
                       + "time the van gets to a house. ")
    return message


def title_level16():
    return ugettext("This time there are even more houses. ")


def description_level16():
    message = ugettext("Well done! You have done really well to get so far - let's take it to the "
                       + "next level and add another house. <br> Can you work out the shortest, "
                       + "most efficient route to each house? ")
    return build_description(title_level16(), message)


def hint_level16():
    message = ugettext("Although the <b>Deliver</b> block is not needed when there is only one "
                       + "house, you need it when there are more houses, like now. <br><br>"
                       + "Once the van is at a house, make sure you use the <b>Deliver</b> block. "
                       + "Do that for each house. ")
    return message


def title_level17():
    return ugettext("House overload! ")


def description_level17():
    message = ugettext("Well done, you're getting a hang of it! Can you do the same for even more "
                       + "houses?<br> Don't forget to use the <b>Deliver</b> block at each house. ")
    return build_description(title_level17(), message)


def hint_level17():
    message = ugettext("Test your sequence to make sure that the van takes the shortest route to "
                       + "visit all the houses on the way. <br><br> Use the <b>Deliver</b> block "
                       + "every time the van gets to a house. ")
    return message


def title_level18():
    return ugettext("This one is quite a tangle. ")


def description_level18():
    message = ugettext("Practise your new skills on this road by getting the van to <b>Deliver</b> "
                       + "to each of the houses. ")
    return build_description(title_level18(), message)


def hint_level18():
    message = ugettext("To make sure the van takes the shortest route, first turn left. <br><br> "
                       + "Use the <b>Deliver</b> block every time the van gets to a house. ")
    return message


def title_level19():
    return ugettext("Repeating yourself is boring.")


def description_level19():
    message = youtubeLink(600, 400, "//www.youtube.com/embed/vFGd0v3msRE", 0)
    message += ugettext("Attach a block inside the <b>Repeat</b> block to make the van repeats "
                        + "that instruction. <br> This means you can use one block instead of lots "
                        + "of blocks to do the same thing over and over again. <br> How many times "
                        + "do you want the instruction repeated? Type the number into the "
                        + "<b>Repeat</b> block. <br> The repeated sets of blocks make a 'loop'.  "
                        + "<br><br> When you are ready, press <b>Play</b>! ")
    return build_description(title_level19(), message)


def hint_level19():
    message = ugettext("A <b>Move forwards</b> block can be placed inside a <b>Repeat</b> block "
                       + "(to the right of the word 'Do'). <br><br> Don't forget to change the "
                       + "number of times you need to repeat the instruction. ")
    return message


def title_level20():
    return ugettext("Use the <b>Repeat</b> block to make your sequence shorter and simpler. ")


def description_level20():
    message = ugettext("You drove the van down this road on Level 5. This time, use the "
                       + "<b>Repeat</b> block to get the van to the house. <br> This will make "
                       + "your sequence shorter and simpler than last time.")
    return build_description(title_level20(), message)


def hint_level20():
    message = ugettext("This level can be broken down into three repeated sets of: <b>Turn "
                       + "left</b>, then <b>Turn right</b>. <br><br> These repeated steps make a "
                       + "'loop'. ")
    return message


def title_level21():
    return ugettext("Four leaf clover.")


def description_level21():
    message = ugettext("This path looks a bit like a four leaf clover. Can you take the driver "
                       + "through it? ")
    return build_description(title_level21(), message)


def hint_level21():
    message = ugettext("This level can be broken down into repeated sets of: <b>Move forwards</b>, "
                       + "<b>Turn left</b>, <b>Turn right<b>, <b>Turn left</b>. ")
    return message


def title_level22():
    return ugettext("Now things are getting quite long and complicated. ")


def description_level22():
    message = ugettext("An algorithm (a set of instructions in a particular order) to get the van "
                       + "to the house might not be very simple, but it can be made shorter by "
                       + "using the <b>Repeat</b> blocks. <br> Are you up for this challenge? ")
    return build_description(title_level22(), message)


def hint_level22():
    message = ugettext("Look to see where you have used <b>Move forwards</b>, <b>Turn "
                       + "left</b> and <b>Turn right</b> blocks. Are any blocks next to them the "
                       + "same? Put them into one <b>Repeat</b> block. Don't forget to change the "
                       + "number of times you need to repeat the instruction. ")
    return message


def title_level23():
    return ugettext("Sssssssssnake!")


def description_level23():
    message = ugettext("This road seems to be winding just like a snake! Can you find a nice and "
                       + "simple route to get the van to the house? ")
    return build_description(title_level23(), message)


def hint_level23():
    message = ugettext("How about using <b>Repeat</b> inside another <b>Repeat</b>? <br><br> This "
                       + "level can be broken down into sets of: "
                       + "<li> a set (nested loop) of <b>Move forwards</b>, </li> "
                       + "<li> two <b>Turn left</b>s, </li> "
                       + "<li> a set (nested loop) of <b>Move forwards</b>, </li> "
                       + "<li> two <b>Turn right</b>s. </li>")
    return message


def title_level24():
    return ugettext("The road is very long and very bendy.")


def description_level24():
    message = ugettext("Wow! Look at that! It won't get more complicated than this, we promise.")
    return build_description(title_level24(), message)


def hint_level24():
    message = ugettext("With all these twists and turns, you will have to think hard about what "
                       + "sets of repeated instructions to use. <br><br>")
    return message


def title_level25():
    return ugettext("Waterfall level. ")


def description_level25():
    message = ugettext("Since you did so well with the repeat loops, have a go at this level. ")
    return build_description(title_level25(), message)


def hint_level25():
    message = ugettext("Most of the program will consist of repeated sets of <b>Move forwards</b> "
                       + "and a set of <b>Turn right</b> and <b>Turn left</b>. ")
    return message


def title_level26():
    return ugettext("Winter wonderland!")


def description_level26():
    message = ugettext("Notice the snow! You can create new levels with different 'themes' of "
                       + "backgrounds and decorations in the Level Editor. But first, try getting "
                       + "the van to the house! ")
    return build_description(title_level26(), message)


def hint_level26():
    message = ugettext("Break the program into two <b>Repeat</b>s with a <b>Turn left</b> in "
                       + "between them. ")
    return message


def title_level27():
    return ugettext("Farmyard")


def description_level27():
    message = ugettext("What a muddy road! Can you help Dee find her way from the barn to the "
                       + "house? ")
    return build_description(title_level27(), message)


def hint_level27():
    message = ugettext("Make sure you drag the correct turns into your <b>Repeat</b> block. ")
    return message


def title_level28():
    return ugettext("The big city")


def description_level28():
    message = ugettext("Can you get the van from the warehouse to the house? Don't stop at any "
                       + "shops on the way! ")
    return build_description(title_level28(), message)


def hint_level28():
    message = ugettext("Make sure you drag the correct turns into your <b>Repeat</b> block.")
    return message


def title_level29():
    return ugettext("No need for numbers. ")


def description_level29():
    message = youtubeLink(600, 400, "//www.youtube.com/embed/EDwc80X_LQI", 0)
    message += ugettext("Drag a block inside a <b>Repeat until</b> block to make the van repeat an "
                        + "instruction. <br> Attach a 'condition' so the van knows when to stop "
                        + "repeating the instruction. <br> Here, you want the van to repeat your "
                        + "instruction until it is at the destination. <br> Doing this means "
                        + "you don't have to work out how many times the van should repeat your "
                        + "instruction. ")
    return build_description(title_level29(), message)


def hint_level29():
    message = ugettext("The blocks should read like a sentence: '<b>Repeat <b>until</b> <b>at "
                       + "destination do: Move forwards</b>'. ")
    return message


def title_level30():
    return ugettext("Can you do that again? ")


def description_level30():
    message = ugettext("Well done, you did it! Now have a go at using the <b>Repeat until<b> block "
                       + "on a road with lots of turns. ")
    return build_description(title_level30(), message)


def hint_level30():
    message = ugettext("The blocks should read like a sentence: '<b>Repeat until at "
                       + "destination</b> <b>do</b>: <b>Turn left</b>, <b>Turn right</b>'. ")
    return message


def title_level31():
    return ugettext("Practice makes perfect. ")


def description_level31():
    message = ugettext("Have another go to make sure you have got the hang of it. ")
    return build_description(title_level31(), message)


def hint_level31():
    message = ugettext("This program can be broken into repeated sets of <b>Turn left</b>, <b>Turn "
                       + "right</b> and two <b>Move forwards</b>. ")
    return message


def title_level32():
    return ugettext("Uh oh, it's <b>Until</b> fever! ")


def description_level32():
    message = ugettext("Good job! Can you help the driver reach the destination again? ")
    return build_description(title_level32(), message)


def hint_level32():
    message = ugettext("This program is quite similar to the one you just solved. Do you remember "
                       + "the solution you came up with back then? ")
    return message


def title_level33():
    return ugettext("Now it's time to try the <b>If</b> block. ")


def description_level33():
    message = youtubeLink(600, 400, "//www.youtube.com/embed/O0RXbJyYq8o", 0)
    message += ugettext("Another way of telling the van what to do is to use the <b>If</b> block. "
                        + "For example, <b>If</b> the <b>road exists forwards do</b> <b>Move "
                        + "forwards</b>. <br> This is called an 'if statement'. <br> Try "
                        + "using the <b>If</b> block and the <b>Repeat</b> block together. <br> "
                        + "The <b>Repeat</b> block will stretch if you attach the <b>If</b> block "
                        + "inside it. ")
    return build_description(title_level33(), message)


def hint_level33():
    message = ugettext("We say that the road 'exists' in a direction. For example, if the road "
                       + "goes forwards we say that it 'exists forwards'. <br><br> "
                       + "<b>If</b> a <b>road exists forwards</b> then <b>do Move forwards</b>."
                       + "<br><br>Repeat this set to get the van to the house. ")
    return message


def title_level34():
    return ugettext("Multiple <b>If</b>s")


def description_level34():
    message = ugettext("It can be handy to use <b>If</b> to give your van choices, so you don't "
                       + "have to give the van new instructions at every step. <br> For "
                       + "example: Tell the van <b>If</b> the <b>road exists forwards do Move "
                       + "forwards,</b> but <b>If</b> the <b>road exists left do Turn left</b>. "
                       + "<br> The van will choose correctly from the <b>Move forwards</b> and "
                       + "<b>Turn left</b> instructions depending on the road. <br> Use an 'if "
                       + "statement' in a 'loop' to drive the van down this bendy road. ")
    return build_description(title_level34(), message)


def hint_level34():
    message = ugettext("At each bend the van can either <b>Move forwards</b> or <b>Turn left</b>. "
                       + "Create a loop so it can make the correct choice. <br><br> We say that "
                       + "the road 'exists' in a direction. For example, if the road goes forwards "
                       + "we say that it 'exists forwards'. ")
    return message


def title_level35():
    return ugettext("Let's put it all together!")


def description_level35():
    message = ugettext("You have discovered the magic of 'if statements'. Can you make a program "
                       + "that uses <b>Move forwards</b>, <b>Turn left</b> and <b>Turn right</b> "
                       + "to get the van to the house. ")
    return build_description(title_level35(), message)


def hint_level35():
    message = ugettext("At each bend the van can either <b>Move forwards</b> or <b>Turn left</b>. "
                       + "Create a loop so it can make the correct choice. <br><br> We say that "
                       + "the road 'exists' in a direction. For example, if the road goes forwards "
                       + "we say that it 'exists forwards'. ")
    return message


def title_level36():
    return ugettext("What else? If-else, that's what! ")


def description_level36():
    message = youtubeLink(600, 400, "//www.youtube.com/embed/GUUJSRuAyU0", 0)
    message += ugettext("You can change the <b>If</b> block to make more choices. Click on the "
                        + "star in the <b>If</b> block and add <b>Else if</b>. <br> This will tell "
                        + "the van what to do if the first <b>If</b> direction can't be done. "
                        + "<br> For example, tell the van to <b>Turn left</b> <b>If</b> the "
                        + "<b>road exists left</b>. Add <b>Else if</b> the <b>road exists right"
                        + "</b>, <b>Turn right</b>. <br> This uses fewer blocks and makes sure "
                        + "that only one step is taken in each loop. <br> This type of "
                        + "algorithm is called a 'general algorithm' as it can be used with most "
                        + "simple routes. ")
    return build_description(title_level36(), message)


def hint_level36():
    message = ugettext("The program should be a simple set of: <b>If road exists forwards do</b> "
                       + "<b>Move forwards</b>, <b>Else if road exists left do Turn left</b>, "
                       + "<b>Else if road exists right do Turn right</b>. <br><br> You can find "
                       + "<b>Else if</b> by clicking the star on the <b>If</b> block and adding "
                       + "the <b>Else if</b>.<br><br> If the first 'condition' is true (this means "
                       + "if the road exists in the direction you put first) the van will follow "
                       + "the blocks after <b>If</b>. <br><br> If not, the van will check to see "
                       + "if it can follow the direction you put after <b>Else if</b>. It will "
                       + "keep checking until it has a direction it can take. ")
    return message


def title_level37():
    return ugettext("A bit longer.")


def description_level37():
    message = ugettext("Let's see if we can go further - this road is longer. Notice that the "
                       + "length of the road does not change the length of your program! ")
    return build_description(title_level37(), message)


def hint_level37():
    message = ugettext("Think back to the solutions you produced using 'if statements' before. ")
    return message


def title_level38():
    return ugettext("Third time lucky! ")


def description_level38():
    message = ugettext("Well done! You've got so far. <br> Can you apply the knowledge you "
                       + "gained going through this part of the game to this level? ")
    return build_description(title_level38(), message)


def hint_level38():
    message = ugettext("Think back to the solutions you produced using 'if statements' before. ")
    return message


def title_level39():
    return ugettext("Dead ends! ")


def description_level39():
    message = ugettext("Can you change the 'general algorithm' so that the van takes a shorter "
                       + "route? <br> What if you change the order the van checks for "
                       + "directions? <br> Keep an eye on the fuel level - try to use as "
                       + "little as possible. ")
    return build_description(title_level39(), message)


def hint_level39():
    message = ugettext("Make the van check if the road exists right before it checks if the road "
                       + "exists left. <br><br> Then it will be able to reach the destination "
                       + "using the 'general algorithm'. Can you see why? ")
    return message


def title_level40():
    return ugettext("Adjust your previous solution.")


def description_level40():
    message = ugettext("Can you think of a way you could change the 'general algorithm' you have "
                       + "implemented earlier to make sure the van driver reaches the house having "
                       + "travelled the shortest route? ")
    return build_description(title_level40(), message)


def hint_level40():
    message = ugettext("The 'general algorithm' will work here. <br><br> Make sure you change the "
                       + "order the van checks for directions to take the shortest route to the "
                       + "destination. ")
    return message


def title_level41():
    return ugettext("Decision time. ")


def description_level41():
    message = ugettext("Do you think changes to the 'general algorithm' will help the van find the "
                       + "shortest route? <br> Or do you have to come up with a different "
                       + "solution? <br> Time to make a decision... ")
    return build_description(title_level41(), message)


def hint_level41():
    message = ugettext("Psst! You can simply make a change to the 'general algorithm'. <br><br> "
                       + "If you make the van check for turns before it checks the road exists "
                       + "forwards, you will come up with the perfect solution. <br><br>"
                       + "Notice that here it doesn't matter which turn you check for first - it "
                       + "will change the route but provide you with the same score. ")
    return message


def title_level42():
    return ugettext("What do you think this time? ")


def description_level42():
    message = ugettext("Can you use the 'general algorithm' here? <br> Can it be changed so that "
                       + "it finds a shorter route, or will you need a new solution? ")
    return build_description(title_level42(), message)


def hint_level42():
    message = ugettext("Uh oh, moving around the blocks in your 'general algorithm' won't help. "
                       + "<br> How about creating a simple solution without 'if statements' that "
                       + "will help the van reach the house? ")
    return message


def title_level43():
    return ugettext("Good work! What else can you do? ")


def description_level43():
    message = ugettext("You should be really good at this by now. Can you manage this complicated "
                       + "road? ")
    return build_description(title_level43(), message)


def hint_level43():
    message = ugettext("This road cannot be solved by a 'general algorithm'. Can you solve it "
                       + "without 'if statements'? <br><br> Remember to choose the shortest route "
                       + "and an algorithm which is as short as possible.  ")
    return message


def title_level44():
    return ugettext("Oh no! Traffic lights! ")


def description_level44():
    message = youtubeLink(600, 400, "//www.youtube.com/embed/EDwc80X_LQI", 0)
    message += ugettext("The light varies from red to green. <br>"
                        + "The van must check which colour the traffic light is when it reaches them "
                                            + "- if it goes past a red light it will break the Highway Code."
                        + "<br> Here, you want the van to repeat the wait instruction while the traffic light is red. "
                        + "Drag a block inside a <b>Repeat while</b> block to make the van repeat an instruction. "
                        + "<br> Attach a 'condition' so the van knows when to repeat the instruction. ")
    return build_description(title_level44(), message)


def hint_level44():
    message = ugettext("Don't worry about the 'general algorithm' here. Just go forwards. <br><br>"
                       + "Once the van is right under the traffic light, make it wait for a green "
                       + "light by adding a <b>Wait</b> block. ")
    return message


def title_level45():
    return ugettext("Green for go, red for wait. ")


def description_level45():
    message = ugettext("Can you write a program so the van moves forwards on a green light but "
                       + "waits at a red light? ")
    return build_description(title_level45(), message)


def hint_level45():
    message = ugettext("Use an 'if statement' to tell the van <b>If traffic light is red, Wait, "
                       + "Else Move forwards</b>. <br><br> Remember to repeat that until you get "
                       + "to the destination. ")
    return message


def title_level46():
    return ugettext("Well done - you've made it really far! ")


def description_level46():
    message = ugettext("Let's practise what you've learnt so far. <br> Don't forget to add a "
                       + "turn and to make the van wait at a traffic light. ")
    return build_description(title_level46(), message)


def hint_level46():
    message = ugettext("Be careful about the order you put your <b>If</b> blocks in. <br><br>"
                       + "If you make the van check the road exists forwards before checking for a "
                       + "light, it might break the Highway Code. ")
    return message


def title_level47():
    return ugettext("What a mess! But can you spot a route? ")


def description_level47():
    message = ugettext("Put your knowledge to test. Create an algorithm to lead the van to the "
                       + "house. <br> Don't forget to add a turn and to make the van wait at a "
                       + "traffic light. ")
    return build_description(title_level47(), message)


def hint_level47():
    message = ugettext("Use an 'if statement' and check if the light is red. <br><br> "
                       + "<b>If traffic light is red, wait, Else if road exists forwards, Move "
                       + "forwards, Else Turn left</b>. <br><br> Remember to repeat that until you "
                       + "get to the destination! ")
    return message


def title_level48():
    return ugettext("Put all that hard work to the test. ")


def description_level48():
    message = ugettext("Congratulations - you've made it really far! <br> Can you create a "
                       + "'general algorithm' that will help the van reach the destination in the "
                       + "shortest way but stop at a traffic light? ")
    return build_description(title_level48(), message)


def hint_level48():
    message = ugettext("You need to check: "
                       + "<li> if the lights are red </li>"
                       + "<li> if the road exists right </li>"
                       + "<li> if the road exists forwards </li> "
                       + "<li> if the road exists left </li>"
                       + "<li> if it is a dead end </li>"
                       + "Make sure you put the checks in the right order. ")
    return message


def title_level49():
    return ugettext("Amazing! Have another go! ")


def description_level49():
    message = ugettext("Can you change the 'general algorithm' you created before to make the van "
                       + "take the shortest route to the destination? ")
    return build_description(title_level49(), message)


def hint_level49():
    message = ugettext("You need to check: "
                       + "<li> if the light is red </li>"
                       + "<li> if the road exists left </li>"
                       + "<li> if the road exists forwards </li>"
                       + "<li> or if the road exists right </li>"
                       + "Do you think you need to check for a dead end? <br> Make sure you put "
                       + "the checks in the right order. ")
    return message


def title_level50():
    return ugettext("Light maze. ")


def description_level50():
    message = ugettext("Well this is tricky. Look at all those lights! <br> Can you find the "
                       + "shortest route to the destination? It would be good if the van doesn't "
                       + "have to wait at too many lights. ")
    return build_description(title_level50(), message)


def hint_level50():
    message = ugettext("Don't worry about the algorithm you've already come up with. Take the "
                       + "first turn left which has fewer traffic lights. <br><br> Once your van "
                       + "is right under the traffic lights, make sure it waits for a green "
                       + "light. ")
    return message










def title_level51():
    return ugettext("Back to basics with a twist")

def description_level51():
    message = ugettext("Can you come up with a solution to this level using the limited number of blocks we provide at the start?")
    return build_description(title_level51(), message)

def hint_level51():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level52():
    return ugettext("A Bit more Tricky")

def description_level52():
    message = ugettext("Well done so far! Can you find a solution to this road? You have to move forward, but you have no forward block to use. Do you know how to help the van get to the destination?")
    return build_description(title_level52(), message)

def hint_level52():
    message = ugettext("Don't forget to use the repeat loop.")
    return message


def title_level53():
    return ugettext("Choose your blocks wisely")

def description_level53():
    message = ugettext("Can you find the shortest route? Use your blocks carefully and don't forget the <b>repeat</b> loop.")
    return build_description(title_level53(), message)

def hint_level53():
    message = ugettext("Think back to earlier levels - what did you learn")
    return message


def title_level54():
    return ugettext("Round and Round")

def description_level54():
    message = ugettext("Can you find the shortest route? Use your blocks carefully and don't forget the <b>repeat</b> loop.")
    return build_description(title_level54(), message)

def hint_level54():
    message = ugettext("Think back to earlier levels - what did you learn")
    return message


def title_level55():
    return ugettext("Wonky Fish!")

def description_level55():
    message = ugettext("Use <b>repeat until</b> and the <b>if</b> statement to find your way around the Wonky Fish.")
    return build_description(title_level55(), message)

def hint_level55():
    message = ugettext("Think back to earlier levels - what did you learn.")
    return message


def title_level56():
    return ugettext("Concrete Wasteland")

def description_level56():
    message = ugettext("Use <b>repeat until</b> and the <b>if</b> statement to find your way around the Concrete Wasteland")
    return build_description(title_level56(), message)

def hint_level56():
    message = ugettext("Think back to earlier levels - what did you learn.")
    return message


def title_level57():
    return ugettext("This is <b>not...</b> the same")

def description_level57():
    message = ugettext("Like <b>repeat until</b>, <b>repeat while</b> is the opposite. Here, you want the van to repeat your instructions while it is not at the destination.<br />Doing this means you don't have to work out how many times the van should repeat your instructions.")
    return build_description(title_level57(), message)

def hint_level57():
    message = ugettext("The blocks should read like a sentence. Repeat while not at destination then add your instructions using the blocks provided.")
    return message


def title_level58():
    return ugettext("Snow snake")

def description_level58():
    message = ugettext("Combining what you have just learnt using <b>repeat while</b> with the repeat loop, can you find your way around the snow snake?")
    return build_description(title_level58(), message)

def hint_level58():
    message = ugettext("The blocks should read like a sentence: <b>repeat while not at destination</b> then using the <b>repeat</b> add your instructions")
    return message


def title_level59():
    return ugettext("Tricky turnaround")

def description_level59():
    message = ugettext("Use your blocks carefully not forgetting the <b>turnaround</b>.")
    return build_description(title_level59(), message)

def hint_level59():
    message = ugettext("Inside the repeat <b>repeat until</b> block, <b>turn left</b>, <b>turn around</b> and <b>turn left<b> again should do it.")
    return message


def title_level60():
    return ugettext("Right around the block")

def description_level60():
    message = ugettext("Can you find your way around this puzzle?")
    return build_description(title_level60(), message)

def hint_level60():
    message = ugettext("The trick to this level is to <b>turn right</b> then <b>turn around</b>.")
    return message


def title_level61():
    return ugettext("Can you create the 'Wiggle' procedure?")

def description_level61():
    message = ugettext("Procedures are groups of instructions that can be executed multiple times without being rewritten. For example, if you want to instruct the van to follow a repeated pattern in the road, you can create a specific procedure. To create a procedure, simply choose the correct blocks and put them in the right order inside the <b>Define do</b> block. Once you have done that, give it a name eg wiggle.<br />Now you're ready! Attach the <b>Call</b> block where you want your 'wiggle' procedure to be executed. Don't forget to put the name in it!")
    return build_description(title_level61(), message)

def hint_level61():
    message = ugettext("Don't forget to use <b>Define</b>. Name your procedure and attach the blocks in the right order. Start with <b>move forwards</b>, <b>turn left</b>, you can add repeat loops to a procedure and ending with <b>turn left</b>. Call your procedure under your start block and off you go...")
    return message


def title_level62():
    return ugettext("Lots of Traffic Lights!")

def description_level62():
    message = ugettext("Create a procedure which tells the van to wait until the traffic lights are green.")
    return build_description(title_level62(), message)

def hint_level62():
    message = ugettext("Don't forget to name your procedure eg 'lights' and every time you want the van to check the traffic lights you need to '<b>call</b>' it.")
    return message


def title_level63():
    return ugettext("Wiggle Wiggle")

def description_level63():
    message = ugettext("Can you find the repeating pattern here and create a new 'wiggle' procedure? And do the Wiggle Wiggle!")
    return build_description(title_level63(), message)

def hint_level63():
    message = ugettext("Can you see the repeating pattern in the path? The 'wiggle' consisting of a <b>turn left</b>, <b>move forwards</b>, <b>turn right</b>, <b>turn right</b>, <b>turn left</b> can be put in a <b>Define</b> block to create a procedure. Once you have named it, attach the <b>Call block with the procedure's name in the text box to execute it.")
    return message


def title_level64():
    return ugettext("Muddy Patterns with Phil")

def description_level64():
    message = ugettext("Can you spot a pattern here? Create several procedures, it can save time when writing a program. Don't forget to clearly name your procedures and then call them.")
    return build_description(title_level64(), message)

def hint_level64():
    message = ugettext("One procedure could be <b>turn left</b>, <b>turn right</b>, <b>move forwards</b>, <b>turn right</b> and <b>turn left</b>. Don't forget you can create a repeat loop in your procedures.")
    return message


def title_level65():
    return ugettext("Complicated roads.")

def description_level65():
    message = ugettext("This road might be a bit more complicated, but the procedures you could come up with are quite simple. Have a go and find out yourself!")
    return build_description(title_level65(), message)

def hint_level65():
    message = ugettext("Your first procedure could be <b>turn left</b> and <b>turn right</b> 'left-right' The second procedure could be <b>turn right</b> <b>turn left</b>, 'right-left'.")
    return message


def title_level66():
    return ugettext("Dee's snowy walk")

def description_level66():
    message = ugettext("Did you know procedures can call other procedures?")
    return build_description(title_level66(), message)

def hint_level66():
    message = ugettext("Create 2 procedures. The first one should read <b>move forwards</b>, <b>move forwards</b>, <b>turn right</b>. The second <b>move forwards</b> then <b>call</b> your first procedure")
    return message


def title_level67():
    return ugettext("Crazy Farm")

def description_level67():
    message = ugettext("This one will really test what you have learnt.")
    return build_description(title_level67(), message)

def hint_level67():
    message = ugettext("It might be easier to write the program without repeats or procedures then create 3 separate procedures from the patterns that your see.")
    return message


def title_level68():
    return ugettext("T - time")

def description_level68():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level68(), message)

def hint_level68():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level69():
    return ugettext("Duck pond dodge")

def description_level69():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level69(), message)

def hint_level69():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level70():
    return ugettext("Winter wonderland")

def description_level70():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level70(), message)

def hint_level70():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level71():
    return ugettext("Frozen challenge")

def description_level71():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level71(), message)

def hint_level71():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level72():
    return ugettext("Can Wes Find his lunch?")

def description_level72():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level72(), message)

def hint_level72():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level73():
    return ugettext("Traffic light freeze up!")

def description_level73():
    message = ugettext("Can you find the shortest algorithm?")
    return build_description(title_level73(), message)

def hint_level73():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level74():
    return ugettext("Pandemonium")

def description_level74():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level74(), message)

def hint_level74():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level75():
    return ugettext("Kirsty's maze time")

def description_level75():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level75(), message)

def hint_level75():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level76():
    return ugettext("Cannot turn left!")

def description_level76():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level76(), message)

def hint_level76():
    message = ugettext("What is that? A barn for ANTS!?")
    return message


def title_level77():
    return ugettext("G Force")

def description_level77():
    message = ugettext("Can you get the van to the house?")
    return build_description(title_level77(), message)

def hint_level77():
    message = ugettext("Heard of recursion?")
    return message


def title_level78():
    return ugettext("Wandering Phil")

def description_level78():
    message = ugettext("Can you get Phil to the house?")
    return build_description(title_level78(), message)

def hint_level78():
    message = ugettext("Repeat while not dead end... turn around...")
    return message


def title_level79():
    return ugettext("Muddy Mayhem")

def description_level79():
    message = ugettext("Can you find the shortest route?")
    return build_description(title_level79(), message)

def hint_level79():
    message = ugettext("Think back to earlier levels - what did you learn?")
    return message


def title_level80():
    return ugettext("Here's Python!")

def description_level80():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Can you tell which Python statement matches which block?")
    return build_description(title_level80(), message)

def hint_level80():
    return ""


def title_level81():
    return ugettext("Matching Blockly")

def description_level81():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Can you tell which Python statement matches which block?")
    return build_description(title_level81(), message)

def hint_level81():
    return ""


def title_level82():
    return ugettext("Don't forget to find the shortest route")

def description_level82():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Can you tell which Python statement matches which block?")
    return build_description(title_level82(), message)

def hint_level82():
    return ""


def title_level83():
    return ugettext("Repeating yourself in Python looks different")

def description_level83():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Try adding a <b>repeat</b> block and watch what happens in Python.")
    return build_description(title_level83(), message)

def hint_level83():
    return ""


def title_level84():
    return ugettext("Repeat and watch.")

def description_level84():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Try adding a <b>repeat</b> block and watch what happens in Python.")
    return build_description(title_level84(), message)

def hint_level84():
    return ""


def title_level85():
    return ugettext("Looks easy but use repeat until and see what happens?")

def description_level85():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Try adding a <b>repeat</b> until block and watch what happens in Python.")
    return build_description(title_level85(), message)

def hint_level85():
    return ""


def title_level86():
    return ugettext("See what the if blocks looks like in Python")

def description_level86():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Try adding an <b>if</b> block and watch what happens in Python.")
    return build_description(title_level86(), message)

def hint_level86():
    return ""


def title_level87():
    return ugettext("Don't forget to use else if")

def description_level87():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Try adding an <b>if</b> block and watch what happens in Python particularly with <b>else if</b> and <b>else</b> statements.")
    return build_description(title_level87(), message)

def hint_level87():
    return ""


def title_level88():
    return ugettext("See what happens when you add Traffic lights")

def description_level88():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Try adding an <b>if</b> block and watch what happens in Python particularly with <b>else if</b> and <b>else</b> statements.")
    return build_description(title_level88(), message)

def hint_level88():
    return ""


def title_level89():
    return ugettext("Watch carefully as you have another go")

def description_level89():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python programming language. Try adding an <b>if</b> block and watch what happens in Python particularly with <b>else if</b> and <b>else</b> statements.")
    return build_description(title_level89(), message)

def hint_level89():
    return ""


def title_level90():
    return ugettext("Have a go at procedures - what do they look like in Python?")

def description_level90():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python language. Try adding a procedure and watch what happens in Python.")
    return build_description(title_level90(), message)

def hint_level90():
    message = ugettext("Don't forget to name your procedure and see what happens in Python.")
    return message


def title_level91():
    return ugettext("Put it all together")

def description_level91():
    message = ugettext("As you create your program using Blockly see what it looks like in the Python language. Try adding a procedure and watch what happens in Python.")
    return build_description(title_level91(), message)

def hint_level91():
    message = ugettext("Don't forget to name your procedure and see what happens in Python.")
    return message


def title_level92():
    return ugettext("Start with the basics, <b>forward</b>, <b>left</b> and <b>right</b>")

def description_level92():
    message = ugettext("Now you are coding in Python! This is what real developers do!! To start you off, the van object has been created for you already. Under this you need to add the correct Python statements to instruct the van to drive to the destination.<br />For more information about coding in Python refer to <a href='http://www.diveintopython.net/' target='_blank'>www.diveintopython.net</a>.")
    return build_description(title_level92(), message)

def hint_level92():
    message = ugettext("""Try using the following commands:<br /><pre>v.move_forwards()<br />v.turn_left()<br />v.turn_right()</pre>""")
    return message


def title_level93():
    return ugettext("Keep it simple")

def description_level93():
    message = ugettext("Try this road. Under the van object you need to add the correct Python statements to instruct the van to drive to the destination.")
    return build_description(title_level93(), message)

def hint_level93():
    message = ugettext("""Try using the following commands:
<pre>v.move_forwards()
v.turn_left()
v.turn_right()</pre>""")
    return message.replace('\n','<br />')


def title_level94():
    return ugettext("Take the shortest route.")

def description_level94():
    message = ugettext("You're getting good at this! Can you drive the van along this road using the correct Python statements.")
    return build_description(title_level94(), message)

def hint_level94():
    message = ugettext("""Try using the following commands:
<pre>v.move_forwards()
v.turn_left()
v.turn_right()</pre>""")
    return message.replace('\n','<br />')


def title_level95():
    return ugettext("Count and repeat")

def description_level95():
    message = ugettext("Now try to use a <b>repeat</b> loop to solve this level. Look back at level 83 to see what this could look like in Python.")
    return build_description(title_level95(), message)

def hint_level95():
    message = ugettext("""To repeat some statements a set number of times you can use something like the following:
<pre>for count in range(3):
    v.turn left
    print count</pre>
The print statement will output the value of count to the console.""")
    return message.replace('\n','<br />')


def title_level96():
    return ugettext("Count and repeat is easy")

def description_level96():
    message = ugettext("Now try to use a <b>repeat loop</b> to solve this level. Look back at level 83 to see what this could look like in Python. This time you could use 2 loops, 1 for each straight piece of road.")
    return build_description(title_level96(), message)

def hint_level96():
    message = ugettext("""To repeat some statements a set number of times you can use something like the following:
<pre>for count in range(3):
    v.turn left
    print count</pre>
The print statement will output the value of count to the console.""")
    return message.replace('\n','<br />')


def title_level97():
    return ugettext("Loop the loop")

def description_level97():
    message = ugettext("Now try to use a loop within a loop, known as a 'nested loop'. Look back at level 84 to see what this could look like in Python.")
    return build_description(title_level97(), message)

def hint_level97():
    message = ugettext("""To repeat within a repeats a set number of times you can use something like the following:
<pre>for i in range(3):
    for j in range(5):
        v.turn left
        print count</pre>
The print statement will output the value of count to the console.""")
    return message.replace('\n','<br />')


def title_level98():
    return ugettext("Repeat and check")

def description_level98():
    message = ugettext("Try to solve this level by repeatedly moving until the van is at the destination. Also, check whether the van can move forward or else must turn left. Now try and write the Python code. Look back at level 86 to give you an idea of what this could look like.")
    return build_description(title_level98(), message)

def hint_level98():
    message = ugettext("""To repeat while a condition is met you can use something like the following:
<pre>while not v.at_destination():
    v.move_forwards()</pre>
To check whether a condition is met you can use something like the following:
<pre>if v.is_road_forward():
    v.move_forwards()</pre>
You may also need to use the <b>else</b> statement.""")
    return message.replace('\n','<br />')


def title_level99():
    return ugettext("Find a general solution")

def description_level99():
    message = ugettext("Now try using what you have just learnt to solve this level. You could also try using the <b>if</b>, <b>elif</b> and <b>else</b> statements. Look back at level 86 to give you an idea of what this could look like.")
    return build_description(title_level99(), message)

def hint_level99():
    message = ugettext("""To repeat while a condition is met you can use something like the following:
<pre>while not v.at_destination():
    v.move_forwards()</pre>
To check whether a condition is met you can use something like the following:
<pre>if v.is_road_forward():
    v.move_forwards()</pre>
You may also need to use the <b>elif</b> and <b>else</b> statements.""")
    return message.replace('\n','<br />')


def title_level100():
    return ugettext("Watch out for the dead end!")

def description_level100():
    message = ugettext("Practice your new Python skills on this road to get the van to the destination. Look back at level 88 for a dead end check.")
    return build_description(title_level100(), message)

def hint_level100():
    message = ugettext("Try using<br /><pre>if v.at_dead_end():</pre><br />to check if the van is at a dead end.")
    return message


def title_level101():
    return ugettext("Function or Junction?")

def description_level101():
    message = ugettext("Try defining your own procedure to solve this level. In Python procedures are generally called functions. Look back at level 90 for an example of how to define a function in Python.")
    return build_description(title_level101(), message)

def hint_level101():
    message = ugettext("""To define a function in Python you could do something like:
<pre>def my_function():
    print 'test'</pre>
To call a defined function you could do something like:
<pre>my_function()</pre>
Remember, you must define a function before you call it.""")
    return message.replace('\n','<br />')


def title_level102():
    return ugettext("Watch for the patterns")

def description_level102():
    message = ugettext("For this level try defining more than one function. Try to look for a repeating pattern to simplify your program.")
    return build_description(title_level102(), message)

def hint_level102():
    message = ugettext("""To define a function in Python you could do something like:
<pre>def my_function():
    print 'test'</pre>
To call a defined function you could do something like:
<pre>my_function()</pre>""")
    return message.replace('\n','<br />')


def title_level103():
    return ugettext("Patterns within patterns.")

def description_level103():
    message = ugettext("For this level try to define 2 or more functions where inside one function you call another function.")
    return build_description(title_level103(), message)

def hint_level103():
    message = ugettext("""To define a function that calls another function you could do something like:
<pre>def my_function():
    print 'test'

def my_other_function():
    for i in range(3):
        my_function()

my_other_function()</pre>""")
    return message.replace('\n','<br />')


def title_level104():
    return ugettext("Can you see the repeating pattern?")

def description_level104():
    message = ugettext("For this level try to define 2 or more functions where inside one function you call another function.")
    return build_description(title_level104(), message)

def hint_level104():
    message = ugettext("""To define a function that calls another function you could do something like:
<pre>def my_function():
    print 'test'

def my_other_function():
    for i in range(3):
        my_function()

my_other_function()</pre>""")
    return message.replace('\n','<br />')


def title_level105():
    return ugettext("Find the shortest route.")

def description_level105():
    message = ugettext("For this level try to implement a general algorithm. Keep the van going until it arrives at the destination, checking for traffic lights and junctions.")
    return build_description(title_level105(), message)

def hint_level105():
    message = ugettext("For this you will have to use a combination of the <b>while</b> and <b>if</b> statements.")
    return message


def title_level106():
    return ugettext("Spiral and add")

def description_level106():
    message = ugettext("For this level the van needs to travel in a spiral. The number of grid squares the van has to move keeps increasing by 1 on each turn. To do this you can have a loop that makes use of a variable to track the length of the road you need to travel after each turn.")
    return build_description(title_level106(), message)

def hint_level106():
    message = ugettext("""To use a variable to store the number of grid squares the van has to move you can do something like the following:
<pre>n = 1
while not v.at_destination():
    print n
    n += 1</pre>
Variables can be used in place of constants when calling functions. For example to repeat something n times you can do something like the following:
<pre>for count in range(n):</pre>""")
    return message.replace('\n','<br />')


def title_level107():
    return ugettext("Spiral and double")

def description_level107():
    message = ugettext("For this level try something similar to what you have just learnt. This time the straight sections of road are doubling in length after each turn.")
    return build_description(title_level107(), message)

def hint_level107():
    message = ugettext("To double the value of a variable you can do something like the following:<br /><pre>n *= 2</pre>")
    return message


def title_level108():
    return ugettext("Think less")

def description_level108():
    message = ugettext("This time the straight sections of road decrease in length by 2 after each turn.")
    return build_description(title_level108(), message)

def hint_level108():
    message = ugettext("To decrease the value of a variable by an amount you can do something like the following:<br /><pre>n -= 5</pre>")
    return message


def title_level109():
    return ugettext("Final challenge!")

def description_level109():
    message = ugettext("For the last challenge, the road straight line sections of road start off increasing by 1 after each turn and then switch to dividing by 2 with a twist!")
    return build_description(title_level109(), message)

def hint_level109():
    message = ugettext("To halve the value of a variable you can do something like the following:<br /><pre>n /= 2</pre>")
    return message
