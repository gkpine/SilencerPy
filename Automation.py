import os
from clr_loader import get_coreclr
from pythonnet import set_runtime

current_path = os.path.dirname(os.path.realpath(__file__))
rtconfig = get_coreclr(current_path + '\\rtconfig.json')
set_runtime(rtconfig)
import clr
from System import IntPtr, Int64, String
clr.AddReference('Silencer')
from Silencer import Automation as AutomationCs

class Automation:
    """Contains Silencer's Automation class functions."""

    def __init__(self):
        pass

    def test_add(self, a, b):
        """
        Test function for debugging.
        a (int)
        b (int)
        """
        return AutomationCs.TestAdd(a, b)

    def silent_type(self, hwnd, text, send_enter, human_type_low = None, human_type_high = None):
        """
        Silently types a message to the window specified by the hwnd.
        hwnd (int): must be in hex format
        text (string): the message to send
        send_enter (boolean): True will send a new line after the message, False does not
        human_type_low (int, optional): lowerbound for random typing like a human
        human_type_high (int, optional): upperbound for random typing like a human
        """
        AutomationCs.SilentType(IntPtr.__overloads__[int](hwnd), text, send_enter, human_type_low, human_type_high)