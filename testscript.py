from Automation import Automation

a = Automation()

print(a.test_add(5, 6))

a.silent_type(0x40824, 'hello', True, 100, 500)