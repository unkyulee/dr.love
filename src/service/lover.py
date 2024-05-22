import time

#
import service.context as context 


# calibrate for x seconds
calibrate = 4

# measure for x seconds
measure = 10

# result display timer
result = 15

#
class Lover:   
    #
    def setup(self):        
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
        context.get()["DISPLAY"]["screen"] = context.S_WELCOME
    #
    def loop(self): 
        # perform actions
        self.actions[context.get()["DISPLAY"]["screen"]]()
    #
    def welcome(self):      
        # Detect to see if both pads are active
        status = context.get()
        #
        if status["A"]["value"] > 0 and status["B"]["value"] > 0:
            # save the timer
            self.calibration_timer = time.monotonic()            
            # Move to the calibration status
            status["DISPLAY"]["screen"] = context.S_CALIBRATION
    #
    def calibration(self):       
        #
        status = context.get()
        
        # check if the timer has passed 
        if time.monotonic() - self.calibration_timer > calibrate:
            # waited enough move on
            # set a little bit lower value so that it increases the chance of getting both in love
            status["LOVER"]["A"]["start"] = status["A"]["value"] * 0.98
            status["LOVER"]["B"]["start"] = status["B"]["value"] * 0.98
            print("A ", status["A"]["value"], " B ", status["B"]["value"])                        
            # save the timer
            self.measuring_timer = time.monotonic()            
            # Move to the calibration status
            status["DISPLAY"]["screen"] = context.S_MEASURING
    #
    def measuring(self):    
        #
        status = context.get()        
        # check if the timer has passed 
        if time.monotonic() - self.measuring_timer > measure:
            # let's see if the value went up or down
            status["LOVER"]["A"]["end"] = status["A"]["value"] 
            status["LOVER"]["B"]["end"] = status["B"]["value"]             
            #
            diffA = status["LOVER"]["A"]["end"] - status["LOVER"]["A"]["start"] 
            diffB = status["LOVER"]["B"]["end"] - status["LOVER"]["B"]["start"]
            #
            print("A ", status["LOVER"]["A"]["start"], status["LOVER"]["A"]["end"], diffA, " B ", status["LOVER"]["B"]["start"], status["LOVER"]["B"]["end"], diffB)
            # save the timer
            self.result_timer = time.monotonic()            
            # if
            if diffA > 0 and diffB > 0:
                status["DISPLAY"]["screen"] = context.S_LOVE
            elif diffA < 0 and diffB < 0:
                status["DISPLAY"]["screen"] = context.S_SORRY
            else:
                status["DISPLAY"]["screen"] = context.S_ONE
    #
    def love(self):
        # check if the timer has passed 
        if time.monotonic() - self.result_timer > result:
            context.get()["DISPLAY"]["screen"] = context.S_WELCOME
    #
    def one(self):
        # check if the timer has passed 
        if time.monotonic() - self.result_timer > result:
            context.get()["DISPLAY"]["screen"] = context.S_WELCOME
    #
    def sorry(self):
        # check if the timer has passed 
        if time.monotonic() - self.result_timer > result:
            context.get()["DISPLAY"]["screen"] = context.S_WELCOME
        
