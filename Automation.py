import os
from enum import IntEnum
current_path = os.path.dirname(os.path.realpath(__file__))

# .NET stuff
from clr_loader import get_coreclr
from pythonnet import set_runtime
rtconfig = get_coreclr(current_path + '\\rtconfig.json')
set_runtime(rtconfig)
import clr
from System import IntPtr
clr.AddReference('Silencer')
from Silencer import Automation as AutomationCs, Types

class MouseButton(IntEnum):
    LEFT = 0x0001
    RIGHT = 0x0002
    MIDDLE = 0x0010

class Automation:
    """Contains Silencer's Automation class functions."""

    def __init__(self):
        pass

    def test_add(self, a: int, b: int):
        """
        Test function for debugging.
        a (int)
        b (int)
        """
        return AutomationCs.TestAdd(a, b)

    def silent_type(self, hwnd: int, text: str, send_enter: bool, human_type_low: int = None, human_type_high: int = None):
        """
        Silently types a message to the window specified by the hwnd.
        hwnd (int): window handle, must be in hex format
        text (string): the message to send
        send_enter (boolean): True will send a new line after the message, False does not
        human_type_low (int, optional): lowerbound for random typing like a human
        human_type_high (int, optional): upperbound for random typing like a human
        """
        hwnd_ptr = IntPtr.__overloads__[int](hwnd)
        AutomationCs.SilentType(hwnd_ptr, text, send_enter, human_type_low, human_type_high)

    def silent_move_mouse(self, hwnd: int, start_x: int, start_y: int, dest_x: int, dest_y: int, step: int = 1):
        """
        Silently move the mouse to the given coordinate within a certain number of steps.
        hwnd(int): window handle, must be in hex format
        start_x(int): X coordinate where the mouse will start from
        start_y(int): Y coordinate where the mouse will start from
        dest_x(int): X coordinate where the mouse is going
        dest_y(int): Y coordinate where the mouse is going
        step(int, optional): how many steps to do the movement in (1 is teleporting the mouse, something like 200 moves the mouse smoothly)
        """
        hwnd_ptr = IntPtr.__overloads__[int](hwnd)
        AutomationCs.SilentMoveMouse(hwnd_ptr, start_x, start_y, dest_x, dest_y, step)

    def silent_click(self, hwnd: int, x: int, y: int, button: MouseButton):
        hwnd_ptr = IntPtr.__overloads__[int](hwnd)
        AutomationCs.SilentClick(hwnd_ptr, x, y, button.value)