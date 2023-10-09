import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Créer un client de test Flask
        self.app = app.test_client()

    def test_get_top_n_valid(self):
        # Appeler l'API avec un paramètre valide N
        response = self.app.get('/top?N=10')
        # Vérifier que le statut de la réponse est 200
        self.assertEqual(response.status_code, 200)

    def test_get_top_n_invalid(self):
        # Appeler l'API avec un paramètre invalide N
        response = self.app.get('/top?N=0')

        # Vérifier que le statut de la réponse est 400
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode('utf-8'), 'Error: N must be between 1 and 100')

    def test_json(self):
        # Appeler l'API avec un paramètre valide N
        response = self.app.get('/top?N=10')
        # Vérifier que la réponse est au format JSON
        self.assertTrue(response.is_json)

if __name__ == '__main__':
    unittest.main()