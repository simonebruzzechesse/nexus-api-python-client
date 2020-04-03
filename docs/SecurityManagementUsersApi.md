# nexus_api_python_client.SecurityManagementUsersApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](SecurityManagementUsersApi.md#change_password) | **PUT** /beta/security/users/{userId}/change-password | Change a user&#39;s password.
[**create_user**](SecurityManagementUsersApi.md#create_user) | **POST** /beta/security/users | Create a new user in the default source.
[**delete_user**](SecurityManagementUsersApi.md#delete_user) | **DELETE** /beta/security/users/{userId} | Delete a user.
[**get_users**](SecurityManagementUsersApi.md#get_users) | **GET** /beta/security/users | Retrieve a list of users. Note if the source is not &#39;default&#39; the response is limited to 100 users.
[**update_user**](SecurityManagementUsersApi.md#update_user) | **PUT** /beta/security/users/{userId} | Update an existing user.


# **change_password**
> change_password(user_id, body=body)

Change a user's password.

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
    api_instance = nexus_api_python_client.SecurityManagementUsersApi(api_client)
    user_id = 'user_id_example' # str | The userid the request should apply to.
body = 'body_example' # str | The new password to use. (optional)

    try:
        # Change a user's password.
        api_instance.change_password(user_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The userid the request should apply to. | 
 **body** | **str**| The new password to use. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Password was not supplied in the body of the request |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | User not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> ApiUser create_user(body=body)

Create a new user in the default source.

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
    api_instance = nexus_api_python_client.SecurityManagementUsersApi(api_client)
    body = nexus_api_python_client.ApiCreateUser() # ApiCreateUser | A representation of the user to create. (optional)

    try:
        # Create a new user in the default source.
        api_response = api_instance.create_user(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateUser**](ApiCreateUser.md)| A representation of the user to create. | [optional] 

### Return type

[**ApiUser**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Password was not supplied in the body of the request |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete a user.

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
    api_instance = nexus_api_python_client.SecurityManagementUsersApi(api_client)
    user_id = 'user_id_example' # str | The userid the request should apply to.

    try:
        # Delete a user.
        api_instance.delete_user(user_id)
    except ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The userid the request should apply to. | 

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
**400** | Password was not supplied in the body of the request |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | User or user source not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[ApiUser] get_users(user_id=user_id, source=source)

Retrieve a list of users. Note if the source is not 'default' the response is limited to 100 users.

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
    api_instance = nexus_api_python_client.SecurityManagementUsersApi(api_client)
    user_id = 'user_id_example' # str | An optional term to search userids for. (optional)
source = 'source_example' # str | An optional user source to restrict the search to. (optional)

    try:
        # Retrieve a list of users. Note if the source is not 'default' the response is limited to 100 users.
        api_response = api_instance.get_users(user_id=user_id, source=source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| An optional term to search userids for. | [optional] 
 **source** | **str**| An optional user source to restrict the search to. | [optional] 

### Return type

[**list[ApiUser]**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Password was not supplied in the body of the request |  -  |
**403** | The user does not have permission to perform the operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user_id, body=body)

Update an existing user.

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
    api_instance = nexus_api_python_client.SecurityManagementUsersApi(api_client)
    user_id = 'user_id_example' # str | The userid the request should apply to.
body = nexus_api_python_client.ApiUser() # ApiUser | A representation of the user to update. (optional)

    try:
        # Update an existing user.
        api_instance.update_user(user_id, body=body)
    except ApiException as e:
        print("Exception when calling SecurityManagementUsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The userid the request should apply to. | 
 **body** | [**ApiUser**](ApiUser.md)| A representation of the user to update. | [optional] 

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
**400** | Password was not supplied in the body of the request |  -  |
**403** | The user does not have permission to perform the operation. |  -  |
**404** | User or user source not found in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

