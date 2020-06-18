# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import TYPE_CHECKING

from . import AsyncChallengeAuthPolicy
from .client_base import ApiVersion
from .._user_agent import USER_AGENT
from .._generated.aio import KeyVaultClient as _KeyVaultClient

if TYPE_CHECKING:
    try:
        # pylint:disable=unused-import
        from typing import Any
        from azure.core.configuration import Configuration
        from azure.core.pipeline.transport import AsyncHttpTransport
        from azure.core.credentials_async import AsyncTokenCredential
    except ImportError:
        # AsyncTokenCredential is a typing_extensions.Protocol; we don't depend on that package
        pass

DEFAULT_VERSION = ApiVersion.V7_1_preview

class AsyncKeyVaultClientBase(object):
    def __init__(self, vault_url: str, credential: "AsyncTokenCredential", **kwargs: "Any") -> None:
        if not credential:
            raise ValueError(
                "credential should be an object supporting the AsyncTokenCredential protocol, "
                "such as a credential from azure-identity"
            )
        if not vault_url:
            raise ValueError("vault_url must be the URL of an Azure Key Vault")

        self._vault_url = vault_url.strip(" /")
        client = kwargs.get("generated_client")
        if client:
            # caller provided a configured client -> nothing left to initialize
            self._client = client
            return

        api_version = kwargs.pop("api_version", DEFAULT_VERSION)

        pipeline = kwargs.pop("pipeline", None)
        transport = kwargs.pop("transport", None)
        if not transport:
            from azure.core.pipeline.transport import AioHttpTransport
            transport = AioHttpTransport(**kwargs)

        try:
            self._client = _KeyVaultClient(
                api_version=api_version,
                pipeline=pipeline,
                transport=transport,
                authentication_policy=AsyncChallengeAuthPolicy(credential),
                sdk_moniker=USER_AGENT,
                **kwargs
            )
            self._models = _KeyVaultClient.models(api_version=api_version)
        except NotImplementedError:
            raise NotImplementedError(
                "This package doesn't support API version '{}'. ".format(api_version)
                + "Supported versions: {}".format(", ".join(v.value for v in ApiVersion))
            )

    @property
    def vault_url(self) -> str:
        return self._vault_url

    async def __aenter__(self) -> "AsyncKeyVaultClientBase":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args: "Any") -> None:
        await self._client.__aexit__(*args)

    async def close(self) -> None:
        """Close sockets opened by the client.

        Calling this method is unnecessary when using the client as a context manager.
        """
        await self._client.close()
