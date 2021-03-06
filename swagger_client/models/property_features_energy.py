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


class PropertyFeaturesEnergy(object):
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
        'heating_types': 'list[str]',
        'heating_mode': 'str',
        'water_heating_types': 'list[str]',
        'water_heating_mode': 'str',
        'consumption': 'int',
        'green_house_gas_consumption': 'int'
    }

    attribute_map = {
        'heating_types': 'heatingTypes',
        'heating_mode': 'heatingMode',
        'water_heating_types': 'waterHeatingTypes',
        'water_heating_mode': 'waterHeatingMode',
        'consumption': 'consumption',
        'green_house_gas_consumption': 'greenHouseGasConsumption'
    }

    def __init__(self, heating_types=None, heating_mode=None, water_heating_types=None, water_heating_mode=None, consumption=None, green_house_gas_consumption=None):
        """
        PropertyFeaturesEnergy - a model defined in Swagger
        """

        self._heating_types = None
        self._heating_mode = None
        self._water_heating_types = None
        self._water_heating_mode = None
        self._consumption = None
        self._green_house_gas_consumption = None

        if heating_types is not None:
          self.heating_types = heating_types
        if heating_mode is not None:
          self.heating_mode = heating_mode
        if water_heating_types is not None:
          self.water_heating_types = water_heating_types
        if water_heating_mode is not None:
          self.water_heating_mode = water_heating_mode
        if consumption is not None:
          self.consumption = consumption
        if green_house_gas_consumption is not None:
          self.green_house_gas_consumption = green_house_gas_consumption

    @property
    def heating_types(self):
        """
        Gets the heating_types of this PropertyFeaturesEnergy.

        :return: The heating_types of this PropertyFeaturesEnergy.
        :rtype: list[str]
        """
        return self._heating_types

    @heating_types.setter
    def heating_types(self, heating_types):
        """
        Sets the heating_types of this PropertyFeaturesEnergy.

        :param heating_types: The heating_types of this PropertyFeaturesEnergy.
        :type: list[str]
        """
        allowed_values = ["ELECTRIC", "GAS", "FUEL", "WOOD", "SOLAR", "HEAT_PUMP", "UNDERFLOOR", "NONE", "OTHER"]
        if not set(heating_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `heating_types` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(heating_types)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._heating_types = heating_types

    @property
    def heating_mode(self):
        """
        Gets the heating_mode of this PropertyFeaturesEnergy.

        :return: The heating_mode of this PropertyFeaturesEnergy.
        :rtype: str
        """
        return self._heating_mode

    @heating_mode.setter
    def heating_mode(self, heating_mode):
        """
        Sets the heating_mode of this PropertyFeaturesEnergy.

        :param heating_mode: The heating_mode of this PropertyFeaturesEnergy.
        :type: str
        """
        allowed_values = ["INDIVIDUAL", "COLLECTIVE", "MIXED"]
        if heating_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `heating_mode` ({0}), must be one of {1}"
                .format(heating_mode, allowed_values)
            )

        self._heating_mode = heating_mode

    @property
    def water_heating_types(self):
        """
        Gets the water_heating_types of this PropertyFeaturesEnergy.

        :return: The water_heating_types of this PropertyFeaturesEnergy.
        :rtype: list[str]
        """
        return self._water_heating_types

    @water_heating_types.setter
    def water_heating_types(self, water_heating_types):
        """
        Sets the water_heating_types of this PropertyFeaturesEnergy.

        :param water_heating_types: The water_heating_types of this PropertyFeaturesEnergy.
        :type: list[str]
        """
        allowed_values = ["ELECTRIC", "GAS", "FUEL", "WOOD", "SOLAR", "HEAT_PUMP", "UNDERFLOOR", "NONE", "OTHER"]
        if not set(water_heating_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `water_heating_types` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(water_heating_types)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._water_heating_types = water_heating_types

    @property
    def water_heating_mode(self):
        """
        Gets the water_heating_mode of this PropertyFeaturesEnergy.

        :return: The water_heating_mode of this PropertyFeaturesEnergy.
        :rtype: str
        """
        return self._water_heating_mode

    @water_heating_mode.setter
    def water_heating_mode(self, water_heating_mode):
        """
        Sets the water_heating_mode of this PropertyFeaturesEnergy.

        :param water_heating_mode: The water_heating_mode of this PropertyFeaturesEnergy.
        :type: str
        """
        allowed_values = ["INDIVIDUAL", "COLLECTIVE", "MIXED"]
        if water_heating_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `water_heating_mode` ({0}), must be one of {1}"
                .format(water_heating_mode, allowed_values)
            )

        self._water_heating_mode = water_heating_mode

    @property
    def consumption(self):
        """
        Gets the consumption of this PropertyFeaturesEnergy.

        :return: The consumption of this PropertyFeaturesEnergy.
        :rtype: int
        """
        return self._consumption

    @consumption.setter
    def consumption(self, consumption):
        """
        Sets the consumption of this PropertyFeaturesEnergy.

        :param consumption: The consumption of this PropertyFeaturesEnergy.
        :type: int
        """
        if consumption is not None and consumption > 10000:
            raise ValueError("Invalid value for `consumption`, must be a value less than or equal to `10000`")
        if consumption is not None and consumption < 0:
            raise ValueError("Invalid value for `consumption`, must be a value greater than or equal to `0`")

        self._consumption = consumption

    @property
    def green_house_gas_consumption(self):
        """
        Gets the green_house_gas_consumption of this PropertyFeaturesEnergy.

        :return: The green_house_gas_consumption of this PropertyFeaturesEnergy.
        :rtype: int
        """
        return self._green_house_gas_consumption

    @green_house_gas_consumption.setter
    def green_house_gas_consumption(self, green_house_gas_consumption):
        """
        Sets the green_house_gas_consumption of this PropertyFeaturesEnergy.

        :param green_house_gas_consumption: The green_house_gas_consumption of this PropertyFeaturesEnergy.
        :type: int
        """
        if green_house_gas_consumption is not None and green_house_gas_consumption > 10000:
            raise ValueError("Invalid value for `green_house_gas_consumption`, must be a value less than or equal to `10000`")
        if green_house_gas_consumption is not None and green_house_gas_consumption < 0:
            raise ValueError("Invalid value for `green_house_gas_consumption`, must be a value greater than or equal to `0`")

        self._green_house_gas_consumption = green_house_gas_consumption

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
        if not isinstance(other, PropertyFeaturesEnergy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
