blockly_default = '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="30" y="30"></block></xml>'

python_default = """from van import Van

my_van = Van()
"""

lvl_92 = """from van import Van

my_van = Van()

my_van.move_forwards()
my_van.turn_right()
my_van.turn_left()
my_van.move_forwards()"""

lvl_93 = """from van import Van
my_van = Van()
my_van.turn_left()
my_van.move_forwards()
my_van.move_forwards()
my_van.turn_right()
my_van.turn_right()
my_van.turn_left()
my_van.turn_right()
my_van.move_forwards()
my_van.move_forwards()
my_van.turn_left()
my_van.turn_left()
my_van.turn_right()"""

lvl_94 = """from van import Van

my_van = Van()

my_van.turn_right()
my_van.turn_left()
my_van.move_forwards()
my_van.turn_right()
my_van.turn_left()
my_van.turn_right()
my_van.turn_left()"""

lvl_95 = """from van import Van

my_van = Van()

for count in range(3):
  my_van.turn_left()
  my_van.turn_right()
  my_van.move_forwards()"""

lvl_96 = """from van import Van

my_van = Van()

for count in range(2):
    my_van.move_forwards()

my_van.turn_left()

for count in range(3):
    my_van.move_forwards()"""

lvl_97 = """from van import Van

my_van = Van()

for count in range(3):
  for forward in range(4):
    my_van.move_forwards()
  for left in range(2):
    my_van.turn_left()
  for forward in range(4):
    my_van.move_forwards()
  for right in range(2):
    my_van.turn_right()"""

lvl_98 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.is_road_forward():
    my_van.move_forwards()
  else:
    my_van.turn_left()"""

lvl_99 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.is_road_forward():
    my_van.move_forwards()
  elif my_van.is_road_left():
    my_van.turn_left()
  else:
    my_van.turn_right()"""

lvl_100 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.is_road_forward():
    my_van.move_forwards()
  elif my_van.is_road_left():
    my_van.turn_left()
  else:
    my_van.turn_right()"""

lvl_101 = """from van import Van

my_van = Van()

def main():
  right_left()
  my_van.move_forwards()
  right_left()

  for count in range(2):
    my_van.move_forwards()
  
  for count in range(2):
    right_left()
    my_van.turn_right()
  my_van.move_forwards()

def right_left():
  my_van.turn_right()
  my_van.turn_left()

main()"""

lvl_102 = """from van import Van

my_van = Van()

def main():
  left()
  right()
  my_van.move_forwards()
  my_van.turn_right()
  for count in range(2):
    my_van.move_forwards()
  my_van.turn_right()
  right()
  left()
  my_van.move_forwards()

def left():
  for count in range(2):
    my_van.turn_left()
    my_van.turn_right()

def right():
  for count in range(2):
    my_van.turn_right()
    my_van.turn_left()

main()"""

lvl_103 = """from van import Van

my_van = Van()

def main():
  big()
  my_van.move_forwards()
  big()
  forward_left()
  for count in range(2):
    forward_right()
    my_van.move_forwards()
  forward_left()

def forward_left():
  my_van.move_forwards()
  my_van.turn_left()

def forward_right():
  my_van.move_forwards()
  my_van.turn_right()

def big():
  forward_left()
  for count in range(2):
    forward_right()

main()"""

lvl_104 = """from van import Van

my_van = Van()

def main():
  big()
  for count in range(4):
    my_van.move_forwards()
  right()
  big()
  for count in range(3):
    my_van.move_forwards()
  my_van.turn_right()
  my_van.turn_left()
  left()
  my_van.move_forwards()

def left():
  for count in range(2):
    my_van.move_forwards()
    my_van.turn_left()

def right():
  for count in range(2):
    my_van.move_forwards()
    my_van.turn_right()

def big():
  left()
  right()

main()"""

lvl_105 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.at_red_traffic_light():
    my_van.wait()
  elif my_van.is_road_left():
    my_van.turn_left()
  elif my_van.is_road_forward():
    my_van.move_forwards()
  else:
    my_van.turn_right()"""

lvl_106 = """from van import Van

my_van = Van()

number = 1

while not my_van.at_destination():
  my_van.turn_right()
  for count in range(number):
    my_van.move_forwards()
  number = number + 1"""

lvl_107 = """from van import Van

my_van = Van()

number = 1
while not my_van.at_destination():
  my_van.turn_left()
  for count in range(number):
    my_van.move_forwards()
  number = number * 2"""

lvl_108 = """from van import Van

my_van = Van()

number = 6
while not my_van.at_destination():
  for count in range(number):
    my_van.move_forwards()
  my_van.turn_left()
  number = number - 2"""

lvl_109 = """from van import Van

my_van = Van()

number = 0

for count in range(4):
  my_van.turn_right()
  for forward in range(number):
    my_van.move_forwards()
  number = number + 1

my_van.turn_right()

while not my_van.at_destination():
  for count in range(number):
    my_van.move_forwards()
  my_van.turn_left()
  number = number / 2"""

lvl_113 = """from van import Van

my_van = Van()

my_van.move_forwards()
my_van.turn_right()
my_van.turn_left()
my_van.move_forwards()"""

lvl_114 = """from van import Van

my_van = Van()

my_van.turn_left()
my_van.move_forwards()
my_van.move_forwards()
my_van.turn_right()
my_van.turn_right()
my_van.turn_left()
my_van.turn_right()
my_van.move_forwards()
my_van.move_forwards()
my_van.turn_left()
my_van.turn_left()
my_van.turn_right()"""

lvl_115 = """from van import Van

my_van = Van()

my_van.turn_right()
my_van.turn_left()
my_van.move_forwards()
my_van.turn_right()
my_van.turn_left()
my_van.turn_right()
my_van.turn_left()"""

lvl_119 = """from van import Van

my_van = Van()

count = 0
while count < 3:
  my_van.turn_left()
  my_van.turn_right()
  my_van.turn_left()
  my_van.move_forwards()
  count = count + 1"""

lvl_120 = """from van import Van

my_van = Van()

count = 0
while count < 4:
  my_van.move_forwards()
  my_van.turn_left()
  my_van.turn_right()
  count = count + 1"""

lvl_121 = """from van import Van

my_van = Van()

count = 0
while count < 6:
  my_van.turn_left()
  my_van.turn_right()
  count = count + 1"""

lvl_122 = """from van import Van

my_van = Van()

count = 0
while count < 3:
  my_van.turn_left()
  my_van.turn_left()
  my_van.turn_right()
  my_van.turn_right()
  count = count + 1
  
count = 0
while count < 3:
  my_van.move_forwards()
  count = count + 1
  
count = 0
while count < 3:
  my_van.turn_right()
  my_van.turn_right()
  my_van.turn_left()
  my_van.turn_left()
  count = count + 1"""

python_lvl_16 = """from van import Van

my_van = Van()

count = 0
my_van.turn_right()
while count < 5:
  if my_van.is_animal_crossing():
    my_van.sound_horn()
  my_van.turn_left()
  my_van.turn_right()
  count = count + 1"""

python_lvl_17 = """from van import Van

my_van = Van()

count = 0
while count < 3:
  if my_van.is_road_left():
    my_van.turn_left()
    my_van.turn_right()
  my_van.move_forwards()
  count = count + 1"""

python_lvl_18 = """from van import Van

my_van = Van()

count = 0
while count < 19:
  if my_van.is_road_left():
    my_van.turn_left()
  my_van.move_forwards()
  count = count + 1"""

python_lvl_20 = """from van import Van

my_van = Van()

count = 0
while count < 8:
  if my_van.is_road_left():
    my_van.turn_left()
  else:
    my_van.turn_right()
  count = count + 1"""

python_lvl_21 = """from van import Van

my_van = Van()

count = 0
while count < 6:
  if my_van.is_road_left():
    my_van.turn_left()
    my_van.deliver()
    my_van.turn_right()
    if count == 5:
      my_van.deliver()
  else:
    my_van.move_forwards()
  count = count + 1"""

python_lvl_24 = """from van import Van

my_van = Van()

count = 0
while count < 8:
  if my_van.is_road_forward():
    my_van.move_forwards()
  elif my_van.is_road_left():
    my_van.turn_left()
  else:
    my_van.turn_right()
  count = count + 1"""

python_lvl_25 = """from van import Van

my_van = Van()

count = 0
while count < 16:
  if my_van.at_red_traffic_light():
    my_van.wait()
  elif my_van.is_road_left():
    my_van.turn_left()
  elif my_van.is_road_forward():
    my_van.move_forwards()
  else:
    my_van.turn_right()
  count = count + 1"""

python_lvl_30 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  my_van.turn_left()
  my_van.turn_right()
  my_van.turn_right()
  my_van.turn_left()"""

python_lvl_33 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.is_road_left():
    my_van.turn_left()
  else:
    my_van.turn_right()"""

python_lvl_34 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.is_road_right():
    my_van.turn_right()
  else:
    my_van.move_forwards()"""

python_lvl_38 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.is_animal_crossing():
    my_van.sound_horn()
  elif my_van.is_road_forward():
    my_van.move_forwards()
  elif my_van.at_dead_end():
    my_van.turn_around()
    my_van.turn_right()"""

python_lvl_39 = """from van import Van

my_van = Van()

while not my_van.at_destination():
  if my_van.is_animal_crossing():
    my_van.sound_horn()
  elif my_van.is_road_forward():
    my_van.move_forwards()
  else:
    my_van.turn_left()"""

python_lvl_40 = """from van import Van

my_van = Van()

for count in range(4):
  while not my_van.at_destination():
    if my_van.at_red_traffic_light():
      my_van.wait()
    elif my_van.is_road_left():
      my_van.turn_left()
    elif my_van.is_road_forward():
      my_van.move_forwards()
    elif my_van.is_road_right():
      my_van.turn_right()
    elif my_van.at_dead_end():
      my_van.turn_around()
  my_van.deliver()"""  #

python_lvl_52 = """from van import Van

my_van = Van()

def wiggle():
  my_van.turn_left()
  my_van.move_forwards()
  my_van.turn_right()
  my_van.turn_right()
  my_van.turn_left()

wiggle()
my_van.move_forwards()
wiggle()
wiggle()
my_van.turn_right()
my_van.move_forwards()
my_van.turn_right()
wiggle()"""

python_lvl_53 = """from van import Van

my_van = Van()

def large_turn():
  my_van.turn_left()
  my_van.turn_right()
  my_van.move_forwards()
  my_van.turn_right()
  my_van.turn_left()

def small_turn():
  my_van.turn_right()
  for count in range(2):
    my_van.turn_left()
  my_van.turn_right()

large_turn()
my_van.move_forwards()
large_turn()
for count2 in range(2):
  my_van.turn_right()
  my_van.move_forwards()
small_turn()
large_turn()
small_turn()"""

python_lvl_54 = """from van import Van

my_van = Van()

def left_right():
  my_van.turn_left()
  my_van.turn_right()

def right_left():
  my_van.turn_right()
  my_van.turn_left()

left_right()
my_van.move_forwards()
right_left()
for count in range(2):
  left_right()
my_van.move_forwards()
for count2 in range(2):
  my_van.move_forwards()
  my_van.turn_right()
for count3 in range(2):
  left_right()
right_left()
my_van.move_forwards()
for count4 in range(2):
  my_van.move_forwards()
  my_van.turn_left()
right_left()
left_right()
for count5 in range(2):
  my_van.move_forwards()
left_right()"""

python_lvl_55 = """from van import Van

my_van = Van()

def triple_straight_right():
  my_van.move_forwards()
  double_straight_right()

def double_straight_right():
  my_van.move_forwards()
  my_van.move_forwards()
  my_van.turn_right()

double_straight_right()
my_van.turn_left()
triple_straight_right()
double_straight_right()
triple_straight_right()
my_van.turn_left()
double_straight_right()"""

python_lvl_56 = """from van import Van

my_van = Van()

def left_right():
  my_van.turn_left()
  my_van.turn_right()

def left_forward():
  my_van.turn_left()
  my_van.move_forwards()

def double_left_right():
  for count in range(2):
    left_right()

double_left_right()
left_forward()
double_left_right()
my_van.turn_left()
left_forward()
for count2 in range(2):
  left_right()
  my_van.turn_right()
double_left_right()
double_left_right()"""

python_lvl_57 = """from van import Van

my_van = Van()

def bend():
  my_van.turn_right()
  my_van.turn_left()

bend()
my_van.move_forwards()
for count in range(2):
  bend()
my_van.move_forwards()
bend()
for count2 in range(2):
  my_van.turn_right()
for count3 in range(4):
  my_van.move_forwards()
for count4 in range(3):
  bend()"""

python_lvl_58 = """from van import Van

my_van = Van()

def bend():
  my_van.move_forwards()
  my_van.move_forwards()
  my_van.turn_right()
  my_van.turn_left()
  my_van.turn_left()

my_van.move_forwards()
my_van.turn_right()
for count in range(2):
  bend()
my_van.move_forwards()
bend()
my_van.move_forwards()
my_van.move_forwards()
my_van.turn_right()"""

solutions = {
    "python_default": python_default,
    "blockly_default": blockly_default,
    "1": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="30"><next><block type="move_forwards"></block></next></block></xml>',
    "2": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="353" y="163"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></xml>',
    "3": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="-7" y="-700"><next><block type="move_forwards"><next><block type="turn_right"></block></next></block></next></block></xml>',
    "4": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="-27" y="166"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "5": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="167" y="316"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "6": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "7": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_left"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "8": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "9": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "10": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="turn_right"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "11": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="turn_right"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "12": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="175" y="202"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "13": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="193" y="156"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "14": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="turn_right"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "15": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="-12" y="290"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="deliver"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="deliver"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "16": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="393" y="296"><next><block type="turn_right"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="deliver"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="deliver"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="deliver"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "17": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="32" y="261"><next><block type="turn_left"><next><block type="turn_left"><next><block type="deliver"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="deliver"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="deliver"><next><block type="turn_right"><next><block type="turn_right"><next><block type="deliver"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "18": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="-14" y="241"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="deliver"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="deliver"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="deliver"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="deliver"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "19": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="19" y="-641"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"></block></statement></block></next></block></xml>',
    "20": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="-40" y="258"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement></block></next></block></xml>',
    "21": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="30" y="230"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></statement></block></next></block></xml>',
    "22": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="8" y="313"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_right"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">7</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "23": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="115" y="337"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="controls_repeat"><field name="TIMES">5</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">5</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_right"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></statement></block></next></block></xml>',
    "24": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="189" y="334"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="turn_left"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_right"></block></next></block></next></block></next></block></statement><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="turn_right"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_left"></block></next></block></next></block></next></block></statement></block></next></block></next></block></next></block></xml>',
    "25": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="128" y="375"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"><next><block type="turn_left"></block></next></block></statement></block></next></block></statement><next><block type="move_forwards"></block></next></block></next></block></xml>',
    "26": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="108" y="380"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"></block></statement></block></next></block></next></block></next></block></xml>',
    "27": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="273" y="330"><next><block type="move_forwards"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"></block></next></block></statement><next><block type="controls_repeat"><field name="TIMES">5</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></statement></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "28": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="247" y="304"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_right"></block></next></block></statement><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_right"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_left"></block></statement><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "29": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="401" y="397"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="move_forwards"></block></statement></block></next></block></xml>',
    "30": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="232" y="392"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement></block></next></block></xml>',
    "31": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="197" y="377"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></statement></block></next></block></xml>',
    "32": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="339" y="438"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"></block></next></block></next></block></statement></block></next></block></xml>',
    "33": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="382" y="551"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "34": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="831" y="794"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "35": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="30" y="30"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO1"><block type="turn_right"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "36": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="599" y="546"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO1"><block type="turn_right"></block></statement><statement name="ELSE"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "37": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="599" y="546"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO1"><block type="turn_right"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "38": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="430"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2" else="1"></mutation><value name="IF0"><block type="cow_crossing"></block></value><statement name="DO0"><block type="sound_horn"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "39": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="30" y="630"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="cow_crossing"></block></value><statement name="DO0"><block type="sound_horn"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="dead_end"></block></value><statement name="DO2"><block type="turn_around"><next><block type="turn_right"></block></next></block></statement></block></statement></block></next></block></xml>',
    "40": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="493" y="569"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO0"><block type="turn_right"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "41": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="316" y="618"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "42": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="299" y="593"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></xml>',
    "43": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="408" y="548"><next><block type="controls_repeat"><field name="TIMES">22</field><statement name="DO"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement><next><block type="turn_right"><next><block type="move_forwards"></block></next></block></next></block></next></block></xml>',
    "44": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="496" y="500"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><statement name="ELSE"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "45": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="389" y="577"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><statement name="ELSE"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "46": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="327" y="771"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO2"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "47": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="530"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="cow_crossing"></block></value><statement name="DO0"><block type="sound_horn"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "48": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="415" y="678"><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="4"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO2"><block type="move_forwards"></block></statement><value name="IF3"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO3"><block type="turn_right"></block></statement><value name="IF4"><block type="dead_end"></block></value><statement name="DO4"><block type="turn_around"></block></statement></block></statement><next><block type="deliver"></block></next></block></statement></block></next></block></xml>',
    "49": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="748" y="797"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2" else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO2"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "50": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="244" y="87"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_repeat_while"><value name="condition"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="body"><block type="wait"></block></statement><next><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO1"><block type="turn_right" id="}L#lTX/D;-@2hKW 5Z#x"></block></statement><statement name="ELSE"><block type="move_forwards"></block></statement></block></next></block></statement></block></next></block></xml>',
    "51": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="458" y="256"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "52": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="423" y="249"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="turn_right"><next><block type="turn_left"></block></next></block></statement></block></next></block></next></block></xml>',
    "53": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="269" y="323"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="turn_right"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"><next><block type="turn_left"></block></next></block></statement><next><block type="move_forwards"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "54": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="541" y="307"><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"></block></statement><next><block type="turn_left"></block></next></block></next></block></statement></block></next></block></xml>',
    "55": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="469"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "56": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="597" y="442"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "57": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="350" y="576"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "58": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="509" y="420"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_left"></block></statement><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"></block></statement></block></next></block></next></block></next></block></statement></block></next></block></xml>',
    "59": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="342" y="354"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="turn_left"><next><block type="turn_around"><next><block type="turn_left"></block></next></block></next></block></statement></block></next></block></xml>',
    "60": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="150" y="284"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_right"><next><block type="turn_around"></block></next></block></next></block></statement></block></next></block></xml>',
    "61": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="192" y="415"><next><block type="call_proc"><field name="NAME">wiggle</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">wiggle</field></block></next></block></next></block></next></block><block type="declare_proc" x="193" y="620"><field name="NAME">wiggle</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"></block></statement><next><block type="turn_left"></block></next></block></next></block></next></block></statement></block></xml>',
    "62": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="310" y="456"><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="turn_right"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="312" y="886"><field name="NAME">lights</field><statement name="DO"><block type="controls_repeat_until"><value name="condition"><block type="traffic_light"><field name="CHOICE">GREEN</field></block></value><statement name="body"><block type="wait"></block></statement></block></statement></block></xml>',
    "63": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="381" y="287"><next><block type="call_proc"><field name="NAME">wiggle</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">wiggle</field><next><block type="call_proc"><field name="NAME">wiggle</field><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="call_proc"><field name="NAME">wiggle</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="383" y="628"><field name="NAME">wiggle</field><statement name="DO"><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></statement></block></xml>',
    "64": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="108" y="374"><next><block type="call_proc"><field name="NAME">large_turn</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">large_turn</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"><next><block type="move_forwards"></block></next></block></statement><next><block type="call_proc"><field name="NAME">small_turn</field><next><block type="call_proc"><field name="NAME">large_turn</field><next><block type="call_proc"><field name="NAME">small_turn</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="346" y="371"><field name="NAME">large_turn</field><statement name="DO"><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></statement></block><block type="declare_proc" x="318" y="638"><field name="NAME">small_turn</field><statement name="DO"><block type="turn_right"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_left"></block></statement><next><block type="turn_right"></block></next></block></next></block></statement></block></xml>',
    "65": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="241" y="386"><next><block type="call_proc"><field name="NAME">left_right</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">right_left</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">left_right</field></block></statement><next><block type="move_forwards"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"><next><block type="turn_right"></block></next></block></statement><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">left_right</field></block></statement><next><block type="call_proc"><field name="NAME">right_left</field><next><block type="move_forwards"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"></block></next></block></statement><next><block type="call_proc"><field name="NAME">right_left</field><next><block type="call_proc"><field name="NAME">left_right</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="call_proc"><field name="NAME">left_right</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="498" y="501"><field name="NAME">left_right</field><statement name="DO"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement></block><block type="declare_proc" x="496" y="716"><field name="NAME">right_left</field><statement name="DO"><block type="turn_right"><next><block type="turn_left"></block></next></block></statement></block></xml>',
    "66": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="110" y="-383"><next><block type="call_proc"><field name="NAME">double_straight_right</field><next><block type="turn_left"><next><block type="call_proc"><field name="NAME">triple_straight_right</field><next><block type="call_proc"><field name="NAME">double_straight_right</field><next><block type="call_proc"><field name="NAME">triple_straight_right</field><next><block type="turn_left"><next><block type="call_proc"><field name="NAME">double_straight_right</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="400" y="-383"><field name="NAME">double_straight_right</field><statement name="DO"><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"></block></next></block></next></block></statement></block><block type="declare_proc" x="400" y="-196"><field name="NAME">triple_straight_right</field><statement name="DO"><block type="move_forwards"><next><block type="call_proc"><field name="NAME">double_straight_right</field></block></next></block></statement></block></xml>',
    "67": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="416" y="454"><next><block type="call_proc"><field name="NAME">double_left_right</field><next><block type="call_proc"><field name="NAME">left_forward</field><next><block type="call_proc"><field name="NAME">double_left_right</field><next><block type="turn_left"><next><block type="call_proc"><field name="NAME">left_forward</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">left_right</field><next><block type="turn_right"></block></next></block></statement><next><block type="call_proc"><field name="NAME">double_left_right</field><next><block type="call_proc"><field name="NAME">double_left_right</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="609" y="498"><field name="NAME">double_left_right</field><statement name="DO"><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">left_right</field></block></statement></block></statement></block><block type="declare_proc" x="633" y="633"><field name="NAME">left_forward</field><statement name="DO"><block type="turn_left"><next><block type="move_forwards"></block></next></block></statement></block><block type="declare_proc" x="607" y="761"><field name="NAME">left_right</field><statement name="DO"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement></block></xml>',
    "68": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="454" y="385"><next><block type="controls_repeat_while"><value name="condition"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="body"><block type="move_forwards"></block></statement><next><block type="turn_around"><next><block type="move_forwards"></block></next></block></next></block></next></block></xml>',
    "69": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="245" y="546"><next><block type="controls_repeat_while"><value name="condition"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="body"><block type="controls_repeat_while"><value name="condition"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="body"><block type="move_forwards"></block></statement><next><block type="turn_left"></block></next></block></statement></block></next></block></xml>',
    "70": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="292" y="496"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="turn_right"><next><block type="turn_around"><next><block type="turn_right"></block></next></block></next></block></statement></block></next></block></xml>',
    "71": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="388" y="472"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="move_forwards"><next><block type="turn_right"><next><block type="controls_if"><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement></block></next></block></next></block></statement></block></next></block></xml>',
    "72": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="781" y="390"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_repeat_until"><value name="condition"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="body"><block type="move_forwards"></block></statement><next><block type="turn_right"></block></next></block></statement></block></next></block></xml>',
    "73": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="728" y="636"><next><block type="controls_repeat_until"><value name="condition"><block type="dead_end"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2" else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "74": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="100" y="100"><next><block type="call_proc"><field name="NAME">right</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">straight</field><next><block type="call_proc"><field name="NAME">straight</field><next><block type="call_proc"><field name="NAME">straight_left</field></block></next></block></next></block></statement><next><block type="call_proc"><field name="NAME">right</field><next><block type="call_proc"><field name="NAME">straight_left</field></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="350" y="100"><field name="NAME">straight</field><statement name="DO"><block type="move_forwards"></block></statement></block><block type="declare_proc" x="350" y="200"><field name="NAME">right</field><statement name="DO"><block type="turn_right"></block></statement></block><block type="declare_proc" x="350" y="300"><field name="NAME">straight_left</field><statement name="DO"><block type="call_proc"><field name="NAME">straight</field><next><block type="turn_left"></block></next></block></statement></block></xml>',
    "75": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="162" y="124"><next><block type="controls_repeat_until"><value name="condition"><block type="dead_end"></block></value><statement name="body"><block type="controls_repeat_until"><value name="condition"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="body"><block type="controls_repeat_until"><value name="condition"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="body"><block type="move_forwards"></block></statement><next><block type="turn_right"></block></next></block></statement><next><block type="turn_left"></block></next></block></statement></block></next></block></xml>',
    "76": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="399" y="647"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"><next><block type="turn_right"><next><block type="turn_right"></block></next></block></next></block></statement></block></statement></block></next></block></xml>',
    "77": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="702" y="362"><next><block type="call_proc"><field name="NAME">go</field></block></next></block><block type="declare_proc" x="702" y="482"><field name="NAME">go</field><statement name="DO"><block type="controls_if"><mutation elseif="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"><next><block type="call_proc"><field name="NAME">go</field></block></next></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"><next><block type="call_proc"><field name="NAME">go</field></block></next></block></statement></block></statement></block></xml>',
    "78": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="832" y="674"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="dead_end"></block></value></block></value><statement name="body"><block type="controls_repeat_while"><value name="condition"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="body"><block type="turn_right"></block></statement><next><block type="controls_repeat_while"><value name="condition"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="body"><block type="move_forwards"></block></statement></block></next></block></statement><next><block type="turn_around"></block></next></block></statement></block></next></block></xml>',
    "79": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="1067" y="539"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="call_proc"><field name="NAME">go</field></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="1068" y="781"><field name="NAME">go</field><statement name="DO"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"><next><block type="call_proc"><field name="NAME">go</field></block></next></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"><next><block type="call_proc"><field name="NAME">go</field></block></next></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO2"><block type="turn_right"><next><block type="call_proc"><field name="NAME">go</field></block></next></block></statement></block></statement></block></xml>',
    "80": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="918" y="191"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "81": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="918" y="152"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "82": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="801" y="131"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "83": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="607" y="268"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></statement></block></next></block></xml>',
    "84": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="425" y="290"><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"></block></statement><next><block type="turn_left"></block></next></block></next></block></statement></block></next></block></xml>',
    "85": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="185" y="273"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="move_forwards"></block></statement></block></next></block></xml>',
    "86": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="1234" y="343"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "87": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="570" y="357"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "88": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="282" y="560"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation elseif="2" else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "89": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="580" y="549"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation elseif="2" else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "90": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="416" y="242"><next><block type="call_proc"><field name="NAME">bend</field><next><block type="move_forwards"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">bend</field></block></statement><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">bend</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"></block></statement><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="call_proc"><field name="NAME">bend</field></block></statement></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="612" y="402"><field name="NAME">bend</field><statement name="DO"><block type="turn_right"><next><block type="turn_left"></block></next></block></statement></block></xml>',
    "91": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="177" y="347"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">bend</field></block></statement><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">bend</field><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="469" y="534"><field name="NAME">bend</field><statement name="DO"><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></statement></block></xml>',
    "92": lvl_92,
    "93": lvl_93,
    "94": lvl_94,
    "95": lvl_95,
    "96": lvl_96,
    "97": lvl_97,
    "98": lvl_98,
    "99": lvl_99,
    "100": lvl_100,
    "101": lvl_101,
    "102": lvl_102,
    "103": lvl_103,
    "104": lvl_104,
    "105": lvl_105,
    "106": lvl_106,
    "107": lvl_107,
    "108": lvl_108,
    "109": lvl_109,
    "1001": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "1002": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "1003": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "1004": lvl_113,
    "1005": lvl_114,
    "1006": lvl_115,
    "1007": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">4</field></block></value></block></value><statement name="body"><block type="move_forwards"><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></statement></block></next></block></next></block></xml>',
    "1008": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="184" y="109"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">4</field></block></value></block></value><statement name="body"><block type="turn_left"><next><block type="turn_right"><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></next></block></statement></block></next></block></next></block></xml>',
    "1009": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="128" y="106"><next><block type="move_forwards"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">3</field></block></value></block></value><statement name="body"><block type="turn_left"><next><block type="turn_right"><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></next></block></statement><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></xml>',
    "1010": lvl_119,
    "1011": lvl_120,
    "1012": lvl_121,
    "1013": lvl_122,
    "1014": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">8</field></block></value></block></value><statement name="body"><block type="controls_if"><value name="IF0"><block type="cow_crossing"></block></value><statement name="DO0"><block type="sound_horn"></block></statement><next><block type="move_forwards"><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></next></block></statement></block></next></block></next></block></xml>',
    "1015": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">4</field></block></value></block></value><statement name="body"><block type="controls_if"><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement><next><block type="move_forwards"><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></next></block></statement></block></next></block></next></block></xml>',
    "1016": python_lvl_16,
    "1017": python_lvl_17,
    "1018": python_lvl_18,
    "1019": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">8</field></block></value></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"><next><block type="turn_left"></block></next></block></statement><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></statement></block></next></block></next></block></xml>',
    "1020": python_lvl_20,
    "1021": python_lvl_21,
    "1022": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">12</field></block></value></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></statement></block></next></block></next></block></xml>',
    "1023": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="variables_numeric_set"><field name="NAME">count</field><field name="VALUE">0</field><next><block type="controls_repeat_while"><value name="condition"><block type="logic_compare"><field name="OP">LT</field><value name="A"><block type="variables_get"><field name="NAME">count</field></block></value><value name="B"><block type="math_number"><field name="NUM">6</field></block></value></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO0"><block type="turn_right"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><statement name="ELSE"><block type="move_forwards"></block></statement><next><block type="variables_increment"><field name="NAME">count</field><field name="VALUE">1</field></block></next></block></statement></block></next></block></next></block></xml>',
    "1024": python_lvl_24,
    "1025": python_lvl_25,
    "1026": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="185" y="273"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="move_forwards"></block></statement></block></next></block></xml>',
    "1027": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="185" y="273"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="move_forwards"></block></statement></block></next></block></xml>',
    "1028": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement></block></next></block></xml>',
    "1029": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="330"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"><next><block type="move_forwards"></block></next></block></next></block></next></block></statement></block></next></block></xml>',
    "1030": python_lvl_30,
    "1031": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="350" y="576"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "1032": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="350" y="576"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><statement name="ELSE"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "1033": python_lvl_33,
    "1034": python_lvl_34,
    "1035": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="350" y="576"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO1"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "1036": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="430"><next><block type="controls_repeat_while"><value name="condition"><block type="logic_negate"><value name="BOOL"><block type="at_destination"></block></value></block></value><statement name="body"><block type="controls_if"><mutation elseif="2" else="1"></mutation><value name="IF0"><block type="cow_crossing"></block></value><statement name="DO0"><block type="sound_horn"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "1037": lvl_100,
    "1038": python_lvl_38,
    "1039": python_lvl_39,
    "1040": python_lvl_40,
    "1041": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="607" y="268"><next><block type="controls_repeat"><field name="TIMES">3</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></statement></block></next></block></xml>',
    "1042": lvl_95,
    "1043": lvl_96,
    "1044": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="425" y="290"><next><block type="controls_repeat"><field name="TIMES">4</field><statement name="DO"><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"></block></statement><next><block type="turn_left"></block></next></block></next></block></statement></block></next></block></xml>',
    "1045": lvl_97,
    "1046": lvl_106,
    "1047": lvl_107,
    "1048": lvl_108,
    "1049": lvl_109,
    "1050": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="192" y="415"><next><block type="call_proc"><field name="NAME">wiggle</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">wiggle</field></block></next></block></next></block></next></block><block type="declare_proc" x="193" y="620"><field name="NAME">wiggle</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"></block></statement><next><block type="turn_left"></block></next></block></next></block></next></block></statement></block></xml>',
    "1051": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="310" y="456"><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="move_forwards"><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="turn_right"><next><block type="call_proc"><field name="NAME">lights</field><next><block type="move_forwards"><next><block type="move_forwards"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="312" y="886"><field name="NAME">lights</field><statement name="DO"><block type="controls_repeat_until"><value name="condition"><block type="traffic_light"><field name="CHOICE">GREEN</field></block></value><statement name="body"><block type="wait"></block></statement></block></statement></block></xml>',
    "1052": python_lvl_52,
    "1053": python_lvl_53,
    "1054": python_lvl_54,
    "1055": python_lvl_55,
    "1056": python_lvl_56,
    "1057": python_lvl_57,
    "1058": python_lvl_58,
    "1059": lvl_101,
    "1060": lvl_102,
}
