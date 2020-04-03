# nexus_api_python_client.SupportApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supportzip**](SupportApi.md#supportzip) | **POST** /v1/support/supportzip | Creates and downloads a support zip


# **supportzip**
> supportzip(body=body)

Creates and downloads a support zip

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
    api_instance = nexus_api_python_client.SupportApi(api_client)
    body = nexus_api_python_client.Request() # Request |  (optional)

    try:
        # Creates and downloads a support zip
        api_instance.supportzip(body=body)
    except ApiException as e:
        print("Exception when calling SupportApi->supportzip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Request**](Request.md)|  | [optional] 

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

