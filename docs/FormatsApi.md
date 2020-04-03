# nexus_api_python_client.FormatsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get1**](FormatsApi.md#get1) | **GET** /v1/formats/{format}/upload-specs | Get upload field requirements for the desired format
[**get2**](FormatsApi.md#get2) | **GET** /v1/formats/upload-specs | Get upload field requirements for each supported format


# **get1**
> UploadDefinitionXO get1(format)

Get upload field requirements for the desired format

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
    api_instance = nexus_api_python_client.FormatsApi(api_client)
    format = 'format_example' # str | The desired repository format

    try:
        # Get upload field requirements for the desired format
        api_response = api_instance.get1(format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormatsApi->get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The desired repository format | 

### Return type

[**UploadDefinitionXO**](UploadDefinitionXO.md)

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

# **get2**
> list[UploadDefinitionXO] get2()

Get upload field requirements for each supported format

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
    api_instance = nexus_api_python_client.FormatsApi(api_client)
    
    try:
        # Get upload field requirements for each supported format
        api_response = api_instance.get2()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormatsApi->get2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UploadDefinitionXO]**](UploadDefinitionXO.md)

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

