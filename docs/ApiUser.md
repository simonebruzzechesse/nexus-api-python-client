# ApiUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The userid which is required for login. This value cannot be changed. | [optional] 
**first_name** | **str** | The first name of the user. | [optional] 
**last_name** | **str** | The last name of the user. | [optional] 
**email_address** | **str** | The email address associated with the user. | [optional] 
**source** | **str** | The user source which is the origin of this user. This value cannot be changed. | [optional] 
**status** | **str** | The user&#39;s status, e.g. active or disabled. | 
**read_only** | **bool** | Indicates whether the user&#39;s properties could be modified by Nexus. When false only roles are considered during update. | [optional] 
**roles** | **list[str]** | The roles which the user has been assigned within Nexus. | [optional] 
**external_roles** | **list[str]** | The roles which the user has been assigned in an external source, e.g. LDAP group. These cannot be changed within Nexus. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


