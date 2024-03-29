from modules.module_base import ModuleBase
import os.path
import subprocess
import platform

class ModuleVersion(ModuleBase):
    PATH = os.path.dirname(os.path.dirname(__file__))

    def __init__(self, bot):
        ModuleBase.__init__(self, bot)
        self.name = "ModuleVersion"

    def notify_command(self, message_id, from_attr, date, chat, commandName, commandStr):
        if commandName == "version":
            try:
                text = ""
                text += "Python version %s\n" % platform.python_version()
                text += "Running on %s\n" % platform.node()
                text += subprocess.check_output(["git","remote", "-v"], cwd=self.PATH).decode("utf-8")
                text += subprocess.check_output(["git","log", "-1"], cwd=self.PATH).decode("utf-8")
                self.bot.sendMessage(text, chat["id"])
            except:
                self.bot.sendMessage("Error getting version", chat["id"])
                self.logger.exception("Error getting version", exc_info=True)

    def get_commands(self):
        return [
            ("version", "Get bot version"),
        ]
