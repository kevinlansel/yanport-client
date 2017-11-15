# swagger_client.MandatairesApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mandatary_networks_get**](MandatairesApi.md#mandatary_networks_get) | **GET** /mandatary-networks | Rechercher des réseaux mandataires
[**mandatary_networks_id_get**](MandatairesApi.md#mandatary_networks_id_get) | **GET** /mandatary-networks/{id} | Récupérer un réseau mandataire


# **mandatary_networks_get**
> InlineResponse2006 mandatary_networks_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, q=q, siren=siren)

Rechercher des réseaux mandataires

Rechercher des réseaux mandataires selon plusieurs critères # Exemples   ## Rechercher le réseau Efficity     /mandatary-networks?q=efficity'

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
api_instance = swagger_client.MandatairesApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
siren = ['siren_example'] # list[str] |  (optional)

try: 
    # Rechercher des réseaux mandataires
    api_response = api_instance.mandatary_networks_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, q=q, siren=siren)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MandatairesApi->mandatary_networks_get: %s\n" % e)
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
 **siren** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mandatary_networks_id_get**
> MandataryNetwork mandatary_networks_id_get(id)

Récupérer un réseau mandataire

Récupérer un réseau mandataire par son identifiant

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
api_instance = swagger_client.MandatairesApi()
id = 789 # int | L'identifiant du réseau de mandataire

try: 
    # Récupérer un réseau mandataire
    api_response = api_instance.mandatary_networks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MandatairesApi->mandatary_networks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant du réseau de mandataire | 

### Return type

[**MandataryNetwork**](MandataryNetwork.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

