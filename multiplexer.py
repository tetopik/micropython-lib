from machine import Pin, ADC, DAC


class MUX_74HC4067_ADC:
    '16-Channel ADC Multiplexer'
    
    def __init__(self, enable, signal, s0, s1, s2, s3):
        self.enable = Pin(enable, Pin.OUT, value=1)
        self.signal = ADC(Pin(signal))
        self.s0     = Pin(s0, Pin.OUT, value=0)
        self.s1     = Pin(s1, Pin.OUT, value=0)
        self.s2     = Pin(s2, Pin.OUT, value=0)
        self.s3     = Pin(s3, Pin.OUT, value=0)
        self.input  = [
            [0,0,0,0],
            [0,0,0,1],
            [0,0,1,0],
            [0,0,1,1],
            [0,1,0,0],
            [0,1,0,1],
            [0,1,1,0],
            [0,1,1,1],
            [1,0,0,0],
            [1,0,0,1],
            [1,0,1,0],
            [1,0,1,1],
            [1,1,0,0],
            [1,1,0,1],
            [1,1,1,0],
            [1,1,1,1],
        ]
    
    def reset_mux(self):
        self.enable.value(1)
        self.s0.value(0)
        self.s1.value(0)
        self.s2.value(0)
        self.s3.value(0)
    
    def mux(self, pin):
        self.enable.value(0)
        self.s0.value(self.input[pin][3])
        self.s1.value(self.input[pin][2])
        self.s2.value(self.input[pin][1])
        self.s3.value(self.input[pin][0])
        value = self.signal.read()
        self.reset_mux()
        return value
    

class MUX_74HC4067:
    '16-Channel Digital Input Multiplexer'
    
    def __init__(self, enable, signal, s0, s1, s2, s3, pull=1):
        self.enable = Pin(enable, Pin.OUT, value=1)
        self.signal = Pin(signal, Pin.IN, Pin.PULL_UP if pull else Pin.PULL_DOWN)
        self.s0     = Pin(s0, Pin.OUT, value=0)
        self.s1     = Pin(s1, Pin.OUT, value=0)
        self.s2     = Pin(s2, Pin.OUT, value=0)
        self.s3     = Pin(s3, Pin.OUT, value=0)
        self.input  = [
            [0,0,0,0],
            [0,0,0,1],
            [0,0,1,0],
            [0,0,1,1],
            [0,1,0,0],
            [0,1,0,1],
            [0,1,1,0],
            [0,1,1,1],
            [1,0,0,0],
            [1,0,0,1],
            [1,0,1,0],
            [1,0,1,1],
            [1,1,0,0],
            [1,1,0,1],
            [1,1,1,0],
            [1,1,1,1],
        ]
    
    def reset_mux(self):
        self.enable.value(1)
        self.s0.value(0)
        self.s1.value(0)
        self.s2.value(0)
        self.s3.value(0)
    
    def mux(self, pin):
        self.enable.value(0)
        self.s0.value(self.input[pin][3])
        self.s1.value(self.input[pin][2])
        self.s2.value(self.input[pin][1])
        self.s3.value(self.input[pin][0])
        value = self.signal.value()
        self.reset_mux()
        return value


class DEMUX_74HC4067_DAC:
    '16-Channel DAC Demultiplexer'
    
    def __init__(self, enable, signal, s0, s1, s2, s3):
        self.enable = Pin(enable, Pin.OUT, value=1)
        self.signal = DAC(Pin(signal))
        self.s0     = Pin(s0, Pin.OUT, value=0)
        self.s1     = Pin(s1, Pin.OUT, value=0)
        self.s2     = Pin(s2, Pin.OUT, value=0)
        self.s3     = Pin(s3, Pin.OUT, value=0)
        self.input  = [
            [0,0,0,0],
            [0,0,0,1],
            [0,0,1,0],
            [0,0,1,1],
            [0,1,0,0],
            [0,1,0,1],
            [0,1,1,0],
            [0,1,1,1],
            [1,0,0,0],
            [1,0,0,1],
            [1,0,1,0],
            [1,0,1,1],
            [1,1,0,0],
            [1,1,0,1],
            [1,1,1,0],
            [1,1,1,1],
        ]
    
    def reset_demux(self):
        self.enable.value(1)
        self.signal.write(0)
        self.s0.value(0)
        self.s1.value(0)
        self.s2.value(0)
        self.s3.value(0)
    
    def mux(self, pin, value):
        self.enable.value(0)
        self.s0.value(self.input[pin][3])
        self.s1.value(self.input[pin][2])
        self.s2.value(self.input[pin][1])
        self.s3.value(self.input[pin][0])
        self.signal.write(value)
        self.reset_demux()
    

class DEMUX_74HC4067:
    '16-Channel Digital Output Demultiplexer'
    
    def __init__(self, enable, signal, s0, s1, s2, s3):
        self.enable = Pin(enable, Pin.OUT, value=1)
        self.signal = Pin(signal, Pin.OUT, value=0)
        self.s0     = Pin(s0, Pin.OUT, value=0)
        self.s1     = Pin(s1, Pin.OUT, value=0)
        self.s2     = Pin(s2, Pin.OUT, value=0)
        self.s3     = Pin(s3, Pin.OUT, value=0)
        self.output = [
            [0,0,0,0],
            [0,0,0,1],
            [0,0,1,0],
            [0,0,1,1],
            [0,1,0,0],
            [0,1,0,1],
            [0,1,1,0],
            [0,1,1,1],
            [1,0,0,0],
            [1,0,0,1],
            [1,0,1,0],
            [1,0,1,1],
            [1,1,0,0],
            [1,1,0,1],
            [1,1,1,0],
            [1,1,1,1],
        ]
    
    def reset_demux(self):
        self.enable.value(1)
        self.signal.value(0)
        self.s0.value(0)
        self.s1.value(0)
        self.s2.value(0)
        self.s3.value(0)
    
    def demux(self, pin, value):
        self.enable.value(0)
        self.s0.value(self.output[pin][3])
        self.s1.value(self.output[pin][2])
        self.s2.value(self.output[pin][1])
        self.s3.value(self.output[pin][0])
        self.signal.value(value)
        self.reset_demux()