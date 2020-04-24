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
    def __init__(self, initx=int(sw), inity=my_pos[0], w=1, height=[1], avatar = 'Z'):
        self.initx = int(initx)
        self.inity = int(inity)
        self.avatar = avatar
        self.pos = []
        self.w = int(w)
        if isinstance(height, list):
            if len(height) == w:
                self.height = height
            else:
                h = len(height)
                if h > w:
                    print(f"just accepting the first {w} elements of {height}")
                    for i in range(w):
                        height.pop()
                    self.height = height
                else:
                    print(f"curtailed width {w} to {h}")
                    self.w = h
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
x = int(sw)
wait_til_next = 15
while True:
    if wait_til_next<0:

        wait_til_next = random.randint(10, 30)

    wait_til_next -= 1
    next_key = w.getch()
    key = 0 if next_key == -1 else next_key
    if key==curses.KEY_RIGHT:
        curses.endwin()
        quit()
    if key==curses.KEY_UP:
        try:
            w.addch(my_pos[0], my_pos[1], " ")
            my_pos[0]-=1
        except:
            my_pos[0] = int(sh/2)
    if key==curses.KEY_DOWN:
        try:
            w.addch(my_pos[0], my_pos[1], " ")
            my_pos[0]+=1
        except:
            my_pos[0] = int(sh/2)
    for t in trexes:
        t.draw(w, x)
    try:    
        w.addch(my_pos[0], my_pos[1], my_avatar)
    except:
        my_pos[0] = int(sh/2)
    # w.addch(int(sh/2), int(sw/2), curses.ACS_PI)
    x-=1
    if (x + 4 < 0):
        x = int(sw)
    score += 1
    w.addstr(0, 7, str(score))
    for t in trexes:
        if tuple(my_pos) in t.pos:
            curses.flash()
            score=0
            w.addstr(0, 7, "    ")
            print("flashing \n")
            print(t.pos)
            
