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


class SectionsEstimationEngine(object):
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
        'estimated_price': 'float',
        'estimated_price_m2': 'float',
        'estimated_price_range': 'Range',
        'zones': 'list[SectionsEstimationEngineZones]'
    }

    attribute_map = {
        'estimated_price': 'estimatedPrice',
        'estimated_price_m2': 'estimatedPriceM2',
        'estimated_price_range': 'estimatedPriceRange',
        'zones': 'zones'
    }

    def __init__(self, estimated_price=None, estimated_price_m2=None, estimated_price_range=None, zones=None):
        """
        SectionsEstimationEngine - a model defined in Swagger
        """

        self._estimated_price = None
        self._estimated_price_m2 = None
        self._estimated_price_range = None
        self._zones = None

        if estimated_price is not None:
          self.estimated_price = estimated_price
        if estimated_price_m2 is not None:
          self.estimated_price_m2 = estimated_price_m2
        if estimated_price_range is not None:
          self.estimated_price_range = estimated_price_range
        if zones is not None:
          self.zones = zones

    @property
    def estimated_price(self):
        """
        Gets the estimated_price of this SectionsEstimationEngine.

        :return: The estimated_price of this SectionsEstimationEngine.
        :rtype: float
        """
        return self._estimated_price

    @estimated_price.setter
    def estimated_price(self, estimated_price):
        """
        Sets the estimated_price of this SectionsEstimationEngine.

        :param estimated_price: The estimated_price of this SectionsEstimationEngine.
        :type: float
        """

        self._estimated_price = estimated_price

    @property
    def estimated_price_m2(self):
        """
        Gets the estimated_price_m2 of this SectionsEstimationEngine.

        :return: The estimated_price_m2 of this SectionsEstimationEngine.
        :rtype: float
        """
        return self._estimated_price_m2

    @estimated_price_m2.setter
    def estimated_price_m2(self, estimated_price_m2):
        """
        Sets the estimated_price_m2 of this SectionsEstimationEngine.

        :param estimated_price_m2: The estimated_price_m2 of this SectionsEstimationEngine.
        :type: float
        """

        self._estimated_price_m2 = estimated_price_m2

    @property
    def estimated_price_range(self):
        """
        Gets the estimated_price_range of this SectionsEstimationEngine.

        :return: The estimated_price_range of this SectionsEstimationEngine.
        :rtype: Range
        """
        return self._estimated_price_range

    @estimated_price_range.setter
    def estimated_price_range(self, estimated_price_range):
        """
        Sets the estimated_price_range of this SectionsEstimationEngine.

        :param estimated_price_range: The estimated_price_range of this SectionsEstimationEngine.
        :type: Range
        """

        self._estimated_price_range = estimated_price_range

    @property
    def zones(self):
        """
        Gets the zones of this SectionsEstimationEngine.

        :return: The zones of this SectionsEstimationEngine.
        :rtype: list[SectionsEstimationEngineZones]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """
        Sets the zones of this SectionsEstimationEngine.

        :param zones: The zones of this SectionsEstimationEngine.
        :type: list[SectionsEstimationEngineZones]
        """

        self._zones = zones

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
        if not isinstance(other, SectionsEstimationEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
