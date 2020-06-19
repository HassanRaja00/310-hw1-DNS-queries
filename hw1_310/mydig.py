import dns.query

import datetime

from dns.message import Message


class MyDig:

    def __init__(self, address: str):
        self.__addr = address

    ''' the method below gets IP address of any site '''

    def getOutput(self):
        import time
        startTime = time.time()  #start timer
        timeOfRequest = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        query = dns.message.make_query(self.__addr, 'A')
        print("Question Section:")
        question = query.question[0]  # get question section
        print(query.question[0])

        print("\nAnswer Section:")
        response = dns.query.udp(query, '199.9.14.201')  # root server
        additional = response.additional

        q2 = self.getIP(additional)
        response = dns.query.udp(query, q2)

        additional = response.additional
        q2 = self.getIP(additional)

        response = dns.query.udp(query, q2)
        print(response.answer[0])
        print('\n')

        time = "Query time: %s ms" % ((time.time() - startTime) * 1000)
        print(time)

        when = "When: " + timeOfRequest
        print(when)
        answer = str(response.answer[0])

    # checks if the ip if for A and not AAAA
    def checkCorrectIP(self, string: str):
        if string.__contains__('.'):
            return True
        elif string.__contains__(':'):
            return False

    # helps get a correct A ip address
    def getIP(self, additional):
        for ip in additional:
            intermediate = str(ip[0])
            correct_ip = self.checkCorrectIP(str(intermediate))
            if correct_ip:
                return intermediate
                break
            else:
                return ""
                pass