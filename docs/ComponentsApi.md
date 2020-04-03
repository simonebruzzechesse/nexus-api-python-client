# nexus_api_python_client.ComponentsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_component**](ComponentsApi.md#delete_component) | **DELETE** /v1/components/{id} | Delete a single component
[**get_component_by_id**](ComponentsApi.md#get_component_by_id) | **GET** /v1/components/{id} | Get a single component
[**get_components**](ComponentsApi.md#get_components) | **GET** /v1/components | List components
[**upload_component**](ComponentsApi.md#upload_component) | **POST** /v1/components | Upload a single component


# **delete_component**
> delete_component(id)

Delete a single component

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
    api_instance = nexus_api_python_client.ComponentsApi(api_client)
    id = 'id_example' # str | ID of the component to delete

    try:
        # Delete a single component
        api_instance.delete_component(id)
    except ApiException as e:
        print("Exception when calling ComponentsApi->delete_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the component to delete | 

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
**204** | Component was successfully deleted |  -  |
**403** | Insufficient permissions to delete component |  -  |
**404** | Component not found |  -  |
**422** | Malformed ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_by_id**
> ComponentXO get_component_by_id(id)

Get a single component

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
    api_instance = nexus_api_python_client.ComponentsApi(api_client)
    id = 'id_example' # str | ID of the component to retrieve

    try:
        # Get a single component
        api_response = api_instance.get_component_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComponentsApi->get_component_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the component to retrieve | 

### Return type

[**ComponentXO**](ComponentXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to get component |  -  |
**404** | Component not found |  -  |
**422** | Malformed ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_components**
> PageComponentXO get_components(repository, continuation_token=continuation_token)

List components

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
    api_instance = nexus_api_python_client.ComponentsApi(api_client)
    repository = 'repository_example' # str | Repository from which you would like to retrieve components
continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)

    try:
        # List components
        api_response = api_instance.get_components(repository, continuation_token=continuation_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComponentsApi->get_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| Repository from which you would like to retrieve components | 
 **continuation_token** | **str**| A token returned by a prior request. If present, the next page of results are returned | [optional] 

### Return type

[**PageComponentXO**](PageComponentXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to list components |  -  |
**422** | Parameter &#39;repository&#39; is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_component**
> upload_component(repository, yum_directory=yum_directory, yum_asset=yum_asset, yum_asset_filename=yum_asset_filename, r_asset=r_asset, r_asset_path_id=r_asset_path_id, rubygems_asset=rubygems_asset, nuget_asset=nuget_asset, raw_directory=raw_directory, raw_asset1=raw_asset1, raw_asset1_filename=raw_asset1_filename, raw_asset2=raw_asset2, raw_asset2_filename=raw_asset2_filename, raw_asset3=raw_asset3, raw_asset3_filename=raw_asset3_filename, pypi_asset=pypi_asset, npm_asset=npm_asset, maven2_group_id=maven2_group_id, maven2_artifact_id=maven2_artifact_id, maven2_version=maven2_version, maven2_generate_pom=maven2_generate_pom, maven2_packaging=maven2_packaging, maven2_asset1=maven2_asset1, maven2_asset1_classifier=maven2_asset1_classifier, maven2_asset1_extension=maven2_asset1_extension, maven2_asset2=maven2_asset2, maven2_asset2_classifier=maven2_asset2_classifier, maven2_asset2_extension=maven2_asset2_extension, maven2_asset3=maven2_asset3, maven2_asset3_classifier=maven2_asset3_classifier, maven2_asset3_extension=maven2_asset3_extension, apt_asset=apt_asset)

Upload a single component

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
    api_instance = nexus_api_python_client.ComponentsApi(api_client)
    repository = 'repository_example' # str | Name of the repository to which you would like to upload the component
yum_directory = 'yum_directory_example' # str | yum Directory (optional)
yum_asset = '/path/to/file' # file | yum Asset  (optional)
yum_asset_filename = 'yum_asset_filename_example' # str | yum Asset  Filename (optional)
r_asset = '/path/to/file' # file | r Asset  (optional)
r_asset_path_id = 'r_asset_path_id_example' # str | r Asset  Package Path (optional)
rubygems_asset = '/path/to/file' # file | rubygems Asset  (optional)
nuget_asset = '/path/to/file' # file | nuget Asset  (optional)
raw_directory = 'raw_directory_example' # str | raw Directory (optional)
raw_asset1 = '/path/to/file' # file | raw Asset 1 (optional)
raw_asset1_filename = 'raw_asset1_filename_example' # str | raw Asset 1 Filename (optional)
raw_asset2 = '/path/to/file' # file | raw Asset 2 (optional)
raw_asset2_filename = 'raw_asset2_filename_example' # str | raw Asset 2 Filename (optional)
raw_asset3 = '/path/to/file' # file | raw Asset 3 (optional)
raw_asset3_filename = 'raw_asset3_filename_example' # str | raw Asset 3 Filename (optional)
pypi_asset = '/path/to/file' # file | pypi Asset  (optional)
npm_asset = '/path/to/file' # file | npm Asset  (optional)
maven2_group_id = 'maven2_group_id_example' # str | maven2 Group ID (optional)
maven2_artifact_id = 'maven2_artifact_id_example' # str | maven2 Artifact ID (optional)
maven2_version = 'maven2_version_example' # str | maven2 Version (optional)
maven2_generate_pom = True # bool | maven2 Generate a POM file with these coordinates (optional)
maven2_packaging = 'maven2_packaging_example' # str | maven2 Packaging (optional)
maven2_asset1 = '/path/to/file' # file | maven2 Asset 1 (optional)
maven2_asset1_classifier = 'maven2_asset1_classifier_example' # str | maven2 Asset 1 Classifier (optional)
maven2_asset1_extension = 'maven2_asset1_extension_example' # str | maven2 Asset 1 Extension (optional)
maven2_asset2 = '/path/to/file' # file | maven2 Asset 2 (optional)
maven2_asset2_classifier = 'maven2_asset2_classifier_example' # str | maven2 Asset 2 Classifier (optional)
maven2_asset2_extension = 'maven2_asset2_extension_example' # str | maven2 Asset 2 Extension (optional)
maven2_asset3 = '/path/to/file' # file | maven2 Asset 3 (optional)
maven2_asset3_classifier = 'maven2_asset3_classifier_example' # str | maven2 Asset 3 Classifier (optional)
maven2_asset3_extension = 'maven2_asset3_extension_example' # str | maven2 Asset 3 Extension (optional)
apt_asset = '/path/to/file' # file | apt Asset  (optional)

    try:
        # Upload a single component
        api_instance.upload_component(repository, yum_directory=yum_directory, yum_asset=yum_asset, yum_asset_filename=yum_asset_filename, r_asset=r_asset, r_asset_path_id=r_asset_path_id, rubygems_asset=rubygems_asset, nuget_asset=nuget_asset, raw_directory=raw_directory, raw_asset1=raw_asset1, raw_asset1_filename=raw_asset1_filename, raw_asset2=raw_asset2, raw_asset2_filename=raw_asset2_filename, raw_asset3=raw_asset3, raw_asset3_filename=raw_asset3_filename, pypi_asset=pypi_asset, npm_asset=npm_asset, maven2_group_id=maven2_group_id, maven2_artifact_id=maven2_artifact_id, maven2_version=maven2_version, maven2_generate_pom=maven2_generate_pom, maven2_packaging=maven2_packaging, maven2_asset1=maven2_asset1, maven2_asset1_classifier=maven2_asset1_classifier, maven2_asset1_extension=maven2_asset1_extension, maven2_asset2=maven2_asset2, maven2_asset2_classifier=maven2_asset2_classifier, maven2_asset2_extension=maven2_asset2_extension, maven2_asset3=maven2_asset3, maven2_asset3_classifier=maven2_asset3_classifier, maven2_asset3_extension=maven2_asset3_extension, apt_asset=apt_asset)
    except ApiException as e:
        print("Exception when calling ComponentsApi->upload_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| Name of the repository to which you would like to upload the component | 
 **yum_directory** | **str**| yum Directory | [optional] 
 **yum_asset** | **file**| yum Asset  | [optional] 
 **yum_asset_filename** | **str**| yum Asset  Filename | [optional] 
 **r_asset** | **file**| r Asset  | [optional] 
 **r_asset_path_id** | **str**| r Asset  Package Path | [optional] 
 **rubygems_asset** | **file**| rubygems Asset  | [optional] 
 **nuget_asset** | **file**| nuget Asset  | [optional] 
 **raw_directory** | **str**| raw Directory | [optional] 
 **raw_asset1** | **file**| raw Asset 1 | [optional] 
 **raw_asset1_filename** | **str**| raw Asset 1 Filename | [optional] 
 **raw_asset2** | **file**| raw Asset 2 | [optional] 
 **raw_asset2_filename** | **str**| raw Asset 2 Filename | [optional] 
 **raw_asset3** | **file**| raw Asset 3 | [optional] 
 **raw_asset3_filename** | **str**| raw Asset 3 Filename | [optional] 
 **pypi_asset** | **file**| pypi Asset  | [optional] 
 **npm_asset** | **file**| npm Asset  | [optional] 
 **maven2_group_id** | **str**| maven2 Group ID | [optional] 
 **maven2_artifact_id** | **str**| maven2 Artifact ID | [optional] 
 **maven2_version** | **str**| maven2 Version | [optional] 
 **maven2_generate_pom** | **bool**| maven2 Generate a POM file with these coordinates | [optional] 
 **maven2_packaging** | **str**| maven2 Packaging | [optional] 
 **maven2_asset1** | **file**| maven2 Asset 1 | [optional] 
 **maven2_asset1_classifier** | **str**| maven2 Asset 1 Classifier | [optional] 
 **maven2_asset1_extension** | **str**| maven2 Asset 1 Extension | [optional] 
 **maven2_asset2** | **file**| maven2 Asset 2 | [optional] 
 **maven2_asset2_classifier** | **str**| maven2 Asset 2 Classifier | [optional] 
 **maven2_asset2_extension** | **str**| maven2 Asset 2 Extension | [optional] 
 **maven2_asset3** | **file**| maven2 Asset 3 | [optional] 
 **maven2_asset3_classifier** | **str**| maven2 Asset 3 Classifier | [optional] 
 **maven2_asset3_extension** | **str**| maven2 Asset 3 Extension | [optional] 
 **apt_asset** | **file**| apt Asset  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Insufficient permissions to upload a component |  -  |
**422** | Parameter &#39;repository&#39; is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

