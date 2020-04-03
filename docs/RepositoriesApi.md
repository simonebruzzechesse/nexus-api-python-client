# nexus_api_python_client.RepositoriesApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repositories1**](RepositoriesApi.md#get_repositories1) | **GET** /v1/repositories | List repositories


# **get_repositories1**
> list[RepositoryXO] get_repositories1()

List repositories

### Example

```python
from __future__ import print_function
import time
import nexus_api_python_client
from nexus_api_python_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with nexus_api_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = nexus_api_python_client.RepositoriesApi(api_client)
    
    try:
        # List repositories
        api_response = api_instance.get_repositories1()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesApi->get_repositories1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RepositoryXO]**](RepositoryXO.md)

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

