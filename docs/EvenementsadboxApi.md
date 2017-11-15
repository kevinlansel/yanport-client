# swagger_client.EvenementsadboxApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adbox_events_count_group_by_group_by_and_sub_group_by_get**](EvenementsadboxApi.md#adbox_events_count_group_by_group_by_and_sub_group_by_get) | **GET** /adbox-events/count/group-by-{groupBy}-and-{subGroupBy} | Nombre de biens
[**adbox_events_count_group_by_group_by_get**](EvenementsadboxApi.md#adbox_events_count_group_by_group_by_get) | **GET** /adbox-events/count/group-by-{groupBy} | Nombre de biens


# **adbox_events_count_group_by_group_by_and_sub_group_by_get**
> CountResponse adbox_events_count_group_by_group_by_and_sub_group_by_get(group_by, terms_size, sub_group_by, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, status=status, event_types=event_types, tags=tags, property_ids=property_ids, event_time_min=event_time_min, event_time_max=event_time_max)

Nombre de biens

Retourne le nombre de biens regroupés selon 1 critère et 1 sous-critère.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EvenementsadboxApi()
group_by = 'group_by_example' # str | Grouper par
terms_size = 30 # int | Précision des résultats (default to 30)
sub_group_by = 'sub_group_by_example' # str | Grouper par
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)
user_ids = [56] # list[int] | Liste d'identifiants d'utilisateurs (optional)
status = 'status_example' # str | Liste de statuts d'évènements (optional)
event_types = 'event_types_example' # str | Liste de types d'évènements (optional)
tags = ['tags_example'] # list[str] | Identifiants (UUID) de tags (optional)
property_ids = ['property_ids_example'] # list[str] | Identifiants de biens (optional)
event_time_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimal de la création de l'évènement (YYYY-mm-ddTHH:mm:ss) (optional)
event_time_max = '2013-10-20T19:20:30+01:00' # datetime | Date maximal de la création de l'évènement (YYYY-mm-ddTHH:mm:ss) (optional)

try: 
    # Nombre de biens
    api_response = api_instance.adbox_events_count_group_by_group_by_and_sub_group_by_get(group_by, terms_size, sub_group_by, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, status=status, event_types=event_types, tags=tags, property_ids=property_ids, event_time_min=event_time_min, event_time_max=event_time_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvenementsadboxApi->adbox_events_count_group_by_group_by_and_sub_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Grouper par | 
 **terms_size** | **int**| Précision des résultats | [default to 30]
 **sub_group_by** | **str**| Grouper par | 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 
 **user_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;utilisateurs | [optional] 
 **status** | **str**| Liste de statuts d&#39;évènements | [optional] 
 **event_types** | **str**| Liste de types d&#39;évènements | [optional] 
 **tags** | [**list[str]**](str.md)| Identifiants (UUID) de tags | [optional] 
 **property_ids** | [**list[str]**](str.md)| Identifiants de biens | [optional] 
 **event_time_min** | **datetime**| Date minimal de la création de l&#39;évènement (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **event_time_max** | **datetime**| Date maximal de la création de l&#39;évènement (YYYY-mm-ddTHH:mm:ss) | [optional] 

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adbox_events_count_group_by_group_by_get**
> CountResponse adbox_events_count_group_by_group_by_get(group_by, terms_size, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, status=status, event_types=event_types, tags=tags, property_ids=property_ids, event_time_min=event_time_min, event_time_max=event_time_max)

Nombre de biens

Retourne le nombre de biens regroupés selon 1 critère

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EvenementsadboxApi()
group_by = 'group_by_example' # str | Grouper par
terms_size = 30 # int | Précision des résultats (default to 30)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)
user_ids = [56] # list[int] | Liste d'identifiants d'utilisateurs (optional)
status = 'status_example' # str | Liste de statuts d'évènements (optional)
event_types = 'event_types_example' # str | Liste de types d'évènements (optional)
tags = ['tags_example'] # list[str] | Identifiants (UUID) de tags (optional)
property_ids = ['property_ids_example'] # list[str] | Identifiants de biens (optional)
event_time_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimal de la création de l'évènement (YYYY-mm-ddTHH:mm:ss) (optional)
event_time_max = '2013-10-20T19:20:30+01:00' # datetime | Date maximal de la création de l'évènement (YYYY-mm-ddTHH:mm:ss) (optional)

try: 
    # Nombre de biens
    api_response = api_instance.adbox_events_count_group_by_group_by_get(group_by, terms_size, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, status=status, event_types=event_types, tags=tags, property_ids=property_ids, event_time_min=event_time_min, event_time_max=event_time_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvenementsadboxApi->adbox_events_count_group_by_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Grouper par | 
 **terms_size** | **int**| Précision des résultats | [default to 30]
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 
 **user_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;utilisateurs | [optional] 
 **status** | **str**| Liste de statuts d&#39;évènements | [optional] 
 **event_types** | **str**| Liste de types d&#39;évènements | [optional] 
 **tags** | [**list[str]**](str.md)| Identifiants (UUID) de tags | [optional] 
 **property_ids** | [**list[str]**](str.md)| Identifiants de biens | [optional] 
 **event_time_min** | **datetime**| Date minimal de la création de l&#39;évènement (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **event_time_max** | **datetime**| Date maximal de la création de l&#39;évènement (YYYY-mm-ddTHH:mm:ss) | [optional] 

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

