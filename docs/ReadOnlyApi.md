# openapi_client.ReadOnlyApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**force_release**](ReadOnlyApi.md#force_release) | **POST** /v1/read-only/force-release | Forcibly release read-only
[**freeze**](ReadOnlyApi.md#freeze) | **POST** /v1/read-only/freeze | Enable read-only
[**get**](ReadOnlyApi.md#get) | **GET** /v1/read-only | Get read-only state
[**release**](ReadOnlyApi.md#release) | **POST** /v1/read-only/release | Release read-only


# **force_release**
> force_release()

Forcibly release read-only

Forcibly release read-only status, including System initiated tasks. Warning: may result in data loss.

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
    api_instance = openapi_client.ReadOnlyApi(api_client)
    
    try:
        # Forcibly release read-only
        api_instance.force_release()
    except ApiException as e:
        print("Exception when calling ReadOnlyApi->force_release: %s\n" % e)
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
**204** | System is no longer read-only |  -  |
**403** | Authentication required |  -  |
**404** | No change to read-only state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freeze**
> freeze()

Enable read-only

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
    api_instance = openapi_client.ReadOnlyApi(api_client)
    
    try:
        # Enable read-only
        api_instance.freeze()
    except ApiException as e:
        print("Exception when calling ReadOnlyApi->freeze: %s\n" % e)
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
**204** | System is now read-only |  -  |
**403** | Authentication required |  -  |
**404** | No change to read-only state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ReadOnlyState get()

Get read-only state

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
    api_instance = openapi_client.ReadOnlyApi(api_client)
    
    try:
        # Get read-only state
        api_response = api_instance.get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReadOnlyApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReadOnlyState**](ReadOnlyState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release**
> release()

Release read-only

Release administrator initiated read-only status. Will not release read-only caused by system tasks.

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
    api_instance = openapi_client.ReadOnlyApi(api_client)
    
    try:
        # Release read-only
        api_instance.release()
    except ApiException as e:
        print("Exception when calling ReadOnlyApi->release: %s\n" % e)
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
**204** | System is no longer read-only |  -  |
**403** | Authentication required |  -  |
**404** | No change to read-only state |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

