a = input()
b = input()
a1 = f"{a:0>3}"
b1 = f"{b:0>3}"
n1 = f"{int(a1[0]) + int(b1[0]):0>3}"[2]
n2 = f"{int(a1[1]) + int(b1[1]):0>3}"[2]
n3 = f"{int(a1[2]) + int(b1[2]):0>3}"[2]
print(n1 + n2 + n3)