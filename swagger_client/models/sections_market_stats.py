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


class SectionsMarketStats(object):
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
        'property_search_query': 'PropertySearchQuery',
        'price_percentiles': 'Percentiles',
        'price_m2_percentiles': 'Percentiles',
        'duration_percentiles': 'Percentiles',
        'price_m2_distribution': 'Histogram',
        'duration_distribution': 'Histogram',
        'price_m2_evolution': 'DateHistogram',
        'duration_evolution': 'DateHistogram'
    }

    attribute_map = {
        'property_search_query': 'propertySearchQuery',
        'price_percentiles': 'pricePercentiles',
        'price_m2_percentiles': 'priceM2Percentiles',
        'duration_percentiles': 'durationPercentiles',
        'price_m2_distribution': 'priceM2Distribution',
        'duration_distribution': 'durationDistribution',
        'price_m2_evolution': 'priceM2Evolution',
        'duration_evolution': 'durationEvolution'
    }

    def __init__(self, property_search_query=None, price_percentiles=None, price_m2_percentiles=None, duration_percentiles=None, price_m2_distribution=None, duration_distribution=None, price_m2_evolution=None, duration_evolution=None):
        """
        SectionsMarketStats - a model defined in Swagger
        """

        self._property_search_query = None
        self._price_percentiles = None
        self._price_m2_percentiles = None
        self._duration_percentiles = None
        self._price_m2_distribution = None
        self._duration_distribution = None
        self._price_m2_evolution = None
        self._duration_evolution = None

        if property_search_query is not None:
          self.property_search_query = property_search_query
        if price_percentiles is not None:
          self.price_percentiles = price_percentiles
        if price_m2_percentiles is not None:
          self.price_m2_percentiles = price_m2_percentiles
        if duration_percentiles is not None:
          self.duration_percentiles = duration_percentiles
        if price_m2_distribution is not None:
          self.price_m2_distribution = price_m2_distribution
        if duration_distribution is not None:
          self.duration_distribution = duration_distribution
        if price_m2_evolution is not None:
          self.price_m2_evolution = price_m2_evolution
        if duration_evolution is not None:
          self.duration_evolution = duration_evolution

    @property
    def property_search_query(self):
        """
        Gets the property_search_query of this SectionsMarketStats.

        :return: The property_search_query of this SectionsMarketStats.
        :rtype: PropertySearchQuery
        """
        return self._property_search_query

    @property_search_query.setter
    def property_search_query(self, property_search_query):
        """
        Sets the property_search_query of this SectionsMarketStats.

        :param property_search_query: The property_search_query of this SectionsMarketStats.
        :type: PropertySearchQuery
        """

        self._property_search_query = property_search_query

    @property
    def price_percentiles(self):
        """
        Gets the price_percentiles of this SectionsMarketStats.

        :return: The price_percentiles of this SectionsMarketStats.
        :rtype: Percentiles
        """
        return self._price_percentiles

    @price_percentiles.setter
    def price_percentiles(self, price_percentiles):
        """
        Sets the price_percentiles of this SectionsMarketStats.

        :param price_percentiles: The price_percentiles of this SectionsMarketStats.
        :type: Percentiles
        """

        self._price_percentiles = price_percentiles

    @property
    def price_m2_percentiles(self):
        """
        Gets the price_m2_percentiles of this SectionsMarketStats.

        :return: The price_m2_percentiles of this SectionsMarketStats.
        :rtype: Percentiles
        """
        return self._price_m2_percentiles

    @price_m2_percentiles.setter
    def price_m2_percentiles(self, price_m2_percentiles):
        """
        Sets the price_m2_percentiles of this SectionsMarketStats.

        :param price_m2_percentiles: The price_m2_percentiles of this SectionsMarketStats.
        :type: Percentiles
        """

        self._price_m2_percentiles = price_m2_percentiles

    @property
    def duration_percentiles(self):
        """
        Gets the duration_percentiles of this SectionsMarketStats.

        :return: The duration_percentiles of this SectionsMarketStats.
        :rtype: Percentiles
        """
        return self._duration_percentiles

    @duration_percentiles.setter
    def duration_percentiles(self, duration_percentiles):
        """
        Sets the duration_percentiles of this SectionsMarketStats.

        :param duration_percentiles: The duration_percentiles of this SectionsMarketStats.
        :type: Percentiles
        """

        self._duration_percentiles = duration_percentiles

    @property
    def price_m2_distribution(self):
        """
        Gets the price_m2_distribution of this SectionsMarketStats.

        :return: The price_m2_distribution of this SectionsMarketStats.
        :rtype: Histogram
        """
        return self._price_m2_distribution

    @price_m2_distribution.setter
    def price_m2_distribution(self, price_m2_distribution):
        """
        Sets the price_m2_distribution of this SectionsMarketStats.

        :param price_m2_distribution: The price_m2_distribution of this SectionsMarketStats.
        :type: Histogram
        """

        self._price_m2_distribution = price_m2_distribution

    @property
    def duration_distribution(self):
        """
        Gets the duration_distribution of this SectionsMarketStats.

        :return: The duration_distribution of this SectionsMarketStats.
        :rtype: Histogram
        """
        return self._duration_distribution

    @duration_distribution.setter
    def duration_distribution(self, duration_distribution):
        """
        Sets the duration_distribution of this SectionsMarketStats.

        :param duration_distribution: The duration_distribution of this SectionsMarketStats.
        :type: Histogram
        """

        self._duration_distribution = duration_distribution

    @property
    def price_m2_evolution(self):
        """
        Gets the price_m2_evolution of this SectionsMarketStats.

        :return: The price_m2_evolution of this SectionsMarketStats.
        :rtype: DateHistogram
        """
        return self._price_m2_evolution

    @price_m2_evolution.setter
    def price_m2_evolution(self, price_m2_evolution):
        """
        Sets the price_m2_evolution of this SectionsMarketStats.

        :param price_m2_evolution: The price_m2_evolution of this SectionsMarketStats.
        :type: DateHistogram
        """

        self._price_m2_evolution = price_m2_evolution

    @property
    def duration_evolution(self):
        """
        Gets the duration_evolution of this SectionsMarketStats.

        :return: The duration_evolution of this SectionsMarketStats.
        :rtype: DateHistogram
        """
        return self._duration_evolution

    @duration_evolution.setter
    def duration_evolution(self, duration_evolution):
        """
        Sets the duration_evolution of this SectionsMarketStats.

        :param duration_evolution: The duration_evolution of this SectionsMarketStats.
        :type: DateHistogram
        """

        self._duration_evolution = duration_evolution

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
        if not isinstance(other, SectionsMarketStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
