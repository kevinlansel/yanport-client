# swagger_client.AnnoncesApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ads_get**](AnnoncesApi.md#ads_get) | **GET** /ads | Rechercher des annonces
[**ads_id_get**](AnnoncesApi.md#ads_id_get) | **GET** /ads/{id} | Récupérer une annonce (ID)
[**ads_ids_get**](AnnoncesApi.md#ads_ids_get) | **GET** /ads/ids | Récupérer des annonces (ID)
[**ads_urls_get**](AnnoncesApi.md#ads_urls_get) | **GET** /ads/urls | Récupérer une annonce (URL)


# **ads_get**
> InlineResponse200 ads_get(_from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, dealer_types=dealer_types, dealer_names=dealer_names, dealer_ids=dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids)

Rechercher des annonces

Recherche sur l'ensemble des annonces publiées par les portails selon certains critères comme la date de publication, le prix, la surface... _(voir ci-dessous pour une liste exhaustive)_.  La recherche plein-texte est disponible sur le titre et la description via le query param `q` _(voir notre [FAQ](https://yanporthelp.zendesk.com/hc/fr/articles/208456909-Comment-affiner-ma-recherche-avec-des-mots-cl%C3%A9s-) concernant la syntaxe)_  Par défaut les résultats sont paginés, pour parcourir l'ensemble des annonces les paramètres `from` et `size` doivent être renseignés. Le paramètre `from` définit le début du set de données et `size` le nombre d'éléments à récupérer. Le nombre `total` d'éléments est renvoyé dans la réponse.  Concernant le tri le paramètre `sort` à pour syntaxe `field:asc|desc` en remplaçant `field` par le nom du champ sur lequel appliqué le tri.  # Exemples   ## Les annonces en cours de publication sur Levallois-Perret entre 120 et 130m²     /ads?active=true&zipCodes=92300&surfaceMin=120&surfaceMax=130   ## Les annonces en cours de publication dans le 17ème arrondissement de Paris avec balcon     /ads?active=true&zipCodes=75017&q=balcon   ## Les dernières annonces de particulier publiées en Corse sur LeBonCoin et PAP     /ads?active=true&crawlSources=LE_BON_COIN&crawlSources=PAP&departments=2B&sort=property.marketing.publicationDate:asc 

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
api_instance = swagger_client.AnnoncesApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)

try: 
    # Rechercher des annonces
    api_response = api_instance.ads_get(_from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, dealer_types=dealer_types, dealer_names=dealer_names, dealer_ids=dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnoncesApi->ads_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ads_id_get**
> Ad ads_id_get(id)

Récupérer une annonce (ID)

Récupérer une annonce par son identifiant

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
api_instance = swagger_client.AnnoncesApi()
id = 'id_example' # str | L'identifiant de l'annonce

try: 
    # Récupérer une annonce (ID)
    api_response = api_instance.ads_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnoncesApi->ads_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| L&#39;identifiant de l&#39;annonce | 

### Return type

[**Ad**](Ad.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ads_ids_get**
> list[Ad] ads_ids_get(ids)

Récupérer des annonces (ID)

Récupérer des annonces par leurs identifiants

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
api_instance = swagger_client.AnnoncesApi()
ids = ['ids_example'] # list[str] | Les identifiants des annonces

try: 
    # Récupérer des annonces (ID)
    api_response = api_instance.ads_ids_get(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnoncesApi->ads_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| Les identifiants des annonces | 

### Return type

[**list[Ad]**](Ad.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ads_urls_get**
> Ad ads_urls_get(url)

Récupérer une annonce (URL)

Récupérer une annonce par son url

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
api_instance = swagger_client.AnnoncesApi()
url = 'url_example' # str | Url de l'annonce

try: 
    # Récupérer une annonce (URL)
    api_response = api_instance.ads_urls_get(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnoncesApi->ads_urls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Url de l&#39;annonce | 

### Return type

[**Ad**](Ad.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

