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


class PropertyFeaturesDescriptiveEquipments(object):
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
        'furniture': 'bool',
        'fireplace': 'bool',
        'air_conditioning': 'bool',
        'adsl': 'bool',
        'cable': 'bool',
        'fiber': 'bool',
        'elevator': 'bool',
        'digicode': 'bool',
        'intercom': 'bool',
        'videophone': 'bool',
        'bike_area': 'bool',
        'two_wheel_park': 'bool',
        'disabled_access': 'bool'
    }

    attribute_map = {
        'furniture': 'FURNITURE',
        'fireplace': 'FIREPLACE',
        'air_conditioning': 'AIR_CONDITIONING',
        'adsl': 'ADSL',
        'cable': 'CABLE',
        'fiber': 'FIBER',
        'elevator': 'ELEVATOR',
        'digicode': 'DIGICODE',
        'intercom': 'INTERCOM',
        'videophone': 'VIDEOPHONE',
        'bike_area': 'BIKE_AREA',
        'two_wheel_park': 'TWO_WHEEL_PARK',
        'disabled_access': 'DISABLED_ACCESS'
    }

    def __init__(self, furniture=None, fireplace=None, air_conditioning=None, adsl=None, cable=None, fiber=None, elevator=None, digicode=None, intercom=None, videophone=None, bike_area=None, two_wheel_park=None, disabled_access=None):
        """
        PropertyFeaturesDescriptiveEquipments - a model defined in Swagger
        """

        self._furniture = None
        self._fireplace = None
        self._air_conditioning = None
        self._adsl = None
        self._cable = None
        self._fiber = None
        self._elevator = None
        self._digicode = None
        self._intercom = None
        self._videophone = None
        self._bike_area = None
        self._two_wheel_park = None
        self._disabled_access = None

        if furniture is not None:
          self.furniture = furniture
        if fireplace is not None:
          self.fireplace = fireplace
        if air_conditioning is not None:
          self.air_conditioning = air_conditioning
        if adsl is not None:
          self.adsl = adsl
        if cable is not None:
          self.cable = cable
        if fiber is not None:
          self.fiber = fiber
        if elevator is not None:
          self.elevator = elevator
        if digicode is not None:
          self.digicode = digicode
        if intercom is not None:
          self.intercom = intercom
        if videophone is not None:
          self.videophone = videophone
        if bike_area is not None:
          self.bike_area = bike_area
        if two_wheel_park is not None:
          self.two_wheel_park = two_wheel_park
        if disabled_access is not None:
          self.disabled_access = disabled_access

    @property
    def furniture(self):
        """
        Gets the furniture of this PropertyFeaturesDescriptiveEquipments.

        :return: The furniture of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._furniture

    @furniture.setter
    def furniture(self, furniture):
        """
        Sets the furniture of this PropertyFeaturesDescriptiveEquipments.

        :param furniture: The furniture of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._furniture = furniture

    @property
    def fireplace(self):
        """
        Gets the fireplace of this PropertyFeaturesDescriptiveEquipments.

        :return: The fireplace of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._fireplace

    @fireplace.setter
    def fireplace(self, fireplace):
        """
        Sets the fireplace of this PropertyFeaturesDescriptiveEquipments.

        :param fireplace: The fireplace of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._fireplace = fireplace

    @property
    def air_conditioning(self):
        """
        Gets the air_conditioning of this PropertyFeaturesDescriptiveEquipments.

        :return: The air_conditioning of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._air_conditioning

    @air_conditioning.setter
    def air_conditioning(self, air_conditioning):
        """
        Sets the air_conditioning of this PropertyFeaturesDescriptiveEquipments.

        :param air_conditioning: The air_conditioning of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._air_conditioning = air_conditioning

    @property
    def adsl(self):
        """
        Gets the adsl of this PropertyFeaturesDescriptiveEquipments.

        :return: The adsl of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._adsl

    @adsl.setter
    def adsl(self, adsl):
        """
        Sets the adsl of this PropertyFeaturesDescriptiveEquipments.

        :param adsl: The adsl of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._adsl = adsl

    @property
    def cable(self):
        """
        Gets the cable of this PropertyFeaturesDescriptiveEquipments.

        :return: The cable of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._cable

    @cable.setter
    def cable(self, cable):
        """
        Sets the cable of this PropertyFeaturesDescriptiveEquipments.

        :param cable: The cable of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._cable = cable

    @property
    def fiber(self):
        """
        Gets the fiber of this PropertyFeaturesDescriptiveEquipments.

        :return: The fiber of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._fiber

    @fiber.setter
    def fiber(self, fiber):
        """
        Sets the fiber of this PropertyFeaturesDescriptiveEquipments.

        :param fiber: The fiber of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._fiber = fiber

    @property
    def elevator(self):
        """
        Gets the elevator of this PropertyFeaturesDescriptiveEquipments.

        :return: The elevator of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._elevator

    @elevator.setter
    def elevator(self, elevator):
        """
        Sets the elevator of this PropertyFeaturesDescriptiveEquipments.

        :param elevator: The elevator of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._elevator = elevator

    @property
    def digicode(self):
        """
        Gets the digicode of this PropertyFeaturesDescriptiveEquipments.

        :return: The digicode of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._digicode

    @digicode.setter
    def digicode(self, digicode):
        """
        Sets the digicode of this PropertyFeaturesDescriptiveEquipments.

        :param digicode: The digicode of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._digicode = digicode

    @property
    def intercom(self):
        """
        Gets the intercom of this PropertyFeaturesDescriptiveEquipments.

        :return: The intercom of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._intercom

    @intercom.setter
    def intercom(self, intercom):
        """
        Sets the intercom of this PropertyFeaturesDescriptiveEquipments.

        :param intercom: The intercom of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._intercom = intercom

    @property
    def videophone(self):
        """
        Gets the videophone of this PropertyFeaturesDescriptiveEquipments.

        :return: The videophone of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._videophone

    @videophone.setter
    def videophone(self, videophone):
        """
        Sets the videophone of this PropertyFeaturesDescriptiveEquipments.

        :param videophone: The videophone of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._videophone = videophone

    @property
    def bike_area(self):
        """
        Gets the bike_area of this PropertyFeaturesDescriptiveEquipments.

        :return: The bike_area of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._bike_area

    @bike_area.setter
    def bike_area(self, bike_area):
        """
        Sets the bike_area of this PropertyFeaturesDescriptiveEquipments.

        :param bike_area: The bike_area of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._bike_area = bike_area

    @property
    def two_wheel_park(self):
        """
        Gets the two_wheel_park of this PropertyFeaturesDescriptiveEquipments.

        :return: The two_wheel_park of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._two_wheel_park

    @two_wheel_park.setter
    def two_wheel_park(self, two_wheel_park):
        """
        Sets the two_wheel_park of this PropertyFeaturesDescriptiveEquipments.

        :param two_wheel_park: The two_wheel_park of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._two_wheel_park = two_wheel_park

    @property
    def disabled_access(self):
        """
        Gets the disabled_access of this PropertyFeaturesDescriptiveEquipments.

        :return: The disabled_access of this PropertyFeaturesDescriptiveEquipments.
        :rtype: bool
        """
        return self._disabled_access

    @disabled_access.setter
    def disabled_access(self, disabled_access):
        """
        Sets the disabled_access of this PropertyFeaturesDescriptiveEquipments.

        :param disabled_access: The disabled_access of this PropertyFeaturesDescriptiveEquipments.
        :type: bool
        """

        self._disabled_access = disabled_access

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
        if not isinstance(other, PropertyFeaturesDescriptiveEquipments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other