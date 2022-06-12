import os
from clr_loader import get_coreclr
from pythonnet import set_runtime

class Automation:
    def __init__(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        rtconfig = get_coreclr(current_path + '\\rtconfig.json')
        set_runtime(rtconfig)
        import clr
        clr.AddReference('Silencer')
        from Silencer import Automation

        self.__w_TestAdd = Automation.TestAdd

    # Test function, prints sum of a + b
    def TestAdd(self, a, b):
        return self.__w_TestAdd(a, b)

print(Automation().TestAdd(5, 7))