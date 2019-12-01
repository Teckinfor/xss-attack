import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 12_000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        # receive the data
        while True:
            data = connection.recv(16)
            if data:
                print('received {!r}'.format(data))

    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()

