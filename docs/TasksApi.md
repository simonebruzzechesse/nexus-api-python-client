# openapi_client.TasksApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_by_id**](TasksApi.md#get_task_by_id) | **GET** /v1/tasks/{id} | Get a single task by id
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /v1/tasks | List tasks
[**run**](TasksApi.md#run) | **POST** /v1/tasks/{id}/run | Run task
[**stop**](TasksApi.md#stop) | **POST** /v1/tasks/{id}/stop | Stop task


# **get_task_by_id**
> TaskXO get_task_by_id(id)

Get a single task by id

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
    api_instance = openapi_client.TasksApi(api_client)
    id = 'id_example' # str | Id of the task to get

    try:
        # Get a single task by id
        api_response = api_instance.get_task_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the task to get | 

### Return type

[**TaskXO**](TaskXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | Task not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> PageTaskXO get_tasks(type=type)

List tasks

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
    api_instance = openapi_client.TasksApi(api_client)
    type = 'type_example' # str | Type of the tasks to get (optional)

    try:
        # List tasks
        api_response = api_instance.get_tasks(type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of the tasks to get | [optional] 

### Return type

[**PageTaskXO**](PageTaskXO.md)

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

# **run**
> run(id)

Run task

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
    api_instance = openapi_client.TasksApi(api_client)
    id = 'id_example' # str | Id of the task to run

    try:
        # Run task
        api_instance.run(id)
    except ApiException as e:
        print("Exception when calling TasksApi->run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the task to run | 

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
**204** | Task was run |  -  |
**404** | Task not found |  -  |
**405** | Task is disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> stop(id)

Stop task

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
    api_instance = openapi_client.TasksApi(api_client)
    id = 'id_example' # str | Id of the task to stop

    try:
        # Stop task
        api_instance.stop(id)
    except ApiException as e:
        print("Exception when calling TasksApi->stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the task to stop | 

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
**204** | Task was stopped |  -  |
**404** | Task not found |  -  |
**409** | Unable to stop task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

