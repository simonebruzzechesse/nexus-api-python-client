# openapi_client.RepositoryManagementApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository1**](RepositoryManagementApi.md#create_repository1) | **POST** /beta/repositories/apt/hosted | 
[**create_repository10**](RepositoryManagementApi.md#create_repository10) | **POST** /beta/repositories/docker/hosted | 
[**create_repository11**](RepositoryManagementApi.md#create_repository11) | **POST** /beta/repositories/gitlfs/hosted | 
[**create_repository2**](RepositoryManagementApi.md#create_repository2) | **POST** /beta/repositories/apt/proxy | 
[**create_repository3**](RepositoryManagementApi.md#create_repository3) | **POST** /beta/repositories/go/group | 
[**create_repository4**](RepositoryManagementApi.md#create_repository4) | **POST** /beta/repositories/go/proxy | 
[**create_repository5**](RepositoryManagementApi.md#create_repository5) | **POST** /beta/repositories/bower/group | 
[**create_repository6**](RepositoryManagementApi.md#create_repository6) | **POST** /beta/repositories/bower/proxy | 
[**create_repository7**](RepositoryManagementApi.md#create_repository7) | **POST** /beta/repositories/bower/hosted | 
[**create_repository8**](RepositoryManagementApi.md#create_repository8) | **POST** /beta/repositories/docker/group | 
[**create_repository9**](RepositoryManagementApi.md#create_repository9) | **POST** /beta/repositories/docker/proxy | 
[**delete_repository**](RepositoryManagementApi.md#delete_repository) | **DELETE** /beta/repositories/{repositoryName} | Delete repository of any format
[**disable_repository_health_check**](RepositoryManagementApi.md#disable_repository_health_check) | **DELETE** /beta/repositories/{repositoryName}/health-check | Disable Repository Health Check. Proxy repositories only.
[**enable_repository_health_check**](RepositoryManagementApi.md#enable_repository_health_check) | **POST** /beta/repositories/{repositoryName}/health-check | Enable Repository Health Check. Proxy repositories only.
[**get_repositories**](RepositoryManagementApi.md#get_repositories) | **GET** /beta/repositories | List repositories
[**invalidate_cache**](RepositoryManagementApi.md#invalidate_cache) | **POST** /beta/repositories/{repositoryName}/invalidate-cache | Invalidate repository cache. Proxy or group repositories only.
[**rebuild_index**](RepositoryManagementApi.md#rebuild_index) | **POST** /beta/repositories/{repositoryName}/rebuild-index | Schedule a &#39;Repair - Rebuild repository search&#39; Task. Hosted or proxy repositories only.
[**update_repository1**](RepositoryManagementApi.md#update_repository1) | **PUT** /beta/repositories/apt/hosted/{repositoryName} | 
[**update_repository10**](RepositoryManagementApi.md#update_repository10) | **PUT** /beta/repositories/docker/hosted/{repositoryName} | 
[**update_repository11**](RepositoryManagementApi.md#update_repository11) | **PUT** /beta/repositories/gitlfs/hosted/{repositoryName} | 
[**update_repository2**](RepositoryManagementApi.md#update_repository2) | **PUT** /beta/repositories/apt/proxy/{repositoryName} | 
[**update_repository3**](RepositoryManagementApi.md#update_repository3) | **PUT** /beta/repositories/go/group/{repositoryName} | 
[**update_repository4**](RepositoryManagementApi.md#update_repository4) | **PUT** /beta/repositories/go/proxy/{repositoryName} | 
[**update_repository5**](RepositoryManagementApi.md#update_repository5) | **PUT** /beta/repositories/bower/group/{repositoryName} | 
[**update_repository6**](RepositoryManagementApi.md#update_repository6) | **PUT** /beta/repositories/bower/proxy/{repositoryName} | 
[**update_repository7**](RepositoryManagementApi.md#update_repository7) | **PUT** /beta/repositories/bower/hosted/{repositoryName} | 
[**update_repository8**](RepositoryManagementApi.md#update_repository8) | **PUT** /beta/repositories/docker/group/{repositoryName} | 
[**update_repository9**](RepositoryManagementApi.md#update_repository9) | **PUT** /beta/repositories/docker/proxy/{repositoryName} | 


# **create_repository1**
> create_repository1(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.AptHostedRepositoryApiRequest() # AptHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository1(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AptHostedRepositoryApiRequest**](AptHostedRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository10**
> create_repository10(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.DockerHostedRepositoryApiRequest() # DockerHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository10(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerHostedRepositoryApiRequest**](DockerHostedRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository11**
> create_repository11(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.GitLfsHostedRepositoryApiRequest() # GitLfsHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository11(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitLfsHostedRepositoryApiRequest**](GitLfsHostedRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository2**
> create_repository2(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.AptProxyRepositoryApiRequest() # AptProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository2(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AptProxyRepositoryApiRequest**](AptProxyRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository3**
> create_repository3(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.GolangGroupRepositoryApiRequest() # GolangGroupRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository3(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GolangGroupRepositoryApiRequest**](GolangGroupRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository4**
> create_repository4(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.GolangProxyRepositoryApiRequest() # GolangProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository4(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GolangProxyRepositoryApiRequest**](GolangProxyRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository5**
> create_repository5(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.BowerGroupRepositoryApiRequest() # BowerGroupRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository5(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BowerGroupRepositoryApiRequest**](BowerGroupRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository6**
> create_repository6(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.BowerProxyRepositoryApiRequest() # BowerProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository6(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BowerProxyRepositoryApiRequest**](BowerProxyRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository7**
> create_repository7(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.BowerHostedRepositoryApiRequest() # BowerHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository7(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BowerHostedRepositoryApiRequest**](BowerHostedRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository8**
> create_repository8(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.DockerGroupRepositoryApiRequest() # DockerGroupRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository8(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerGroupRepositoryApiRequest**](DockerGroupRepositoryApiRequest.md)|  | [optional] 

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

# **create_repository9**
> create_repository9(body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    body = openapi_client.DockerProxyRepositoryApiRequest() # DockerProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.create_repository9(body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->create_repository9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DockerProxyRepositoryApiRequest**](DockerProxyRepositoryApiRequest.md)|  | [optional] 

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

# **delete_repository**
> delete_repository(repository_name)

Delete repository of any format

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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | Name of the repository to delete

    try:
        # Delete repository of any format
        api_instance.delete_repository(repository_name)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->delete_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to delete | 

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
**204** | Repository deleted |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |
**404** | Repository not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_repository_health_check**
> disable_repository_health_check(repository_name)

Disable Repository Health Check. Proxy repositories only.

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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | Name of the repository to disable Repository Health Check for

    try:
        # Disable Repository Health Check. Proxy repositories only.
        api_instance.disable_repository_health_check(repository_name)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->disable_repository_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to disable Repository Health Check for | 

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
**204** | Repository Health Check disabled |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |
**404** | Repository not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_repository_health_check**
> enable_repository_health_check(repository_name)

Enable Repository Health Check. Proxy repositories only.

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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | Name of the repository to enable Repository Health Check for

    try:
        # Enable Repository Health Check. Proxy repositories only.
        api_instance.enable_repository_health_check(repository_name)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->enable_repository_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to enable Repository Health Check for | 

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
**204** | Repository Health Check enabled |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |
**404** | Repository not found |  -  |
**409** | EULA not accepted or Repository Health Check capability not active |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories**
> get_repositories()

List repositories

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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    
    try:
        # List repositories
        api_instance.get_repositories()
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->get_repositories: %s\n" % e)
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
**200** | Repositories list returned |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_cache**
> invalidate_cache(repository_name)

Invalidate repository cache. Proxy or group repositories only.

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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | Name of the repository to invalidate cache

    try:
        # Invalidate repository cache. Proxy or group repositories only.
        api_instance.invalidate_cache(repository_name)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->invalidate_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to invalidate cache | 

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
**204** | Repository cache invalidated |  -  |
**400** | Repository is not of proxy or group type |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |
**404** | Repository not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild_index**
> rebuild_index(repository_name)

Schedule a 'Repair - Rebuild repository search' Task. Hosted or proxy repositories only.

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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | Name of the repository to rebuild index

    try:
        # Schedule a 'Repair - Rebuild repository search' Task. Hosted or proxy repositories only.
        api_instance.rebuild_index(repository_name)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->rebuild_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Name of the repository to rebuild index | 

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
**204** | Repository search index rebuild has been scheduled |  -  |
**400** | Repository is not of hosted or proxy type |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |
**404** | Repository not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repository1**
> update_repository1(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.AptHostedRepositoryApiRequest() # AptHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository1(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**AptHostedRepositoryApiRequest**](AptHostedRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository10**
> update_repository10(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.DockerHostedRepositoryApiRequest() # DockerHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository10(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**DockerHostedRepositoryApiRequest**](DockerHostedRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository11**
> update_repository11(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.GitLfsHostedRepositoryApiRequest() # GitLfsHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository11(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**GitLfsHostedRepositoryApiRequest**](GitLfsHostedRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository2**
> update_repository2(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.AptProxyRepositoryApiRequest() # AptProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository2(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**AptProxyRepositoryApiRequest**](AptProxyRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository3**
> update_repository3(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.GolangGroupRepositoryApiRequest() # GolangGroupRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository3(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**GolangGroupRepositoryApiRequest**](GolangGroupRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository4**
> update_repository4(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.GolangProxyRepositoryApiRequest() # GolangProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository4(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**GolangProxyRepositoryApiRequest**](GolangProxyRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository5**
> update_repository5(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.BowerGroupRepositoryApiRequest() # BowerGroupRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository5(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**BowerGroupRepositoryApiRequest**](BowerGroupRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository6**
> update_repository6(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.BowerProxyRepositoryApiRequest() # BowerProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository6(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**BowerProxyRepositoryApiRequest**](BowerProxyRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository7**
> update_repository7(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.BowerHostedRepositoryApiRequest() # BowerHostedRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository7(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**BowerHostedRepositoryApiRequest**](BowerHostedRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository8**
> update_repository8(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.DockerGroupRepositoryApiRequest() # DockerGroupRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository8(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**DockerGroupRepositoryApiRequest**](DockerGroupRepositoryApiRequest.md)|  | [optional] 

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

# **update_repository9**
> update_repository9(repository_name, body=body)



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
    api_instance = openapi_client.RepositoryManagementApi(api_client)
    repository_name = 'repository_name_example' # str | 
body = openapi_client.DockerProxyRepositoryApiRequest() # DockerProxyRepositoryApiRequest |  (optional)

    try:
        api_instance.update_repository9(repository_name, body=body)
    except ApiException as e:
        print("Exception when calling RepositoryManagementApi->update_repository9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**|  | 
 **body** | [**DockerProxyRepositoryApiRequest**](DockerProxyRepositoryApiRequest.md)|  | [optional] 

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

