def main():
    name = input()
    cost = int(input())
    weight = float(input())
    money = int(input())
    fin_cost = int(cost * weight)
    change = money - fin_cost
    print("Чек")
    print(f"{name} - {int(weight)}кг - {cost}руб/кг")
    print(f"Итого: {fin_cost}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {change}руб")
if __name__ == "__main__":
    main()