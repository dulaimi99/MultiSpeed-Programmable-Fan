from microbit import *

#define constants
vin = 3
R1 = 9960
on = 1
off = 0

while True:

    #read voltage/Calc thermistor resistance
    vout = (pin0.read_analog() /340 )
    if(button_a.is_pressed()):
        display.scroll(vout)

    R2 = (vout * R1) / (vin - vout)

    #Translate R2 into Temperature
    # And print
    temp = (-0.0024 * R2) + 98.715
    if(button_b.is_pressed()):
        display.scroll(temp)

    #Determining On or Off
    if(temp >= 75):
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)

