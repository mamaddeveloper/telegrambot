class ModuleTest():
    def __init__(self):
        self.name = "yolo"
        self.bot = null

    def getName(self):
        return self.name

    def setBot(self, bot):
        self.bot = bot
        print("Bot set" + str(bot))

    def notify(self, update):
        pass