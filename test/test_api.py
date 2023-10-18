from fastapi.testclient import TestClient
from main import app

# Intanciando um objeto do tipo TesteClient
client = TestClient(app)


def test_response_root():
    """Função que testa a resposta do endpoint Get raiz

    Return: Deve retornar o teste feito com sucesso
    """
    
    response = client.get('/api/v1')
    
    assert response.status_code == 200

