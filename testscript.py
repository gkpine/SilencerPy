"""
This file can be used as an example of how to use SilencerPy.
"""

from Automation import Automation, MouseButton
from Management import Management

a = Automation()
m = Management()

print(a.test_add(5, 6))

hwnd = 0x000C067A # This handle was found using Spy++ x64. It points to an active Notepad window on my machine.
pt = m.screen_to_client(hwnd, 3000, 1000)
print(pt)

# This will type "hello" on Notepad using the human typing feature. It'll type one letter at a time.
# It'll then move the mouse to 500, 500 and right click.
a.silent_type(hwnd, 'hello', True, 100, 500)
a.silent_move_mouse(hwnd, 0, 0, 500, 500, 1)
a.silent_click(hwnd, 100, 100, MouseButton.RIGHT)