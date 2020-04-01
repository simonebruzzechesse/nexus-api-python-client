# openapi_client.SecurityManagementApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_sources**](SecurityManagementApi.md#get_user_sources) | **GET** /beta/security/user-sources | Retrieve a list of the available user sources.


# **get_user_sources**
> list[ApiUserSource] get_user_sources()

Retrieve a list of the available user sources.

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
    api_instance = openapi_client.SecurityManagementApi(api_client)
    
    try:
        # Retrieve a list of the available user sources.
        api_response = api_instance.get_user_sources()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementApi->get_user_sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiUserSource]**](ApiUserSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

