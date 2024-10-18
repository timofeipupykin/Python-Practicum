def main():
    n = int(input())
    m = int(input())
    nums = [int(input()) for i in range(n)]
    max_nums = []

    for x in range(len(nums) - 1):
        if abs(nums[x + 1] - nums[x]) < m:
            max_nums.append(nums[x + 1])
    print(max(max_nums))
if __name__ == "__main__":
    main()