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

trexes = []

class trex:
    def __init__(self, initx=sw/2, inity=my_pos[0], w=1, height=[1], avatar = 'Z'):
        self.initx = int(initx)
        self.inity = int(inity)
        self.avatar = avatar
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
    def draw(self, window, x=sw/2, y=my_pos[0], avatar = None):
        if avatar ==None:
            avatar = self.avatar
        for i in range(self.w):
            for y_rn in range(self.height[i]):
                try:
                    w.addch(i+x+1, y_rn+y, ' ')
                except:
                    pass
            x += 1
            
        for i in range(self.w):
            for y_rn in range(self.height[i]):
                try:
                    w.addch(i+x, y_rn+y, avatar)
                except:
                    pass
            x += 1
            
trexes.append(trex(avatar=curses.ACS_PI))
for t in trexes:
    t.draw(w)
key=0
x = sw/2
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    if key==curses.KEY_RIGHT:
        curses.endwin()
        quit()
    for t in trexes:
        t.draw(w, x)
    x-=1
