# openapi_client.EmailApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_email_configuration**](EmailApi.md#delete_email_configuration) | **DELETE** /beta/email | Disable and clear the email configuration
[**get_email_configuration**](EmailApi.md#get_email_configuration) | **GET** /beta/email | Retrieve the current email configuration
[**set_email_configuration**](EmailApi.md#set_email_configuration) | **PUT** /beta/email | Set the current email configuration
[**test_email_configuration**](EmailApi.md#test_email_configuration) | **POST** /beta/email/verify | Send a test email to the email address provided in the request body


# **delete_email_configuration**
> delete_email_configuration()

Disable and clear the email configuration

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
    api_instance = openapi_client.EmailApi(api_client)
    
    try:
        # Disable and clear the email configuration
        api_instance.delete_email_configuration()
    except ApiException as e:
        print("Exception when calling EmailApi->delete_email_configuration: %s\n" % e)
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
**204** | Email configuration was successfully cleared |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_configuration**
> ApiEmailConfiguration get_email_configuration()

Retrieve the current email configuration

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
    api_instance = openapi_client.EmailApi(api_client)
    
    try:
        # Retrieve the current email configuration
        api_response = api_instance.get_email_configuration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailApi->get_email_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiEmailConfiguration**](ApiEmailConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to retrieve the email configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_email_configuration**
> set_email_configuration(body)

Set the current email configuration

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
    api_instance = openapi_client.EmailApi(api_client)
    body = openapi_client.ApiEmailConfiguration() # ApiEmailConfiguration | 

    try:
        # Set the current email configuration
        api_instance.set_email_configuration(body)
    except ApiException as e:
        print("Exception when calling EmailApi->set_email_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiEmailConfiguration**](ApiEmailConfiguration.md)|  | 

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
**204** | Email configuration was successfully updated |  -  |
**400** | Invalid request |  -  |
**403** | Insufficient permissions to update the email configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_email_configuration**
> test_email_configuration(body)

Send a test email to the email address provided in the request body

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
    api_instance = openapi_client.EmailApi(api_client)
    body = 'body_example' # str | An email address to send a test email to

    try:
        # Send a test email to the email address provided in the request body
        api_instance.test_email_configuration(body)
    except ApiException as e:
        print("Exception when calling EmailApi->test_email_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| An email address to send a test email to | 

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
**200** | Validation was complete, look at the body to determine success |  -  |
**403** | Insufficient permissions to verify the email configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

