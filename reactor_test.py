import photo_reactor as pr

try:
    pr.initialize_pins()
    duty_cycle = pr.initialize_fan(fan_index=0,duty_cycle=30) #Initialize fan 0 with duty cycle = 30 
    duty_cycle = pr.set_fan_rpm(fan_index=0,target_rpm=600,duty_cycle=duty_cycle) #Move fan 0 to 600 rpm
    pr.turn_on_LED(0)
    pr.turn_on_LED(1)
    pr.hold_fan_rpm(fan_index=0,target_rpm=600,target_time=120,duty_cycle=duty_cycle) #Hold the fan at 600 rpm as best as possible for 120 s
    pr.turn_off_fan()
    pr.turn_off_LED(0)
    pr.turn_off_LED(1)
except KeyboardInterrupt:
    pr.turn_off_fan()
    pr.turn_off_LED(0)
    pr.turn_off_LED(1)