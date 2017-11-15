# swagger_client.UtilisateursApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UtilisateursApi.md#users_get) | **GET** /users | Rechercher des utilisateurs
[**users_id_activate_get**](UtilisateursApi.md#users_id_activate_get) | **GET** /users/{id}/activate | Activer un utilisateur
[**users_id_avatars_post**](UtilisateursApi.md#users_id_avatars_post) | **POST** /users/{id}/avatars | Mettre à jour l&#39;avatar d&#39;un utilisateur
[**users_id_deactivate_get**](UtilisateursApi.md#users_id_deactivate_get) | **GET** /users/{id}/deactivate | Désactiver un utilisateur
[**users_id_delete**](UtilisateursApi.md#users_id_delete) | **DELETE** /users/{id} | Supprimer un utilisateur
[**users_id_get**](UtilisateursApi.md#users_id_get) | **GET** /users/{id} | Recupérer un utilisateur par id
[**users_id_put**](UtilisateursApi.md#users_id_put) | **PUT** /users/{id} | Mettre à jour un utilisateur
[**users_id_team_get**](UtilisateursApi.md#users_id_team_get) | **GET** /users/{id}/team | Recupérer les utilisateurs (agents) faisant équipe avec l&#39;utilsateur correspondant à l&#39;id donné
[**users_post**](UtilisateursApi.md#users_post) | **POST** /users | Créer un utilisateur


# **users_get**
> InlineResponse2004 users_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, q=q, username=username, email=email, external_id=external_id, organization_id=organization_id, mandatary_network_ids=mandatary_network_ids, agency_ids=agency_ids, active=active, first_connection=first_connection, admin=admin)

Rechercher des utilisateurs

Rechercher des utilisateurs

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
api_instance = swagger_client.UtilisateursApi()
_from = 0 # int | Début de la pagination (optional) (default to 0)
size = 20 # int | Nombre de résultats (optional) (default to 20)
sort = 'sort_example' # str | Trier par (optional)
includes = ['includes_example'] # list[str] | Inclure un ou plusieurs élements par identifiant (optional)
excludes = ['excludes_example'] # list[str] | Exclure un ou plusieurs élements par identifiant (optional)
q = 'q_example' # str | Recherche plein-texte (optional)
username = 'username_example' # str | Nom de l'utilisateur (optional)
email = 'email_example' # str | Email de l'utilisateur (optional)
external_id = 'external_id_example' # str | TODO (optional)
organization_id = 789 # int | Identifiant de l'organisation (optional)
mandatary_network_ids = [56] # list[int] | Identifiants de réseaux mandataires (optional)
agency_ids = [56] # list[int] | Identifiants d'agences (optional)
active = true # bool | Filter les utilisateurs actifs ou non (optional)
first_connection = true # bool | Filtrer les utilisateurs s'étant deja connectés à l'application ou non (optional)
admin = true # bool | Filter les utilisateurs administrateurs ou non (optional)

try: 
    # Rechercher des utilisateurs
    api_response = api_instance.users_get(_from=_from, size=size, sort=sort, includes=includes, excludes=excludes, q=q, username=username, email=email, external_id=external_id, organization_id=organization_id, mandatary_network_ids=mandatary_network_ids, agency_ids=agency_ids, active=active, first_connection=first_connection, admin=admin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_get: %s\n" % e)
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
 **username** | **str**| Nom de l&#39;utilisateur | [optional] 
 **email** | **str**| Email de l&#39;utilisateur | [optional] 
 **external_id** | **str**| TODO | [optional] 
 **organization_id** | **int**| Identifiant de l&#39;organisation | [optional] 
 **mandatary_network_ids** | [**list[int]**](int.md)| Identifiants de réseaux mandataires | [optional] 
 **agency_ids** | [**list[int]**](int.md)| Identifiants d&#39;agences | [optional] 
 **active** | **bool**| Filter les utilisateurs actifs ou non | [optional] 
 **first_connection** | **bool**| Filtrer les utilisateurs s&#39;étant deja connectés à l&#39;application ou non | [optional] 
 **admin** | **bool**| Filter les utilisateurs administrateurs ou non | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_activate_get**
> DefaultResponse users_id_activate_get(id)

Activer un utilisateur

Activer un utilisateur correspondant à l'id donné

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
api_instance = swagger_client.UtilisateursApi()
id = 789 # int | L'identifiant de l'utilisateur

try: 
    # Activer un utilisateur
    api_response = api_instance.users_id_activate_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_id_activate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;utilisateur | 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_avatars_post**
> str users_id_avatars_post(id, location, file_name, media_type, content, md5, base64)

Mettre à jour l'avatar d'un utilisateur

Met à jour l'avatar d'un utilisateur et retourne son url

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
api_instance = swagger_client.UtilisateursApi()
id = 789 # int | L'identifiant de l'utilisateur
location = 'location_example' # str | Localisation de l'image
file_name = 'file_name_example' # str | Nom du fichier
media_type = 'media_type_example' # str | Type de l'image
content = 'content_example' # str | L'image
md5 = 'md5_example' # str | Somme md5 de l'image
base64 = true # bool | L'image est-elle encodée en base 64

try: 
    # Mettre à jour l'avatar d'un utilisateur
    api_response = api_instance.users_id_avatars_post(id, location, file_name, media_type, content, md5, base64)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_id_avatars_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;utilisateur | 
 **location** | **str**| Localisation de l&#39;image | 
 **file_name** | **str**| Nom du fichier | 
 **media_type** | **str**| Type de l&#39;image | 
 **content** | **str**| L&#39;image | 
 **md5** | **str**| Somme md5 de l&#39;image | 
 **base64** | **bool**| L&#39;image est-elle encodée en base 64 | 

### Return type

**str**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_deactivate_get**
> DefaultResponse users_id_deactivate_get(id)

Désactiver un utilisateur

Désactiver un utilisateur correspondant à l'id donné

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
api_instance = swagger_client.UtilisateursApi()
id = 789 # int | L'identifiant de l'utilisateur

try: 
    # Désactiver un utilisateur
    api_response = api_instance.users_id_deactivate_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_id_deactivate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;utilisateur | 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_delete**
> DefaultResponse users_id_delete(id)

Supprimer un utilisateur

Supprime l'utilisateur correspondant à l'id donné

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
api_instance = swagger_client.UtilisateursApi()
id = 789 # int | L'identifiant de l'utilisateur

try: 
    # Supprimer un utilisateur
    api_response = api_instance.users_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;utilisateur | 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_get**
> User users_id_get(id)

Recupérer un utilisateur par id

Retourne l'utilisateur correspondant

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
api_instance = swagger_client.UtilisateursApi()
id = 789 # int | L'identifiant de l'utilisateur

try: 
    # Recupérer un utilisateur par id
    api_response = api_instance.users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;utilisateur | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_put**
> User users_id_put(id, user)

Mettre à jour un utilisateur

Met à jour un utilisateur et retourne celui-ci

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
api_instance = swagger_client.UtilisateursApi()
id = 789 # int | L'identifiant de l'utilisateur
user = swagger_client.User() # User | Données de l'utilisateur à mettre à jour

try: 
    # Mettre à jour un utilisateur
    api_response = api_instance.users_id_put(id, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;utilisateur | 
 **user** | [**User**](User.md)| Données de l&#39;utilisateur à mettre à jour | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_team_get**
> list[User] users_id_team_get(id)

Recupérer les utilisateurs (agents) faisant équipe avec l'utilsateur correspondant à l'id donné

Retourne les utilisateurs correspondants

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
api_instance = swagger_client.UtilisateursApi()
id = 789 # int | L'identifiant de l'utilisateur

try: 
    # Recupérer les utilisateurs (agents) faisant équipe avec l'utilsateur correspondant à l'id donné
    api_response = api_instance.users_id_team_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_id_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| L&#39;identifiant de l&#39;utilisateur | 

### Return type

[**list[User]**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(body)

Créer un utilisateur

Retourne l'utilisateur créé

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
api_instance = swagger_client.UtilisateursApi()
body = swagger_client.Body1() # Body1 | Formulaire pour la création d'un utilisateur

try: 
    # Créer un utilisateur
    api_response = api_instance.users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilisateursApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| Formulaire pour la création d&#39;un utilisateur | 

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

