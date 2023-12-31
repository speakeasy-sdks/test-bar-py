"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass, field
from typing import Dict, Tuple, Callable, Union
from enum import Enum
from .utils.retries import RetryConfig
from .utils import utils
from test_bar.models import components


SERVER_PROD = 'prod'
r"""The production server."""
SERVER_STAGING = 'staging'
r"""The staging server."""
SERVER_CUSTOMER = 'customer'
r"""A per-organization and per-environment API."""
SERVERS = {
	SERVER_PROD: 'https://speakeasy.bar',
	SERVER_STAGING: 'https://staging.speakeasy.bar',
	SERVER_CUSTOMER: 'https://{organization}.{environment}.speakeasy.bar',
}
"""Contains the list of servers available to the SDK"""


class ServerEnvironment(str, Enum):
    r"""The environment name. Defaults to the production environment."""
    PROD = 'prod'
    STAGING = 'staging'
    DEV = 'dev'


@dataclass
class SDKConfiguration:
    client: requests.Session
    security: Union[components.Security,Callable[[], components.Security]] = None
    server_url: str = ''
    server: str = ''
    server_defaults: Dict[str, Dict[str, str]] = field(default_factory=Dict)
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '0.3.1'
    gen_version: str = '2.228.1'
    user_agent: str = 'speakeasy-sdk/python 0.3.1 2.228.1 1.0.0 test-bar'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_PROD

        return SERVERS[self.server], self.server_defaults.get(self.server, {})
