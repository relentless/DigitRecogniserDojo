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
    TK Inter graphic widget library is used, simply because this is almost always available
    where any version of Python is installed.    
    Something like Python Image Library (PIL) would be more efficient but less available.
    """

    if disableDraw:
        
        print("TK Inter graphics library not available - pixels cannot be drawn.")

    else:

        root = Tk()
        root.title(text)

        tilesize = 10
        charactersize = 28

        def dimension():
            return tilesize * charactersize

        mainframe = Frame(root, width=dimension(), height=dimension())
        mainframe.pack()


        for pixel in enumerate(pixels):

            xOffset = (pixel[0] % charactersize) * tilesize
            yOffset = (pixel[0] / charactersize) * tilesize
            colour = getmonochromehex(pixel[1])
            
            # Draw each pixel as an individual frame widget (!)
            pixeltile = Frame(mainframe, width=tilesize, height=tilesize,
                              background=colour)
            pixeltile.place( x = xOffset, y = yOffset )
            
        root.mainloop()


def getmonochromehex(pixelvalue):
    partialhex = hex(pixelvalue).replace("0x", "")
    if len(partialhex)== 1:
        partialhex = "0" + partialhex
    return "#{0}{0}{0}".format(partialhex)
