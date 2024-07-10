from transcation_interface import TransactionHandler

class DepositHandler(TransactionHandler):
    def handle(self, transaction):
        if transaction['type'] == 'deposit':
            if transaction['amount'] > 0:
                transaction['account'].balance += transaction['amount']
                return f"Deposito de {transaction['amount']} processado.\nNovo Balanço: {transaction['account'].balance}"
            else:
                return  "Deposito Invalido"

        else:
            return  super().handle(transaction)