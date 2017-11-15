# swagger_client.BienssimilairesApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similar_properties_get**](BienssimilairesApi.md#similar_properties_get) | **GET** /similar-properties | Récuperer des biens similaires
[**similar_properties_percentiles_get**](BienssimilairesApi.md#similar_properties_percentiles_get) | **GET** /similar-properties/percentiles | Indicateurs de références
[**similar_properties_query_get**](BienssimilairesApi.md#similar_properties_query_get) | **GET** /similar-properties/query | Paramètres optimaux


# **similar_properties_get**
> InlineResponse2003 similar_properties_get(min_doc_count=min_doc_count, city_ids=city_ids, marketing_types=marketing_types, property_types=property_types, price=price, surface=surface, publication_date_min=publication_date_min, active=active, room_count=room_count, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes)

Récuperer des biens similaires

Retourne les biens similaires correspondants aux critères demandés.

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
api_instance = swagger_client.BienssimilairesApi()
min_doc_count = 10 # int | Le nombre minimum de documents a matcher (optional) (default to 10)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
price = 1.2 # float | Prix (optional)
surface = 1.2 # float | Surface (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
active = true # bool | En cours de publication (optional) (default to true)
room_count = 56 # int | Nombre de pièces (optional)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)

try: 
    # Récuperer des biens similaires
    api_response = api_instance.similar_properties_get(min_doc_count=min_doc_count, city_ids=city_ids, marketing_types=marketing_types, property_types=property_types, price=price, surface=surface, publication_date_min=publication_date_min, active=active, room_count=room_count, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BienssimilairesApi->similar_properties_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_doc_count** | **int**| Le nombre minimum de documents a matcher | [optional] [default to 10]
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **price** | **float**| Prix | [optional] 
 **surface** | **float**| Surface | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **active** | **bool**| En cours de publication | [optional] [default to true]
 **room_count** | **int**| Nombre de pièces | [optional] 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar_properties_percentiles_get**
> Percentiles similar_properties_percentiles_get(field, percentiles, min_doc_count=min_doc_count, city_ids=city_ids, marketing_types=marketing_types, property_types=property_types, price=price, surface=surface, publication_date_min=publication_date_min, active=active, room_count=room_count, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes)

Indicateurs de références

Permet de récupérer les indicateurs de références des biens similaires

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
api_instance = swagger_client.BienssimilairesApi()
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
percentiles = [3.4] # list[float] | Les percentiles (ex: 10.0, 50.0, 90.0)
min_doc_count = 10 # int | Le nombre minimum de documents a matcher (optional) (default to 10)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
price = 1.2 # float | Prix (optional)
surface = 1.2 # float | Surface (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
active = true # bool | En cours de publication (optional) (default to true)
room_count = 56 # int | Nombre de pièces (optional)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)

try: 
    # Indicateurs de références
    api_response = api_instance.similar_properties_percentiles_get(field, percentiles, min_doc_count=min_doc_count, city_ids=city_ids, marketing_types=marketing_types, property_types=property_types, price=price, surface=surface, publication_date_min=publication_date_min, active=active, room_count=room_count, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BienssimilairesApi->similar_properties_percentiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **percentiles** | [**list[float]**](float.md)| Les percentiles (ex: 10.0, 50.0, 90.0) | 
 **min_doc_count** | **int**| Le nombre minimum de documents a matcher | [optional] [default to 10]
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **price** | **float**| Prix | [optional] 
 **surface** | **float**| Surface | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **active** | **bool**| En cours de publication | [optional] [default to true]
 **room_count** | **int**| Nombre de pièces | [optional] 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 

### Return type

[**Percentiles**](Percentiles.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar_properties_query_get**
> PropertySearchQuery similar_properties_query_get(min_doc_count=min_doc_count, city_ids=city_ids, marketing_types=marketing_types, property_types=property_types, price=price, surface=surface, publication_date_min=publication_date_min, active=active, room_count=room_count, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes)

Paramètres optimaux

Permet de récupérer les paramètres de requêtes optimaux pour avoir au minimum X biens similaires.

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
api_instance = swagger_client.BienssimilairesApi()
min_doc_count = 10 # int | Le nombre minimum de documents a matcher (optional) (default to 10)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
price = 1.2 # float | Prix (optional)
surface = 1.2 # float | Surface (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
active = true # bool | En cours de publication (optional) (default to true)
room_count = 56 # int | Nombre de pièces (optional)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)

try: 
    # Paramètres optimaux
    api_response = api_instance.similar_properties_query_get(min_doc_count=min_doc_count, city_ids=city_ids, marketing_types=marketing_types, property_types=property_types, price=price, surface=surface, publication_date_min=publication_date_min, active=active, room_count=room_count, _from=_from, size=size, sort=sort, includes=includes, excludes=excludes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BienssimilairesApi->similar_properties_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_doc_count** | **int**| Le nombre minimum de documents a matcher | [optional] [default to 10]
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **price** | **float**| Prix | [optional] 
 **surface** | **float**| Surface | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **active** | **bool**| En cours de publication | [optional] [default to true]
 **room_count** | **int**| Nombre de pièces | [optional] 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 

### Return type

[**PropertySearchQuery**](PropertySearchQuery.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

