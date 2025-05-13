class TV:
    def __init__(self,channel,vol,on):
        self.channel=channel
        self.vol=vol
        self.on=on

    def Show(self):
        print(self.channel,self.vol,self.on)
    
    def setChannel(self,channel):
        self.channel = channel

    def getChannel(self):
        return f"{self.channel}"


t = TV(9,10,True)

t.Show()
t.setChannel(11)
print(t.getChannel())