# coding: utf-8

"""
    Yanport API

    ## À propos Voici quelques ressources qui vous aideront à explorer notre API, si vous avez des problèmes ou des demandes, veuillez contacter le [support](mailto:support@yanport.com). ## REST API Nos services webs utilisent le protocle **HTTPS** sur le port 443, tout accès en HTTP sur le port 80 est bloqué par notre pare-feu. Les échanges de données sont réalisés en **JSON**. ## Authentification Avant de commencer à explorer notre API, vous devez nous [contacter](https://www.yanport.com/contact) afin d'obtenir un [JSON Web Token](https://jwt.io) (**JWT**) qui vous permettra de vous identifier à chaque requêtes. ### JWT (header) La méthode privilégiée pour s'authentifier est de passer à chaque requêtes le token dans le header `Authorization: Bearer {{ JWT }}` en remplaçant `{{ JWT }}` par votre token. ### JWT (query param) Il est aussi possible de passer le token directement en query param de la requête `https://api.yanport.com/?token={{ JWT }}`. (_privilégié le passage par header en production._) ## Pour démarrer Lorsque vous disposez de votre token d'authentification, vous pouvez commencer à explorer notre API grâce au boutton  `Try it out` sur chacun de nos webs services. Mais au préalable, vous devez vous authentifier en cliquant sur le boutton `Authorize `, en remplissant l'input `api_key` avec `Bearer {{ JWT }}`.  **Exemple** `Bearer eyUEkiLCJh...CHCUiBfD63oxoo=` ## Limitation Toutes les requêtes à notre API sont loggées, c'est pourquoi vous devez respecter nos [CGU](https://dev.yanport.com/cgu) afin d'éviter tout usage abusif de notre API. 

    OpenAPI spec version: 1.0
    Contact: dev@yanport.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AgencesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def agencies_get(self, **kwargs):
        """
        Rechercher des agences
        Rechercher des agences selon plusieurs critères # Exemples   ## Les agences situées à Levallois-Perret et qui ont au moins 10 biens en vente et en location     /agencies?cityIds=54178039&salePropertyCountMin=10&rentPropertyCountMin=10   ## Les agences situées dans un rayon de 100m autour de Levallois-Perret     /agencies?lat=48.8932&lon=2.2879&radius=100m   ## Les agences Nexity     /agencies?siren=487530099
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.agencies_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int _from: Début de la pagination
        :param int size: Nombre de résultats
        :param str sort: Trier par
        :param list[str] includes: Inclure un ou plusieurs élements par identifiant
        :param list[str] excludes: Exclure un ou plusieurs élements par identifiant
        :param str q: Recherche plein-texte
        :param str external_id: Identifiant externe client
        :param int organization_id: Identifiant de l'organisation
        :param list[str] siren: Siren de l'entreprise
        :param list[str] siret: Siret de l'entreprise
        :param list[int] city_ids: Liste d'identifiants de villes
        :param float lat: Latitude
        :param float lng: Longitude
        :param str radius: Radius
        :param int sale_property_count_min: Nombre minimal de biens en vente
        :param int sale_property_count_max: Nombre maximal de biens en vente
        :param int rent_property_count_min: Nombre minimal de biens en location
        :param int rent_property_count_max: Nombre maximal de biens en location
        :param bool active: Agence active
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.agencies_get_with_http_info(**kwargs)
        else:
            (data) = self.agencies_get_with_http_info(**kwargs)
            return data

    def agencies_get_with_http_info(self, **kwargs):
        """
        Rechercher des agences
        Rechercher des agences selon plusieurs critères # Exemples   ## Les agences situées à Levallois-Perret et qui ont au moins 10 biens en vente et en location     /agencies?cityIds=54178039&salePropertyCountMin=10&rentPropertyCountMin=10   ## Les agences situées dans un rayon de 100m autour de Levallois-Perret     /agencies?lat=48.8932&lon=2.2879&radius=100m   ## Les agences Nexity     /agencies?siren=487530099
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.agencies_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int _from: Début de la pagination
        :param int size: Nombre de résultats
        :param str sort: Trier par
        :param list[str] includes: Inclure un ou plusieurs élements par identifiant
        :param list[str] excludes: Exclure un ou plusieurs élements par identifiant
        :param str q: Recherche plein-texte
        :param str external_id: Identifiant externe client
        :param int organization_id: Identifiant de l'organisation
        :param list[str] siren: Siren de l'entreprise
        :param list[str] siret: Siret de l'entreprise
        :param list[int] city_ids: Liste d'identifiants de villes
        :param float lat: Latitude
        :param float lng: Longitude
        :param str radius: Radius
        :param int sale_property_count_min: Nombre minimal de biens en vente
        :param int sale_property_count_max: Nombre maximal de biens en vente
        :param int rent_property_count_min: Nombre minimal de biens en location
        :param int rent_property_count_max: Nombre maximal de biens en location
        :param bool active: Agence active
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_from', 'size', 'sort', 'includes', 'excludes', 'q', 'external_id', 'organization_id', 'siren', 'siret', 'city_ids', 'lat', 'lng', 'radius', 'sale_property_count_min', 'sale_property_count_max', 'rent_property_count_min', 'rent_property_count_max', 'active']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agencies_get" % key
                )
            params[key] = val
        del params['kwargs']

        if '_from' in params and params['_from'] < 0:
            raise ValueError("Invalid value for parameter `_from` when calling `agencies_get`, must be a value greater than or equal to `0`")
        if 'size' in params and params['size'] > 1000:
            raise ValueError("Invalid value for parameter `size` when calling `agencies_get`, must be a value less than or equal to `1000`")
        if 'size' in params and params['size'] < 0:
            raise ValueError("Invalid value for parameter `size` when calling `agencies_get`, must be a value greater than or equal to `0`")
        if 'sale_property_count_min' in params and params['sale_property_count_min'] < 0:
            raise ValueError("Invalid value for parameter `sale_property_count_min` when calling `agencies_get`, must be a value greater than or equal to `0`")
        if 'sale_property_count_max' in params and params['sale_property_count_max'] < 0:
            raise ValueError("Invalid value for parameter `sale_property_count_max` when calling `agencies_get`, must be a value greater than or equal to `0`")
        if 'rent_property_count_min' in params and params['rent_property_count_min'] < 0:
            raise ValueError("Invalid value for parameter `rent_property_count_min` when calling `agencies_get`, must be a value greater than or equal to `0`")
        if 'rent_property_count_max' in params and params['rent_property_count_max'] < 0:
            raise ValueError("Invalid value for parameter `rent_property_count_max` when calling `agencies_get`, must be a value greater than or equal to `0`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'includes' in params:
            query_params.append(('includes', params['includes']))
            collection_formats['includes'] = 'multi'
        if 'excludes' in params:
            query_params.append(('excludes', params['excludes']))
            collection_formats['excludes'] = 'multi'
        if 'q' in params:
            query_params.append(('q', params['q']))
        if 'external_id' in params:
            query_params.append(('externalId', params['external_id']))
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))
        if 'siren' in params:
            query_params.append(('siren', params['siren']))
            collection_formats['siren'] = 'csv'
        if 'siret' in params:
            query_params.append(('siret', params['siret']))
            collection_formats['siret'] = 'csv'
        if 'city_ids' in params:
            query_params.append(('cityIds', params['city_ids']))
            collection_formats['cityIds'] = 'csv'
        if 'lat' in params:
            query_params.append(('lat', params['lat']))
        if 'lng' in params:
            query_params.append(('lng', params['lng']))
        if 'radius' in params:
            query_params.append(('radius', params['radius']))
        if 'sale_property_count_min' in params:
            query_params.append(('salePropertyCountMin', params['sale_property_count_min']))
        if 'sale_property_count_max' in params:
            query_params.append(('salePropertyCountMax', params['sale_property_count_max']))
        if 'rent_property_count_min' in params:
            query_params.append(('rentPropertyCountMin', params['rent_property_count_min']))
        if 'rent_property_count_max' in params:
            query_params.append(('rentPropertyCountMax', params['rent_property_count_max']))
        if 'active' in params:
            query_params.append(('active', params['active']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/agencies', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2005',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def agencies_id_get(self, id, **kwargs):
        """
        Récupérer une agence
        Récupérer une agence par son identifiant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.agencies_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: L'identifiant de l'agence (required)
        :return: Agency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.agencies_id_get_with_http_info(id, **kwargs)
        else:
            (data) = self.agencies_id_get_with_http_info(id, **kwargs)
            return data

    def agencies_id_get_with_http_info(self, id, **kwargs):
        """
        Récupérer une agence
        Récupérer une agence par son identifiant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.agencies_id_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: L'identifiant de l'agence (required)
        :return: Agency
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method agencies_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `agencies_id_get`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/agencies/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Agency',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
