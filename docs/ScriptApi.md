# nexus_api_python_client.ScriptApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](ScriptApi.md#add) | **POST** /v1/script | Add a new script
[**browse**](ScriptApi.md#browse) | **GET** /v1/script | List all stored scripts
[**delete1**](ScriptApi.md#delete1) | **DELETE** /v1/script/{name} | Delete stored script by name
[**edit**](ScriptApi.md#edit) | **PUT** /v1/script/{name} | Update stored script by name
[**read**](ScriptApi.md#read) | **GET** /v1/script/{name} | Read stored script by name
[**run1**](ScriptApi.md#run1) | **POST** /v1/script/{name}/run | Run stored script by name


# **add**
> add(body=body)

Add a new script

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
    api_instance = nexus_api_python_client.ScriptApi(api_client)
    body = nexus_api_python_client.ScriptXO() # ScriptXO |  (optional)

    try:
        # Add a new script
        api_instance.add(body=body)
    except ApiException as e:
        print("Exception when calling ScriptApi->add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScriptXO**](ScriptXO.md)|  | [optional] 

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
**204** | Script was added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **browse**
> list[ScriptXO] browse()

List all stored scripts

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
    api_instance = nexus_api_python_client.ScriptApi(api_client)
    
    try:
        # List all stored scripts
        api_response = api_instance.browse()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptApi->browse: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ScriptXO]**](ScriptXO.md)

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

# **delete1**
> delete1(name)

Delete stored script by name

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
    api_instance = nexus_api_python_client.ScriptApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete stored script by name
        api_instance.delete1(name)
    except ApiException as e:
        print("Exception when calling ScriptApi->delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

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
**204** | Script was deleted |  -  |
**404** | No script with the specified name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit**
> edit(name, body=body)

Update stored script by name

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
    api_instance = nexus_api_python_client.ScriptApi(api_client)
    name = 'name_example' # str | 
body = nexus_api_python_client.ScriptXO() # ScriptXO |  (optional)

    try:
        # Update stored script by name
        api_instance.edit(name, body=body)
    except ApiException as e:
        print("Exception when calling ScriptApi->edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**ScriptXO**](ScriptXO.md)|  | [optional] 

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
**204** | Script was updated |  -  |
**404** | No script with the specified name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> ScriptXO read(name)

Read stored script by name

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
    api_instance = nexus_api_python_client.ScriptApi(api_client)
    name = 'name_example' # str | 

    try:
        # Read stored script by name
        api_response = api_instance.read(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ScriptXO**](ScriptXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | No script with the specified name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run1**
> ScriptResultXO run1(name, body=body)

Run stored script by name

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
    api_instance = nexus_api_python_client.ScriptApi(api_client)
    name = 'name_example' # str | 
body = 'body_example' # str |  (optional)

    try:
        # Run stored script by name
        api_response = api_instance.run1(name, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptApi->run1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**ScriptResultXO**](ScriptResultXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | No script with the specified name |  -  |
**500** | Script execution failed with exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

