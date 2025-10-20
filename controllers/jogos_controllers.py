from models.jogos_models import Jogos
from db import db
import json
from flask import make_response

def get_jogos():
    filmes = Jogos.query.all()
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogos.',
            'dados': [jogos.json() for jogos in Jogos]
        }, ensure_ascíí=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def create_jogos(jogos_data):
    if not all(key in jogos_data for key in ['Título', 'Gênero', 'Desenvolvidor', 'Plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Título, Gênero, Desenvolvidor e Plataforma são obrigatórios.'}, ensure_ascíí=False),
            400
        )
        response.headers['Content.Type']= 'application/json'
        return response
    
    novo_jogos = Jogos(
        id =jogos_data['id'],  
        Titulo=jogos_data['Titulo'],  
        Genero=jogos_data['Genero'],    
        Desenvolvidor=jogos_data['Duracao'],
        Plataforma=jogos_data['lancamento'],
    )
    db.session.add(novo_jogos)
    db.session.commit()
    response = make_response(
        json.dumps({  
            'mensagem': 'Jogo cadastrado com sucesso.',  
            'jogos': novo_jogos.json()  
        },ensure_ascii=False, sort_keys=False)  
    )
    response.headers['content-Type'] = 'application/json'
    return response

def get_jogos_by_id(jogos_id):
    carro = Jogos.query.get(jogos_id)  # Busca o carro pelo ID

    if carro:  # Verifica se o carro foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'Jogo encontrado.',
                'dados': carro.json()  # Converte os dados do carro para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o carro não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'Jogo não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo carro
def create_jogo(jogo_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogo_data for key in ['Titulo', 'Genero', 'desenvolvedor', 'Plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, desenvolvedore plataforma são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo carro
    novo_jogos = Jogos(
        id =jogo_data['id'],  
        Titulo=jogo_data['Titulo'],  
        Genero=jogo_data['Genero'],    
        Desenvolvedor=jogo_data['Desenvolvedor'],
        Plataforma=jogo_data['plataforma']
    )
    
    db.session.add(novo_jogos)  # Adiciona o novo carro ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    # Resposta de sucesso com os dados do novo carro
    response = make_response(
        json.dumps({
            'mensagem': 'Jogo cadastrado com sucesso.',
            'carro': novo_jogos.json()  # Retorna os dados do carro cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

def update_jogo(jogo_id, jogo_data):
    jogo = jogo.query.get(jogo_id)

    if not jogo:
        response = make_response(
            json.dumps({'mensegem': 'Jogo não encontrado'}, ensure_ascii=False),
            404
        )
        response.headerst['Ccontent-Type'] = 'applicattion/json'
        return response
    
    if not all(key in jogo_data for key in ['titulo', 'genero', 'desenvolvidor', 'Plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, desenvolvidor e plataforma são obrigatórios'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response 
    
    jogo.titulo = jogo_data['titulo']
    jogo.genero = jogo_data['genero']
    jogo.desenvoldor = jogo_data['desenvolvedor']
    jogo.plataform = jogo_data['plataforma']


    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Jogo atualizado com sucesso.',
            'Jogos': jogo.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response
