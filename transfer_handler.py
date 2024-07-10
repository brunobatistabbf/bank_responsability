from transcation_interface import TransactionHandler

class TransferHandler(TransactionHandler):
    def handle(self, transaction):
        if transaction['type'] == 'transfer':
            if transaction['account'].balance >= transaction['amount']:
                transaction['account'].balance -= transaction['amount']
                transaction['destination_account'].balance += transaction['amount']
                return f"Tranferencia de {transaction['amount']} processada.\nNovo Balanço: {transaction['account'].balance}"
            else:
                return "Fundos insuficientes para transferencia"
        else:
            return super().handle(transaction)