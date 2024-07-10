from transcation_interface import TransactionHandler

class WithdrawHandler(TransactionHandler):
    def handle(self, transaction):
        if transaction['type'] == 'withdraw':
            if transaction['account'].balance >= transaction['amount']:
                transaction['account'].balance -= transaction['amount']
                return f"Retirada {transaction['amount']} Processada. \nNovo Balanço: {transaction['account'].balance}"
            else:
                return "Fundos insuficientes para retirada"
        else:
            return super().handle(transaction)