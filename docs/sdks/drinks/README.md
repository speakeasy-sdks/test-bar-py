# Drinks
(*drinks*)

## Overview

The drinks endpoints.

### Available Operations

* [get_drink](#get_drink) - Get a drink.
* [list_drinks](#list_drinks) - Get a list of drinks.

## get_drink

Get a drink by name, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import test_bar

s = test_bar.TestBar(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.drinks.get_drink(name='<value>')

if res.drink is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetDrinkResponse](../../models/operations/getdrinkresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |

## list_drinks

Get a list of drinks, if authenticated this will include stock levels and product codes otherwise it will only include public information.

### Example Usage

```python
import test_bar
from test_bar.models import components

s = test_bar.TestBar()


res = s.drinks.list_drinks(drink_type=components.DrinkType.SPIRIT)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `drink_type`                                                                 | [Optional[components.DrinkType]](../../models/components/drinktype.md)       | :heavy_minus_sign:                                                           | The type of drink to filter by. If not provided all drinks will be returned. |


### Response

**[operations.ListDrinksResponse](../../models/operations/listdrinksresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
