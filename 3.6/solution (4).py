import sys
import json


def check(x_num):
    for it in range(2, x_num):
        if x_num % it == 0:
            return False
    return x_num > 1


def count_del(num):
    sim_count = []
    for delitel in range(1, num + 1):
        if num % delitel == 0 and check(delitel):
            sim_count.append(delitel)
    return sim_count


result = dict()

in_file = sys.stdin.readlines()
for i in in_file:
    i = i.strip("\n")
    dels = count_del(int(i))
    for delit in dels:
        result[delit] = set()

for i in result:
    for x in in_file:
        if int(x) % int(i) == 0:
            result[i].add(int(x))
            
for item in result:
    result[item] = sorted(result[item])

with open("result.json", "w", encoding="UTF-8") as out_file:
    json.dump(result, out_file, ensure_ascii=False, indent=2)
