# UpdateLdapServerXo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LDAP server name | 
**protocol** | **str** | LDAP server connection Protocol to use | 
**use_trust_store** | **bool** | Whether to use certificates stored in NXRM&#39;s truststore | [optional] 
**host** | **str** | LDAP server connection hostname | 
**port** | **int** | LDAP server connection port to use | 
**search_base** | **str** | LDAP location to be added to the connection URL | 
**auth_scheme** | **str** | Authentication scheme used for connecting to LDAP server | 
**auth_realm** | **str** | The SASL realm to bind to. Required if authScheme is CRAM_MD5 or DIGEST_MD5 | [optional] 
**auth_username** | **str** | This must be a fully qualified username if simple authentication is used. Required if authScheme other than none. | [optional] 
**connection_timeout_seconds** | **int** | How long to wait before timeout | 
**connection_retry_delay_seconds** | **int** | How long to wait before retrying | 
**max_incidents_count** | **int** | How many retry attempts | 
**user_base_dn** | **str** | The relative DN where user objects are found (e.g. ou&#x3D;people). This value will have the Search base DN value appended to form the full User search base DN. | [optional] 
**user_subtree** | **bool** | Are users located in structures below the user base DN? | [optional] 
**user_object_class** | **str** | LDAP class for user objects | [optional] 
**user_ldap_filter** | **str** | LDAP search filter to limit user search | [optional] 
**user_id_attribute** | **str** | This is used to find a user given its user ID | [optional] 
**user_real_name_attribute** | **str** | This is used to find a real name given the user ID | [optional] 
**user_email_address_attribute** | **str** | This is used to find an email address given the user ID | [optional] 
**user_password_attribute** | **str** | If this field is blank the user will be authenticated against a bind with the LDAP server | [optional] 
**ldap_groups_as_roles** | **bool** | Denotes whether LDAP assigned roles are used as NXRM roles | [optional] 
**group_type** | **str** | Defines a type of groups used: static (a group contains a list of users) or dynamic (a user contains a list of groups). Required if ldapGroupsAsRoles is true. | 
**group_base_dn** | **str** | The relative DN where group objects are found (e.g. ou&#x3D;Group). This value will have the Search base DN value appended to form the full Group search base DN. | [optional] 
**group_subtree** | **bool** | Are groups located in structures below the group base DN | [optional] 
**group_object_class** | **str** | LDAP class for group objects. Required if groupType is static | [optional] 
**group_id_attribute** | **str** | This field specifies the attribute of the Object class that defines the Group ID. Required if groupType is static | [optional] 
**group_member_attribute** | **str** | LDAP attribute containing the usernames for the group. Required if groupType is static | [optional] 
**group_member_format** | **str** | The format of user ID stored in the group member attribute. Required if groupType is static | [optional] 
**user_member_of_attribute** | **str** | Set this to the attribute used to store the attribute which holds groups DN in the user object. Required if groupType is dynamic | [optional] 
**auth_password** | **str** | The password to bind with. Required if authScheme other than none. | 
**id** | **str** | LDAP server ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


