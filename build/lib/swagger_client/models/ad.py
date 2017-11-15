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


class Ad(object):
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
        'id': 'str',
        'url': 'str',
        'crawl_source': 'CrawlSource',
        'last_crawl_date': 'datetime',
        '_property': 'ModelProperty'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'crawl_source': 'crawlSource',
        'last_crawl_date': 'lastCrawlDate',
        '_property': 'property'
    }

    def __init__(self, id=None, url=None, crawl_source=None, last_crawl_date=None, _property=None):
        """
        Ad - a model defined in Swagger
        """

        self._id = None
        self._url = None
        self._crawl_source = None
        self._last_crawl_date = None
        self.__property = None

        if id is not None:
          self.id = id
        if url is not None:
          self.url = url
        if crawl_source is not None:
          self.crawl_source = crawl_source
        if last_crawl_date is not None:
          self.last_crawl_date = last_crawl_date
        if _property is not None:
          self._property = _property

    @property
    def id(self):
        """
        Gets the id of this Ad.

        :return: The id of this Ad.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ad.

        :param id: The id of this Ad.
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """
        Gets the url of this Ad.

        :return: The url of this Ad.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Ad.

        :param url: The url of this Ad.
        :type: str
        """

        self._url = url

    @property
    def crawl_source(self):
        """
        Gets the crawl_source of this Ad.

        :return: The crawl_source of this Ad.
        :rtype: CrawlSource
        """
        return self._crawl_source

    @crawl_source.setter
    def crawl_source(self, crawl_source):
        """
        Sets the crawl_source of this Ad.

        :param crawl_source: The crawl_source of this Ad.
        :type: CrawlSource
        """

        self._crawl_source = crawl_source

    @property
    def last_crawl_date(self):
        """
        Gets the last_crawl_date of this Ad.

        :return: The last_crawl_date of this Ad.
        :rtype: datetime
        """
        return self._last_crawl_date

    @last_crawl_date.setter
    def last_crawl_date(self, last_crawl_date):
        """
        Sets the last_crawl_date of this Ad.

        :param last_crawl_date: The last_crawl_date of this Ad.
        :type: datetime
        """

        self._last_crawl_date = last_crawl_date

    @property
    def _property(self):
        """
        Gets the _property of this Ad.

        :return: The _property of this Ad.
        :rtype: ModelProperty
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """
        Sets the _property of this Ad.

        :param _property: The _property of this Ad.
        :type: ModelProperty
        """

        self.__property = _property

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
        if not isinstance(other, Ad):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
