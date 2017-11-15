# swagger_client.EtudesApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studies_count_get**](EtudesApi.md#studies_count_get) | **GET** /studies/count | Nombre d&#39;études
[**studies_get**](EtudesApi.md#studies_get) | **GET** /studies | Rechercher des études
[**studies_id_delete**](EtudesApi.md#studies_id_delete) | **DELETE** /studies/{id} | Supprimer une étude
[**studies_id_duplicate_get**](EtudesApi.md#studies_id_duplicate_get) | **GET** /studies/{id}/duplicate | Dupliquer une étude
[**studies_id_get**](EtudesApi.md#studies_id_get) | **GET** /studies/{id} | Récupérer une étude
[**studies_id_put**](EtudesApi.md#studies_id_put) | **PUT** /studies/{id} | Mettre à jour une étude
[**studies_post**](EtudesApi.md#studies_post) | **POST** /studies | Créer une étude


# **studies_count_get**
> CountResponse studies_count_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, external_user_ids=external_user_ids, agency_ids=agency_ids, external_agency_ids=external_agency_ids, organization_ids=organization_ids, marketing_types=marketing_types, property_external_ids=property_external_ids, creation_date_min=creation_date_min, creation_date_max=creation_date_max)

Nombre d'études

Compte le nombre d'études par rapport à certains critères de recherches.

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
api_instance = swagger_client.EtudesApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)
user_ids = [56] # list[int] | Liste d'identifiants d'utilisateurs (optional)
external_user_ids = ['external_user_ids_example'] # list[str] | Liste d'identifiants externe client (optional)
agency_ids = [56] # list[int] | Liste d'identifiants d'agences (optional)
external_agency_ids = ['external_agency_ids_example'] # list[str] | Liste d'identifiants externes d'agences (optional)
organization_ids = [56] # list[int] | Liste d'identifiants d'organisations (optional)
marketing_types = ['marketing_types_example'] # list[str] | Liste de types de marché (vente, location, vente en viager) (optional)
property_external_ids = ['property_external_ids_example'] # list[str] | Liste d'identifiants externes de biens (optional)
creation_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de création de l'étude (optional)
creation_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de création de l'étude (optional)

try: 
    # Nombre d'études
    api_response = api_instance.studies_count_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, external_user_ids=external_user_ids, agency_ids=agency_ids, external_agency_ids=external_agency_ids, organization_ids=organization_ids, marketing_types=marketing_types, property_external_ids=property_external_ids, creation_date_min=creation_date_min, creation_date_max=creation_date_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EtudesApi->studies_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 
 **user_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;utilisateurs | [optional] 
 **external_user_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants externe client | [optional] 
 **agency_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;agences | [optional] 
 **external_agency_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants externes d&#39;agences | [optional] 
 **organization_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;organisations | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Liste de types de marché (vente, location, vente en viager) | [optional] 
 **property_external_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants externes de biens | [optional] 
 **creation_date_min** | **datetime**| Date minimale de création de l&#39;étude | [optional] 
 **creation_date_max** | **datetime**| Date limite de création de l&#39;étude | [optional] 

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_get**
> InlineResponse2007 studies_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, external_user_ids=external_user_ids, agency_ids=agency_ids, external_agency_ids=external_agency_ids, organization_ids=organization_ids, marketing_types=marketing_types, property_external_ids=property_external_ids, creation_date_min=creation_date_min, creation_date_max=creation_date_max)

Rechercher des études

Rechercher des études selon plusieurs critères

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
api_instance = swagger_client.EtudesApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)
user_ids = [56] # list[int] | Liste d'identifiants d'utilisateurs (optional)
external_user_ids = ['external_user_ids_example'] # list[str] | Liste d'identifiants externe client (optional)
agency_ids = [56] # list[int] | Liste d'identifiants d'agences (optional)
external_agency_ids = ['external_agency_ids_example'] # list[str] | Liste d'identifiants externes d'agences (optional)
organization_ids = [56] # list[int] | Liste d'identifiants d'organisations (optional)
marketing_types = ['marketing_types_example'] # list[str] | Liste de types de marché (vente, location, vente en viager) (optional)
property_external_ids = ['property_external_ids_example'] # list[str] | Liste d'identifiants externes de biens (optional)
creation_date_min = '2013-10-20T19:20:30+01:00' # datetime | Date minimale de création de l'étude (optional)
creation_date_max = '2013-10-20T19:20:30+01:00' # datetime | Date limite de création de l'étude (optional)

try: 
    # Rechercher des études
    api_response = api_instance.studies_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, user_ids=user_ids, external_user_ids=external_user_ids, agency_ids=agency_ids, external_agency_ids=external_agency_ids, organization_ids=organization_ids, marketing_types=marketing_types, property_external_ids=property_external_ids, creation_date_min=creation_date_min, creation_date_max=creation_date_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EtudesApi->studies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Début de la pagination | [optional] [default to 0]
 **size** | **int**| Nombre de résultats | [optional] [default to 20]
 **sort** | **str**| Trier par | [optional] 
 **includes** | [**list[str]**](str.md)| Inclure un ou plusieurs élements par identifiant | [optional] 
 **excludes** | [**list[str]**](str.md)| Exclure un ou plusieurs élements par identifiant | [optional] 
 **user_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;utilisateurs | [optional] 
 **external_user_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants externe client | [optional] 
 **agency_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;agences | [optional] 
 **external_agency_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants externes d&#39;agences | [optional] 
 **organization_ids** | [**list[int]**](int.md)| Liste d&#39;identifiants d&#39;organisations | [optional] 
 **marketing_types** | [**list[str]**](str.md)| Liste de types de marché (vente, location, vente en viager) | [optional] 
 **property_external_ids** | [**list[str]**](str.md)| Liste d&#39;identifiants externes de biens | [optional] 
 **creation_date_min** | **datetime**| Date minimale de création de l&#39;étude | [optional] 
 **creation_date_max** | **datetime**| Date limite de création de l&#39;étude | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_delete**
> DefaultResponse studies_id_delete(id)

Supprimer une étude

Supprimer une étude par son identifiant

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
api_instance = swagger_client.EtudesApi()
id = 'id_example' # str | L'identifiant de l'étude

try: 
    # Supprimer une étude
    api_response = api_instance.studies_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EtudesApi->studies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| L&#39;identifiant de l&#39;étude | 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_duplicate_get**
> Study studies_id_duplicate_get(id)

Dupliquer une étude

Dupliquer une étude par son identifiant

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
api_instance = swagger_client.EtudesApi()
id = 'id_example' # str | L'identifiant de l'étude

try: 
    # Dupliquer une étude
    api_response = api_instance.studies_id_duplicate_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EtudesApi->studies_id_duplicate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| L&#39;identifiant de l&#39;étude | 

### Return type

[**Study**](Study.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_get**
> Study studies_id_get(id)

Récupérer une étude

Récupérer une étude par son identifiant

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
api_instance = swagger_client.EtudesApi()
id = 'id_example' # str | L'identifiant de l'étude

try: 
    # Récupérer une étude
    api_response = api_instance.studies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EtudesApi->studies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| L&#39;identifiant de l&#39;étude | 

### Return type

[**Study**](Study.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_put**
> Study studies_id_put(id)

Mettre à jour une étude

Mettre à jour une étude par son identifiant

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
api_instance = swagger_client.EtudesApi()
id = 'id_example' # str | L'identifiant de l'étude

try: 
    # Mettre à jour une étude
    api_response = api_instance.studies_id_put(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EtudesApi->studies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| L&#39;identifiant de l&#39;étude | 

### Return type

[**Study**](Study.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_post**
> Study studies_post(body)

Créer une étude

Retourne l'étude créé

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
api_instance = swagger_client.EtudesApi()
body = swagger_client.Body2() # Body2 | Formulaire pour la création d'une étude

try: 
    # Créer une étude
    api_response = api_instance.studies_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EtudesApi->studies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| Formulaire pour la création d&#39;une étude | 

### Return type

[**Study**](Study.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

