# openapi_client.StatusApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_status_checks**](StatusApi.md#get_system_status_checks) | **GET** /v1/status/check | Health check endpoint that returns the results of the system status checks
[**is_available**](StatusApi.md#is_available) | **GET** /v1/status | Health check endpoint that validates server can respond to read requests
[**is_writable**](StatusApi.md#is_writable) | **GET** /v1/status/writable | Health check endpoint that validates server can respond to read and write requests


# **get_system_status_checks**
> get_system_status_checks()

Health check endpoint that returns the results of the system status checks

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusApi(api_client)
    
    try:
        # Health check endpoint that returns the results of the system status checks
        api_instance.get_system_status_checks()
    except ApiException as e:
        print("Exception when calling StatusApi->get_system_status_checks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The system status check results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_available**
> is_available()

Health check endpoint that validates server can respond to read requests

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusApi(api_client)
    
    try:
        # Health check endpoint that validates server can respond to read requests
        api_instance.is_available()
    except ApiException as e:
        print("Exception when calling StatusApi->is_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available to service requests |  -  |
**503** | Unavailable to service requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_writable**
> is_writable()

Health check endpoint that validates server can respond to read and write requests

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusApi(api_client)
    
    try:
        # Health check endpoint that validates server can respond to read and write requests
        api_instance.is_writable()
    except ApiException as e:
        print("Exception when calling StatusApi->is_writable: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available to service requests |  -  |
**503** | Unavailable to service requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

