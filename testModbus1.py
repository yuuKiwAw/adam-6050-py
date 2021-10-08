import clr
clr.FindAssembly('/YukiAdamV.dll')
clr.AddReference('YukiAdamV')
from YukiAdamV import *

# 封装的Adam类

class AdamSet(object):
    """adam6050 channels value change
    Args:
        object ([type]): [description]
    """
    def __init__(self, ip ="192.168.0.198", port = "502", channel = "22"):
        """init values
        Args:
            ip (str, optional): adammodbus ip setting. Defaults to "192.168.0.198".
            port (str, optional): adammodbus port setting. Defaults to "502".
            channel (str, optional): adammodbus channel do from 0-5 (channel 5 total is 22). Defaults to "22".
        """
        self.ip = ip
        self.port = port
        self.channel = channel

    def setON(self):
        """channel set value 1 (on)
        """
        adam_modbus = AdamClass()
        adam_modbus.Adam6050Status(self.ip, self.port, self.channel, 1)

    def setOFF(self):
        """channel set value 2 (off)
        """
        adam_modbus = AdamClass()
        adam_modbus.Adam6050Status(self.ip, self.port, self.channel, 0)
        

def terminalSelect():
    adam = AdamSet()
    
    print("plz input set:")
    
    while True:
        c = input()
        if c == "1":
            adam.setON()
            print("set value 1 on")
        elif c == "0":
            adam.setOFF()
            print("set value 0 off")
        elif c == "exit":
            break
        else:
            print("plz input available value !!!")


def main():
    terminalSelect()


if __name__ == '__main__':
    main()
