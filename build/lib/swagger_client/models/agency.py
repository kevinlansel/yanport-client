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


class Agency(object):
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
        'id': 'int',
        'external_id': 'str',
        'organization_id': 'int',
        'name': 'str',
        'usage_name': 'str',
        'siren': 'str',
        'siret': 'str',
        'naf_code': 'AgencyNafCode',
        'city_ref_id': 'int',
        'address': 'Address',
        'description': 'str',
        'phone': 'str',
        'email': 'str',
        'url': 'str',
        'image_url': 'str',
        'active': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'sale_property_count': 'int',
        'rent_property_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'externalId',
        'organization_id': 'organizationId',
        'name': 'name',
        'usage_name': 'usageName',
        'siren': 'siren',
        'siret': 'siret',
        'naf_code': 'nafCode',
        'city_ref_id': 'cityRefId',
        'address': 'address',
        'description': 'description',
        'phone': 'phone',
        'email': 'email',
        'url': 'url',
        'image_url': 'imageUrl',
        'active': 'active',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'sale_property_count': 'salePropertyCount',
        'rent_property_count': 'rentPropertyCount'
    }

    def __init__(self, id=None, external_id=None, organization_id=None, name=None, usage_name=None, siren=None, siret=None, naf_code=None, city_ref_id=None, address=None, description=None, phone=None, email=None, url=None, image_url=None, active=None, created_at=None, updated_at=None, sale_property_count=None, rent_property_count=None):
        """
        Agency - a model defined in Swagger
        """

        self._id = None
        self._external_id = None
        self._organization_id = None
        self._name = None
        self._usage_name = None
        self._siren = None
        self._siret = None
        self._naf_code = None
        self._city_ref_id = None
        self._address = None
        self._description = None
        self._phone = None
        self._email = None
        self._url = None
        self._image_url = None
        self._active = None
        self._created_at = None
        self._updated_at = None
        self._sale_property_count = None
        self._rent_property_count = None

        if id is not None:
          self.id = id
        if external_id is not None:
          self.external_id = external_id
        if organization_id is not None:
          self.organization_id = organization_id
        if name is not None:
          self.name = name
        if usage_name is not None:
          self.usage_name = usage_name
        if siren is not None:
          self.siren = siren
        if siret is not None:
          self.siret = siret
        if naf_code is not None:
          self.naf_code = naf_code
        if city_ref_id is not None:
          self.city_ref_id = city_ref_id
        if address is not None:
          self.address = address
        if description is not None:
          self.description = description
        if phone is not None:
          self.phone = phone
        if email is not None:
          self.email = email
        if url is not None:
          self.url = url
        if image_url is not None:
          self.image_url = image_url
        if active is not None:
          self.active = active
        if created_at is not None:
          self.created_at = created_at
        if updated_at is not None:
          self.updated_at = updated_at
        if sale_property_count is not None:
          self.sale_property_count = sale_property_count
        if rent_property_count is not None:
          self.rent_property_count = rent_property_count

    @property
    def id(self):
        """
        Gets the id of this Agency.

        :return: The id of this Agency.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Agency.

        :param id: The id of this Agency.
        :type: int
        """

        self._id = id

    @property
    def external_id(self):
        """
        Gets the external_id of this Agency.

        :return: The external_id of this Agency.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this Agency.

        :param external_id: The external_id of this Agency.
        :type: str
        """

        self._external_id = external_id

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Agency.

        :return: The organization_id of this Agency.
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Agency.

        :param organization_id: The organization_id of this Agency.
        :type: int
        """

        self._organization_id = organization_id

    @property
    def name(self):
        """
        Gets the name of this Agency.

        :return: The name of this Agency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Agency.

        :param name: The name of this Agency.
        :type: str
        """

        self._name = name

    @property
    def usage_name(self):
        """
        Gets the usage_name of this Agency.

        :return: The usage_name of this Agency.
        :rtype: str
        """
        return self._usage_name

    @usage_name.setter
    def usage_name(self, usage_name):
        """
        Sets the usage_name of this Agency.

        :param usage_name: The usage_name of this Agency.
        :type: str
        """

        self._usage_name = usage_name

    @property
    def siren(self):
        """
        Gets the siren of this Agency.

        :return: The siren of this Agency.
        :rtype: str
        """
        return self._siren

    @siren.setter
    def siren(self, siren):
        """
        Sets the siren of this Agency.

        :param siren: The siren of this Agency.
        :type: str
        """

        self._siren = siren

    @property
    def siret(self):
        """
        Gets the siret of this Agency.

        :return: The siret of this Agency.
        :rtype: str
        """
        return self._siret

    @siret.setter
    def siret(self, siret):
        """
        Sets the siret of this Agency.

        :param siret: The siret of this Agency.
        :type: str
        """

        self._siret = siret

    @property
    def naf_code(self):
        """
        Gets the naf_code of this Agency.

        :return: The naf_code of this Agency.
        :rtype: AgencyNafCode
        """
        return self._naf_code

    @naf_code.setter
    def naf_code(self, naf_code):
        """
        Sets the naf_code of this Agency.

        :param naf_code: The naf_code of this Agency.
        :type: AgencyNafCode
        """

        self._naf_code = naf_code

    @property
    def city_ref_id(self):
        """
        Gets the city_ref_id of this Agency.

        :return: The city_ref_id of this Agency.
        :rtype: int
        """
        return self._city_ref_id

    @city_ref_id.setter
    def city_ref_id(self, city_ref_id):
        """
        Sets the city_ref_id of this Agency.

        :param city_ref_id: The city_ref_id of this Agency.
        :type: int
        """

        self._city_ref_id = city_ref_id

    @property
    def address(self):
        """
        Gets the address of this Agency.

        :return: The address of this Agency.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Agency.

        :param address: The address of this Agency.
        :type: Address
        """

        self._address = address

    @property
    def description(self):
        """
        Gets the description of this Agency.

        :return: The description of this Agency.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Agency.

        :param description: The description of this Agency.
        :type: str
        """

        self._description = description

    @property
    def phone(self):
        """
        Gets the phone of this Agency.

        :return: The phone of this Agency.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Agency.

        :param phone: The phone of this Agency.
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """
        Gets the email of this Agency.

        :return: The email of this Agency.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Agency.

        :param email: The email of this Agency.
        :type: str
        """

        self._email = email

    @property
    def url(self):
        """
        Gets the url of this Agency.

        :return: The url of this Agency.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Agency.

        :param url: The url of this Agency.
        :type: str
        """

        self._url = url

    @property
    def image_url(self):
        """
        Gets the image_url of this Agency.

        :return: The image_url of this Agency.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this Agency.

        :param image_url: The image_url of this Agency.
        :type: str
        """

        self._image_url = image_url

    @property
    def active(self):
        """
        Gets the active of this Agency.

        :return: The active of this Agency.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Agency.

        :param active: The active of this Agency.
        :type: bool
        """

        self._active = active

    @property
    def created_at(self):
        """
        Gets the created_at of this Agency.

        :return: The created_at of this Agency.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Agency.

        :param created_at: The created_at of this Agency.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Agency.

        :return: The updated_at of this Agency.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Agency.

        :param updated_at: The updated_at of this Agency.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def sale_property_count(self):
        """
        Gets the sale_property_count of this Agency.

        :return: The sale_property_count of this Agency.
        :rtype: int
        """
        return self._sale_property_count

    @sale_property_count.setter
    def sale_property_count(self, sale_property_count):
        """
        Sets the sale_property_count of this Agency.

        :param sale_property_count: The sale_property_count of this Agency.
        :type: int
        """

        self._sale_property_count = sale_property_count

    @property
    def rent_property_count(self):
        """
        Gets the rent_property_count of this Agency.

        :return: The rent_property_count of this Agency.
        :rtype: int
        """
        return self._rent_property_count

    @rent_property_count.setter
    def rent_property_count(self, rent_property_count):
        """
        Sets the rent_property_count of this Agency.

        :param rent_property_count: The rent_property_count of this Agency.
        :type: int
        """

        self._rent_property_count = rent_property_count

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
        if not isinstance(other, Agency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
