<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->