import serial
import threading
from queue import Queue

DEFAULT_BAUDRATE = 921600
DEFAULT_BYTESIZE = 8
DEFAULT_STOPBITS = 1
DEFAULT_PARITY = 'N'



class UWB(object):
    def __init__(self, port, buadrate=DEFAULT_BAUDRATE, bytesize=DEFAULT_BYTESIZE,
                stopbits=DEFAULT_STOPBITS):
        def __serialthread():
            while self.serialthread_alive:

                if self.serial.in_waiting:
                    data = self.serial.read(self.serial.in_waiting)
                    
                    self.binbuffer.extend(data)
                else:
                    pass
        
        self.serial =serial.Serial(port, buadrate, bytesize, timeout=None)
        self.serialthread_alive = True

        self.module_data_fifo = Queue()
        self.binbuffer = []

        self.serialthread = threading.Thread(target=__serialthread)
        self.serialthread.start()

    
    def get_data(self, timeout=None):

        data = self.binbuffer.pop()
        #data = self.module_data_fifo.get(block=True, timeout=timeout)
        return data

    def get_data_size(self):
        return self.module_data_fifo.qsize()
    
    def close(self):
        self.serialthread_alive = False
        self.serial.close()
    

def main():
    port = '/dev/tty.SLAB_USBtoUART'
    uwb = UWB(port)
    while True:
        print(uwb.get_data())
    uwb.close()


if __name__ == '__main__':
    main()