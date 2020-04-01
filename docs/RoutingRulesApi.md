# openapi_client.RoutingRulesApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_routing_rule**](RoutingRulesApi.md#create_routing_rule) | **POST** /beta/routing-rules | Create a single routing rule
[**delete_routing_rule**](RoutingRulesApi.md#delete_routing_rule) | **DELETE** /beta/routing-rules/{name} | Delete a single routing rule
[**get_routing_rule**](RoutingRulesApi.md#get_routing_rule) | **GET** /beta/routing-rules/{name} | Get a single routing rule
[**get_routing_rules**](RoutingRulesApi.md#get_routing_rules) | **GET** /beta/routing-rules | List routing rules
[**update_routing_rule**](RoutingRulesApi.md#update_routing_rule) | **PUT** /beta/routing-rules/{name} | Update a single routing rule


# **create_routing_rule**
> create_routing_rule(body)

Create a single routing rule

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
    api_instance = openapi_client.RoutingRulesApi(api_client)
    body = openapi_client.RoutingRuleXO() # RoutingRuleXO | A routing rule configuration

    try:
        # Create a single routing rule
        api_instance.create_routing_rule(body)
    except ApiException as e:
        print("Exception when calling RoutingRulesApi->create_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoutingRuleXO**](RoutingRuleXO.md)| A routing rule configuration | 

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
**204** | Routing rule was successfully created |  -  |
**400** | A routing rule with the same name already exists or required parameters missing |  -  |
**403** | Insufficient permissions to create routing rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_routing_rule**
> delete_routing_rule(name)

Delete a single routing rule

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
    api_instance = openapi_client.RoutingRulesApi(api_client)
    name = 'name_example' # str | The name of the routing rule to delete

    try:
        # Delete a single routing rule
        api_instance.delete_routing_rule(name)
    except ApiException as e:
        print("Exception when calling RoutingRulesApi->delete_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the routing rule to delete | 

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
**204** | Routing rule was successfully deleted |  -  |
**403** | Insufficient permissions to delete routing rules |  -  |
**404** | Routing rule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_rule**
> RoutingRuleXO get_routing_rule(name)

Get a single routing rule

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
    api_instance = openapi_client.RoutingRulesApi(api_client)
    name = 'name_example' # str | The name of the routing rule to get

    try:
        # Get a single routing rule
        api_response = api_instance.get_routing_rule(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutingRulesApi->get_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the routing rule to get | 

### Return type

[**RoutingRuleXO**](RoutingRuleXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to read routing rules |  -  |
**404** | Routing rule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_rules**
> list[RoutingRuleXO] get_routing_rules()

List routing rules

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
    api_instance = openapi_client.RoutingRulesApi(api_client)
    
    try:
        # List routing rules
        api_response = api_instance.get_routing_rules()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutingRulesApi->get_routing_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoutingRuleXO]**](RoutingRuleXO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to read routing rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_routing_rule**
> update_routing_rule(name, body)

Update a single routing rule

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
    api_instance = openapi_client.RoutingRulesApi(api_client)
    name = 'name_example' # str | The name of the routing rule to update
body = openapi_client.RoutingRuleXO() # RoutingRuleXO | A routing rule configuration

    try:
        # Update a single routing rule
        api_instance.update_routing_rule(name, body)
    except ApiException as e:
        print("Exception when calling RoutingRulesApi->update_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the routing rule to update | 
 **body** | [**RoutingRuleXO**](RoutingRuleXO.md)| A routing rule configuration | 

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
**204** | Routing rule was successfully updated |  -  |
**400** | Another routing rule with the same name already exists or required parameters missing |  -  |
**403** | Insufficient permissions to edit routing rules |  -  |
**404** | Routing rule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

