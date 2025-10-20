from flask import Blueprint, request  
from controllers.jogos_controllers import get_jogos, create_jogos,update_jogos, get_jogo_by_id 

# Define um Blueprint para as rotas de "Carro"
jogos_routes = Blueprint('jogo_routes', __name__)  

# Rota para listar todos os carros (GET)
@jogos_routes.route('/Jogo', methods=['GET'])
def jogos_get():
    return get_jogos()

# Rota para buscar um carro pelo ID (GET)
@jogos_routes.route('/Jogo/<int:jogo_id>', methods=['GET'])
def jogo_get_by_id(jogo_id):
    return get_jogo_by_id(jogo_id)

# Rota para criar um novo carro (POST)
@jogos_routes.route('/Jogo', methods=['POST'])
def jogos_post():
    return create_jogos(request.json)

@jogos_routes.route('/Jogo/<int:jogo_id>', methods=['PUT'])
def jogos_put(jogos_id):
    jogos_data = request.json 
    return update_jogos(jogos_id, jogos_data)