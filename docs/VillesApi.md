# swagger_client.VillesApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cities_get**](VillesApi.md#cities_get) | **GET** /cities | Rechercher des villes
[**cities_id_get**](VillesApi.md#cities_id_get) | **GET** /cities/{id} | Récupérer une ville (ID)
[**cities_ids_get**](VillesApi.md#cities_ids_get) | **GET** /cities/ids | Récupérer des villes (ID)


# **cities_get**
> InlineResponse2001 cities_get(_from=_from, size=size, sort=sort, q=q, lat=lat, lng=lng, radius=radius)

Rechercher des villes

Récupérer des villes selon différents critères

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
api_instance = swagger_client.VillesApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
lat = 1.2 # float | Latitude (optional)
lng = 1.2 # float | Longitude (optional)
radius = '10m' # str | Radius (optional) (default to 10m)

try: 
    # Rechercher des villes
    api_response = api_instance.cities_get(_from=_from, size=size, sort=sort, q=q, lat=lat, lng=lng, radius=radius)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VillesApi->cities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **lat** | **float**| Latitude | [optional] 
 **lng** | **float**| Longitude | [optional] 
 **radius** | **str**| Radius | [optional] [default to 10m]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cities_id_get**
> City cities_id_get(id)

Récupérer une ville (ID)

Récupérer une ville par son identifiant

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
api_instance = swagger_client.VillesApi()
id = 56 # int | L'identifiant de la ville

try: 
    # Récupérer une ville (ID)
    api_response = api_instance.cities_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VillesApi->cities_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de la ville | 

### Return type

[**City**](City.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cities_ids_get**
> list[City] cities_ids_get(ids)

Récupérer des villes (ID)

Récupérer des villes par leur identifiant

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
api_instance = swagger_client.VillesApi()
ids = [56] # list[int] | Liste d'identifiants

try: 
    # Récupérer des villes (ID)
    api_response = api_instance.cities_ids_get(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VillesApi->cities_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Liste d&#39;identifiants | 

### Return type

[**list[City]**](City.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

