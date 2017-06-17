
class WindowManager:
    def __init__(self):
        self.selectedwindow = None
        self.windows = []

    def select(self):
        pass

    def add(self,item):
        self.windows.append(item)

    def remove(self,item):
        from ..globals import Globals
        self.windows.remove(item)
        if len(self.windows) == 0:
            Globals.RUNNING = False