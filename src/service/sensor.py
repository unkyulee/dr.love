import board
import analogio

#
import service.context as context 

#
class Sensor:
    num_samples = 5000

    def setup(self):
        print("Sensor Setup")
         # Initialize ADC pins
        self.ADC0 = analogio.AnalogIn(board.GP26) 
        self.ADC1 = analogio.AnalogIn(board.GP27)  
    
    
    def loop(self):
        # save ADC values to context
        data = context.get()
        
        data["A"]["value"] = self.read_adc(self.ADC0)
        data["B"]["value"] = self.read_adc(self.ADC1)
               
    
    def read_adc(self, adc):
        total = 0
        for _ in range(self.num_samples):
            total += adc.value
        average_value = total / self.num_samples
        
        # below 300 consider it as 0
        if(average_value < 300.0):
            average_value = 0
                 
        return average_value

