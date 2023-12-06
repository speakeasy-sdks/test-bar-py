# test-bar

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/test-bar-py.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/test-bar-py/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/test-bar-py.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import test_bar
from test_bar.models import operations

s = test_bar.TestBar(
    api_key="",
)


res = s.drinks.get_drink(name='string')

if res.drink is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [authentication](docs/sdks/authentication/README.md)

* [authenticate](docs/sdks/authentication/README.md#authenticate) - Authenticate with the API by providing a username and password.

### [drinks](docs/sdks/drinks/README.md)

* [get_drink](docs/sdks/drinks/README.md#get_drink) - Get a drink.
* [list_drinks](docs/sdks/drinks/README.md#list_drinks) - Get a list of drinks.

### [ingredients](docs/sdks/ingredients/README.md)

* [list_ingredients](docs/sdks/ingredients/README.md#list_ingredients) - Get a list of ingredients.

### [orders](docs/sdks/orders/README.md)

* [create_order](docs/sdks/orders/README.md#create_order) - Create an order.

### [config](docs/sdks/config/README.md)

* [subscribe_to_webhooks](docs/sdks/config/README.md#subscribe_to_webhooks) - Subscribe to webhooks.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.APIError  | 5XX              | application/json |
| errors.SDKError  | 400-600          | */*              |

### Example

```python
import test_bar
from test_bar.models import operations

s = test_bar.TestBar(
    api_key="",
)

req = operations.AuthenticateRequestBody()

res = None
try:
    res = s.authentication.authenticate(req)
except errors.APIError as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.object is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `prod` | `https://speakeasy.bar` | None |
| `staging` | `https://staging.speakeasy.bar` | None |
| `customer` | `https://{organization}.{environment}.speakeasy.bar` | `environment` (default is `prod`), `organization` (default is `api`) |

#### Example

```python
import test_bar
from test_bar.models import operations

s = test_bar.TestBar(
    server="customer",
    api_key="",
)

req = operations.AuthenticateRequestBody()

res = s.authentication.authenticate(req)

if res.object is not None:
    # handle response
    pass
```

#### Variables

Some of the server options above contain variables. If you want to set the values of those variables, the following optional parameters are available when initializing the SDK client instance:
 * `environment: models.ServerEnvironment`
 * `organization: str`

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import test_bar
from test_bar.models import operations

s = test_bar.TestBar(
    server_url="https://speakeasy.bar",
    api_key="",
)

req = operations.AuthenticateRequestBody()

res = s.authentication.authenticate(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import test_bar
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = test_bar.TestBar(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import test_bar
from test_bar.models import operations

s = test_bar.TestBar(
    api_key="",
)

req = operations.AuthenticateRequestBody()

res = s.authentication.authenticate(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
