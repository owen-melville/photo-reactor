from photo_reactor import PhotoReactor
from machine import Pin, SoftI2C, I2C
import time

try:
    pr = PhotoReactor()
    #Add fans
    pr.add_fan(SoftI2C(scl=Pin(9),sda=Pin(8)))
    pr.add_fan(SoftI2C(scl=Pin(7),sda=Pin(6)))
    #Add leds
    pr.add_led(gpio_pin=0)
    pr.add_led(gpio_pin=1)

    #duty_cycle = pr.initialize_fan(fan_index=0,starting_duty_cycle=30) #Initialize fan 0 with duty cycle = 30 
    #duty_cycle = pr.set_fan_rpm(fan_index=0,target_rpm=600,duty_cycle=duty_cycle) #Move fan 0 to 600 rpm
    pr.turn_on_LED(0)
    pr.turn_on_LED(1)
    pr.hold_fan_rpm(fan_index=0,target_rpm=600,target_time=120,duty_cycle=duty_cycle) #Hold the fan at 600 rpm as best as possible for 120 s
    pr.turn_off_fan(0)
    pr.turn_off_LED(0)
    pr.turn_off_LED(1)
except KeyboardInterrupt:
    pr.turn_off_fan(0)
    pr.turn_off_LED(0)
    pr.turn_off_LED(1)
