# Config
(*config*)

### Available Operations

* [subscribe_to_webhooks](#subscribe_to_webhooks) - Subscribe to webhooks.

## subscribe_to_webhooks

Subscribe to webhooks.

### Example Usage

```python
import test_bar
from test_bar.models import operations

s = test_bar.TestBar(
    api_key="",
)

req = [
    operations.RequestBody(),
]

res = s.config.subscribe_to_webhooks(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [List[operations.RequestBody]](../../models/.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.SubscribeToWebhooksResponse](../../models/operations/subscribetowebhooksresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 400-600          | */*              |