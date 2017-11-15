# swagger_client.EncadrementloyersApi

All URIs are relative to *https://api.yanport.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rent_control_check_post**](EncadrementloyersApi.md#rent_control_check_post) | **POST** /rent-control/check | Encadrement des loyers


# **rent_control_check_post**
> RentControlResult rent_control_check_post(body)

Encadrement des loyers

Permet de controller vis-à-vis de la législation si un loyer est hors/dans l'encadrement des loyers.

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
api_instance = swagger_client.EncadrementloyersApi()
body = swagger_client.Body() # Body | Requête d'encadrement d'un loyer

try: 
    # Encadrement des loyers
    api_response = api_instance.rent_control_check_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EncadrementloyersApi->rent_control_check_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Requête d&#39;encadrement d&#39;un loyer | 

### Return type

[**RentControlResult**](RentControlResult.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

