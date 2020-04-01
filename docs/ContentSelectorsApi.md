# openapi_client.ContentSelectorsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_selector**](ContentSelectorsApi.md#create_content_selector) | **POST** /beta/security/content-selectors | Create a new content selector
[**delete_content_selector**](ContentSelectorsApi.md#delete_content_selector) | **DELETE** /beta/security/content-selectors/{name} | Delete a content selector
[**get_content_selector**](ContentSelectorsApi.md#get_content_selector) | **GET** /beta/security/content-selectors/{name} | Get a content selector by id
[**get_content_selectors**](ContentSelectorsApi.md#get_content_selectors) | **GET** /beta/security/content-selectors | List Content Selectors
[**update_content_selector**](ContentSelectorsApi.md#update_content_selector) | **PUT** /beta/security/content-selectors/{name} | Update a content selector


# **create_content_selector**
> create_content_selector(body=body)

Create a new content selector

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
    api_instance = openapi_client.ContentSelectorsApi(api_client)
    body = openapi_client.ContentSelectorApiCreateRequest() # ContentSelectorApiCreateRequest |  (optional)

    try:
        # Create a new content selector
        api_instance.create_content_selector(body=body)
    except ApiException as e:
        print("Exception when calling ContentSelectorsApi->create_content_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentSelectorApiCreateRequest**](ContentSelectorApiCreateRequest.md)|  | [optional] 

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
**204** | Content selector successfully created |  -  |
**400** | Invalid request |  -  |
**403** | Insufficient permissions to create content selectors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_selector**
> delete_content_selector(name)

Delete a content selector

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
    api_instance = openapi_client.ContentSelectorsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete a content selector
        api_instance.delete_content_selector(name)
    except ApiException as e:
        print("Exception when calling ContentSelectorsApi->delete_content_selector: %s\n" % e)
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
**204** | Content selector deleted successfully |  -  |
**400** | Invalid request |  -  |
**403** | Insufficient permissions to delete the content selector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_selector**
> get_content_selector(name)

Get a content selector by id

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
    api_instance = openapi_client.ContentSelectorsApi(api_client)
    name = 'name_example' # str | The content selector name

    try:
        # Get a content selector by id
        api_instance.get_content_selector(name)
    except ApiException as e:
        print("Exception when calling ContentSelectorsApi->get_content_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The content selector name | 

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
**200** | successful operation |  -  |
**403** | Insufficient permissions to read the content selector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_selectors**
> get_content_selectors()

List Content Selectors

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
    api_instance = openapi_client.ContentSelectorsApi(api_client)
    
    try:
        # List Content Selectors
        api_instance.get_content_selectors()
    except ApiException as e:
        print("Exception when calling ContentSelectorsApi->get_content_selectors: %s\n" % e)
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
**200** | successful operation |  -  |
**403** | Insufficient permissions to read content selectors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_selector**
> update_content_selector(name, body=body)

Update a content selector

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
    api_instance = openapi_client.ContentSelectorsApi(api_client)
    name = 'name_example' # str | The content selector name
body = openapi_client.ContentSelectorApiUpdateRequest() # ContentSelectorApiUpdateRequest |  (optional)

    try:
        # Update a content selector
        api_instance.update_content_selector(name, body=body)
    except ApiException as e:
        print("Exception when calling ContentSelectorsApi->update_content_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The content selector name | 
 **body** | [**ContentSelectorApiUpdateRequest**](ContentSelectorApiUpdateRequest.md)|  | [optional] 

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
**204** | Content selector updated successfully |  -  |
**400** | Invalid request |  -  |
**403** | Insufficient permissions to update the content selector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

