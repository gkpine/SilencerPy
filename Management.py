import os

current_path = os.path.dirname(os.path.realpath(__file__))

# .NET stuff
from clr_loader import get_coreclr
from pythonnet import set_runtime
rtconfig = get_coreclr(current_path + '\\rtconfig.json')
set_runtime(rtconfig)

import clr
import System
from System import IntPtr
# from System.Drawing import Point
clr.AddReference('Silencer')
from Silencer import Management as ManagementCs

class Management:
    """Contains Silencer's Management class functions."""

    def __init__(self):
        pass

    def lock_window(self, hwnd: int):
        """
        Locks the target window, preventing silent input from giving the window focus.
        hwnd (int): window handle, must be in hex format (you can use the Python function hex(...) for this)
        """
        hwnd_ptr = IntPtr.__overloads__[int](hwnd)
        ManagementCs.LockWindow(hwnd_ptr)

    def unlock_window(self, hwnd: int):
        """
        Unlocks the target window, allowing input to give it focus again.
        hwnd (int): window handle, must be in hex format (you can use the Python function hex(...) for this)
        """
        hwnd_ptr = IntPtr.__overloads__[int](hwnd)
        ManagementCs.UnlockWindow(hwnd_ptr)

    def screen_to_client(self, hwnd: int, screen_x: int, screen_y: int):
        """
        Converts the given screen-space point to a client-space point. 
        hwnd (int): window handle, must be in hex format (you can use the Python function hex(...) for this)
        screen_x (int): The screen point's X coordinate.
        screen_y (int): The screen point's Y coordinate.

        Returns:
            list: Returns a 2 element list representing the client point [X, Y].
        """
        pt = System.Drawing.Point(screen_x, screen_y)
        hwnd_ptr = IntPtr.__overloads__[int](hwnd)
        client_pt = ManagementCs.ScreenToClient(hwnd_ptr, pt)
        return [client_pt.X, client_pt.Y]