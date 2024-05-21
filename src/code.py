import asyncio
import time

#
from service.sensor import Sensor
from service.display import Display
from service.lover import Lover

# Reading Sensors
async def sensor_loop():
    # loop interval
    interval = 1
    
    # Sensor Setup
    sensor = Sensor()
    sensor.setup()
    
    # Task Loop
    while True:
        # Loop Measure Interval - Begin
        start_time = time.monotonic()
        
        # Code
        sensor.loop()
        
        # Loop Measure Interval - End
        elapsed_time = time.monotonic() - start_time
        sleep_time = max(0, interval - elapsed_time)
        await asyncio.sleep(sleep_time)


# Display Loop
async def display_loop():
    # display loop interval
    interval = 0.5
    
    # Display Setup
    display = Display()
    display.setup()
   
    # Task Loop
    while True:
        # Loop Measure Interval - Begin
        start_time = time.monotonic()
        
        # Code
        display.loop()
        
        # Loop Measure Interval - End
        elapsed_time = time.monotonic() - start_time
        sleep_time = max(0, interval - elapsed_time)
        await asyncio.sleep(sleep_time)


# Lover Loop
async def lover_loop():
    # display loop interval
    interval = 0.5
   
    # Lover Logic
    lover = Lover()
    lover.setup()
    
    # Task Loop
    while True:
        # Loop Measure Interval - Begin
        start_time = time.monotonic()
        
        # Code
        lover.loop()
        
        # Loop Measure Interval - End
        elapsed_time = time.monotonic() - start_time
        sleep_time = max(0, interval - elapsed_time)
        await asyncio.sleep(sleep_time)
        

# Main function to run tasks concurrently
async def main():
    task1 = asyncio.create_task(sensor_loop())
    task2 = asyncio.create_task(display_loop())
    task3 = asyncio.create_task(lover_loop())

    await asyncio.gather(task1, task2, task3)

# Run the main function
asyncio.run(main())
