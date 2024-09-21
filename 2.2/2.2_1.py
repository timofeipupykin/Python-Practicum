def main():
    print("Как Вас зовут?")
    name = input()
    print(f"Здравствуйте, {name}!")
    print("Как дела?")
    mood = input()
    print("Я за вас рада!") if mood == "хорошо" else print(f"Всё наладится!")
if __name__ == "__main__":
    main()