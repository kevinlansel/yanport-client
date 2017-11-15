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


class UserUserPreference(object):
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
        'commercial_zone': 'UserUserPreferenceCommercialZone',
        'marketing_type': 'str'
    }

    attribute_map = {
        'commercial_zone': 'commercialZone',
        'marketing_type': 'marketingType'
    }

    def __init__(self, commercial_zone=None, marketing_type=None):
        """
        UserUserPreference - a model defined in Swagger
        """

        self._commercial_zone = None
        self._marketing_type = None

        if commercial_zone is not None:
          self.commercial_zone = commercial_zone
        if marketing_type is not None:
          self.marketing_type = marketing_type

    @property
    def commercial_zone(self):
        """
        Gets the commercial_zone of this UserUserPreference.

        :return: The commercial_zone of this UserUserPreference.
        :rtype: UserUserPreferenceCommercialZone
        """
        return self._commercial_zone

    @commercial_zone.setter
    def commercial_zone(self, commercial_zone):
        """
        Sets the commercial_zone of this UserUserPreference.

        :param commercial_zone: The commercial_zone of this UserUserPreference.
        :type: UserUserPreferenceCommercialZone
        """

        self._commercial_zone = commercial_zone

    @property
    def marketing_type(self):
        """
        Gets the marketing_type of this UserUserPreference.

        :return: The marketing_type of this UserUserPreference.
        :rtype: str
        """
        return self._marketing_type

    @marketing_type.setter
    def marketing_type(self, marketing_type):
        """
        Sets the marketing_type of this UserUserPreference.

        :param marketing_type: The marketing_type of this UserUserPreference.
        :type: str
        """
        allowed_values = ["SALE", "RENT", "LIFE_ANNUITY", "NEW_BUILD"]
        if marketing_type not in allowed_values:
            raise ValueError(
                "Invalid value for `marketing_type` ({0}), must be one of {1}"
                .format(marketing_type, allowed_values)
            )

        self._marketing_type = marketing_type

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
        if not isinstance(other, UserUserPreference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
