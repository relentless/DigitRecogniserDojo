import sys

# Try and import TK Inter using version-appropriate module name.
# If it fails we need to flag the Draw function not to run.

disableDraw = False

try:

    if sys.version_info > (3, 0):
        from tkinter import *
    else:
        from Tkinter import *

except ImportError as e:
    
    importwarning = "WARNING: TK Inter graphics library not imported due to error \"{0}\"."
    importwarning = ''.join((importwarning, "\nIf you wish to use the pixel draw function, this will need to be fixed."))
    importwarning = ''.join((importwarning, "\nOther code should be unaffected."))
    print(importwarning.format(e))
    disableDraw = True


def Draw (text, pixels):
    """Function to draw the pixel data passed to it.
    TK Inter graphic library is used, simply because this is almost always available
    where any version of Python is installed.    
    Something like Python Image Library (PIL) would be more efficient but less available.
    """

    if disableDraw:
        
        print("TK Inter graphics library not available - pixels cannot be drawn.")

    else:

        print("Drawing pixels...")

        root = Tk()
        root.title(text)

        frame = Frame(root, width=500, height=500)
        frame.pack()
        
        root.mainloop()




def Test():

    print()
    Draw('Hello world, this is a test', 0)


if __name__ == '__main__':
    Test()
