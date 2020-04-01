# openapi_client.SecurityCertificatesApi

All URIs are relative to *http://localhost/service/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_certificate**](SecurityCertificatesApi.md#add_certificate) | **POST** /beta/security/ssl/truststore | Add a certificate to the trust store.
[**get_trust_store_certificates**](SecurityCertificatesApi.md#get_trust_store_certificates) | **GET** /beta/security/ssl/truststore | Retrieve a list of certificates added to the trust store.
[**remove_certificate**](SecurityCertificatesApi.md#remove_certificate) | **DELETE** /beta/security/ssl/truststore/{id} | Remove a certificate in the trust store.
[**retrieve_certificate**](SecurityCertificatesApi.md#retrieve_certificate) | **GET** /beta/security/ssl | Helper method to retrieve certificate details from a remote system.


# **add_certificate**
> object add_certificate(body=body)

Add a certificate to the trust store.

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
    api_instance = openapi_client.SecurityCertificatesApi(api_client)
    body = 'body_example' # str | The certificate to add encoded in PEM format (optional)

    try:
        # Add a certificate to the trust store.
        api_response = api_instance.add_certificate(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityCertificatesApi->add_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| The certificate to add encoded in PEM format | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The certificate was successfully added. |  -  |
**403** | Insufficient permissions to add certificate to the trust store. |  -  |
**409** | The certificate already exists in the system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trust_store_certificates**
> list[ApiCertificate] get_trust_store_certificates()

Retrieve a list of certificates added to the trust store.

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
    api_instance = openapi_client.SecurityCertificatesApi(api_client)
    
    try:
        # Retrieve a list of certificates added to the trust store.
        api_response = api_instance.get_trust_store_certificates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityCertificatesApi->get_trust_store_certificates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiCertificate]**](ApiCertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Insufficient permissions to list certificates in the trust store. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_certificate**
> remove_certificate(id)

Remove a certificate in the trust store.

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
    api_instance = openapi_client.SecurityCertificatesApi(api_client)
    id = 'id_example' # str | The id of the certificate that should be removed.

    try:
        # Remove a certificate in the trust store.
        api_instance.remove_certificate(id)
    except ApiException as e:
        print("Exception when calling SecurityCertificatesApi->remove_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the certificate that should be removed. | 

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
**403** | Insufficient permissions to remove certificate from the trust store |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_certificate**
> ApiCertificate retrieve_certificate(host, port=port, protocol_hint=protocol_hint)

Helper method to retrieve certificate details from a remote system.

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
    api_instance = openapi_client.SecurityCertificatesApi(api_client)
    host = 'host_example' # str | The remote system's host name
port = 443 # int | The port on the remote system to connect to (optional) (default to 443)
protocol_hint = 'protocol_hint_example' # str | An optional hint of the protocol to try for the connection (optional)

    try:
        # Helper method to retrieve certificate details from a remote system.
        api_response = api_instance.retrieve_certificate(host, port=port, protocol_hint=protocol_hint)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityCertificatesApi->retrieve_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| The remote system&#39;s host name | 
 **port** | **int**| The port on the remote system to connect to | [optional] [default to 443]
 **protocol_hint** | **str**| An optional hint of the protocol to try for the connection | [optional] 

### Return type

[**ApiCertificate**](ApiCertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | A certificate could not be retrieved, see the message for details. |  -  |
**403** | Insufficient permissions to retrieve remote certificate. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

