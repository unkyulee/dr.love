import board
import time
import busio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

import gc
import gifio

#
import service.context as context 

#
class Display:
    #
    # Initialize Display
    #
    def setup(self):
        print("Display Setup")
        
        # Pins
        displayio.release_displays()
        
        self.clk = board.GP10
        self.mosi = board.GP11
        self.rst = board.GP12
        self.dc = board.GP8
        self.cs = board.GP9
        self.bl = board.GP25
        
        self.width = 160
        self.height = 80
        
        self.spi = busio.SPI(clock=self.clk, MOSI=self.mosi)
        self.display_bus = displayio.FourWire(self.spi, command=self.dc, chip_select=self.cs, reset=self.rst)
        self.display = ST7735R(
            self.display_bus, 
            width=self.width, 
            height=self.height,
            rotation=270,
            rowstart=1,
            colstart=26,
            invert=True,
            backlight_pin=self.bl)
        
    
        #
        self.actions = {
            context.S_WELCOME: self.welcome,
            context.S_CALIBRATION: self.calibration,
            context.S_MEASURING: self.measuring,
            context.S_LOVE: self.love,
            context.S_SORRY: self.sorry,
            context.S_ONE: self.one
        }
        
        #
        self.screen = context.get()["DISPLAY"]["screen"]
        self.stop = False
        self.odg = None

    #
    #
    #
    def loop(self): 
        # verify the status
        self.verify()
      
        # perform actions
        self.actions[context.get()["DISPLAY"]["screen"]]()
               
        pass
    
    def verify(self):
        # detect if the screen has changed
        curr_screen = context.get()["DISPLAY"]["screen"]
        
        # stop gif
        if curr_screen != self.screen:
            self.stop = True
            self.screen = curr_screen
    
    
    def gif(self, path):
        
        # Check Stop Flag
        if self.stop: 
            # Clean up memory
            self.odg.deinit()
            self.odg = None
            gc.collect()
            
            # Unflag
            self.stop = False

        # Load GIF
        if self.odg == None:
            # loading GIF
            self.odg = gifio.OnDiskGif(path)
            
            # Load GIF
            face = displayio.TileGrid(
                self.odg.bitmap,
                pixel_shader=displayio.ColorConverter
                (input_colorspace=displayio.Colorspace.RGB565_SWAPPED))
            
            # Display the GIF
            splash = displayio.Group()
            splash.append(face)
            self.display.root_group = splash
            self.display.refresh()
            
            # Register Start Time
            self.gif_next = time.monotonic() + self.odg.next_frame()            
        
        # Play the GIF next frame
        if time.monotonic() - self.gif_next > 0: 
            self.gif_next = time.monotonic() + self.odg.next_frame()
        
        
        
        
    def welcome(self):
        self.gif("/gif/welcome.gif")           
    
    def calibration(self):
        self.gif("/gif/calibration.gif")
    
    def measuring(self):
        self.gif("/gif/measuring.gif")
    
    def love(self):
        self.gif("/gif/love.gif")
    
    def one(self):
        self.gif("/gif/one.gif")
    
    def sorry(self):
        self.gif("/gif/sorry.gif")
