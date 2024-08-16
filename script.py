import csv
from datetime import datetime, timedelta

# Lista de jogos 
#Para preencher, pesquise "calendario (time) próximos jogos" e entre na espn. no meu caso o link foi https://www.espn.com.br/futebol/time/calendario/_/id/3445/fluminense
#Então, fale pro chatGPT substituir o código com as datas que você enviar (copie e cole toda a página)
jogos = [
    # Jogos de agosto
    {"data": "2024-08-17", "hora": "21:00", "oponente": "Corinthians"},
    {"data": "2024-08-20", "hora": "19:00", "oponente": "Grêmio"},
    {"data": "2024-08-24", "hora": "21:00", "oponente": "Atlético-MG"},
    # Jogos de setembro
    {"data": "2024-09-01", "hora": "18:30", "oponente": "São Paulo"},
    {"data": "2024-09-15", "hora": None, "oponente": "Juventude"},  # Horário a definir
    {"data": "2024-09-22", "hora": None, "oponente": "Botafogo"},  # Horário a definir
    {"data": "2024-09-29", "hora": None, "oponente": "Atlético-GO"},  # Horário a definir
    # Jogos de outubro
    {"data": "2024-10-05", "hora": None, "oponente": "Cruzeiro"},  # Horário a definir
    {"data": "2024-10-20", "hora": None, "oponente": "Flamengo"},  # Horário a definir
    {"data": "2024-10-26", "hora": None, "oponente": "Vitória"},  # Horário a definir
    # Jogos de novembro
    {"data": "2024-11-06", "hora": None, "oponente": "Grêmio"},  # Horário a definir
    {"data": "2024-11-13", "hora": None, "oponente": "Internacional"},  # Horário a definir
    {"data": "2024-11-20", "hora": None, "oponente": "Fortaleza"},  # Horário a definir
    {"data": "2024-11-24", "hora": None, "oponente": "Criciúma"},  # Horário a definir
    # Jogos de dezembro
    {"data": "2024-12-01", "hora": None, "oponente": "Athletico-PR"},  # Horário a definir
    {"data": "2024-12-04", "hora": None, "oponente": "Cuiabá"},  # Horário a definir
    {"data": "2024-12-08", "hora": None, "oponente": "Palmeiras"},  # Horário a definir
]

def criar_agenda(jogos):
    with open('agenda_fluminense_2024.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Start Date", "Start Time", "End Date", "End Time"])
        
        for jogo in jogos:
            data_inicio = jogo["data"]
            hora_inicio = jogo.get("hora")
            data_fim = data_inicio
            if hora_inicio is None:
                # Evento de dia inteiro
                writer.writerow([f"Fluminense x {jogo['oponente']}", data_inicio, "", data_fim, ""])
            else:
                hora_fim = (datetime.strptime(hora_inicio, "%H:%M") + timedelta(hours=2)).strftime("%H:%M")
                writer.writerow([f"Fluminense x {jogo['oponente']}", data_inicio, hora_inicio, data_fim, hora_fim])

# Chamada da função para criar o arquivo
criar_agenda(jogos)