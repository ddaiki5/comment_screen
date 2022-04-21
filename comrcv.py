import socket

# ソケット通信テスト

host = "127.0.0.1" #Processingで立ち上げたサーバのIPアドレス
port = 49000       #Processingで設定したポート番号

if __name__ == '__main__':
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成
    socket_client.connect((host, port))                               #サーバに接続

    socket_client.send('送信するメッセージ'.encode('shift-jis')) #データを送信 Python