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

for i in range(3):
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

def right_left():
  my_van.turn_right()
  my_van.turn_left()

right_left()
my_van.move_forwards()
right_left()
for count in range(2):
  my_van.move_forwards()
for count in range(2):
  right_left()
  my_van.turn_right()
my_van.move_forwards()"""

lvl_102 = """from van import Van

my_van = Van()

def left():
  for count in range(2):
    my_van.turn_left()
    my_van.turn_right()

def right():
  for count in range(2):
    my_van.turn_right()
    my_van.turn_left()

left()
right()
my_van.move_forwards()
my_van.turn_right()
for count in range(2):
  my_van.move_forwards()
my_van.turn_right()
right()
left()
my_van.move_forwards()"""

lvl_103 = """from van import Van

my_van = Van()

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

big()
my_van.move_forwards()
big()
forward_left()
for count in range(2):
  forward_right()
  my_van.move_forwards()
forward_left()"""

lvl_104 = """from van import Van

my_van = Van()

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
my_van.move_forwards()"""

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

n = 1

while not my_van.at_destination():
  my_van.turn_right()
  for count in range(n):
    my_van.move_forwards()
  n = n + 1"""

lvl_107 = """from van import Van

my_van = Van()

n = 1
while not my_van.at_destination():
  my_van.turn_left()
  for count in range(n):
    my_van.move_forwards()
  n = n * 2"""

lvl_108 = """from van import Van

my_van = Van()

n = 6
while not my_van.at_destination():
  for i in range(n):
    my_van.move_forwards()
  my_van.turn_left()
  n = n - 2"""

lvl_109 = """from van import Van

my_van = Van()

n = 0

for count in range(4):
  my_van.turn_right()
  for forward in range(n):
    my_van.move_forwards()
  n = n + 1

my_van.turn_right()

while not my_van.at_destination():
  for count in range(n):
    my_van.move_forwards()
  my_van.turn_left()
  n = n / 2"""

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
    "14": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="130"><next><block type="turn_right"><next><block type="turn_left"><next><block type="move_forwards"><next><block type="turn_right"><next><block type="turn_left"><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="turn_left" x="-115" y="192"></block></xml>',
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
    "36": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="599" y="546"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO1"><block type="turn_right"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "37": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="599" y="546"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO1"><block type="turn_right"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "38": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="599" y="546"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO0"><block type="move_forwards"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO1"><block type="turn_right"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
    "39": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="617" y="734"><next><block type="controls_repeat"><field name="TIMES">6</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_left"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="move_forwards"></block></statement></block></next></block></next></block></next></block></xml>',
    "40": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="493" y="569"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO0"><block type="turn_right"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "41": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="316" y="618"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "42": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="299" y="593"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="turn_right"><next><block type="turn_left"></block></next></block></next></block></next></block></xml>',
    "43": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="408" y="548"><next><block type="controls_repeat"><field name="TIMES">20</field><statement name="DO"><block type="controls_if"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO0"><block type="turn_left"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><statement name="ELSE"><block type="turn_right"></block></statement></block></statement><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="turn_right"><next><block type="move_forwards"></block></next></block></statement></block></next></block></next></block></xml>',
    "44": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="496" y="500"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><statement name="ELSE"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "45": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="389" y="577"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation else="1"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><statement name="ELSE"><block type="move_forwards"></block></statement></block></statement></block></next></block></xml>',
    "46": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="327" y="771"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">RIGHT</field></block></value><statement name="DO2"><block type="turn_right"></block></statement></block></statement></block></next></block></xml>',
    "47": '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="413" y="-296"><next><block type="controls_repeat_until"><value name="condition"><block type="at_destination"></block></value><statement name="body"><block type="controls_if"><mutation elseif="2"></mutation><value name="IF0"><block type="traffic_light"><field name="CHOICE">RED</field></block></value><statement name="DO0"><block type="wait"></block></statement><value name="IF1"><block type="road_exists"><field name="CHOICE">FORWARD</field></block></value><statement name="DO1"><block type="move_forwards"></block></statement><value name="IF2"><block type="road_exists"><field name="CHOICE">LEFT</field></block></value><statement name="DO2"><block type="turn_left"></block></statement></block></statement></block></next></block></xml>',
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
}
