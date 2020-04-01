# openapi_client.SecurityManagementPrivilegesApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_privilege**](SecurityManagementPrivilegesApi.md#create_privilege) | **POST** /beta/security/privileges/application | Create an application type privilege.
[**create_privilege1**](SecurityManagementPrivilegesApi.md#create_privilege1) | **POST** /beta/security/privileges/wildcard | Create a wildcard type privilege.
[**create_privilege2**](SecurityManagementPrivilegesApi.md#create_privilege2) | **POST** /beta/security/privileges/repository-content-selector | Create a repository content selector type privilege.
[**create_privilege3**](SecurityManagementPrivilegesApi.md#create_privilege3) | **POST** /beta/security/privileges/repository-admin | Create a repository admin type privilege.
[**create_privilege4**](SecurityManagementPrivilegesApi.md#create_privilege4) | **POST** /beta/security/privileges/repository-view | Create a repository view type privilege.
[**create_privilege5**](SecurityManagementPrivilegesApi.md#create_privilege5) | **POST** /beta/security/privileges/script | Create a script type privilege.
[**delete_privilege**](SecurityManagementPrivilegesApi.md#delete_privilege) | **DELETE** /beta/security/privileges/{privilegeId} | Delete a privilege by id.
[**get_privilege**](SecurityManagementPrivilegesApi.md#get_privilege) | **GET** /beta/security/privileges/{privilegeId} | Retrieve a privilege by id.
[**get_privileges**](SecurityManagementPrivilegesApi.md#get_privileges) | **GET** /beta/security/privileges | Retrieve a list of privileges.
[**update_privilege**](SecurityManagementPrivilegesApi.md#update_privilege) | **PUT** /beta/security/privileges/wildcard/{privilegeId} | Update a wildcard type privilege.
[**update_privilege1**](SecurityManagementPrivilegesApi.md#update_privilege1) | **PUT** /beta/security/privileges/application/{privilegeId} | Update an application type privilege.
[**update_privilege2**](SecurityManagementPrivilegesApi.md#update_privilege2) | **PUT** /beta/security/privileges/repository-view/{privilegeId} | Update a repository view type privilege.
[**update_privilege3**](SecurityManagementPrivilegesApi.md#update_privilege3) | **PUT** /beta/security/privileges/repository-content-selector/{privilegeId} | Update a repository content selector type privilege.
[**update_privilege4**](SecurityManagementPrivilegesApi.md#update_privilege4) | **PUT** /beta/security/privileges/repository-admin/{privilegeId} | Update a repository admin type privilege.
[**update_privilege5**](SecurityManagementPrivilegesApi.md#update_privilege5) | **PUT** /beta/security/privileges/script/{privilegeId} | Update a script type privilege.


# **create_privilege**
> create_privilege(body=body)

Create an application type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    body = openapi_client.ApiPrivilegeApplicationRequest() # ApiPrivilegeApplicationRequest | The privilege to create. (optional)

    try:
        # Create an application type privilege.
        api_instance.create_privilege(body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiPrivilegeApplicationRequest**](ApiPrivilegeApplicationRequest.md)| The privilege to create. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege1**
> create_privilege1(body=body)

Create a wildcard type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    body = openapi_client.ApiPrivilegeWildcardRequest() # ApiPrivilegeWildcardRequest | The privilege to create. (optional)

    try:
        # Create a wildcard type privilege.
        api_instance.create_privilege1(body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiPrivilegeWildcardRequest**](ApiPrivilegeWildcardRequest.md)| The privilege to create. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege2**
> create_privilege2(body=body)

Create a repository content selector type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    body = openapi_client.ApiPrivilegeRepositoryContentSelectorRequest() # ApiPrivilegeRepositoryContentSelectorRequest | The privilege to create. (optional)

    try:
        # Create a repository content selector type privilege.
        api_instance.create_privilege2(body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiPrivilegeRepositoryContentSelectorRequest**](ApiPrivilegeRepositoryContentSelectorRequest.md)| The privilege to create. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege3**
> create_privilege3(body=body)

Create a repository admin type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    body = openapi_client.ApiPrivilegeRepositoryAdminRequest() # ApiPrivilegeRepositoryAdminRequest | The privilege to create. (optional)

    try:
        # Create a repository admin type privilege.
        api_instance.create_privilege3(body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiPrivilegeRepositoryAdminRequest**](ApiPrivilegeRepositoryAdminRequest.md)| The privilege to create. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege4**
> create_privilege4(body=body)

Create a repository view type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    body = openapi_client.ApiPrivilegeRepositoryViewRequest() # ApiPrivilegeRepositoryViewRequest | The privilege to create. (optional)

    try:
        # Create a repository view type privilege.
        api_instance.create_privilege4(body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiPrivilegeRepositoryViewRequest**](ApiPrivilegeRepositoryViewRequest.md)| The privilege to create. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege5**
> create_privilege5(body=body)

Create a script type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    body = openapi_client.ApiPrivilegeScriptRequest() # ApiPrivilegeScriptRequest | The privilege to create. (optional)

    try:
        # Create a script type privilege.
        api_instance.create_privilege5(body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->create_privilege5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiPrivilegeScriptRequest**](ApiPrivilegeScriptRequest.md)| The privilege to create. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_privilege**
> delete_privilege(privilege_id)

Delete a privilege by id.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to delete.

    try:
        # Delete a privilege by id.
        api_instance.delete_privilege(privilege_id)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->delete_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to delete. | 

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
**400** | The privilege is internal and may not be altered. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privilege**
> ApiPrivilege get_privilege(privilege_id)

Retrieve a privilege by id.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to retrieve.

    try:
        # Retrieve a privilege by id.
        api_response = api_instance.get_privilege(privilege_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->get_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to retrieve. | 

### Return type

[**ApiPrivilege**](ApiPrivilege.md)

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
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privileges**
> list[ApiPrivilege] get_privileges()

Retrieve a list of privileges.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    
    try:
        # Retrieve a list of privileges.
        api_response = api_instance.get_privileges()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->get_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiPrivilege]**](ApiPrivilege.md)

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

# **update_privilege**
> update_privilege(privilege_id, body=body)

Update a wildcard type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to update.
body = openapi_client.ApiPrivilegeWildcardRequest() # ApiPrivilegeWildcardRequest | The privilege to update. (optional)

    try:
        # Update a wildcard type privilege.
        api_instance.update_privilege(privilege_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to update. | 
 **body** | [**ApiPrivilegeWildcardRequest**](ApiPrivilegeWildcardRequest.md)| The privilege to update. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege1**
> update_privilege1(privilege_id, body=body)

Update an application type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to update.
body = openapi_client.ApiPrivilegeApplicationRequest() # ApiPrivilegeApplicationRequest | The privilege to update. (optional)

    try:
        # Update an application type privilege.
        api_instance.update_privilege1(privilege_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to update. | 
 **body** | [**ApiPrivilegeApplicationRequest**](ApiPrivilegeApplicationRequest.md)| The privilege to update. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege2**
> update_privilege2(privilege_id, body=body)

Update a repository view type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to update.
body = openapi_client.ApiPrivilegeRepositoryViewRequest() # ApiPrivilegeRepositoryViewRequest | The privilege to update. (optional)

    try:
        # Update a repository view type privilege.
        api_instance.update_privilege2(privilege_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to update. | 
 **body** | [**ApiPrivilegeRepositoryViewRequest**](ApiPrivilegeRepositoryViewRequest.md)| The privilege to update. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege3**
> update_privilege3(privilege_id, body=body)

Update a repository content selector type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to update.
body = openapi_client.ApiPrivilegeRepositoryContentSelectorRequest() # ApiPrivilegeRepositoryContentSelectorRequest | The privilege to update. (optional)

    try:
        # Update a repository content selector type privilege.
        api_instance.update_privilege3(privilege_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to update. | 
 **body** | [**ApiPrivilegeRepositoryContentSelectorRequest**](ApiPrivilegeRepositoryContentSelectorRequest.md)| The privilege to update. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege4**
> update_privilege4(privilege_id, body=body)

Update a repository admin type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to update.
body = openapi_client.ApiPrivilegeRepositoryAdminRequest() # ApiPrivilegeRepositoryAdminRequest | The privilege to update. (optional)

    try:
        # Update a repository admin type privilege.
        api_instance.update_privilege4(privilege_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to update. | 
 **body** | [**ApiPrivilegeRepositoryAdminRequest**](ApiPrivilegeRepositoryAdminRequest.md)| The privilege to update. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege5**
> update_privilege5(privilege_id, body=body)

Update a script type privilege.

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
    api_instance = openapi_client.SecurityManagementPrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | The id of the privilege to update.
body = openapi_client.ApiPrivilegeScriptRequest() # ApiPrivilegeScriptRequest | The privilege to update. (optional)

    try:
        # Update a script type privilege.
        api_instance.update_privilege5(privilege_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementPrivilegesApi->update_privilege5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**| The id of the privilege to update. | 
 **body** | [**ApiPrivilegeScriptRequest**](ApiPrivilegeScriptRequest.md)| The privilege to update. | [optional] 

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
**400** | Privilege object not configured properly. |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | Privilege not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

