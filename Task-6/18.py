from abc import ABC, abstractmethod
class Plugin(ABC):
    @abstractmethod
    def run(self):
        pass

class PluginA(Plugin):
    def run(self):
        print("Plugin A running")

class PluginB(Plugin):
    def run(self):
        print("Plugin B running")

plugins = [PluginA(), PluginB()]
for p in plugins:
    p.run()
