#
import time
#
import service.context as context 
# calibrate for x seconds
calibrate = 10
# measure for x seconds
measure = 10
# result display timer
result = 15
#
class Sleep:
    #
    def setup(self):        
        # after 1 minute of inactivity goes into sleep mode
        self.timer_end = time.monotonic() + 60
        #
        self.brightness = context.get()['DISPLAY']['brightness']
    #
    def loop(self): 
        #
        status = context.get()
        # check if the device is active
        if status["A"]["value"] > 0.0 or status["B"]["value"] > 0.0:
            # if active then refresh the sleep timer limit 
            self.timer_end = time.monotonic() + 60
        
        # check if the sleep timer has reached
        if self.timer_end < time.monotonic():
            status['DISPLAY']['brightness'] = 0.0
        else:
            status['DISPLAY']['brightness'] = self.brightness
