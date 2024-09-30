# Payments

Types:

```python
from mpesaflow.types import PaymentCreateResponse
```

Methods:

- <code title="post /paybill">client.payments.<a href="./src/mpesaflow/resources/payments.py">create</a>(\*\*<a href="src/mpesaflow/types/payment_create_params.py">params</a>) -> <a href="./src/mpesaflow/types/payment_create_response.py">PaymentCreateResponse</a></code>

# Transactions

Types:

```python
from mpesaflow.types import TransactionRetrieveStatusResponse
```

Methods:

- <code title="get /transaction-status/{transactionId}">client.transactions.<a href="./src/mpesaflow/resources/transactions.py">retrieve_status</a>(transaction_id) -> <a href="./src/mpesaflow/types/transaction_retrieve_status_response.py">TransactionRetrieveStatusResponse</a></code>
