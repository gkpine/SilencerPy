from Automation import Automation, MouseButton

a = Automation()

print(a.test_add(5, 6))

hwnd = 0x40824

a.silent_type(hwnd, 'hello', True, 100, 500)
a.silent_move_mouse(hwnd, 0, 0, 500, 500, 1)
a.silent_click(hwnd, 100, 100, MouseButton.RIGHT)