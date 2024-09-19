n = input()
a = input()
b = input()
print(*set(n[0]) & set(a[0]) & set(b[0]) | set(n[1]) & set(a[1]) & set(b[1]))
if __name__ == "__main__":
    print("2.2_13 completed")