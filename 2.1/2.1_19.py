name = input()
cost = int(input())
weight = int(input())
money = int(input())
x = f"{weight}кг * {cost}руб/кг"
print("================Чек================"),
print(f"Товар:{name: >29}")
print(f"Цена:{x: >30}")
print(f"Итого:{weight * cost: >26}руб")
print(f"Внесено:{money: >24}руб")
print(f"Сдача:{money - (weight * cost): >26}руб")
print("===================================")
if __name__ == "__main__":
    print("2.1_19 completed")