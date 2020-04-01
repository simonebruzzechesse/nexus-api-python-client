# HttpClientConnectionAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retries** | **int** | Total retries if the initial connection attempt suffers a timeout | [optional] 
**user_agent_suffix** | **str** | Custom fragment to append to User-Agent header in HTTP requests | [optional] 
**timeout** | **int** | Seconds to wait for activity before stopping and retrying the connection | [optional] 
**enable_circular_redirects** | **bool** | Whether to enable redirects to the same location (may be required by some servers) | [optional] 
**enable_cookies** | **bool** | Whether to allow cookies to be stored and used | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


