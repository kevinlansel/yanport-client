# swagger_client.BiensApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**properties_count_get**](BiensApi.md#properties_count_get) | **GET** /properties/count | Nombre de biens
[**properties_count_group_by_group_by_and_sub_group_by_get**](BiensApi.md#properties_count_group_by_group_by_and_sub_group_by_get) | **GET** /properties/count/group-by-{groupBy}-and-{subGroupBy} | Nombre de biens
[**properties_count_group_by_group_by_get**](BiensApi.md#properties_count_group_by_group_by_get) | **GET** /properties/count/group-by-{groupBy} | Nombre de biens
[**properties_distribution_get**](BiensApi.md#properties_distribution_get) | **GET** /properties/distribution | Disitribution des biens
[**properties_evolution_get**](BiensApi.md#properties_evolution_get) | **GET** /properties/evolution | Evolution des biens dans le temps
[**properties_get**](BiensApi.md#properties_get) | **GET** /properties | Rechercher des biens
[**properties_id_get**](BiensApi.md#properties_id_get) | **GET** /properties/{id} | Récupérer un bien (ID)
[**properties_ids_get**](BiensApi.md#properties_ids_get) | **GET** /properties/ids | Récupérer des biens (ID)
[**properties_percentiles_get**](BiensApi.md#properties_percentiles_get) | **GET** /properties/percentiles | Indicateurs de références
[**properties_percentiles_group_by_group_by_get**](BiensApi.md#properties_percentiles_group_by_group_by_get) | **GET** /properties/percentiles/group-by-{groupBy} | Indicateurs de réferences
[**properties_stats_get**](BiensApi.md#properties_stats_get) | **GET** /properties/stats | Statistiques sur les biens
[**properties_stats_group_by_group_by_and_sub_group_by_get**](BiensApi.md#properties_stats_group_by_group_by_and_sub_group_by_get) | **GET** /properties/stats/group-by-{groupBy}-and-{subGroupBy} | Statistiques sur les biens
[**properties_stats_group_by_group_by_get**](BiensApi.md#properties_stats_group_by_group_by_get) | **GET** /properties/stats/group-by-{groupBy} | Statistiques sur les biens
[**properties_stock_evolution_get**](BiensApi.md#properties_stock_evolution_get) | **GET** /properties/stock-evolution | L&#39;évolution du stock de biens


# **properties_count_get**
> CountResponse properties_count_get(_from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Nombre de biens

Compte le nombre de biens par rapport à certains critères de recherches. (prix, surface, ville, ...) # Exemples   ## Nombre de biens en cours de publication sur Levallois-Perret entre 120 et 130m²     /properties/count?active=true&published=true&zipCodes=92300&surfaceMin=120&surfaceMax=130

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
api_instance = swagger_client.BiensApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Nombre de biens
    api_response = api_instance.properties_count_get(_from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_count_get: %s\n" % e)
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
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_count_group_by_group_by_and_sub_group_by_get**
> CountResponse properties_count_group_by_group_by_and_sub_group_by_get(group_by, sub_group_by, terms_size, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Nombre de biens

Retourne le nombre de biens regroupés selon 1 critère et 1 sous-critère. # Exemples   ## Nombre de biens regroupés par portails et par type de vendeur en cours de publication sur Levallois-Perret     /properties/count/group-by-CRAWL_SOURCES-and-DEALER_TYPE?active=true&published=true&zipCodes=92300

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
api_instance = swagger_client.BiensApi()
group_by = 'group_by_example' # str | Grouper par
sub_group_by = 'sub_group_by_example' # str | Grouper par
terms_size = 30 # int | Précision des résultats (default to 30)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Nombre de biens
    api_response = api_instance.properties_count_group_by_group_by_and_sub_group_by_get(group_by, sub_group_by, terms_size, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_count_group_by_group_by_and_sub_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Grouper par | 
 **sub_group_by** | **str**| Grouper par | 
 **terms_size** | **int**| Précision des résultats | [default to 30]
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_count_group_by_group_by_get**
> CountResponse properties_count_group_by_group_by_get(group_by, terms_size, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Nombre de biens

Retourne le nombre de biens regroupés selon 1 critère. # Exemples   ## Nombre de biens regroupés par portails en cours de publication sur Levallois-Perret     /properties/count/group-by-CRAWL_SOURCES?active=true&published=true&zipCodes=92300

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
api_instance = swagger_client.BiensApi()
group_by = 'group_by_example' # str | Grouper par
terms_size = 30 # int | Précision des résultats (default to 30)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Nombre de biens
    api_response = api_instance.properties_count_group_by_group_by_get(group_by, terms_size, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_count_group_by_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Grouper par | 
 **terms_size** | **int**| Précision des résultats | [default to 30]
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_distribution_get**
> Histogram properties_distribution_get(field, percentiles, interval_field, interval=interval, extended_bound_min=extended_bound_min, extended_bound_max=extended_bound_max, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Disitribution des biens

Permet de construire un graphique de distribution des biens selon plusieurs critères. # Exemples   ## Distribution des durées de publication des biens en vente entre 2016 et 2017 à Levallois-Perret     /properties/distribution?field=DURATION_DAYS&intervalField=DURATION_DAYS&marketingTypes=SALE&active=false&published=true&zipCodes=92300&publicationDateMin=2016-01-01T00%3A00%3A00.00&publicationDateMax=2017-01-01T00%3A00%3A00.00

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
api_instance = swagger_client.BiensApi()
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
percentiles = [3.4] # list[float] | Les percentiles (ex: 10.0, 50.0, 90.0)
interval_field = 'interval_field_example' # str | Champ sur lequel sont calculés les statistiques
interval = 1 # int | Valeur de l'intervalle de l'histogramme (optional) (default to 1)
extended_bound_min = 789 # int | Garantit un intervalle minimale (optional)
extended_bound_max = 789 # int | Garantit un intervalle maximale (optional)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Disitribution des biens
    api_response = api_instance.properties_distribution_get(field, percentiles, interval_field, interval=interval, extended_bound_min=extended_bound_min, extended_bound_max=extended_bound_max, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_distribution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **percentiles** | [**list[float]**](float.md)| Les percentiles (ex: 10.0, 50.0, 90.0) | 
 **interval_field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **interval** | **int**| Valeur de l&#39;intervalle de l&#39;histogramme | [optional] [default to 1]
 **extended_bound_min** | **int**| Garantit un intervalle minimale | [optional] 
 **extended_bound_max** | **int**| Garantit un intervalle maximale | [optional] 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**Histogram**](Histogram.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_evolution_get**
> DateHistogram properties_evolution_get(field, percentiles, interval_field, interval=interval, interval_unit=interval_unit, extended_bound_min=extended_bound_min, extended_bound_max=extended_bound_max, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Evolution des biens dans le temps

Permet de constuire une courbe d'évolution du nombre de biens selon plusieurs critères. # Exemples   ##Evolution des prix des biens en vente entre 2016 et 2017 à Levallois-Perret     /properties/evolution?field=PRICE&intervalField=DELETE_DATE&interval=1&intervalUnit=MONTHS&marketingTypes=SALE&active=false&published=true&zipCodes=92300&publicationDateMin=2016-01-01T00:00:00.00&publicationDateMax=2017-01-01T00:00:00.00

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
api_instance = swagger_client.BiensApi()
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
percentiles = [3.4] # list[float] | Les percentiles (ex: 10.0, 50.0, 90.0)
interval_field = 'interval_field_example' # str | Champ sur lequel sont calculés les statistiques
interval = 1 # int | Valeur de l'intervalle de l'histogramme (optional) (default to 1)
interval_unit = 'MONTHS' # str | Unité de temps de l'intervalle (optional) (default to MONTHS)
extended_bound_min = 789 # int | Garantit un intervalle minimale (optional)
extended_bound_max = 789 # int | Garantit un intervalle maximale (optional)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Evolution des biens dans le temps
    api_response = api_instance.properties_evolution_get(field, percentiles, interval_field, interval=interval, interval_unit=interval_unit, extended_bound_min=extended_bound_min, extended_bound_max=extended_bound_max, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **percentiles** | [**list[float]**](float.md)| Les percentiles (ex: 10.0, 50.0, 90.0) | 
 **interval_field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **interval** | **int**| Valeur de l&#39;intervalle de l&#39;histogramme | [optional] [default to 1]
 **interval_unit** | **str**| Unité de temps de l&#39;intervalle | [optional] [default to MONTHS]
 **extended_bound_min** | **int**| Garantit un intervalle minimale | [optional] 
 **extended_bound_max** | **int**| Garantit un intervalle maximale | [optional] 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**DateHistogram**](DateHistogram.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_get**
> InlineResponse2002 properties_get(_from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Rechercher des biens

Rechercher les biens actifs ou expirés selon plusieurs critères (prix, surface, ville, ...)  La recherche plein-texte est disponible sur le titre et la description via le query param `q` _(voir notre [FAQ](https://yanporthelp.zendesk.com/hc/fr/articles/208456909-Comment-affiner-ma-recherche-avec-des-mots-cl%C3%A9s-) concernant la syntaxe)_  Par défaut les résultats sont paginés, pour parcourir l'ensemble des biens les paramètres `from` et `size` doivent être renseignés. Le paramètre `from` définit le début du set de données et `size` le nombre d'éléments à récupérer. Le nombre `total` d'éléments est renvoyé dans la réponse.  Concernant le tri le paramètre `sort` à pour syntaxe `field:asc|desc` en remplaçant `field` par le nom du champ sur lequel appliqué le tri. # Exemples   ## Les biens en cours de publication sur Levallois-Perret entre 120 et 130m²     /properties?active=true&published=true&zipCodes=92300&surfaceMin=120&surfaceMax=130   ## Les biens en cours de publication dans le 17ème arrondissement de Paris avec balcon     /properties?active=true&published=true&zipCodes=75017&q=balcon   ## Les dernièrs biens de particulier publiés en Corse sur LeBonCoin et PAP     /properties?active=true&published=true&crawlSources=LE_BON_COIN&crawlSources=PAP&departments=2B&sort=marketing.publicationStartDate:asc

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
api_instance = swagger_client.BiensApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Rechercher des biens
    api_response = api_instance.properties_get(_from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_get: %s\n" % e)
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
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_id_get**
> ModelProperty properties_id_get(id)

Récupérer un bien (ID)

Récupérer un bien par son identifiant

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
api_instance = swagger_client.BiensApi()
id = 'id_example' # str | 

try: 
    # Récupérer un bien (ID)
    api_response = api_instance.properties_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_ids_get**
> list[ModelProperty] properties_ids_get(ids)

Récupérer des biens (ID)

Récupérer des biens par leur identifiant

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
api_instance = swagger_client.BiensApi()
ids = ['ids_example'] # list[str] | 

try: 
    # Récupérer des biens (ID)
    api_response = api_instance.properties_ids_get(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)|  | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_percentiles_get**
> Percentiles properties_percentiles_get(field, percentiles, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Indicateurs de références

Permet de récupérer les indicateurs de références sur les biens selon plusieurs critères. # Exemples   ## PrixM2 median des biens en cours de publication en vente à Levallois-Perret     /properties/percentiles?field=PRICE&percentiles=50&marketingTypes=SALE&active=true&zipCodes=92300

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
api_instance = swagger_client.BiensApi()
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
percentiles = [3.4] # list[float] | Les percentiles (ex: 10.0, 50.0, 90.0)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Indicateurs de références
    api_response = api_instance.properties_percentiles_get(field, percentiles, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_percentiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **percentiles** | [**list[float]**](float.md)| Les percentiles (ex: 10.0, 50.0, 90.0) | 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**Percentiles**](Percentiles.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_percentiles_group_by_group_by_get**
> object properties_percentiles_group_by_group_by_get(group_by, terms_size, field, percentiles, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Indicateurs de réferences

Permet de récupérer les indicateurs de références regroupé selon 1 critère.

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
api_instance = swagger_client.BiensApi()
group_by = 'group_by_example' # str | Grouper par
terms_size = 30 # int | Précision des résultats (default to 30)
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
percentiles = [3.4] # list[float] | Les percentiles (ex: 10.0, 50.0, 90.0)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Indicateurs de réferences
    api_response = api_instance.properties_percentiles_group_by_group_by_get(group_by, terms_size, field, percentiles, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_percentiles_group_by_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Grouper par | 
 **terms_size** | **int**| Précision des résultats | [default to 30]
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **percentiles** | [**list[float]**](float.md)| Les percentiles (ex: 10.0, 50.0, 90.0) | 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_stats_get**
> Stats properties_stats_get(field, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Statistiques sur les biens

Permet de récupérer les statistiques des biens selon plusieurs critères.

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
api_instance = swagger_client.BiensApi()
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Statistiques sur les biens
    api_response = api_instance.properties_stats_get(field, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**Stats**](Stats.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_stats_group_by_group_by_and_sub_group_by_get**
> object properties_stats_group_by_group_by_and_sub_group_by_get(field, group_by, sub_group_by, terms_size, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Statistiques sur les biens

Permet de récupérer les statistiques basiques des biens regroupé selon 1 critère et 1 sous-critère.

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
api_instance = swagger_client.BiensApi()
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
group_by = 'group_by_example' # str | Grouper par
sub_group_by = 'sub_group_by_example' # str | Grouper par
terms_size = 30 # int | Précision des résultats (default to 30)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Statistiques sur les biens
    api_response = api_instance.properties_stats_group_by_group_by_and_sub_group_by_get(field, group_by, sub_group_by, terms_size, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_stats_group_by_group_by_and_sub_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **group_by** | **str**| Grouper par | 
 **sub_group_by** | **str**| Grouper par | 
 **terms_size** | **int**| Précision des résultats | [default to 30]
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_stats_group_by_group_by_get**
> object properties_stats_group_by_group_by_get(group_by, terms_size, field, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

Statistiques sur les biens

Permet de récupérer les statistiques basiques des biens regroupé selon 1 critère.

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
api_instance = swagger_client.BiensApi()
group_by = 'group_by_example' # str | Grouper par
terms_size = 30 # int | Précision des résultats (default to 30)
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # Statistiques sur les biens
    api_response = api_instance.properties_stats_group_by_group_by_get(group_by, terms_size, field, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_stats_group_by_group_by_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Grouper par | 
 **terms_size** | **int**| Précision des résultats | [default to 30]
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_stock_evolution_get**
> StockEvolution properties_stock_evolution_get(field, percentiles, interval_field, interval=interval, interval_unit=interval_unit, extended_bound_min=extended_bound_min, extended_bound_max=extended_bound_max, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)

L'évolution du stock de biens

Permet de constuire une courbe représentant l'évolution du stock de biens selon plusieurs critères.

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
api_instance = swagger_client.BiensApi()
field = 'field_example' # str | Champ sur lequel sont calculés les statistiques
percentiles = [3.4] # list[float] | Les percentiles (ex: 10.0, 50.0, 90.0)
interval_field = 'interval_field_example' # str | Champ sur lequel sont calculés les statistiques
interval = 1 # int | Valeur de l'intervalle de l'histogramme (optional) (default to 1)
interval_unit = 'MONTHS' # str | Unité de temps de l'intervalle (optional) (default to MONTHS)
extended_bound_min = 789 # int | Garantit un intervalle minimale (optional)
extended_bound_max = 789 # int | Garantit un intervalle maximale (optional)
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
marketing_types = ['marketing_types_example'] # list[str] | Types de marché (vente, location, vente en viager) (optional)
crawl_sources = ['crawl_sources_example'] # list[str] | Portails immobiliers (optional)
active = true # bool | Statut de l'annonce (expirée ou pas) (optional)
published = true # bool | Le bien est-il annoncé en ligne ou pas (optional)
dealer_types = ['dealer_types_example'] # list[str] | Types de vendeur (agence, mandataire..) (optional)
dealer_names = ['dealer_names_example'] # list[str] | Liste de noms de vendeurs (optional)
exclusive_mandate = true # bool | Mandat Exclusif (optional)
dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs (optional)
excluded_dealer_ids = [56] # list[int] | Liste d'identifiants de vendeurs à exclure (optional)
property_ids = ['property_ids_example'] # list[str] | Liste d'identifiants de biens (optional)
property_types = ['property_types_example'] # list[str] | Types de bien (optional)
room_counts = [56] # list[int] | Nombre de pièces (optional)
departments = ['departments_example'] # list[str] | Liste de départements (optional)
zip_codes = ['zip_codes_example'] # list[str] | Liste de codes postaux (optional)
city_ids = [56] # list[int] | Liste d'identifiants de villes (optional)
publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication (YYYY-mm-ddTHH:mm:ss) (optional)
publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
ad_publication_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de publication de l'annonce (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
last_price_decrease_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
delete_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de suppression (YYYY-mm-ddTHH:mm:ss) (optional)
duration_days_min = 56 # int | Durée minimale en jours (optional)
duration_days_max = 56 # int | Durée maximale en jours (optional)
surface_min = 56 # int | Surface minimale (optional)
surface_max = 56 # int | Surface maximale (optional)
price_min = 56 # int | Prix minimum (optional)
price_max = 56 # int | Prix maximum (optional)
price_m2_min = 56 # int | Prix au mètre carré minimum (optional)
price_m2_max = 56 # int | Prix au mètre carré maximum (optional)
price_hc_min = 56 # int | Prix hors charges minimum (optional)
price_hc_max = 56 # int | Prix hors charges maximum (optional)
price_m2_hc_min = 56 # int | Prix au mètres carré hors charges minimum (optional)
price_m2_hc_max = 56 # int | Prix au mètres carré hors charges maximum (optional)
price_cc_min = 56 # int | Prix charges comprises minimum (optional)
price_cc_max = 56 # int | Prix charges comprises maximum (optional)
fees_min = 56 # int | Honoraires minimales (optional)
fees_max = 56 # int | Honoraires maximales (optional)
deposit_min = 56 # int | Caution minimale (optional)
deposit_max = 56 # int | Caution maximale (optional)
furnished = true # bool | Meublé (optional)
new_build = true # bool | Nouvelle construction (optional)
missing_fields = ['missing_fields_example'] # list[str] | Attributs manquants (optional)
existing_fields = ['existing_fields_example'] # list[str] | Attributs existants (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | Identifiants à exclure (optional)
external_ids = ['external_ids_example'] # list[str] | Identifiants externes (optional)
organization_ids = ['organization_ids_example'] # list[str] | Identifiants d'organisations (optional)

try: 
    # L'évolution du stock de biens
    api_response = api_instance.properties_stock_evolution_get(field, percentiles, interval_field, interval=interval, interval_unit=interval_unit, extended_bound_min=extended_bound_min, extended_bound_max=extended_bound_max, _from=_from, size=size, sort=sort, q=q, marketing_types=marketing_types, crawl_sources=crawl_sources, active=active, published=published, dealer_types=dealer_types, dealer_names=dealer_names, exclusive_mandate=exclusive_mandate, dealer_ids=dealer_ids, excluded_dealer_ids=excluded_dealer_ids, property_ids=property_ids, property_types=property_types, room_counts=room_counts, departments=departments, zip_codes=zip_codes, city_ids=city_ids, publication_date_min=publication_date_min, publication_date_max=publication_date_max, ad_publication_date_min=ad_publication_date_min, ad_publication_date_max=ad_publication_date_max, last_price_decrease_date_min=last_price_decrease_date_min, last_price_decrease_date_max=last_price_decrease_date_max, delete_date_min=delete_date_min, delete_date_max=delete_date_max, duration_days_min=duration_days_min, duration_days_max=duration_days_max, surface_min=surface_min, surface_max=surface_max, price_min=price_min, price_max=price_max, price_m2_min=price_m2_min, price_m2_max=price_m2_max, price_hc_min=price_hc_min, price_hc_max=price_hc_max, price_m2_hc_min=price_m2_hc_min, price_m2_hc_max=price_m2_hc_max, price_cc_min=price_cc_min, price_cc_max=price_cc_max, fees_min=fees_min, fees_max=fees_max, deposit_min=deposit_min, deposit_max=deposit_max, furnished=furnished, new_build=new_build, missing_fields=missing_fields, existing_fields=existing_fields, excluded_ids=excluded_ids, external_ids=external_ids, organization_ids=organization_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BiensApi->properties_stock_evolution_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **percentiles** | [**list[float]**](float.md)| Les percentiles (ex: 10.0, 50.0, 90.0) | 
 **interval_field** | **str**| Champ sur lequel sont calculés les statistiques | 
 **interval** | **int**| Valeur de l&#39;intervalle de l&#39;histogramme | [optional] [default to 1]
 **interval_unit** | **str**| Unité de temps de l&#39;intervalle | [optional] [default to MONTHS]
 **extended_bound_min** | **int**| Garantit un intervalle minimale | [optional] 
 **extended_bound_max** | **int**| Garantit un intervalle maximale | [optional] 
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **q** | **str**| Recherche plein-texte | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Types de marché (vente, location, vente en viager) | [optional] 
 **crawl_sources** | [**list[str]**](str.md)| Portails immobiliers | [optional] 
 **active** | **bool**| Statut de l&#39;annonce (expirée ou pas) | [optional] 
 **published** | **bool**| Le bien est-il annoncé en ligne ou pas | [optional] 
 **dealer_types** | [**list[str]**](str.md)| Types de vendeur (agence, mandataire..) | [optional] 
 **dealer_names** | [**list[str]**](str.md)| Liste de noms de vendeurs | [optional] 
 **exclusive_mandate** | **bool**| Mandat Exclusif | [optional] 
 **dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs | [optional] 
 **excluded_dealer_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de vendeurs à exclure | [optional] 
 **property_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants de biens | [optional] 
 **property_types** | [**list[str]**](str.md)| Types de bien | [optional] 
 **room_counts** | [**list[int]**](int.md)| Nombre de pièces | [optional] 
 **departments** | [**list[str]**](str.md)| Liste de départements | [optional] 
 **zip_codes** | [**list[str]**](str.md)| Liste de codes postaux | [optional] 
 **city_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants de villes | [optional] 
 **publication_date_min** | **datetime**| Date minimale de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **publication_date_max** | **datetime**| Date limite de publication (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_min** | **datetime**| Date minimale de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **ad_publication_date_max** | **datetime**| Date limite de publication de l&#39;annonce (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_min** | **datetime**| Date minimale de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **last_price_decrease_date_max** | **datetime**| Date limite de la dernière baisse de prix (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_min** | **datetime**| Date minimale de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **delete_date_max** | **datetime**| Date limite de suppression (YYYY-mm-ddTHH:mm:ss) | [optional] 
 **duration_days_min** | **int**| Durée minimale en jours | [optional] 
 **duration_days_max** | **int**| Durée maximale en jours | [optional] 
 **surface_min** | **int**| Surface minimale | [optional] 
 **surface_max** | **int**| Surface maximale | [optional] 
 **price_min** | **int**| Prix minimum | [optional] 
 **price_max** | **int**| Prix maximum | [optional] 
 **price_m2_min** | **int**| Prix au mètre carré minimum | [optional] 
 **price_m2_max** | **int**| Prix au mètre carré maximum | [optional] 
 **price_hc_min** | **int**| Prix hors charges minimum | [optional] 
 **price_hc_max** | **int**| Prix hors charges maximum | [optional] 
 **price_m2_hc_min** | **int**| Prix au mètres carré hors charges minimum | [optional] 
 **price_m2_hc_max** | **int**| Prix au mètres carré hors charges maximum | [optional] 
 **price_cc_min** | **int**| Prix charges comprises minimum | [optional] 
 **price_cc_max** | **int**| Prix charges comprises maximum | [optional] 
 **fees_min** | **int**| Honoraires minimales | [optional] 
 **fees_max** | **int**| Honoraires maximales | [optional] 
 **deposit_min** | **int**| Caution minimale | [optional] 
 **deposit_max** | **int**| Caution maximale | [optional] 
 **furnished** | **bool**| Meublé | [optional] 
 **new_build** | **bool**| Nouvelle construction | [optional] 
 **missing_fields** | [**list[str]**](str.md)| Attributs manquants | [optional] 
 **existing_fields** | [**list[str]**](str.md)| Attributs existants | [optional] 
 **excluded_ids** | [**list[str]**](str.md)| Identifiants à exclure | [optional] 
 **external_ids** | [**list[str]**](str.md)| Identifiants externes | [optional] 
 **organization_ids** | [**list[str]**](str.md)| Identifiants d&#39;organisations | [optional] 

### Return type

[**StockEvolution**](StockEvolution.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

