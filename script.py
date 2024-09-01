import csv
from datetime import datetime, timedelta

# Lista de jogos 
#Para preencher, pesquise "calendario (time) próximos jogos" e entre na espn. no meu caso o link foi https://www.espn.com.br/futebol/time/calendario/_/id/3445/fluminense
#Então, fale pro chatGPT substituir o código com as datas que você enviar (copie e cole toda a página)
jogos = [
    # Jogos de agosto
    {"data": "2024-09-01", "hora": "18:30", "oponente": "São Paulo", "fluminense_em_casa": True},
    {"data": "2024-09-15", "hora": "16:00", "oponente": "Juventude", "fluminense_em_casa": False},  # Verde
    {"data": "2024-09-18", "hora": "19:00", "oponente": "Atlético-MG (Ida)", "fluminense_em_casa": True},
    {"data": "2024-09-21", "hora": "18:30", "oponente": "Botafogo", "fluminense_em_casa": True},
    {"data": "2024-09-25", "hora": "19:00", "oponente": "Atlético-MG (Volta)", "fluminense_em_casa": False},  # Verde
    {"data": "2024-09-29", "hora": "16:00", "oponente": "Atlético-GO", "fluminense_em_casa": False},  # Verde
    # Jogos de outubro
    {"data": "2024-10-03", "hora": "21:30", "oponente": "Cruzeiro", "fluminense_em_casa": True},
    {"data": "2024-10-20", "hora": None, "oponente": "Flamengo", "fluminense_em_casa": False},  # Horário a definir
    {"data": "2024-10-26", "hora": None, "oponente": "Vitória", "fluminense_em_casa": False},  # Horário a definir
    # Jogos de novembro
    {"data": "2024-11-06", "hora": None, "oponente": "Grêmio", "fluminense_em_casa": True},  # Horário a definir
    {"data": "2024-11-13", "hora": None, "oponente": "Internacional", "fluminense_em_casa": False},  # Horário a definir
    {"data": "2024-11-20", "hora": None, "oponente": "Fortaleza", "fluminense_em_casa": True},  # Horário a definir
    {"data": "2024-11-24", "hora": None, "oponente": "Criciúma", "fluminense_em_casa": True},  # Horário a definir
    # Jogos de dezembro
    {"data": "2024-12-01", "hora": None, "oponente": "Athletico-PR", "fluminense_em_casa": False},  # Horário a definir
    {"data": "2024-12-04", "hora": None, "oponente": "Cuiabá", "fluminense_em_casa": True},  # Horário a definir
    {"data": "2024-12-08", "hora": None, "oponente": "Palmeiras", "fluminense_em_casa": False},  # Horário a definir
]

def criar_agenda(jogos):
    with open('agenda_fluminense_2024.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Start Date", "Start Time", "End Date", "End Time"])
        
        for jogo in jogos:
            data_inicio = jogo["data"]
            hora_inicio = jogo.get("hora")
            data_fim = data_inicio
            #se o jogo for fora de casa, o nome virá com Fora; se for em casa, virá com Maraca
            fora = " Fora" if not jogo["fluminense_em_casa"] else " Maraca"
            if hora_inicio is None:
                # Evento de dia inteiro
                writer.writerow([f"Fluminense x {jogo['oponente']}{fora}", data_inicio, "", data_fim])
            else:
                hora_fim = (datetime.strptime(hora_inicio, "%H:%M") + timedelta(hours=2)).strftime("%H:%M")
                writer.writerow([f"Fluminense x {jogo['oponente']}{fora}", data_inicio, hora_inicio, data_fim, hora_fim])

# Chamada da função para criar o arquivo
criar_agenda(jogos)