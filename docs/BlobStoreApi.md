# nexus_api_python_client.BlobStoreApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_blob_store**](BlobStoreApi.md#create_blob_store) | **POST** /beta/blobstores/s3 | Create an S3 blob store
[**create_file_blob_store**](BlobStoreApi.md#create_file_blob_store) | **POST** /beta/blobstores/file | Create a file blob store
[**delete_blob_store**](BlobStoreApi.md#delete_blob_store) | **DELETE** /beta/blobstores/{name} | Delete a blob store by name
[**get_blob_store**](BlobStoreApi.md#get_blob_store) | **GET** /beta/blobstores/s3/{name} | Fetch a S3 blob store configuration
[**get_file_blob_store_configuration**](BlobStoreApi.md#get_file_blob_store_configuration) | **GET** /beta/blobstores/file/{name} | Get a file blob store configuration by name
[**list_blob_stores**](BlobStoreApi.md#list_blob_stores) | **GET** /beta/blobstores | List the blob stores
[**quota_status**](BlobStoreApi.md#quota_status) | **GET** /v1/blobstores/{id}/quota-status | Get quota status for a given blob store
[**update_blob_store**](BlobStoreApi.md#update_blob_store) | **PUT** /beta/blobstores/s3/{name} | Update an S3 blob store configuration
[**update_file_blob_store**](BlobStoreApi.md#update_file_blob_store) | **PUT** /beta/blobstores/file/{name} | Update a file blob store configuration by name


# **create_blob_store**
> create_blob_store(body=body)

Create an S3 blob store

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    body = nexus_api_python_client.S3BlobStoreApiModel() # S3BlobStoreApiModel |  (optional)

    try:
        # Create an S3 blob store
        api_instance.create_blob_store(body=body)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->create_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3BlobStoreApiModel**](S3BlobStoreApiModel.md)|  | [optional] 

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
**201** | S3 blob store created |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_blob_store**
> create_file_blob_store(body=body)

Create a file blob store

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    body = nexus_api_python_client.FileBlobStoreApiCreateRequest() # FileBlobStoreApiCreateRequest |  (optional)

    try:
        # Create a file blob store
        api_instance.create_file_blob_store(body=body)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->create_file_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileBlobStoreApiCreateRequest**](FileBlobStoreApiCreateRequest.md)|  | [optional] 

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

# **delete_blob_store**
> delete_blob_store(name)

Delete a blob store by name

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    name = 'name_example' # str | The name of the blob store to delete

    try:
        # Delete a blob store by name
        api_instance.delete_blob_store(name)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->delete_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the blob store to delete | 

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
**0** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob_store**
> get_blob_store(name)

Fetch a S3 blob store configuration

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    name = 'name_example' # str | Name of the blob store configuration to fetch

    try:
        # Fetch a S3 blob store configuration
        api_instance.get_blob_store(name)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->get_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the blob store configuration to fetch | 

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
**200** | OK |  -  |
**400** | Specified S3 blob store doesn&#39;t exist |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_blob_store_configuration**
> FileBlobStoreApiModel get_file_blob_store_configuration(name)

Get a file blob store configuration by name

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    name = 'name_example' # str | The name of the file blob store to read

    try:
        # Get a file blob store configuration by name
        api_response = api_instance.get_file_blob_store_configuration(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->get_file_blob_store_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file blob store to read | 

### Return type

[**FileBlobStoreApiModel**](FileBlobStoreApiModel.md)

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

# **list_blob_stores**
> list[GenericBlobStoreApiResponse] list_blob_stores()

List the blob stores

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    
    try:
        # List the blob stores
        api_response = api_instance.list_blob_stores()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->list_blob_stores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GenericBlobStoreApiResponse]**](GenericBlobStoreApiResponse.md)

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

# **quota_status**
> BlobStoreQuotaResultXO quota_status(id)

Get quota status for a given blob store

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get quota status for a given blob store
        api_response = api_instance.quota_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->quota_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BlobStoreQuotaResultXO**](BlobStoreQuotaResultXO.md)

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

# **update_blob_store**
> update_blob_store(name, body=body)

Update an S3 blob store configuration

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    name = 'name_example' # str | Name of the blob store to update
body = nexus_api_python_client.S3BlobStoreApiModel() # S3BlobStoreApiModel |  (optional)

    try:
        # Update an S3 blob store configuration
        api_instance.update_blob_store(name, body=body)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->update_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the blob store to update | 
 **body** | [**S3BlobStoreApiModel**](S3BlobStoreApiModel.md)|  | [optional] 

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
**204** | S3 blob store updated |  -  |
**400** | Specified S3 blob store doesn&#39;t exist |  -  |
**401** | Authentication required |  -  |
**403** | Insufficient permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_blob_store**
> update_file_blob_store(name, body=body)

Update a file blob store configuration by name

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
    api_instance = nexus_api_python_client.BlobStoreApi(api_client)
    name = 'name_example' # str | The name of the file blob store to update
body = nexus_api_python_client.FileBlobStoreApiUpdateRequest() # FileBlobStoreApiUpdateRequest |  (optional)

    try:
        # Update a file blob store configuration by name
        api_instance.update_file_blob_store(name, body=body)
    except ApiException as e:
        print("Exception when calling BlobStoreApi->update_file_blob_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file blob store to update | 
 **body** | [**FileBlobStoreApiUpdateRequest**](FileBlobStoreApiUpdateRequest.md)|  | [optional] 

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

