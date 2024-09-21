def main():
    n = input()
    nums = list(map(int, n))
    nums.sort()
    if nums[0] + nums[2] == nums[1] * 2:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()