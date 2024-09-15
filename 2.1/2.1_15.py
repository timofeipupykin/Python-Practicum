n = int(input())
m = int(input())
t = int(input())
real_time = n * 60 + m
fin_time = real_time + t
real_fin_time = fin_time % (24 * 60)
print(f"{real_fin_time // 60:0>2}:{real_fin_time % 60:0>2}")