# Payments

Types:

```python
from mpesaflow.types import PaymentPaybillResponse
```

Methods:

- <code title="post /paybill">client.payments.<a href="./src/mpesaflow/resources/payments.py">paybill</a>(\*\*<a href="src/mpesaflow/types/payment_paybill_params.py">params</a>) -> <a href="./src/mpesaflow/types/payment_paybill_response.py">PaymentPaybillResponse</a></code>

# Transactions

## TransactionStatus

Types:

```python
from mpesaflow.types.transactions import TransactionStatus
```

Methods:

- <code title="get /transaction-status/{transactionId}">client.transactions.transaction_status.<a href="./src/mpesaflow/resources/transactions/transaction_status.py">retrieve</a>(transaction_id) -> <a href="./src/mpesaflow/types/transactions/transaction_status.py">TransactionStatus</a></code>
