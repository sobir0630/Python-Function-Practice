def create_account():
    """hisob raqam ochish """
    hisob = input("Hisob raqam kiriting (karta raqam): ")
    print(f"\n Hisob ochildi: {hisob}")
    return 0.0  # boshlang'ich balans

def deposit(balance):
    """Deposit qo‘yish funksiyasi"""
    amount = float(input("Qancha pul qoymoqchisiz? "))
    if amount > 0:
        balance += amount
        print(f"{amount} som qoyildi. Yangi balans: {balance} som.")
    else:
        print("Notogri summa")
    return balance

def withdraw(balance):
    """Pul yechish funksiyasi"""
    amount = float(input("Qancha pul yechmoqchisiz? "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"{amount} som yechildi. Yangi balans: {balance} som.")
    else:
        print("Mablag yetarli emas yoki notogri summa!")
    return balance

def check_balance(balance):
    """Hisobdagi balansni korsatish"""
    print(f"Hisobingizdagi balans: {balance} som")

def main():
    print("Bank dasturiga xush kelibsiz!")
    balance = create_account()

    while True:
        print("\n--- M E N U ---")
        print("1. Pul qoyish")
        print("2. Pul yechib olish")
        print("3. Balansni korish")
        print("4. Dasturdan chiqish")

        choice = input("Tanlang (1-4): ")

        if choice == "1":
            balance = deposit(balance)
        elif choice == "2":
            balance = withdraw(balance)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Dastur toxtadi.")
            break
        else:
            print("Notogri tanlov!")

main()

