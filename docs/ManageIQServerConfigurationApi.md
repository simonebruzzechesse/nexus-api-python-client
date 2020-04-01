# openapi_client.ManageIQServerConfigurationApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_iq**](ManageIQServerConfigurationApi.md#disable_iq) | **POST** /beta/iq/disable | Disable IQ Server
[**enable_iq**](ManageIQServerConfigurationApi.md#enable_iq) | **POST** /beta/iq/enable | Enable IQ Server
[**get_configuration**](ManageIQServerConfigurationApi.md#get_configuration) | **GET** /beta/iq | Get IQ Server configuration
[**update_configuration**](ManageIQServerConfigurationApi.md#update_configuration) | **PUT** /beta/iq | Update IQ Server configuration
[**verify_connection**](ManageIQServerConfigurationApi.md#verify_connection) | **POST** /beta/iq/verify-connection | Verify IQ Server connection


# **disable_iq**
> disable_iq()

Disable IQ Server

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
    api_instance = openapi_client.ManageIQServerConfigurationApi(api_client)
    
    try:
        # Disable IQ Server
        api_instance.disable_iq()
    except ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->disable_iq: %s\n" % e)
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
**204** | IQ Server has been disabled |  -  |
**400** | IQ Server connection not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_iq**
> enable_iq()

Enable IQ Server

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
    api_instance = openapi_client.ManageIQServerConfigurationApi(api_client)
    
    try:
        # Enable IQ Server
        api_instance.enable_iq()
    except ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->enable_iq: %s\n" % e)
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
**204** | IQ Server has been enabled |  -  |
**400** | IQ Server connection not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> get_configuration()

Get IQ Server configuration

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
    api_instance = openapi_client.ManageIQServerConfigurationApi(api_client)
    
    try:
        # Get IQ Server configuration
        api_instance.get_configuration()
    except ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->get_configuration: %s\n" % e)
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
**200** | IQ Server configuration returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> update_configuration(body=body)

Update IQ Server configuration

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
    api_instance = openapi_client.ManageIQServerConfigurationApi(api_client)
    body = openapi_client.IqConnectionXo() # IqConnectionXo |  (optional)

    try:
        # Update IQ Server configuration
        api_instance.update_configuration(body=body)
    except ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->update_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IqConnectionXo**](IqConnectionXo.md)|  | [optional] 

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
**204** | IQ Server configuration has been updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_connection**
> verify_connection()

Verify IQ Server connection

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
    api_instance = openapi_client.ManageIQServerConfigurationApi(api_client)
    
    try:
        # Verify IQ Server connection
        api_instance.verify_connection()
    except ApiException as e:
        print("Exception when calling ManageIQServerConfigurationApi->verify_connection: %s\n" % e)
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
**200** | Connection verification complete, check response body for result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

