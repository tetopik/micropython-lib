from machine import Pin
from time import ticks_ms, ticks_diff


class MultiplePB:
    "Make multiple click function on a single PB"
        
    def __init__(self, pin, pull, sprint=0):
        self.pin = pin
        self.pull = pull
        self.print = sprint
        self.is_pressed = 0
        self.pressed = 0
        self.pressed_time = 0
        self.pressed_trigger = 1000
        self.trig = 0
        self.trig_time = 0
        self.trig_hold = 50
        self.wait_hold = 250
        self.firstclick = 0
        self.output = 0
        
    def state(self):
        
        if self.pull==1:
            pb = Pin(self.pin, Pin.IN, Pin.PULL_UP)
            self.is_pressed = not pb.value()
        else:
            pb = Pin(self.pin, Pin.IN, Pin.PULL_DOWN)
            self.is_pressed = pb.value()
        
        if self.is_pressed and not self.pressed:
            self.pressed = 1
            self.pressed_time = ticks_ms()
            if self.print: print('Button %s Pressed!' % self)
        
        if not self.is_pressed and self.pressed:
            self.pressed = 0
            interval = ticks_diff(ticks_ms(),self.pressed_time)
            if interval >= self.pressed_trigger:
                self.output = 3
            else:
                if self.firstclick == 1:
                    self.output = 2
                    self.firstclick = 0
                else:
                    self.firstclick = 1
                    self.wait_secondclick = ticks_ms()
        
        if self.firstclick:
            if ticks_diff(ticks_ms(),self.wait_secondclick) >= self.wait_hold:
                self.firstclick = 0
                self.output = 1
                
        if (self.output>0) and (self.trig==0):
            self.trig = 1
            self.trig_time = ticks_ms()
            if self.print: print('Button %s State = %d' % (self, self.output))
        
        if (self.output>0) and (self.trig==1):
            if (ticks_diff(ticks_ms(),self.trig_time)) >= self.trig_hold:
                self.trig = 0
                self.output = 0
                if self.print: print('Button %s State = %d\n' % (self, self.output))
        
        return self.output
    
    
