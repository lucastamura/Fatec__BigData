#Orientacoes em : https://youtu.be/rywDqxJTDPY

import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        iTOKEN  = '5343663633:AAHZ5C2QZlH5Zl1IJlI43lEsTQJT87zzgbs'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'

    def Iniciar(self):
        iUPDATE_ID = None
        while True:
            iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = iATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    msg = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_msg = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(msg, primeira_msg)
                    self.responder(resposta, chat_id)
                    print(chat_id)

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, msg, primeira_msg):
        print('msg do cliente: ' + str(msg))
        if primeira_msg == True or msg.lower() in ('oi','start'):
            return f'''Olá seja bem vindo ao BusKredit, informe a opção desejada:{os.linesep}1 - Horário dos Ônibus{os.linesep}2 - Locais de parada{os.linesep}3 - Recarga de Cartão'''
        if msg == '1':
            return f'''Local de partida (Digite a Sigla):{os.linesep}Mr - Marília{os.linesep}Pn - Padre Nóbrega{os.linesep}Or - Oriente{os.linesep}Po - Pompéia{os.linesep}Pl - Paulópolis{os.linesep}Qt - Quintana{os.linesep}Hc - Herculândia{os.linesep}Tp - Tupã'''

        elif msg == '2':
            return f'''Pizza Napolitana - R$27,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif msg == '3':
            return f'''Pizza 4 Queijos - R$30,00{os.linesep}Confirmar pedido?(s/n)'''

        elif msg.lower() in ('s', 'sim'):
            return ''' Pedido Confirmado! '''
        elif msg.lower() in ('n', 'não'):
            return ''' Item não incluso! Informe o codigo do item: '''
        else:
            return 'Para acessar o cardapio digite "menu"'

    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))


bot = TelegramBot()
bot.Iniciar()