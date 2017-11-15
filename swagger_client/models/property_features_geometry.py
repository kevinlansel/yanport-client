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


class PropertyFeaturesGeometry(object):
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
        'surface': 'float',
        'surface_carrez': 'float',
        'areas': 'list[PropertyFeaturesGeometryAreas]',
        'room_count': 'int',
        'floors': 'list[PropertyFeaturesGeometryFloors]'
    }

    attribute_map = {
        'surface': 'surface',
        'surface_carrez': 'surfaceCarrez',
        'areas': 'areas',
        'room_count': 'roomCount',
        'floors': 'floors'
    }

    def __init__(self, surface=None, surface_carrez=None, areas=None, room_count=None, floors=None):
        """
        PropertyFeaturesGeometry - a model defined in Swagger
        """

        self._surface = None
        self._surface_carrez = None
        self._areas = None
        self._room_count = None
        self._floors = None

        if surface is not None:
          self.surface = surface
        if surface_carrez is not None:
          self.surface_carrez = surface_carrez
        if areas is not None:
          self.areas = areas
        if room_count is not None:
          self.room_count = room_count
        if floors is not None:
          self.floors = floors

    @property
    def surface(self):
        """
        Gets the surface of this PropertyFeaturesGeometry.

        :return: The surface of this PropertyFeaturesGeometry.
        :rtype: float
        """
        return self._surface

    @surface.setter
    def surface(self, surface):
        """
        Sets the surface of this PropertyFeaturesGeometry.

        :param surface: The surface of this PropertyFeaturesGeometry.
        :type: float
        """
        if surface is not None and surface > 10000:
            raise ValueError("Invalid value for `surface`, must be a value less than or equal to `10000`")
        if surface is not None and surface < 1:
            raise ValueError("Invalid value for `surface`, must be a value greater than or equal to `1`")

        self._surface = surface

    @property
    def surface_carrez(self):
        """
        Gets the surface_carrez of this PropertyFeaturesGeometry.

        :return: The surface_carrez of this PropertyFeaturesGeometry.
        :rtype: float
        """
        return self._surface_carrez

    @surface_carrez.setter
    def surface_carrez(self, surface_carrez):
        """
        Sets the surface_carrez of this PropertyFeaturesGeometry.

        :param surface_carrez: The surface_carrez of this PropertyFeaturesGeometry.
        :type: float
        """
        if surface_carrez is not None and surface_carrez > 10000:
            raise ValueError("Invalid value for `surface_carrez`, must be a value less than or equal to `10000`")
        if surface_carrez is not None and surface_carrez < 1:
            raise ValueError("Invalid value for `surface_carrez`, must be a value greater than or equal to `1`")

        self._surface_carrez = surface_carrez

    @property
    def areas(self):
        """
        Gets the areas of this PropertyFeaturesGeometry.

        :return: The areas of this PropertyFeaturesGeometry.
        :rtype: list[PropertyFeaturesGeometryAreas]
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """
        Sets the areas of this PropertyFeaturesGeometry.

        :param areas: The areas of this PropertyFeaturesGeometry.
        :type: list[PropertyFeaturesGeometryAreas]
        """

        self._areas = areas

    @property
    def room_count(self):
        """
        Gets the room_count of this PropertyFeaturesGeometry.

        :return: The room_count of this PropertyFeaturesGeometry.
        :rtype: int
        """
        return self._room_count

    @room_count.setter
    def room_count(self, room_count):
        """
        Sets the room_count of this PropertyFeaturesGeometry.

        :param room_count: The room_count of this PropertyFeaturesGeometry.
        :type: int
        """
        if room_count is not None and room_count > 100:
            raise ValueError("Invalid value for `room_count`, must be a value less than or equal to `100`")
        if room_count is not None and room_count < 1:
            raise ValueError("Invalid value for `room_count`, must be a value greater than or equal to `1`")

        self._room_count = room_count

    @property
    def floors(self):
        """
        Gets the floors of this PropertyFeaturesGeometry.

        :return: The floors of this PropertyFeaturesGeometry.
        :rtype: list[PropertyFeaturesGeometryFloors]
        """
        return self._floors

    @floors.setter
    def floors(self, floors):
        """
        Sets the floors of this PropertyFeaturesGeometry.

        :param floors: The floors of this PropertyFeaturesGeometry.
        :type: list[PropertyFeaturesGeometryFloors]
        """

        self._floors = floors

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
        if not isinstance(other, PropertyFeaturesGeometry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other