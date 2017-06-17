
class WindowManager:
    def __init__(self):
        self.selectedwindow = None
        self.windows = []

    def select(self,item):
        self.selectedwindow = item

    def add(self,item):
        self.windows.append(item)
        if len(self.windows) == 1:
            self.selectedwindow = item

    def remove(self,item):
        from ..globals import Globals
        self.windows.remove(item)
        if len(self.windows) == 0:
            Globals.RUNNING = False