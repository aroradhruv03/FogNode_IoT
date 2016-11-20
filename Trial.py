


class fog_node:
    host_name = ""
    IP_addr = ""
    TCP_port = ""
    UDP_port = ""
    Queue = ""
    list_neighbours = ""
    max_response_time = ""
    queue_time = ""

    def __init__(self):
        host_name = "localhost"
        IP_addr = ""
        TCP_port = "12345"
        UDP_port = "1234"
        Queue = []
        list_neighbours = []
        max_response_time = 123
        queue_time = 123

    def __init__(self, host, tcp, udp, resp_time):
        self.host_name = host
        self.TCP_port = tcp
        self.UDP_port = udp
        self.max_response_time = resp_time

    def __init__(self, ip, tcp, udp, resp_time):
        self.IP_addr = ip
        self.TCP_port = tcp
        self.UDP_port = udp
        self.max_response_time = resp_time