from abc import ABC, abstractmethod
class Plugin(ABC):
    @abstractmethod
    def run(self):
        pass

class PluginX(Plugin):
    def run(self):
        print("Plugin X running")

class PluginY(Plugin):
    def run(self):
        print("Plugin Y running")

plugins = [PluginX(), PluginY()]
for p in plugins:
    p.run()
