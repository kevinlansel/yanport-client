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


class PropertyFeaturesGeometryFloors(object):
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
        'level': 'int',
        'surface': 'float',
        'basement_type': 'str'
    }

    attribute_map = {
        'level': 'level',
        'surface': 'surface',
        'basement_type': 'basementType'
    }

    def __init__(self, level=None, surface=None, basement_type=None):
        """
        PropertyFeaturesGeometryFloors - a model defined in Swagger
        """

        self._level = None
        self._surface = None
        self._basement_type = None

        if level is not None:
          self.level = level
        if surface is not None:
          self.surface = surface
        if basement_type is not None:
          self.basement_type = basement_type

    @property
    def level(self):
        """
        Gets the level of this PropertyFeaturesGeometryFloors.

        :return: The level of this PropertyFeaturesGeometryFloors.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this PropertyFeaturesGeometryFloors.

        :param level: The level of this PropertyFeaturesGeometryFloors.
        :type: int
        """
        if level is not None and level > 100:
            raise ValueError("Invalid value for `level`, must be a value less than or equal to `100`")
        if level is not None and level < -10:
            raise ValueError("Invalid value for `level`, must be a value greater than or equal to `-10`")

        self._level = level

    @property
    def surface(self):
        """
        Gets the surface of this PropertyFeaturesGeometryFloors.

        :return: The surface of this PropertyFeaturesGeometryFloors.
        :rtype: float
        """
        return self._surface

    @surface.setter
    def surface(self, surface):
        """
        Sets the surface of this PropertyFeaturesGeometryFloors.

        :param surface: The surface of this PropertyFeaturesGeometryFloors.
        :type: float
        """
        if surface is not None and surface > 10000:
            raise ValueError("Invalid value for `surface`, must be a value less than or equal to `10000`")
        if surface is not None and surface < 1:
            raise ValueError("Invalid value for `surface`, must be a value greater than or equal to `1`")

        self._surface = surface

    @property
    def basement_type(self):
        """
        Gets the basement_type of this PropertyFeaturesGeometryFloors.

        :return: The basement_type of this PropertyFeaturesGeometryFloors.
        :rtype: str
        """
        return self._basement_type

    @basement_type.setter
    def basement_type(self, basement_type):
        """
        Sets the basement_type of this PropertyFeaturesGeometryFloors.

        :param basement_type: The basement_type of this PropertyFeaturesGeometryFloors.
        :type: str
        """
        allowed_values = ["PARTIAL", "FULL"]
        if basement_type not in allowed_values:
            raise ValueError(
                "Invalid value for `basement_type` ({0}), must be one of {1}"
                .format(basement_type, allowed_values)
            )

        self._basement_type = basement_type

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
        if not isinstance(other, PropertyFeaturesGeometryFloors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
