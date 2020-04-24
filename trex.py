import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
# w.flash()
w.keypad(1)
w.timeout(100)
my_pos = [int(sh/2), int(sw/7)]
my_avatar = "M"
trexes = []
w.addstr(0, 0, "SCORE")
class trex:
    def __init__(self, x=int(sw), inity=my_pos[0], w=1, height=[1], avatar = 'Z'):
        self.x = int(x)
        self.inity = int(inity)
        self.avatar = avatar
        self.pos = []
        self.w = int(w)
        if isinstance(height, list):
            if len(height) == w:
                self.height = height
            else:
                self.w = len(height)
                self.height = height
        elif isinstance(height, int) or isinstance(height, float):
            self.height = [int(height)]*int(w)
        else:
            print("That's blasphemy, let the height be 1")
            self.height = [1]*int(w)
    def draw(self, window, x=int(sw/2), y=my_pos[0], avatar = None):
        if avatar ==None:
            avatar = self.avatar
        for i in range(self.w):
            for y_rn in range(self.height[i]):
                try:
                    w.addch(y-y_rn, i+x+1, ' ')
                    # print(f"{i+x+1} {y_rn+y}")
                    self.pos.clear()
                except:
                    # print(f"gosh {i+x+1} > {sw} {y_rn+y} > {sh} ")
                    pass
            
        for i in range(self.w):
            for y_rn in range(self.height[i]):
                try:
                    w.addch(y-y_rn, i+x, avatar)
                    self.pos.append((y-y_rn, i+x))
                    
                except:
                    # print("happy?")
                    pass
                    
trexes.append(trex(avatar=curses.ACS_PI, height = [1,2,3,4], w=4))
w.addstr(0, 10, "press right arrow to exit") 
key=0
score = 0
x = 0
steps = [6, 1, 0, 0, 0,0, 0, -1, -5, -1]
steplength = len(steps)
stepcounter = 0
blocked = False
wait_til_next = 15
while True:
    if wait_til_next<0:

        trexes.append(trex(w=random.randint(1, 4), height = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]))
        wait_til_next = random.randint(10, 45)

    wait_til_next -= 1
    next_key = w.getch()
    key = 0 if next_key == -1 else next_key
    if key==curses.KEY_RIGHT:
        curses.endwin()
        quit()
    if not blocked:
        if key==curses.KEY_UP:
            blocked = True
            stepcounter = 0
    else:
        if (stepcounter == steplength):
            blocked = False
            stepcounter = 0
        else:
            w.addch(my_pos[0], my_pos[1], " ")
            my_pos[0]-= steps[stepcounter]
            print(steps[stepcounter], my_pos[0])
            stepcounter += 1
    # if key==curses.KEY_DOWN:
    #     try:
    #         w.addch(my_pos[0], my_pos[1], " ")
    #         my_pos[0]+=1
    #     except:
    #         my_pos[0] = int(sh/2)
    for t in trexes:
        if (t.x+t.w<0):
            trexes.remove(t)
        t.draw(w, t.x)
        t.x -= 1
    try:    
        w.addch(my_pos[0], my_pos[1], my_avatar)
    except:
        my_pos[0] = int(sh/2)
    # w.addch(int(sh/2), int(sw/2), curses.ACS_PI)
    
    score += 1
    w.addstr(0, 7, str(score))
    for t in trexes:
        if tuple(my_pos) in t.pos:
            curses.flash()
            score=0
            w.addstr(0, 7, "    ")
            print("flashing \n")
            print(t.pos)
            
