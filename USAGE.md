<!-- Start SDK Example Usage [usage] -->
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