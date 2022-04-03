class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
            transactions = [transaction.split(",") for transaction in transactions]
            invalidTransactions = []
            invalidIndexes = set()
            for i in range(len(transactions)):
                if i not in invalidIndexes and int(transactions[i][2]) > 1000:
                    invalidIndexes.add(i)
                    invalidTransactions.append(",".join(transactions[i]))
                for j in range(i+1, len(transactions)):
                    if transactions[i][0] == transactions[j][0] and transactions[i][3] != transactions[j][3] and ((int(transactions[i][1])-60 <= int(transactions[j][1]) <= int(transactions[i][1])+60) or (int(transactions[j][1])-60 <= int(transactions[i][1]) <= int( transactions[j][1])+60)):
                        if i not in invalidIndexes:
                            invalidIndexes.add(i)
                            invalidTransactions.append(",".join(transactions[i]))
                        if j not in invalidIndexes:
                            invalidIndexes.add(j)
                            invalidTransactions.append(",".join(transactions[j]))
                    if j not in invalidIndexes and int(transactions[j][2]) > 1000:
                        invalidIndexes.add(j)
                        invalidTransactions.append(",".join(transactions[j]))

            return invalidTransactions
