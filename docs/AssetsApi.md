# openapi_client.AssetsApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset**](AssetsApi.md#delete_asset) | **DELETE** /v1/assets/{id} | Delete a single asset
[**get_asset_by_id**](AssetsApi.md#get_asset_by_id) | **GET** /v1/assets/{id} | Get a single asset
[**get_assets**](AssetsApi.md#get_assets) | **GET** /v1/assets | List assets


# **delete_asset**
> delete_asset(id)

Delete a single asset

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
    api_instance = openapi_client.AssetsApi(api_client)
    id = 'id_example' # str | Id of the asset to delete

    try:
        # Delete a single asset
        api_instance.delete_asset(id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the asset to delete | 

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
**204** | Asset was successfully deleted |  -  |
**403** | Insufficient permissions to delete asset |  -  |
**404** | Asset not found |  -  |
**422** | Malformed ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> AssetXO get_asset_by_id(id)

Get a single asset

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
    api_instance = openapi_client.AssetsApi(api_client)
    id = 'id_example' # str | Id of the asset to get

    try:
        # Get a single asset
        api_response = api_instance.get_asset_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_asset_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the asset to get | 

### Return type

[**AssetXO**](AssetXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to get asset |  -  |
**404** | Asset not found |  -  |
**422** | Malformed ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> PageAssetXO get_assets(repository, continuation_token=continuation_token)

List assets

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
    api_instance = openapi_client.AssetsApi(api_client)
    repository = 'repository_example' # str | Repository from which you would like to retrieve assets.
continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)

    try:
        # List assets
        api_response = api_instance.get_assets(repository, continuation_token=continuation_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**| Repository from which you would like to retrieve assets. | 
 **continuation_token** | **str**| A token returned by a prior request. If present, the next page of results are returned | [optional] 

### Return type

[**PageAssetXO**](PageAssetXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to list assets |  -  |
**422** | Parameter &#39;repository&#39; is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

