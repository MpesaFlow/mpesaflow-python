# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mpesaflow import Mpesaflow, AsyncMpesaflow
from tests.utils import assert_matches_type
from mpesaflow.types.transactions import TransactionStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Mpesaflow) -> None:
        status = client.transactions.status.retrieve(
            "transactionId",
        )
        assert_matches_type(TransactionStatus, status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mpesaflow) -> None:
        response = client.transactions.status.with_raw_response.retrieve(
            "transactionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(TransactionStatus, status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mpesaflow) -> None:
        with client.transactions.status.with_streaming_response.retrieve(
            "transactionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(TransactionStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mpesaflow) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            client.transactions.status.with_raw_response.retrieve(
                "",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMpesaflow) -> None:
        status = await async_client.transactions.status.retrieve(
            "transactionId",
        )
        assert_matches_type(TransactionStatus, status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMpesaflow) -> None:
        response = await async_client.transactions.status.with_raw_response.retrieve(
            "transactionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(TransactionStatus, status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMpesaflow) -> None:
        async with async_client.transactions.status.with_streaming_response.retrieve(
            "transactionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(TransactionStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMpesaflow) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_id` but received ''"):
            await async_client.transactions.status.with_raw_response.retrieve(
                "",
            )
