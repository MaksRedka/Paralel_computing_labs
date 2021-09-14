import socket, time

questions = ["What do you prefer?", "How many will be 2 + 2?", "What do you like more?"] #Our Questions
answers = [["Apple", "Banana", "Pineapple"], ["4", "6", "8"], ["Films", "Games", "Sport"]]#Our answers

host = socket.gethostbyname(socket.gethostname()) 
port = 9090

#gethostname Return a string containing the hostname of the
#machine where the Python interpreter is currently executing
#gethostbyname Translate a host name to IPv4 address format.

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # tcp,ip protocol
s.bind((host, port))  # create server using this host and port(Bind the socket to address)

res_ans = []
indx = 0
shutdown = False
quit = False
print("[ Server Started ]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)  # recieve data and address not more than 1024b

        if addr not in clients: #if address is new we addin it to array
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "/]", end="")
        print(data.decode("utf-8"))#printin addres, time when massage come and data 

        text = data.decode("utf-8").split()#spliting data into pieces for more comfortable usage

        if text[-1] == "quit":#if our massage equal (quite) coming out from the loop and closing our connection.
            print("\n[ Server Stopped ]")
            quit = True

        if text[-2] == "join":#if our massage equal join, we send our question to user
            for client in clients:
                # s.sendto("Wrong answers try again.",client)
                s.sendto((f"{questions[indx]} \n{answers[indx]}").encode("utf-8"), client)
        else:#the we checking users answer


            if text[-1] in answers[indx]:#if answer is locadet in our subarray we increase index and sending new question to user
                indx += 1
                res_ans.append(text[-1])
                if indx < 3:
                    s.sendto((f"{questions[indx]} \n{answers[indx]}").encode("utf-8"), client)#sending new question
            else:#if answer is not locadet in our subarray we saying that anser is wrong and
                for client in clients:
                    if indx < 3:
                        s.sendto(
                            ("\nWrong answers try again.\n" + f"{questions[indx]} \n{answers[indx]}").encode("utf-8"),
                            client)
        #print(text, res_ans, text[-1], indx)

        if indx == 3:#when we send all questions and get all answers we printing users ansers
            for client in clients:
                s.sendto((f"\nYour answers are {res_ans}.\nWrite quite to exit and press Ctrl+C.").encode("utf-8"),client)

    except:#if any error we coming out the loop and closing our server
        print("\n[ Server Stopped ]")
        quit = True

s.close()