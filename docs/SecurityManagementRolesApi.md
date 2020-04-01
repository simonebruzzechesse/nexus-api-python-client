# openapi_client.SecurityManagementRolesApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SecurityManagementRolesApi.md#create) | **POST** /beta/security/roles | Create role
[**delete**](SecurityManagementRolesApi.md#delete) | **DELETE** /beta/security/roles/{id} | Delete role
[**get_role**](SecurityManagementRolesApi.md#get_role) | **GET** /beta/security/roles/{id} | Get role
[**get_roles**](SecurityManagementRolesApi.md#get_roles) | **GET** /beta/security/roles | List roles
[**update**](SecurityManagementRolesApi.md#update) | **PUT** /beta/security/roles/{id} | Update role


# **create**
> RoleXOResponse create(body)

Create role

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
    api_instance = openapi_client.SecurityManagementRolesApi(api_client)
    body = openapi_client.RoleXORequest() # RoleXORequest | A role configuration

    try:
        # Create role
        api_response = api_instance.create(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementRolesApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleXORequest**](RoleXORequest.md)| A role configuration | 

### Return type

[**RoleXOResponse**](RoleXOResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to create role |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete role

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
    api_instance = openapi_client.SecurityManagementRolesApi(api_client)
    id = 'id_example' # str | The id of the role to delete

    try:
        # Delete role
        api_instance.delete(id)
    except ApiException as e:
        print("Exception when calling SecurityManagementRolesApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the role to delete | 

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
**403** | Insufficient permissions to delete role |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleXOResponse get_role(id, source=source)

Get role

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
    api_instance = openapi_client.SecurityManagementRolesApi(api_client)
    id = 'id_example' # str | The id of the role to get
source = 'default' # str | The id of the user source to filter the roles by. Available sources can be fetched using the 'User Sources' endpoint. (optional) (default to 'default')

    try:
        # Get role
        api_response = api_instance.get_role(id, source=source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementRolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the role to get | 
 **source** | **str**| The id of the user source to filter the roles by. Available sources can be fetched using the &#39;User Sources&#39; endpoint. | [optional] [default to &#39;default&#39;]

### Return type

[**RoleXOResponse**](RoleXOResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | The specified source does not exist |  -  |
**403** | Insufficient permissions to read roles |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> list[RoleXOResponse] get_roles(source=source)

List roles

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
    api_instance = openapi_client.SecurityManagementRolesApi(api_client)
    source = 'source_example' # str | The id of the user source to filter the roles by, if supplied. Otherwise roles from all user sources will be returned. (optional)

    try:
        # List roles
        api_response = api_instance.get_roles(source=source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementRolesApi->get_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The id of the user source to filter the roles by, if supplied. Otherwise roles from all user sources will be returned. | [optional] 

### Return type

[**list[RoleXOResponse]**](RoleXOResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | The specified source does not exist |  -  |
**403** | Insufficient permissions to read roles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(id, body)

Update role

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
    api_instance = openapi_client.SecurityManagementRolesApi(api_client)
    id = 'id_example' # str | The id of the role to update
body = openapi_client.RoleXORequest() # RoleXORequest | A role configuration

    try:
        # Update role
        api_instance.update(id, body)
    except ApiException as e:
        print("Exception when calling SecurityManagementRolesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the role to update | 
 **body** | [**RoleXORequest**](RoleXORequest.md)| A role configuration | 

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
**403** | Insufficient permissions to update role |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

