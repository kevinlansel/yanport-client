# coding: utf-8

"""
    Yanport API

    ## À propos Voici quelques ressources qui vous aideront à explorer notre API, si vous avez des problèmes ou des demandes, veuillez contacter le [support](mailto:support@yanport.com). ## REST API Nos services webs utilisent le protocle **HTTPS** sur le port 443, tout accès en HTTP sur le port 80 est bloqué par notre pare-feu. Les échanges de données sont réalisés en **JSON**. ## Authentification Avant de commencer à explorer notre API, vous devez nous [contacter](https://www.yanport.com/contact) afin d'obtenir un [JSON Web Token](https://jwt.io) (**JWT**) qui vous permettra de vous identifier à chaque requêtes. ### JWT (header) La méthode privilégiée pour s'authentifier est de passer à chaque requêtes le token dans le header `Authorization: Bearer {{ JWT }}` en remplaçant `{{ JWT }}` par votre token. ### JWT (query param) Il est aussi possible de passer le token directement en query param de la requête `https://api.yanport.com/?token={{ JWT }}`. (_privilégié le passage par header en production._) ## Pour démarrer Lorsque vous disposez de votre token d'authentification, vous pouvez commencer à explorer notre API grâce au boutton  `Try it out` sur chacun de nos webs services. Mais au préalable, vous devez vous authentifier en cliquant sur le boutton `Authorize `, en remplissant l'input `api_key` avec `Bearer {{ JWT }}`.  **Exemple** `Bearer eyUEkiLCJh...CHCUiBfD63oxoo=` ## Limitation Toutes les requêtes à notre API sont loggées, c'est pourquoi vous devez respecter nos [CGU](https://dev.yanport.com/cgu) afin d'éviter tout usage abusif de notre API. 

    OpenAPI spec version: 1.0
    Contact: dev@yanport.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PropertySearchQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'search_query_param': 'SearchQueryParam',
        'query_string': 'str',
        'marketing_types': 'list[MarketingType]',
        'crawl_sources': 'list[CrawlSource]',
        'active': 'bool',
        'dealer_types': 'list[DealerType]',
        'dealer_names': 'list[str]',
        'exclusive_mandate': 'bool',
        'dealer_ids': 'int',
        'excluded_dealer_ids': 'list[int]',
        'property_ids': 'list[str]',
        'property_types': 'list[PropertyType]',
        'room_counts': 'list[int]',
        'departments': 'list[str]',
        'zip_codes': 'list[str]',
        'city_ids': 'list[int]',
        'publication_date_min': 'datetime',
        'publication_date_max': 'datetime',
        'ad_publication_date_min': 'datetime',
        'ad_publication_date_max': 'datetime',
        'last_price_decrease_date_min': 'datetime',
        'last_price_decrease_date_max': 'datetime',
        'delete_date_min': 'datetime',
        'delete_date_max': 'datetime',
        'duration_days_min': 'int',
        'duration_days_max': 'int',
        'surface_min': 'float',
        'surface_max': 'float',
        'price_min': 'float',
        'price_max': 'float',
        'price_m2_min': 'float',
        'price_m2_max': 'float',
        'price_hc_min': 'float',
        'price_hc_max': 'float',
        'price_m2_hc_min': 'float',
        'price_m2_hc_max': 'float',
        'price_cc_min': 'float',
        'price_cc_max': 'float',
        'fees_min': 'float',
        'fees_max': 'float',
        'deposit_min': 'float',
        'deposit_max': 'float',
        'furnished': 'bool',
        'new_build': 'bool',
        'missing_fields': 'list[str]',
        'excluded_ids': 'list[str]'
    }

    attribute_map = {
        'search_query_param': 'searchQueryParam',
        'query_string': 'queryString',
        'marketing_types': 'marketingTypes',
        'crawl_sources': 'crawlSources',
        'active': 'active',
        'dealer_types': 'dealerTypes',
        'dealer_names': 'dealerNames',
        'exclusive_mandate': 'exclusiveMandate',
        'dealer_ids': 'dealerIds',
        'excluded_dealer_ids': 'excludedDealerIds',
        'property_ids': 'propertyIds',
        'property_types': 'propertyTypes',
        'room_counts': 'roomCounts',
        'departments': 'departments',
        'zip_codes': 'zipCodes',
        'city_ids': 'cityIds',
        'publication_date_min': 'publicationDateMin',
        'publication_date_max': 'publicationDateMax',
        'ad_publication_date_min': 'adPublicationDateMin',
        'ad_publication_date_max': 'adPublicationDateMax',
        'last_price_decrease_date_min': 'lastPriceDecreaseDateMin',
        'last_price_decrease_date_max': 'lastPriceDecreaseDateMax',
        'delete_date_min': 'deleteDateMin',
        'delete_date_max': 'deleteDateMax',
        'duration_days_min': 'durationDaysMin',
        'duration_days_max': 'durationDaysMax',
        'surface_min': 'surfaceMin',
        'surface_max': 'surfaceMax',
        'price_min': 'priceMin',
        'price_max': 'priceMax',
        'price_m2_min': 'priceM2Min',
        'price_m2_max': 'priceM2Max',
        'price_hc_min': 'priceHCMin',
        'price_hc_max': 'priceHCMax',
        'price_m2_hc_min': 'priceM2HCMin',
        'price_m2_hc_max': 'priceM2HCMax',
        'price_cc_min': 'priceCCMin',
        'price_cc_max': 'priceCCMax',
        'fees_min': 'feesMin',
        'fees_max': 'feesMax',
        'deposit_min': 'depositMin',
        'deposit_max': 'depositMax',
        'furnished': 'furnished',
        'new_build': 'newBuild',
        'missing_fields': 'missingFields',
        'excluded_ids': 'excludedIds'
    }

    def __init__(self, search_query_param=None, query_string=None, marketing_types=None, crawl_sources=None, active=None, dealer_types=None, dealer_names=None, exclusive_mandate=None, dealer_ids=None, excluded_dealer_ids=None, property_ids=None, property_types=None, room_counts=None, departments=None, zip_codes=None, city_ids=None, publication_date_min=None, publication_date_max=None, ad_publication_date_min=None, ad_publication_date_max=None, last_price_decrease_date_min=None, last_price_decrease_date_max=None, delete_date_min=None, delete_date_max=None, duration_days_min=None, duration_days_max=None, surface_min=None, surface_max=None, price_min=None, price_max=None, price_m2_min=None, price_m2_max=None, price_hc_min=None, price_hc_max=None, price_m2_hc_min=None, price_m2_hc_max=None, price_cc_min=None, price_cc_max=None, fees_min=None, fees_max=None, deposit_min=None, deposit_max=None, furnished=None, new_build=None, missing_fields=None, excluded_ids=None):
        """
        PropertySearchQuery - a model defined in Swagger
        """

        self._search_query_param = None
        self._query_string = None
        self._marketing_types = None
        self._crawl_sources = None
        self._active = None
        self._dealer_types = None
        self._dealer_names = None
        self._exclusive_mandate = None
        self._dealer_ids = None
        self._excluded_dealer_ids = None
        self._property_ids = None
        self._property_types = None
        self._room_counts = None
        self._departments = None
        self._zip_codes = None
        self._city_ids = None
        self._publication_date_min = None
        self._publication_date_max = None
        self._ad_publication_date_min = None
        self._ad_publication_date_max = None
        self._last_price_decrease_date_min = None
        self._last_price_decrease_date_max = None
        self._delete_date_min = None
        self._delete_date_max = None
        self._duration_days_min = None
        self._duration_days_max = None
        self._surface_min = None
        self._surface_max = None
        self._price_min = None
        self._price_max = None
        self._price_m2_min = None
        self._price_m2_max = None
        self._price_hc_min = None
        self._price_hc_max = None
        self._price_m2_hc_min = None
        self._price_m2_hc_max = None
        self._price_cc_min = None
        self._price_cc_max = None
        self._fees_min = None
        self._fees_max = None
        self._deposit_min = None
        self._deposit_max = None
        self._furnished = None
        self._new_build = None
        self._missing_fields = None
        self._excluded_ids = None

        if search_query_param is not None:
          self.search_query_param = search_query_param
        if query_string is not None:
          self.query_string = query_string
        if marketing_types is not None:
          self.marketing_types = marketing_types
        if crawl_sources is not None:
          self.crawl_sources = crawl_sources
        if active is not None:
          self.active = active
        if dealer_types is not None:
          self.dealer_types = dealer_types
        if dealer_names is not None:
          self.dealer_names = dealer_names
        if exclusive_mandate is not None:
          self.exclusive_mandate = exclusive_mandate
        if dealer_ids is not None:
          self.dealer_ids = dealer_ids
        if excluded_dealer_ids is not None:
          self.excluded_dealer_ids = excluded_dealer_ids
        if property_ids is not None:
          self.property_ids = property_ids
        if property_types is not None:
          self.property_types = property_types
        if room_counts is not None:
          self.room_counts = room_counts
        if departments is not None:
          self.departments = departments
        if zip_codes is not None:
          self.zip_codes = zip_codes
        if city_ids is not None:
          self.city_ids = city_ids
        if publication_date_min is not None:
          self.publication_date_min = publication_date_min
        if publication_date_max is not None:
          self.publication_date_max = publication_date_max
        if ad_publication_date_min is not None:
          self.ad_publication_date_min = ad_publication_date_min
        if ad_publication_date_max is not None:
          self.ad_publication_date_max = ad_publication_date_max
        if last_price_decrease_date_min is not None:
          self.last_price_decrease_date_min = last_price_decrease_date_min
        if last_price_decrease_date_max is not None:
          self.last_price_decrease_date_max = last_price_decrease_date_max
        if delete_date_min is not None:
          self.delete_date_min = delete_date_min
        if delete_date_max is not None:
          self.delete_date_max = delete_date_max
        if duration_days_min is not None:
          self.duration_days_min = duration_days_min
        if duration_days_max is not None:
          self.duration_days_max = duration_days_max
        if surface_min is not None:
          self.surface_min = surface_min
        if surface_max is not None:
          self.surface_max = surface_max
        if price_min is not None:
          self.price_min = price_min
        if price_max is not None:
          self.price_max = price_max
        if price_m2_min is not None:
          self.price_m2_min = price_m2_min
        if price_m2_max is not None:
          self.price_m2_max = price_m2_max
        if price_hc_min is not None:
          self.price_hc_min = price_hc_min
        if price_hc_max is not None:
          self.price_hc_max = price_hc_max
        if price_m2_hc_min is not None:
          self.price_m2_hc_min = price_m2_hc_min
        if price_m2_hc_max is not None:
          self.price_m2_hc_max = price_m2_hc_max
        if price_cc_min is not None:
          self.price_cc_min = price_cc_min
        if price_cc_max is not None:
          self.price_cc_max = price_cc_max
        if fees_min is not None:
          self.fees_min = fees_min
        if fees_max is not None:
          self.fees_max = fees_max
        if deposit_min is not None:
          self.deposit_min = deposit_min
        if deposit_max is not None:
          self.deposit_max = deposit_max
        if furnished is not None:
          self.furnished = furnished
        if new_build is not None:
          self.new_build = new_build
        if missing_fields is not None:
          self.missing_fields = missing_fields
        if excluded_ids is not None:
          self.excluded_ids = excluded_ids

    @property
    def search_query_param(self):
        """
        Gets the search_query_param of this PropertySearchQuery.

        :return: The search_query_param of this PropertySearchQuery.
        :rtype: SearchQueryParam
        """
        return self._search_query_param

    @search_query_param.setter
    def search_query_param(self, search_query_param):
        """
        Sets the search_query_param of this PropertySearchQuery.

        :param search_query_param: The search_query_param of this PropertySearchQuery.
        :type: SearchQueryParam
        """

        self._search_query_param = search_query_param

    @property
    def query_string(self):
        """
        Gets the query_string of this PropertySearchQuery.

        :return: The query_string of this PropertySearchQuery.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """
        Sets the query_string of this PropertySearchQuery.

        :param query_string: The query_string of this PropertySearchQuery.
        :type: str
        """

        self._query_string = query_string

    @property
    def marketing_types(self):
        """
        Gets the marketing_types of this PropertySearchQuery.

        :return: The marketing_types of this PropertySearchQuery.
        :rtype: list[MarketingType]
        """
        return self._marketing_types

    @marketing_types.setter
    def marketing_types(self, marketing_types):
        """
        Sets the marketing_types of this PropertySearchQuery.

        :param marketing_types: The marketing_types of this PropertySearchQuery.
        :type: list[MarketingType]
        """

        self._marketing_types = marketing_types

    @property
    def crawl_sources(self):
        """
        Gets the crawl_sources of this PropertySearchQuery.

        :return: The crawl_sources of this PropertySearchQuery.
        :rtype: list[CrawlSource]
        """
        return self._crawl_sources

    @crawl_sources.setter
    def crawl_sources(self, crawl_sources):
        """
        Sets the crawl_sources of this PropertySearchQuery.

        :param crawl_sources: The crawl_sources of this PropertySearchQuery.
        :type: list[CrawlSource]
        """

        self._crawl_sources = crawl_sources

    @property
    def active(self):
        """
        Gets the active of this PropertySearchQuery.

        :return: The active of this PropertySearchQuery.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this PropertySearchQuery.

        :param active: The active of this PropertySearchQuery.
        :type: bool
        """

        self._active = active

    @property
    def dealer_types(self):
        """
        Gets the dealer_types of this PropertySearchQuery.

        :return: The dealer_types of this PropertySearchQuery.
        :rtype: list[DealerType]
        """
        return self._dealer_types

    @dealer_types.setter
    def dealer_types(self, dealer_types):
        """
        Sets the dealer_types of this PropertySearchQuery.

        :param dealer_types: The dealer_types of this PropertySearchQuery.
        :type: list[DealerType]
        """

        self._dealer_types = dealer_types

    @property
    def dealer_names(self):
        """
        Gets the dealer_names of this PropertySearchQuery.

        :return: The dealer_names of this PropertySearchQuery.
        :rtype: list[str]
        """
        return self._dealer_names

    @dealer_names.setter
    def dealer_names(self, dealer_names):
        """
        Sets the dealer_names of this PropertySearchQuery.

        :param dealer_names: The dealer_names of this PropertySearchQuery.
        :type: list[str]
        """

        self._dealer_names = dealer_names

    @property
    def exclusive_mandate(self):
        """
        Gets the exclusive_mandate of this PropertySearchQuery.

        :return: The exclusive_mandate of this PropertySearchQuery.
        :rtype: bool
        """
        return self._exclusive_mandate

    @exclusive_mandate.setter
    def exclusive_mandate(self, exclusive_mandate):
        """
        Sets the exclusive_mandate of this PropertySearchQuery.

        :param exclusive_mandate: The exclusive_mandate of this PropertySearchQuery.
        :type: bool
        """

        self._exclusive_mandate = exclusive_mandate

    @property
    def dealer_ids(self):
        """
        Gets the dealer_ids of this PropertySearchQuery.

        :return: The dealer_ids of this PropertySearchQuery.
        :rtype: int
        """
        return self._dealer_ids

    @dealer_ids.setter
    def dealer_ids(self, dealer_ids):
        """
        Sets the dealer_ids of this PropertySearchQuery.

        :param dealer_ids: The dealer_ids of this PropertySearchQuery.
        :type: int
        """

        self._dealer_ids = dealer_ids

    @property
    def excluded_dealer_ids(self):
        """
        Gets the excluded_dealer_ids of this PropertySearchQuery.

        :return: The excluded_dealer_ids of this PropertySearchQuery.
        :rtype: list[int]
        """
        return self._excluded_dealer_ids

    @excluded_dealer_ids.setter
    def excluded_dealer_ids(self, excluded_dealer_ids):
        """
        Sets the excluded_dealer_ids of this PropertySearchQuery.

        :param excluded_dealer_ids: The excluded_dealer_ids of this PropertySearchQuery.
        :type: list[int]
        """

        self._excluded_dealer_ids = excluded_dealer_ids

    @property
    def property_ids(self):
        """
        Gets the property_ids of this PropertySearchQuery.

        :return: The property_ids of this PropertySearchQuery.
        :rtype: list[str]
        """
        return self._property_ids

    @property_ids.setter
    def property_ids(self, property_ids):
        """
        Sets the property_ids of this PropertySearchQuery.

        :param property_ids: The property_ids of this PropertySearchQuery.
        :type: list[str]
        """

        self._property_ids = property_ids

    @property
    def property_types(self):
        """
        Gets the property_types of this PropertySearchQuery.

        :return: The property_types of this PropertySearchQuery.
        :rtype: list[PropertyType]
        """
        return self._property_types

    @property_types.setter
    def property_types(self, property_types):
        """
        Sets the property_types of this PropertySearchQuery.

        :param property_types: The property_types of this PropertySearchQuery.
        :type: list[PropertyType]
        """

        self._property_types = property_types

    @property
    def room_counts(self):
        """
        Gets the room_counts of this PropertySearchQuery.

        :return: The room_counts of this PropertySearchQuery.
        :rtype: list[int]
        """
        return self._room_counts

    @room_counts.setter
    def room_counts(self, room_counts):
        """
        Sets the room_counts of this PropertySearchQuery.

        :param room_counts: The room_counts of this PropertySearchQuery.
        :type: list[int]
        """

        self._room_counts = room_counts

    @property
    def departments(self):
        """
        Gets the departments of this PropertySearchQuery.

        :return: The departments of this PropertySearchQuery.
        :rtype: list[str]
        """
        return self._departments

    @departments.setter
    def departments(self, departments):
        """
        Sets the departments of this PropertySearchQuery.

        :param departments: The departments of this PropertySearchQuery.
        :type: list[str]
        """

        self._departments = departments

    @property
    def zip_codes(self):
        """
        Gets the zip_codes of this PropertySearchQuery.

        :return: The zip_codes of this PropertySearchQuery.
        :rtype: list[str]
        """
        return self._zip_codes

    @zip_codes.setter
    def zip_codes(self, zip_codes):
        """
        Sets the zip_codes of this PropertySearchQuery.

        :param zip_codes: The zip_codes of this PropertySearchQuery.
        :type: list[str]
        """

        self._zip_codes = zip_codes

    @property
    def city_ids(self):
        """
        Gets the city_ids of this PropertySearchQuery.

        :return: The city_ids of this PropertySearchQuery.
        :rtype: list[int]
        """
        return self._city_ids

    @city_ids.setter
    def city_ids(self, city_ids):
        """
        Sets the city_ids of this PropertySearchQuery.

        :param city_ids: The city_ids of this PropertySearchQuery.
        :type: list[int]
        """

        self._city_ids = city_ids

    @property
    def publication_date_min(self):
        """
        Gets the publication_date_min of this PropertySearchQuery.

        :return: The publication_date_min of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._publication_date_min

    @publication_date_min.setter
    def publication_date_min(self, publication_date_min):
        """
        Sets the publication_date_min of this PropertySearchQuery.

        :param publication_date_min: The publication_date_min of this PropertySearchQuery.
        :type: datetime
        """

        self._publication_date_min = publication_date_min

    @property
    def publication_date_max(self):
        """
        Gets the publication_date_max of this PropertySearchQuery.

        :return: The publication_date_max of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._publication_date_max

    @publication_date_max.setter
    def publication_date_max(self, publication_date_max):
        """
        Sets the publication_date_max of this PropertySearchQuery.

        :param publication_date_max: The publication_date_max of this PropertySearchQuery.
        :type: datetime
        """

        self._publication_date_max = publication_date_max

    @property
    def ad_publication_date_min(self):
        """
        Gets the ad_publication_date_min of this PropertySearchQuery.

        :return: The ad_publication_date_min of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._ad_publication_date_min

    @ad_publication_date_min.setter
    def ad_publication_date_min(self, ad_publication_date_min):
        """
        Sets the ad_publication_date_min of this PropertySearchQuery.

        :param ad_publication_date_min: The ad_publication_date_min of this PropertySearchQuery.
        :type: datetime
        """

        self._ad_publication_date_min = ad_publication_date_min

    @property
    def ad_publication_date_max(self):
        """
        Gets the ad_publication_date_max of this PropertySearchQuery.

        :return: The ad_publication_date_max of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._ad_publication_date_max

    @ad_publication_date_max.setter
    def ad_publication_date_max(self, ad_publication_date_max):
        """
        Sets the ad_publication_date_max of this PropertySearchQuery.

        :param ad_publication_date_max: The ad_publication_date_max of this PropertySearchQuery.
        :type: datetime
        """

        self._ad_publication_date_max = ad_publication_date_max

    @property
    def last_price_decrease_date_min(self):
        """
        Gets the last_price_decrease_date_min of this PropertySearchQuery.

        :return: The last_price_decrease_date_min of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._last_price_decrease_date_min

    @last_price_decrease_date_min.setter
    def last_price_decrease_date_min(self, last_price_decrease_date_min):
        """
        Sets the last_price_decrease_date_min of this PropertySearchQuery.

        :param last_price_decrease_date_min: The last_price_decrease_date_min of this PropertySearchQuery.
        :type: datetime
        """

        self._last_price_decrease_date_min = last_price_decrease_date_min

    @property
    def last_price_decrease_date_max(self):
        """
        Gets the last_price_decrease_date_max of this PropertySearchQuery.

        :return: The last_price_decrease_date_max of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._last_price_decrease_date_max

    @last_price_decrease_date_max.setter
    def last_price_decrease_date_max(self, last_price_decrease_date_max):
        """
        Sets the last_price_decrease_date_max of this PropertySearchQuery.

        :param last_price_decrease_date_max: The last_price_decrease_date_max of this PropertySearchQuery.
        :type: datetime
        """

        self._last_price_decrease_date_max = last_price_decrease_date_max

    @property
    def delete_date_min(self):
        """
        Gets the delete_date_min of this PropertySearchQuery.

        :return: The delete_date_min of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._delete_date_min

    @delete_date_min.setter
    def delete_date_min(self, delete_date_min):
        """
        Sets the delete_date_min of this PropertySearchQuery.

        :param delete_date_min: The delete_date_min of this PropertySearchQuery.
        :type: datetime
        """

        self._delete_date_min = delete_date_min

    @property
    def delete_date_max(self):
        """
        Gets the delete_date_max of this PropertySearchQuery.

        :return: The delete_date_max of this PropertySearchQuery.
        :rtype: datetime
        """
        return self._delete_date_max

    @delete_date_max.setter
    def delete_date_max(self, delete_date_max):
        """
        Sets the delete_date_max of this PropertySearchQuery.

        :param delete_date_max: The delete_date_max of this PropertySearchQuery.
        :type: datetime
        """

        self._delete_date_max = delete_date_max

    @property
    def duration_days_min(self):
        """
        Gets the duration_days_min of this PropertySearchQuery.

        :return: The duration_days_min of this PropertySearchQuery.
        :rtype: int
        """
        return self._duration_days_min

    @duration_days_min.setter
    def duration_days_min(self, duration_days_min):
        """
        Sets the duration_days_min of this PropertySearchQuery.

        :param duration_days_min: The duration_days_min of this PropertySearchQuery.
        :type: int
        """

        self._duration_days_min = duration_days_min

    @property
    def duration_days_max(self):
        """
        Gets the duration_days_max of this PropertySearchQuery.

        :return: The duration_days_max of this PropertySearchQuery.
        :rtype: int
        """
        return self._duration_days_max

    @duration_days_max.setter
    def duration_days_max(self, duration_days_max):
        """
        Sets the duration_days_max of this PropertySearchQuery.

        :param duration_days_max: The duration_days_max of this PropertySearchQuery.
        :type: int
        """

        self._duration_days_max = duration_days_max

    @property
    def surface_min(self):
        """
        Gets the surface_min of this PropertySearchQuery.

        :return: The surface_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._surface_min

    @surface_min.setter
    def surface_min(self, surface_min):
        """
        Sets the surface_min of this PropertySearchQuery.

        :param surface_min: The surface_min of this PropertySearchQuery.
        :type: float
        """

        self._surface_min = surface_min

    @property
    def surface_max(self):
        """
        Gets the surface_max of this PropertySearchQuery.

        :return: The surface_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._surface_max

    @surface_max.setter
    def surface_max(self, surface_max):
        """
        Sets the surface_max of this PropertySearchQuery.

        :param surface_max: The surface_max of this PropertySearchQuery.
        :type: float
        """

        self._surface_max = surface_max

    @property
    def price_min(self):
        """
        Gets the price_min of this PropertySearchQuery.

        :return: The price_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_min

    @price_min.setter
    def price_min(self, price_min):
        """
        Sets the price_min of this PropertySearchQuery.

        :param price_min: The price_min of this PropertySearchQuery.
        :type: float
        """

        self._price_min = price_min

    @property
    def price_max(self):
        """
        Gets the price_max of this PropertySearchQuery.

        :return: The price_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_max

    @price_max.setter
    def price_max(self, price_max):
        """
        Sets the price_max of this PropertySearchQuery.

        :param price_max: The price_max of this PropertySearchQuery.
        :type: float
        """

        self._price_max = price_max

    @property
    def price_m2_min(self):
        """
        Gets the price_m2_min of this PropertySearchQuery.

        :return: The price_m2_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_m2_min

    @price_m2_min.setter
    def price_m2_min(self, price_m2_min):
        """
        Sets the price_m2_min of this PropertySearchQuery.

        :param price_m2_min: The price_m2_min of this PropertySearchQuery.
        :type: float
        """

        self._price_m2_min = price_m2_min

    @property
    def price_m2_max(self):
        """
        Gets the price_m2_max of this PropertySearchQuery.

        :return: The price_m2_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_m2_max

    @price_m2_max.setter
    def price_m2_max(self, price_m2_max):
        """
        Sets the price_m2_max of this PropertySearchQuery.

        :param price_m2_max: The price_m2_max of this PropertySearchQuery.
        :type: float
        """

        self._price_m2_max = price_m2_max

    @property
    def price_hc_min(self):
        """
        Gets the price_hc_min of this PropertySearchQuery.

        :return: The price_hc_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_hc_min

    @price_hc_min.setter
    def price_hc_min(self, price_hc_min):
        """
        Sets the price_hc_min of this PropertySearchQuery.

        :param price_hc_min: The price_hc_min of this PropertySearchQuery.
        :type: float
        """

        self._price_hc_min = price_hc_min

    @property
    def price_hc_max(self):
        """
        Gets the price_hc_max of this PropertySearchQuery.

        :return: The price_hc_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_hc_max

    @price_hc_max.setter
    def price_hc_max(self, price_hc_max):
        """
        Sets the price_hc_max of this PropertySearchQuery.

        :param price_hc_max: The price_hc_max of this PropertySearchQuery.
        :type: float
        """

        self._price_hc_max = price_hc_max

    @property
    def price_m2_hc_min(self):
        """
        Gets the price_m2_hc_min of this PropertySearchQuery.

        :return: The price_m2_hc_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_m2_hc_min

    @price_m2_hc_min.setter
    def price_m2_hc_min(self, price_m2_hc_min):
        """
        Sets the price_m2_hc_min of this PropertySearchQuery.

        :param price_m2_hc_min: The price_m2_hc_min of this PropertySearchQuery.
        :type: float
        """

        self._price_m2_hc_min = price_m2_hc_min

    @property
    def price_m2_hc_max(self):
        """
        Gets the price_m2_hc_max of this PropertySearchQuery.

        :return: The price_m2_hc_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_m2_hc_max

    @price_m2_hc_max.setter
    def price_m2_hc_max(self, price_m2_hc_max):
        """
        Sets the price_m2_hc_max of this PropertySearchQuery.

        :param price_m2_hc_max: The price_m2_hc_max of this PropertySearchQuery.
        :type: float
        """

        self._price_m2_hc_max = price_m2_hc_max

    @property
    def price_cc_min(self):
        """
        Gets the price_cc_min of this PropertySearchQuery.

        :return: The price_cc_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_cc_min

    @price_cc_min.setter
    def price_cc_min(self, price_cc_min):
        """
        Sets the price_cc_min of this PropertySearchQuery.

        :param price_cc_min: The price_cc_min of this PropertySearchQuery.
        :type: float
        """

        self._price_cc_min = price_cc_min

    @property
    def price_cc_max(self):
        """
        Gets the price_cc_max of this PropertySearchQuery.

        :return: The price_cc_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._price_cc_max

    @price_cc_max.setter
    def price_cc_max(self, price_cc_max):
        """
        Sets the price_cc_max of this PropertySearchQuery.

        :param price_cc_max: The price_cc_max of this PropertySearchQuery.
        :type: float
        """

        self._price_cc_max = price_cc_max

    @property
    def fees_min(self):
        """
        Gets the fees_min of this PropertySearchQuery.

        :return: The fees_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._fees_min

    @fees_min.setter
    def fees_min(self, fees_min):
        """
        Sets the fees_min of this PropertySearchQuery.

        :param fees_min: The fees_min of this PropertySearchQuery.
        :type: float
        """

        self._fees_min = fees_min

    @property
    def fees_max(self):
        """
        Gets the fees_max of this PropertySearchQuery.

        :return: The fees_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._fees_max

    @fees_max.setter
    def fees_max(self, fees_max):
        """
        Sets the fees_max of this PropertySearchQuery.

        :param fees_max: The fees_max of this PropertySearchQuery.
        :type: float
        """

        self._fees_max = fees_max

    @property
    def deposit_min(self):
        """
        Gets the deposit_min of this PropertySearchQuery.

        :return: The deposit_min of this PropertySearchQuery.
        :rtype: float
        """
        return self._deposit_min

    @deposit_min.setter
    def deposit_min(self, deposit_min):
        """
        Sets the deposit_min of this PropertySearchQuery.

        :param deposit_min: The deposit_min of this PropertySearchQuery.
        :type: float
        """

        self._deposit_min = deposit_min

    @property
    def deposit_max(self):
        """
        Gets the deposit_max of this PropertySearchQuery.

        :return: The deposit_max of this PropertySearchQuery.
        :rtype: float
        """
        return self._deposit_max

    @deposit_max.setter
    def deposit_max(self, deposit_max):
        """
        Sets the deposit_max of this PropertySearchQuery.

        :param deposit_max: The deposit_max of this PropertySearchQuery.
        :type: float
        """

        self._deposit_max = deposit_max

    @property
    def furnished(self):
        """
        Gets the furnished of this PropertySearchQuery.

        :return: The furnished of this PropertySearchQuery.
        :rtype: bool
        """
        return self._furnished

    @furnished.setter
    def furnished(self, furnished):
        """
        Sets the furnished of this PropertySearchQuery.

        :param furnished: The furnished of this PropertySearchQuery.
        :type: bool
        """

        self._furnished = furnished

    @property
    def new_build(self):
        """
        Gets the new_build of this PropertySearchQuery.

        :return: The new_build of this PropertySearchQuery.
        :rtype: bool
        """
        return self._new_build

    @new_build.setter
    def new_build(self, new_build):
        """
        Sets the new_build of this PropertySearchQuery.

        :param new_build: The new_build of this PropertySearchQuery.
        :type: bool
        """

        self._new_build = new_build

    @property
    def missing_fields(self):
        """
        Gets the missing_fields of this PropertySearchQuery.

        :return: The missing_fields of this PropertySearchQuery.
        :rtype: list[str]
        """
        return self._missing_fields

    @missing_fields.setter
    def missing_fields(self, missing_fields):
        """
        Sets the missing_fields of this PropertySearchQuery.

        :param missing_fields: The missing_fields of this PropertySearchQuery.
        :type: list[str]
        """

        self._missing_fields = missing_fields

    @property
    def excluded_ids(self):
        """
        Gets the excluded_ids of this PropertySearchQuery.

        :return: The excluded_ids of this PropertySearchQuery.
        :rtype: list[str]
        """
        return self._excluded_ids

    @excluded_ids.setter
    def excluded_ids(self, excluded_ids):
        """
        Sets the excluded_ids of this PropertySearchQuery.

        :param excluded_ids: The excluded_ids of this PropertySearchQuery.
        :type: list[str]
        """

        self._excluded_ids = excluded_ids

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PropertySearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
