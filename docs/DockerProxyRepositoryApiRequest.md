# DockerProxyRepositoryApiRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique identifier for this repository | 
**online** | **bool** | Whether this repository accepts incoming requests | 
**storage** | [**StorageAttributes**](StorageAttributes.md) |  | 
**cleanup** | [**CleanupPolicyAttributes**](CleanupPolicyAttributes.md) |  | [optional] 
**proxy** | [**ProxyAttributes**](ProxyAttributes.md) |  | 
**negative_cache** | [**NegativeCacheAttributes**](NegativeCacheAttributes.md) |  | 
**http_client** | [**HttpClientAttributes**](HttpClientAttributes.md) |  | 
**routing_rule** | **str** |  | [optional] 
**docker** | [**DockerAttributes**](DockerAttributes.md) |  | 
**docker_proxy** | [**DockerProxyAttributes**](DockerProxyAttributes.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


