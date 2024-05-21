import pytest
from flask_testing import TestCase
import sys,os
# Adiciona o diretório raiz ao caminho do sistema
sys.path.insert(0, os.path.abspath('/home/runner/.local/lib/python3.10/site-packages')) 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestApp(TestCase):
    def create_app(self):
        # Configura a aplicação para o modo de testes
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        return app

    def test_consulta_fatura(self):
        response = self.client.get('/fatura/consulta_fatura/3')
        self.assertEqual(response.status_code, 200)

    def test_consulta_todas_faturas(self):
        response = self.client.get('/fatura/consulta_all/')
        self.assertEqual(response.status_code, 200)


    def test_update_fatura_pago(self):
        response = self.client.put('/fatura/atualiza_fatura_pago/3')
        self.assertEqual(response.status_code, 200)
    
    
    def test_update_fatura_nao_pago(self):
        response = self.client.put('/fatura/atualiza_fatura_nao_pago/3')
        self.assertEqual(response.status_code, 200)


    def test_update_fatura_cancelado(self):
        response = self.client.put('/fatura/atualiza_fatura_cancelado/3')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    pytest.main()
