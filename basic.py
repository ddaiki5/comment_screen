import discord
import queue
from socket import socket, AF_INET, SOCK_STREAM

#client = discord.Client()
HOST        = 'localhost'
PORT        = 49000

CHR_CAN     = '\18'
CHR_EOT     = '\04'

class get_message_bot:
    def __init__(self):
        self.client = discord.Client()
        self.q = queue.Queue()

        @self.client.event
        async def on_ready():
            print("ログインしました")

        @self.client.event
        async def on_message(message):
            #except bot
            if message.author.bot:
                return

            def check(msg):
                return msg.author == message.author
            
            async def print_m(m):
                #print()
                self.q.put(m)
    
            wait_message = await self.client.wait_for("message", check=check)

            #await message.channel.send(wait_message.content)
            #await print_m(wait_message.content)
            #self.q.put(wait_message.content)

            # 通信の確立
            try:
                sock = socket(AF_INET, SOCK_STREAM)
                sock.connect((HOST, PORT))

                # メッセージ送信
                sock.send((wait_message.content).encode('shift-jis'))

                # 通信の終了
                sock.close()
            except:
                print("miss")
            
    
    def run(self, token):
        self.client.run(token)


def load_token():
    with open("token.txt", "r") as f:
        token = f.read()
    return token


if __name__ == '__main__':
    token = load_token()
    bot = get_message_bot()
    bot.run(token)
    #self.sock.close()

