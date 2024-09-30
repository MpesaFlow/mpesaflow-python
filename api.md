# Payments

Types:

```python
from mpesaflow.types import Payment
```

Methods:

- <code title="post /paybill">client.payments.<a href="./src/mpesaflow/resources/payments.py">create</a>(\*\*<a href="src/mpesaflow/types/payment_create_params.py">params</a>) -> <a href="./src/mpesaflow/types/payment.py">Payment</a></code>

# Transactions

## Status

Types:

```python
from mpesaflow.types.transactions import TransactionStatus
```

Methods:

- <code title="get /transaction-status/{transactionId}">client.transactions.status.<a href="./src/mpesaflow/resources/transactions/status.py">retrieve</a>(transaction_id) -> <a href="./src/mpesaflow/types/transactions/transaction_status.py">TransactionStatus</a></code>
