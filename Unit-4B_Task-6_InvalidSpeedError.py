class LowBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise LowBalanceError('Insufficient balance!')
    return balance - amount

try:
    bal = withdraw(1000, 1500)
    print('Remaining balance:', bal)
except LowBalanceError as e:
    print('Error:', e)