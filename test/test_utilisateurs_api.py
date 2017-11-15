# coding: utf-8

"""
    Yanport API

    ## À propos Voici quelques ressources qui vous aideront à explorer notre API, si vous avez des problèmes ou des demandes, veuillez contacter le [support](mailto:support@yanport.com). ## REST API Nos services webs utilisent le protocle **HTTPS** sur le port 443, tout accès en HTTP sur le port 80 est bloqué par notre pare-feu. Les échanges de données sont réalisés en **JSON**. ## Authentification Avant de commencer à explorer notre API, vous devez nous [contacter](https://www.yanport.com/contact) afin d'obtenir un [JSON Web Token](https://jwt.io) (**JWT**) qui vous permettra de vous identifier à chaque requêtes. ### JWT (header) La méthode privilégiée pour s'authentifier est de passer à chaque requêtes le token dans le header `Authorization: Bearer {{ JWT }}` en remplaçant `{{ JWT }}` par votre token. ### JWT (query param) Il est aussi possible de passer le token directement en query param de la requête `https://api.yanport.com/?token={{ JWT }}`. (_privilégié le passage par header en production._) ## Pour démarrer Lorsque vous disposez de votre token d'authentification, vous pouvez commencer à explorer notre API grâce au boutton  `Try it out` sur chacun de nos webs services. Mais au préalable, vous devez vous authentifier en cliquant sur le boutton `Authorize `, en remplissant l'input `api_key` avec `Bearer {{ JWT }}`.  **Exemple** `Bearer eyUEkiLCJh...CHCUiBfD63oxoo=` ## Limitation Toutes les requêtes à notre API sont loggées, c'est pourquoi vous devez respecter nos [CGU](https://dev.yanport.com/cgu) afin d'éviter tout usage abusif de notre API. 

    OpenAPI spec version: 1.0
    Contact: dev@yanport.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.utilisateurs_api import UtilisateursApi


class TestUtilisateursApi(unittest.TestCase):
    """ UtilisateursApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.utilisateurs_api.UtilisateursApi()

    def tearDown(self):
        pass

    def test_users_get(self):
        """
        Test case for users_get

        Rechercher des utilisateurs
        """
        pass

    def test_users_id_activate_get(self):
        """
        Test case for users_id_activate_get

        Activer un utilisateur
        """
        pass

    def test_users_id_avatars_post(self):
        """
        Test case for users_id_avatars_post

        Mettre à jour l'avatar d'un utilisateur
        """
        pass

    def test_users_id_deactivate_get(self):
        """
        Test case for users_id_deactivate_get

        Désactiver un utilisateur
        """
        pass

    def test_users_id_delete(self):
        """
        Test case for users_id_delete

        Supprimer un utilisateur
        """
        pass

    def test_users_id_get(self):
        """
        Test case for users_id_get

        Recupérer un utilisateur par id
        """
        pass

    def test_users_id_put(self):
        """
        Test case for users_id_put

        Mettre à jour un utilisateur
        """
        pass

    def test_users_id_team_get(self):
        """
        Test case for users_id_team_get

        Recupérer les utilisateurs (agents) faisant équipe avec l'utilsateur correspondant à l'id donné
        """
        pass

    def test_users_post(self):
        """
        Test case for users_post

        Créer un utilisateur
        """
        pass


if __name__ == '__main__':
    unittest.main()
