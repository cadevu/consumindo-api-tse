import requests
import json
from time import sleep
hora_apuracao = 0
def buscar_dados():
    global hora_apuracao
    request = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')
    conteudo = json.loads(request.content)
    if conteudo['hg'] != hora_apuracao:
        print(f"Horário da apuração: {conteudo['hg']},\n{conteudo['pst']}% de urnas apuradas ")
        print(f"Candidato: {conteudo['cand'][0]['nm']}, Votos válidos: {conteudo['cand'][0]['vap']},percentual: {conteudo['cand'][0]['pvap']}%")
        print(f"Candidato: {conteudo['cand'][1]['nm']}, Votos válidos: {conteudo['cand'][1]['vap']},percentual: {conteudo['cand'][1]['pvap']}%\n")
    hora_apuracao = conteudo['hg']

while True:
    buscar_dados()
    sleep(30)