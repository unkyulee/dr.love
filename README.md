# Dr. Love: Measures your love

Dr. Love: is the creepy gadget to test if your partner is in love with you or just kind of meh. Simply place your fingers on Dr. Love, and it will reveal if neither of you, both of you, or just one of you is smitten. Thankfully, it won’t spill the beans on which one of you is the lovesick puppy.

# Usecase

Flashback to my high school days, my first encounter with a girl had me avoiding eye contact and fidgeting like I had ants in my pants. If only Dr. Love had existed back then! I could have saved myself the embarrassment, tested our "connection" and perhaps redirected my energy into mastering Circuit Python instead.

Dr. Love is the perfect ice-unbreaker. Picture this: youre on a blind date, and your date looks like she’d rather be anywhere else. She’s leaning back, legs angled towards the nearest exit. Even your best joke, rehearsed for hours, barely gets a polite smile. Shes probably a Star Wars fan, and you're all about Lord of the Rings. Oh, the tragedy!

Here comes the Dr. Love. You place it on the table as a last-ditch effort. Suddenly, shes intrigued. For the first time in hours, her hands cross the table, and she asks, "What’s this?" in a curious tone. With a suave smile, you reply, "Want to give it a try?"

A little creeped out, she hesitates. "What if it says we’re in love? Do we have to get married and have kids? Share school drop-off duties every morning? Is there a way to avoid this creepy nerd but still keep Dr. Love?"

Absolutely! Here’s the link to get your own Dr. Love.


# Some Techincal Details

Galvanic Skin Response (GSR): This is a fancy way of saying that your skin changes its electrical properties when you sweat. When you get nervous or excited, your body sweats a tiny bit, even if you don’t notice it. This sweat changes how easily electricity can pass through your skin.

When people are nervous, it can make them sweat just a bit more than usual. Especially if you are in testing whether you are in love or not with someone that you care. You or the other will get nervous.  

Dr. Love measures this change in sweat using GSR. It has sensors that are placed on your fingers or hand, which detect the slight increase in sweat and thus the change in electrical conductivity of your skin. Dr. Love uses the GSR data to guess if someone is in love. If the machine notices a spike in sweating when a person is in front of someone that you love, it suggests that the person might be in love.

Well... if you are in a season'd relationship, then you might not sweat. So, that is why, phone number of a divorce lawyer is on the cover as well.

# Build Guide

This is a DIY project and contains build guides. Some soldering must be done. Also, some wrong wiring can cause a hazardous fire and burn down your beloved house. But I am sure y'all like to have one Dr. Love on your hand. So, why not give it a try. 

## Step 1. What to prepare

Micro controller used here is called, "RP2040-LCD-0.96". This is Raspberry Pi Pico micro controller with 0.96 inch display attached to it. You can find the item by searching with "RP2040-LCD-0.96"

* RP2040-LCD-0.96

You can use typical lithium battery. That has 3.6 ~ 3.7 V nominal voltage.
I have used LIR2032 coin cell sized lithium battery and the same sized holder in order to place inside the enclosure.

You can find the item by searching with the keyword: 

* LIR2032 - for the battery 
* CR2032 holder - for the battery holder
* JST 1.25mm male connector

You need nickel strips to make a place for the fingers. You could search for nickel strips. Then you would find bunch of 8 mm wide strips. 

* Nickel Strips 8 mm wide. Any thickness is fine, as long as you can bend them at will

Some other components

* 2k ohm resistor x 2
* Slide switch dimension of 20 mm x 6 mm
* M2 threaded inserts and screws x 4
* M2.5 machine screws and nuts


## Step 2. Soler nickel plates with wires

Cut them nicely, around 3 cm long. Four of them are required. Peel off 2 cm of the wire. Wrap around the nick plate and put some solering paste, then solder it on.


## Step 3. Solder the battery contact and the slide switch

Cut the JST connector wires to fit in the enclosure. 

* JST connector GND to Battery holder GND
* JST connector V+ to Slide switch
* Battery holder V+ to Slide switch

This setup is not the best because the rp2040 board needs to be powered on while the charge is on going. Since the battery charge controller is on the board. So, I don't see other options. If anyone know any better setup. Please let me know.


## Step 4. Solder to the rp2040 board

It is going to one resister and some wiring to be done. Make sure to solder first then check with the image below, so that when you mess up. You will have even more mess to clean up.

* ADC pin is pulled down to GND via 2k resistor. 
* ADC pin is connected to one of nickel contact. 
* 3.3 V is connected to the other nickel contact.


## Step 5. Assemble

* Insert the threaded inserts on the bottom enclosure. 
* Place the sliding switch and hold it with the M2.5 machine screw and nuts
* Glue the battery holder 
* Use some double sided adhesives to place the rp2040 board in place
* Install the nickel plates on the corresponding location
* Close the lid and lock it with the m2 screws


# Conclusion

This project was initiated by the business card challenge on Hackaday. Hackaday is really an intimidating place where things posted there are mostly green and yellow. People there speaks in a languages of some series alphabets combined with numbers mostly.

I have always find interests and inspirations from hackaday posts. It feels like people take things seriously to a level that is unimaginable.  

https://hackaday.io/contest/195949-2024-business-card-contest

This place is probably the least appropriate place to put a relationship related stuff. But I am going to try anyways. 


# Online Shop 

Not sure if this item would ever sell. But I have put it in my shop anyways. Because it looks cute.

https://www.tindie.com/stores/unkyulee/