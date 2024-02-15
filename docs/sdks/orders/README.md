# Orders
(*orders*)

## Overview

The orders endpoints.

### Available Operations

* [create_order](#create_order) - Create an order.

## create_order

Create an order for a drink.

### Example Usage

```python
import test_bar
from test_bar.models import components

s = test_bar.TestBar(
    api_key="<YOUR_API_KEY_HERE>",
)


res = s.orders.create_order(request_body=[
    components.OrderInput(
        product_code='APM-1F2D3',
        quantity=26535,
        type=components.OrderType.DRINK,
    ),
], callback_url='<value>')

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request_body`                                                       | List[[components.OrderInput](../../models/components/orderinput.md)] | :heavy_check_mark:                                                   | N/A                                                                  |
| `callback_url`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The url to call when the order is updated.                           |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
