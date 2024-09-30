# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transaction_status import (
    TransactionStatusResource,
    AsyncTransactionStatusResource,
    TransactionStatusResourceWithRawResponse,
    AsyncTransactionStatusResourceWithRawResponse,
    TransactionStatusResourceWithStreamingResponse,
    AsyncTransactionStatusResourceWithStreamingResponse,
)

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def transaction_status(self) -> TransactionStatusResource:
        return TransactionStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/MpesaFlow/mpesaflow-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/MpesaFlow/mpesaflow-python#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def transaction_status(self) -> AsyncTransactionStatusResource:
        return AsyncTransactionStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/MpesaFlow/mpesaflow-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/MpesaFlow/mpesaflow-python#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def transaction_status(self) -> TransactionStatusResourceWithRawResponse:
        return TransactionStatusResourceWithRawResponse(self._transactions.transaction_status)


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def transaction_status(self) -> AsyncTransactionStatusResourceWithRawResponse:
        return AsyncTransactionStatusResourceWithRawResponse(self._transactions.transaction_status)


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def transaction_status(self) -> TransactionStatusResourceWithStreamingResponse:
        return TransactionStatusResourceWithStreamingResponse(self._transactions.transaction_status)


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

    @cached_property
    def transaction_status(self) -> AsyncTransactionStatusResourceWithStreamingResponse:
        return AsyncTransactionStatusResourceWithStreamingResponse(self._transactions.transaction_status)
