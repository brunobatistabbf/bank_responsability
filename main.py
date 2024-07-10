from account import Account
from deposit_handler import DepositHandler
from withdraw_handler import WithdrawHandler
from transfer_handler import TransferHandler

if __name__ == '__main__':
    conta1 = Account(10000)
    conta2 = Account(500)

    deposit_handler = DepositHandler()
    withdraw_handler = WithdrawHandler()
    transfer_handler = TransferHandler()

    # Criando a corrente
    deposit_handler.set_next(withdraw_handler).set_next(transfer_handler)

    transactions = [
        {'type': 'deposit', 'amount': 2000, 'account': conta1},
        {'type': 'withdraw', 'amount': 200, 'account': conta1},
        {'type': 'transfer', 'amount': 100, 'account': conta1, 'destination_account': conta2},
        {'type': 'withdraw', 'amount': 100, 'account': conta2},
        {'type': 'invalid', 'amount': 100, 'account': conta1},
    ]

    for transaction in transactions:
        result = deposit_handler.handle(transaction)
        if result:
            print(result)
        else:
            print("Transação não pode ser processada")






















