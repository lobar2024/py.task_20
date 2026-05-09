def make_account(balans):
    def deposit(summa):
        nonlocal balans
        balans += summa
        return balans
    def withdraw(summa):
        nonlocal balans
        if summa > balans:
            return "Mablag' yetarli emas"
        balans -= summa
        return balans
    def balance():
        return balans
    return deposit, withdraw, balance

dep, with_, bal = make_account(1000)
print(dep(500))    # 1500
print(with_(200))  # 1300
print(bal())       # 1300
