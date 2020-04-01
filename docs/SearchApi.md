# openapi_client.SearchApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /v1/search | Search components
[**search_and_download_assets**](SearchApi.md#search_and_download_assets) | **GET** /v1/search/assets/download | Search and download asset
[**search_assets**](SearchApi.md#search_assets) | **GET** /v1/search/assets | Search assets


# **search**
> PageComponentXO search(continuation_token=continuation_token, sort=sort, direction=direction, timeout=timeout, q=q, repository=repository, format=format, group=group, name=name, version=version, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, prerelease=prerelease, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, yum_architecture=yum_architecture)

Search components

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
    api_instance = openapi_client.SearchApi(api_client)
    continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)
sort = 'sort_example' # str | The field to sort the results against, if left empty, a sort based on match weight will be used. (optional)
direction = 'direction_example' # str | The direction to sort records in, defaults to ascending ('asc') for all sort fields, except version, which defaults to descending ('desc') (optional)
timeout = 56 # int | How long to wait for search results in seconds. If this value is not provided, the system default timeout will be used. (optional)
q = 'q_example' # str | Query by keyword (optional)
repository = 'repository_example' # str | Repository name (optional)
format = 'format_example' # str | Query by format (optional)
group = 'group_example' # str | Component group (optional)
name = 'name_example' # str | Component name (optional)
version = 'version_example' # str | Component version (optional)
md5 = 'md5_example' # str | Specific MD5 hash of component's asset (optional)
sha1 = 'sha1_example' # str | Specific SHA-1 hash of component's asset (optional)
sha256 = 'sha256_example' # str | Specific SHA-256 hash of component's asset (optional)
sha512 = 'sha512_example' # str | Specific SHA-512 hash of component's asset (optional)
prerelease = 'prerelease_example' # str | Prerelease version flag (optional)
docker_image_name = 'docker_image_name_example' # str | Docker image name (optional)
docker_image_tag = 'docker_image_tag_example' # str | Docker image tag (optional)
docker_layer_id = 'docker_layer_id_example' # str | Docker layer ID (optional)
docker_content_digest = 'docker_content_digest_example' # str | Docker content digest (optional)
maven_group_id = 'maven_group_id_example' # str | Maven groupId (optional)
maven_artifact_id = 'maven_artifact_id_example' # str | Maven artifactId (optional)
maven_base_version = 'maven_base_version_example' # str | Maven base version (optional)
maven_extension = 'maven_extension_example' # str | Maven extension of component's asset (optional)
maven_classifier = 'maven_classifier_example' # str | Maven classifier of component's asset (optional)
npm_scope = 'npm_scope_example' # str | NPM scope (optional)
nuget_id = 'nuget_id_example' # str | Nuget id (optional)
nuget_tags = 'nuget_tags_example' # str | Nuget tags (optional)
pypi_classifiers = 'pypi_classifiers_example' # str | PyPi classifiers (optional)
pypi_description = 'pypi_description_example' # str | PyPi description (optional)
pypi_keywords = 'pypi_keywords_example' # str | PyPi keywords (optional)
pypi_summary = 'pypi_summary_example' # str | PyPi summary (optional)
rubygems_description = 'rubygems_description_example' # str | RubyGems description (optional)
rubygems_platform = 'rubygems_platform_example' # str | RubyGems platform (optional)
rubygems_summary = 'rubygems_summary_example' # str | RubyGems summary (optional)
yum_architecture = 'yum_architecture_example' # str | Yum architecture (optional)

    try:
        # Search components
        api_response = api_instance.search(continuation_token=continuation_token, sort=sort, direction=direction, timeout=timeout, q=q, repository=repository, format=format, group=group, name=name, version=version, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, prerelease=prerelease, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, yum_architecture=yum_architecture)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuation_token** | **str**| A token returned by a prior request. If present, the next page of results are returned | [optional] 
 **sort** | **str**| The field to sort the results against, if left empty, a sort based on match weight will be used. | [optional] 
 **direction** | **str**| The direction to sort records in, defaults to ascending (&#39;asc&#39;) for all sort fields, except version, which defaults to descending (&#39;desc&#39;) | [optional] 
 **timeout** | **int**| How long to wait for search results in seconds. If this value is not provided, the system default timeout will be used. | [optional] 
 **q** | **str**| Query by keyword | [optional] 
 **repository** | **str**| Repository name | [optional] 
 **format** | **str**| Query by format | [optional] 
 **group** | **str**| Component group | [optional] 
 **name** | **str**| Component name | [optional] 
 **version** | **str**| Component version | [optional] 
 **md5** | **str**| Specific MD5 hash of component&#39;s asset | [optional] 
 **sha1** | **str**| Specific SHA-1 hash of component&#39;s asset | [optional] 
 **sha256** | **str**| Specific SHA-256 hash of component&#39;s asset | [optional] 
 **sha512** | **str**| Specific SHA-512 hash of component&#39;s asset | [optional] 
 **prerelease** | **str**| Prerelease version flag | [optional] 
 **docker_image_name** | **str**| Docker image name | [optional] 
 **docker_image_tag** | **str**| Docker image tag | [optional] 
 **docker_layer_id** | **str**| Docker layer ID | [optional] 
 **docker_content_digest** | **str**| Docker content digest | [optional] 
 **maven_group_id** | **str**| Maven groupId | [optional] 
 **maven_artifact_id** | **str**| Maven artifactId | [optional] 
 **maven_base_version** | **str**| Maven base version | [optional] 
 **maven_extension** | **str**| Maven extension of component&#39;s asset | [optional] 
 **maven_classifier** | **str**| Maven classifier of component&#39;s asset | [optional] 
 **npm_scope** | **str**| NPM scope | [optional] 
 **nuget_id** | **str**| Nuget id | [optional] 
 **nuget_tags** | **str**| Nuget tags | [optional] 
 **pypi_classifiers** | **str**| PyPi classifiers | [optional] 
 **pypi_description** | **str**| PyPi description | [optional] 
 **pypi_keywords** | **str**| PyPi keywords | [optional] 
 **pypi_summary** | **str**| PyPi summary | [optional] 
 **rubygems_description** | **str**| RubyGems description | [optional] 
 **rubygems_platform** | **str**| RubyGems platform | [optional] 
 **rubygems_summary** | **str**| RubyGems summary | [optional] 
 **yum_architecture** | **str**| Yum architecture | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_and_download_assets**
> search_and_download_assets(sort=sort, direction=direction, timeout=timeout, q=q, repository=repository, format=format, group=group, name=name, version=version, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, prerelease=prerelease, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, yum_architecture=yum_architecture)

Search and download asset

Returns a 302 Found with location header field set to download URL. Unless a sort parameter is supplied, the search must return a single asset to receive download URL.

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
    api_instance = openapi_client.SearchApi(api_client)
    sort = 'sort_example' # str | The field to sort the results against, if left empty and more than 1 result is returned, the request will fail. (optional)
direction = 'direction_example' # str | The direction to sort records in, defaults to ascending ('asc') for all sort fields, except version, which defaults to descending ('desc') (optional)
timeout = 56 # int | How long to wait for search results in seconds. If this value is not provided, the system default timeout will be used. (optional)
q = 'q_example' # str | Query by keyword (optional)
repository = 'repository_example' # str | Repository name (optional)
format = 'format_example' # str | Query by format (optional)
group = 'group_example' # str | Component group (optional)
name = 'name_example' # str | Component name (optional)
version = 'version_example' # str | Component version (optional)
md5 = 'md5_example' # str | Specific MD5 hash of component's asset (optional)
sha1 = 'sha1_example' # str | Specific SHA-1 hash of component's asset (optional)
sha256 = 'sha256_example' # str | Specific SHA-256 hash of component's asset (optional)
sha512 = 'sha512_example' # str | Specific SHA-512 hash of component's asset (optional)
prerelease = 'prerelease_example' # str | Prerelease version flag (optional)
docker_image_name = 'docker_image_name_example' # str | Docker image name (optional)
docker_image_tag = 'docker_image_tag_example' # str | Docker image tag (optional)
docker_layer_id = 'docker_layer_id_example' # str | Docker layer ID (optional)
docker_content_digest = 'docker_content_digest_example' # str | Docker content digest (optional)
maven_group_id = 'maven_group_id_example' # str | Maven groupId (optional)
maven_artifact_id = 'maven_artifact_id_example' # str | Maven artifactId (optional)
maven_base_version = 'maven_base_version_example' # str | Maven base version (optional)
maven_extension = 'maven_extension_example' # str | Maven extension of component's asset (optional)
maven_classifier = 'maven_classifier_example' # str | Maven classifier of component's asset (optional)
npm_scope = 'npm_scope_example' # str | NPM scope (optional)
nuget_id = 'nuget_id_example' # str | Nuget id (optional)
nuget_tags = 'nuget_tags_example' # str | Nuget tags (optional)
pypi_classifiers = 'pypi_classifiers_example' # str | PyPi classifiers (optional)
pypi_description = 'pypi_description_example' # str | PyPi description (optional)
pypi_keywords = 'pypi_keywords_example' # str | PyPi keywords (optional)
pypi_summary = 'pypi_summary_example' # str | PyPi summary (optional)
rubygems_description = 'rubygems_description_example' # str | RubyGems description (optional)
rubygems_platform = 'rubygems_platform_example' # str | RubyGems platform (optional)
rubygems_summary = 'rubygems_summary_example' # str | RubyGems summary (optional)
yum_architecture = 'yum_architecture_example' # str | Yum architecture (optional)

    try:
        # Search and download asset
        api_instance.search_and_download_assets(sort=sort, direction=direction, timeout=timeout, q=q, repository=repository, format=format, group=group, name=name, version=version, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, prerelease=prerelease, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, yum_architecture=yum_architecture)
    except ApiException as e:
        print("Exception when calling SearchApi->search_and_download_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field to sort the results against, if left empty and more than 1 result is returned, the request will fail. | [optional] 
 **direction** | **str**| The direction to sort records in, defaults to ascending (&#39;asc&#39;) for all sort fields, except version, which defaults to descending (&#39;desc&#39;) | [optional] 
 **timeout** | **int**| How long to wait for search results in seconds. If this value is not provided, the system default timeout will be used. | [optional] 
 **q** | **str**| Query by keyword | [optional] 
 **repository** | **str**| Repository name | [optional] 
 **format** | **str**| Query by format | [optional] 
 **group** | **str**| Component group | [optional] 
 **name** | **str**| Component name | [optional] 
 **version** | **str**| Component version | [optional] 
 **md5** | **str**| Specific MD5 hash of component&#39;s asset | [optional] 
 **sha1** | **str**| Specific SHA-1 hash of component&#39;s asset | [optional] 
 **sha256** | **str**| Specific SHA-256 hash of component&#39;s asset | [optional] 
 **sha512** | **str**| Specific SHA-512 hash of component&#39;s asset | [optional] 
 **prerelease** | **str**| Prerelease version flag | [optional] 
 **docker_image_name** | **str**| Docker image name | [optional] 
 **docker_image_tag** | **str**| Docker image tag | [optional] 
 **docker_layer_id** | **str**| Docker layer ID | [optional] 
 **docker_content_digest** | **str**| Docker content digest | [optional] 
 **maven_group_id** | **str**| Maven groupId | [optional] 
 **maven_artifact_id** | **str**| Maven artifactId | [optional] 
 **maven_base_version** | **str**| Maven base version | [optional] 
 **maven_extension** | **str**| Maven extension of component&#39;s asset | [optional] 
 **maven_classifier** | **str**| Maven classifier of component&#39;s asset | [optional] 
 **npm_scope** | **str**| NPM scope | [optional] 
 **nuget_id** | **str**| Nuget id | [optional] 
 **nuget_tags** | **str**| Nuget tags | [optional] 
 **pypi_classifiers** | **str**| PyPi classifiers | [optional] 
 **pypi_description** | **str**| PyPi description | [optional] 
 **pypi_keywords** | **str**| PyPi keywords | [optional] 
 **pypi_summary** | **str**| PyPi summary | [optional] 
 **rubygems_description** | **str**| RubyGems description | [optional] 
 **rubygems_platform** | **str**| RubyGems platform | [optional] 
 **rubygems_summary** | **str**| RubyGems summary | [optional] 
 **yum_architecture** | **str**| Yum architecture | [optional] 

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
**400** | Search returned multiple assets, please refine search criteria to find a single asset or use the sort query parameter to retrieve the first result. |  -  |
**404** | Asset search returned no results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_assets**
> PageAssetXO search_assets(continuation_token=continuation_token, sort=sort, direction=direction, timeout=timeout, q=q, repository=repository, format=format, group=group, name=name, version=version, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, prerelease=prerelease, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, yum_architecture=yum_architecture)

Search assets

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
    api_instance = openapi_client.SearchApi(api_client)
    continuation_token = 'continuation_token_example' # str | A token returned by a prior request. If present, the next page of results are returned (optional)
sort = 'sort_example' # str | The field to sort the results against, if left empty, a sort based on match weight will be used. (optional)
direction = 'direction_example' # str | The direction to sort records in, defaults to ascending ('asc') for all sort fields, except version, which defaults to descending ('desc') (optional)
timeout = 56 # int | How long to wait for search results in seconds. If this value is not provided, the system default timeout will be used. (optional)
q = 'q_example' # str | Query by keyword (optional)
repository = 'repository_example' # str | Repository name (optional)
format = 'format_example' # str | Query by format (optional)
group = 'group_example' # str | Component group (optional)
name = 'name_example' # str | Component name (optional)
version = 'version_example' # str | Component version (optional)
md5 = 'md5_example' # str | Specific MD5 hash of component's asset (optional)
sha1 = 'sha1_example' # str | Specific SHA-1 hash of component's asset (optional)
sha256 = 'sha256_example' # str | Specific SHA-256 hash of component's asset (optional)
sha512 = 'sha512_example' # str | Specific SHA-512 hash of component's asset (optional)
prerelease = 'prerelease_example' # str | Prerelease version flag (optional)
docker_image_name = 'docker_image_name_example' # str | Docker image name (optional)
docker_image_tag = 'docker_image_tag_example' # str | Docker image tag (optional)
docker_layer_id = 'docker_layer_id_example' # str | Docker layer ID (optional)
docker_content_digest = 'docker_content_digest_example' # str | Docker content digest (optional)
maven_group_id = 'maven_group_id_example' # str | Maven groupId (optional)
maven_artifact_id = 'maven_artifact_id_example' # str | Maven artifactId (optional)
maven_base_version = 'maven_base_version_example' # str | Maven base version (optional)
maven_extension = 'maven_extension_example' # str | Maven extension of component's asset (optional)
maven_classifier = 'maven_classifier_example' # str | Maven classifier of component's asset (optional)
npm_scope = 'npm_scope_example' # str | NPM scope (optional)
nuget_id = 'nuget_id_example' # str | Nuget id (optional)
nuget_tags = 'nuget_tags_example' # str | Nuget tags (optional)
pypi_classifiers = 'pypi_classifiers_example' # str | PyPi classifiers (optional)
pypi_description = 'pypi_description_example' # str | PyPi description (optional)
pypi_keywords = 'pypi_keywords_example' # str | PyPi keywords (optional)
pypi_summary = 'pypi_summary_example' # str | PyPi summary (optional)
rubygems_description = 'rubygems_description_example' # str | RubyGems description (optional)
rubygems_platform = 'rubygems_platform_example' # str | RubyGems platform (optional)
rubygems_summary = 'rubygems_summary_example' # str | RubyGems summary (optional)
yum_architecture = 'yum_architecture_example' # str | Yum architecture (optional)

    try:
        # Search assets
        api_response = api_instance.search_assets(continuation_token=continuation_token, sort=sort, direction=direction, timeout=timeout, q=q, repository=repository, format=format, group=group, name=name, version=version, md5=md5, sha1=sha1, sha256=sha256, sha512=sha512, prerelease=prerelease, docker_image_name=docker_image_name, docker_image_tag=docker_image_tag, docker_layer_id=docker_layer_id, docker_content_digest=docker_content_digest, maven_group_id=maven_group_id, maven_artifact_id=maven_artifact_id, maven_base_version=maven_base_version, maven_extension=maven_extension, maven_classifier=maven_classifier, npm_scope=npm_scope, nuget_id=nuget_id, nuget_tags=nuget_tags, pypi_classifiers=pypi_classifiers, pypi_description=pypi_description, pypi_keywords=pypi_keywords, pypi_summary=pypi_summary, rubygems_description=rubygems_description, rubygems_platform=rubygems_platform, rubygems_summary=rubygems_summary, yum_architecture=yum_architecture)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchApi->search_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **continuation_token** | **str**| A token returned by a prior request. If present, the next page of results are returned | [optional] 
 **sort** | **str**| The field to sort the results against, if left empty, a sort based on match weight will be used. | [optional] 
 **direction** | **str**| The direction to sort records in, defaults to ascending (&#39;asc&#39;) for all sort fields, except version, which defaults to descending (&#39;desc&#39;) | [optional] 
 **timeout** | **int**| How long to wait for search results in seconds. If this value is not provided, the system default timeout will be used. | [optional] 
 **q** | **str**| Query by keyword | [optional] 
 **repository** | **str**| Repository name | [optional] 
 **format** | **str**| Query by format | [optional] 
 **group** | **str**| Component group | [optional] 
 **name** | **str**| Component name | [optional] 
 **version** | **str**| Component version | [optional] 
 **md5** | **str**| Specific MD5 hash of component&#39;s asset | [optional] 
 **sha1** | **str**| Specific SHA-1 hash of component&#39;s asset | [optional] 
 **sha256** | **str**| Specific SHA-256 hash of component&#39;s asset | [optional] 
 **sha512** | **str**| Specific SHA-512 hash of component&#39;s asset | [optional] 
 **prerelease** | **str**| Prerelease version flag | [optional] 
 **docker_image_name** | **str**| Docker image name | [optional] 
 **docker_image_tag** | **str**| Docker image tag | [optional] 
 **docker_layer_id** | **str**| Docker layer ID | [optional] 
 **docker_content_digest** | **str**| Docker content digest | [optional] 
 **maven_group_id** | **str**| Maven groupId | [optional] 
 **maven_artifact_id** | **str**| Maven artifactId | [optional] 
 **maven_base_version** | **str**| Maven base version | [optional] 
 **maven_extension** | **str**| Maven extension of component&#39;s asset | [optional] 
 **maven_classifier** | **str**| Maven classifier of component&#39;s asset | [optional] 
 **npm_scope** | **str**| NPM scope | [optional] 
 **nuget_id** | **str**| Nuget id | [optional] 
 **nuget_tags** | **str**| Nuget tags | [optional] 
 **pypi_classifiers** | **str**| PyPi classifiers | [optional] 
 **pypi_description** | **str**| PyPi description | [optional] 
 **pypi_keywords** | **str**| PyPi keywords | [optional] 
 **pypi_summary** | **str**| PyPi summary | [optional] 
 **rubygems_description** | **str**| RubyGems description | [optional] 
 **rubygems_platform** | **str**| RubyGems platform | [optional] 
 **rubygems_summary** | **str**| RubyGems summary | [optional] 
 **yum_architecture** | **str**| Yum architecture | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

