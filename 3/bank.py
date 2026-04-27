import math

class Bank:
    def __init__(self, rate):
        self.rate = rate      # 연이자
        self.money = 0        # 예금액 (모든 객체 0으로 시작)

    def deposit(self, amount):
        self.money += amount

    def withdraw(self, amount):
        self.money -= amount

    def after_n_years(self, n):
        self.money = self.money * math.pow((1 + self.rate), n)
    
    def show(self):
        print("예금액:", self.money)
        print("연이자:", self.rate)

# 은행 객체 생성
A = Bank(0.005)   # 0.5%
B = Bank(0.01)    # 1%
C = Bank(0.02)    # 2%

A.deposit(1000)
B.deposit(1000)
C.deposit(1000)
print("각 1000원 입금")
A.show()
B.show()
C.show()
A.withdraw(500)
B.withdraw(500)
C.withdraw(500)
print("각 500원 출금")
A.show()
B.show()
C.show()
A.after_n_years(5)
B.after_n_years(5)
C.after_n_years(5)
print("5년뒤")
A.show()
B.show()
C.show()
