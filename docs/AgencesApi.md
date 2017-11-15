# swagger_client.AgencesApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agencies_get**](AgencesApi.md#agencies_get) | **GET** /agencies | Rechercher des agences
[**agencies_id_get**](AgencesApi.md#agencies_id_get) | **GET** /agencies/{id} | Récupérer une agence


# **agencies_get**
> InlineResponse2005 agencies_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, q=q, external_id=external_id, organization_id=organization_id, siren=siren, siret=siret, city_ids=city_ids, lat=lat, lng=lng, radius=radius, sale_property_count_min=sale_property_count_min, sale_property_count_max=sale_property_count_max, rent_property_count_min=rent_property_count_min, rent_property_count_max=rent_property_count_max, active=active)

Rechercher des agences

Rechercher des agences selon plusieurs critères # Exemples   ## Les agences situées à Levallois-Perret et qui ont au moins 10 biens en vente et en location     /agencies?cityIds=54178039&salePropertyCountMin=10&rentPropertyCountMin=10   ## Les agences situées dans un rayon de 100m autour de Levallois-Perret     /agencies?lat=48.8932&lon=2.2879&radius=100m   ## Les agences Nexity     /agencies?siren=487530099

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
api_instance = swagger_client.AgencesApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
external_id = 'external_id_example' # str | Identifiant externe client (optional)
organization_id = 789 # int | Identifiant de l'organisation (optional)
siren = ['siren_example'] # list[str] | Siren de l'entreprise (optional)
siret = ['siret_example'] # list[str] | Siret de l'entreprise (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
lat = 1.2 # float | Latitude (optional)
lng = 1.2 # float | Longitude (optional)
radius = '10m' # str | Radius (optional) (default to 10m)
sale_property_count_min = 56 # int | Nombre minimal de biens en vente (optional)
sale_property_count_max = 56 # int | Nombre maximal de biens en vente (optional)
rent_property_count_min = 56 # int | Nombre minimal de biens en location (optional)
rent_property_count_max = 56 # int | Nombre maximal de biens en location (optional)
active = true # bool | Agence active (optional)

try: 
    # Rechercher des agences
    api_response = api_instance.agencies_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, q=q, external_id=external_id, organization_id=organization_id, siren=siren, siret=siret, city_ids=city_ids, lat=lat, lng=lng, radius=radius, sale_property_count_min=sale_property_count_min, sale_property_count_max=sale_property_count_max, rent_property_count_min=rent_property_count_min, rent_property_count_max=rent_property_count_max, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgencesApi->agencies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **external_id** | **str**| Identifiant externe client | [optional] 
 **organization_id** | **int**| Identifiant de l&#39;organisation | [optional] 
 **siren** | [**list[str]**](str.md)| Siren de l&#39;entreprise | [optional] 
 **siret** | [**list[str]**](str.md)| Siret de l&#39;entreprise | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **lat** | **float**| Latitude | [optional] 
 **lng** | **float**| Longitude | [optional] 
 **radius** | **str**| Radius | [optional] [default to 10m]
 **sale_property_count_min** | **int**| Nombre minimal de biens en vente | [optional] 
 **sale_property_count_max** | **int**| Nombre maximal de biens en vente | [optional] 
 **rent_property_count_min** | **int**| Nombre minimal de biens en location | [optional] 
 **rent_property_count_max** | **int**| Nombre maximal de biens en location | [optional] 
 **active** | **bool**| Agence active | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agencies_id_get**
> Agency agencies_id_get(id)

Récupérer une agence

Récupérer une agence par son identifiant

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
api_instance = swagger_client.AgencesApi()
id = 789 # int | L'identifiant de l'agence

try: 
    # Récupérer une agence
    api_response = api_instance.agencies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgencesApi->agencies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;agence | 

### Return type

[**Agency**](Agency.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

