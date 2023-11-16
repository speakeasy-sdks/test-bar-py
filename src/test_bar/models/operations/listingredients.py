"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import error as components_error
from ...models.components import ingredient as components_ingredient
from typing import List, Optional


@dataclasses.dataclass
class ListIngredientsRequest:
    ingredients: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ingredients', 'style': 'form', 'explode': False }})
    r"""A list of ingredients to filter by. If not provided all ingredients will be returned."""
    



@dataclasses.dataclass
class ListIngredientsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[components_ingredient.Ingredient]] = dataclasses.field(default=None)
    r"""A list of ingredients."""
    error: Optional[components_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    

