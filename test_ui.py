'''
Created on Apr 1, 2017

@author: williamkhaine
'''

"""
traffic
restaurants
population density
olympic events
    -API Share on social media
 
"""

CONSTANT_FONT   = ("Helvetica", 12)
INITIAL_WIDTH   = 500
INITIAL_HEIGHT  = 500
CONSTANT_BKG    = "#000000"

import tkinter


class UserInterface:
    def __init__(self):
        # INITIALIZE BASE WINDOW
        self._base_win = tkinter.Tk()
        self._base_win.title('Olympic Tracker')
        
        # INITIALIZE BASE CONSTANTS
        self._width = INITIAL_WIDTH
        self._height = INITIAL_HEIGHT
        
        # INITIALIZE CANVAS
        self._canvas = tkinter.Canvas(master = self._base_win, width = INITIAL_WIDTH, 
                                      height = INITIAL_HEIGHT, background = CONSTANT_BKG)
        self._canvas.grid(row = 0, column = 0,
                          sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._canvas_being_resized)

    def _canvas_being_resized(self, event: tkinter.Event):
        self._width = self._canvas.winfo_width()
        self._height = self._canvas.winfo_height()
        self._canvas.delete(tkinter.ALL)
        self._draw_everything()
        
    def _draw_everything(self):
        pass
    
    def run(self):
        self._base_win.mainloop()    

def run_user_interface():
    u = UserInterface()
    u.run()
    
#     DICT EXAMPLE
#     d = {"key1":"value1", 1:["Harambe", "Pepe"]}
#     print(d["key1"]) 
#     print(d.keys())
#     print(d.values())
#     print(d.items())

if __name__ == "__main__": 
    run_user_interface() 