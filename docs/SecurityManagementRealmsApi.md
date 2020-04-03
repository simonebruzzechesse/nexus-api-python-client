# nexus_api_python_client.SecurityManagementRealmsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_realms**](SecurityManagementRealmsApi.md#get_active_realms) | **GET** /beta/security/realms/active | List the active realm IDs in order
[**get_realms**](SecurityManagementRealmsApi.md#get_realms) | **GET** /beta/security/realms/available | List the available realms
[**set_active_realms**](SecurityManagementRealmsApi.md#set_active_realms) | **PUT** /beta/security/realms/active | Set the active security realms in the order they should be used


# **get_active_realms**
> list[str] get_active_realms()

List the active realm IDs in order

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
    api_instance = nexus_api_python_client.SecurityManagementRealmsApi(api_client)
    
    try:
        # List the active realm IDs in order
        api_response = api_instance.get_active_realms()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementRealmsApi->get_active_realms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

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

# **get_realms**
> list[RealmApiXO] get_realms()

List the available realms

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
    api_instance = nexus_api_python_client.SecurityManagementRealmsApi(api_client)
    
    try:
        # List the available realms
        api_response = api_instance.get_realms()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementRealmsApi->get_realms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RealmApiXO]**](RealmApiXO.md)

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

# **set_active_realms**
> set_active_realms(body=body)

Set the active security realms in the order they should be used

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
    api_instance = nexus_api_python_client.SecurityManagementRealmsApi(api_client)
    body = ['body_example'] # list[str] | The realm IDs (optional)

    try:
        # Set the active security realms in the order they should be used
        api_instance.set_active_realms(body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementRealmsApi->set_active_realms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The realm IDs | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

