"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import drink as components_drink
from ...models.components import drinktype as components_drinktype
from ...models.components import error as components_error
from typing import List, Optional


@dataclasses.dataclass
class ListDrinksRequest:
    drink_type: Optional[components_drinktype.DrinkType] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'drinkType', 'style': 'form', 'explode': True }})
    r"""The type of drink to filter by. If not provided all drinks will be returned."""
    



@dataclasses.dataclass
class ListDrinksResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[components_drink.Drink]] = dataclasses.field(default=None)
    r"""A list of drinks."""
    error: Optional[components_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
