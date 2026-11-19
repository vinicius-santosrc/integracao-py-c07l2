# planta_dao.py
# EXERCÍCIO: complete cada função no espaço indicado (onde está o TODO).
# Use sempre parâmetros (%s) e feche a conexão no finally.

from mysql.connector import Error

from connection_dao import close_connection, get_connection


# Questão 1: inserir uma planta.
# Deve inserir na tabela planta e devolver o id gerado (cursor.lastrowid).
# Lembre-se do commit!
def inserir_planta(nome, especie, preco, estoque):
    # TODO
    return None


# Questão 2: listar todas as plantas, ordenadas pelo id.
# Deve devolver a lista de tuplas (cursor.fetchall()).
def listar_plantas():
    # TODO
    return []


# Questão 3: buscar as plantas de uma espécie.
# Deve devolver a lista de tuplas das plantas cuja espécie seja igual ao parâmetro.
def buscar_por_especie(especie):
    # TODO
    return []


# Questão 4: atualizar o preço de uma planta pelo id.
# Deve devolver True se alguma linha foi alterada (cursor.rowcount > 0), senão False.
def atualizar_preco(id_planta, novo_preco):
    # TODO
    return False


# Questão 5: remover uma planta pelo id.
# Deve devolver True se alguma linha foi removida, senão False.
def remover_planta(id_planta):
    # TODO
    return False


# Questão 6 (Desafio): valor total do estoque.
# Deve devolver a soma de preco * estoque de todas as plantas, como float.
# Dica: SELECT COALESCE(SUM(preco * estoque), 0) FROM planta
def valor_total_estoque():
    # TODO
    return 0.0
