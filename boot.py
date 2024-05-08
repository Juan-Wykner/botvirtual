from telethon import TelegramClient,sync,events
from time import sleep
import requests
from senhas import api_hash,api_id

sessao = 'repassar mensagem'

def main():
        print('Monitoramento iniciado...')
        client = TelegramClient (sessao, api_id, api_hash)
        @client.on(events.NewMessage (chats = [6154888245]))
        async def enviar_mensagem(event):
            await client.send_message(4247947277,event.raw_text)
        client.start()
        client.run_until_disconnected()


main()
