from client import Client
from manager import Manager
from order import Order

class Trade:
    """

    """
    def __init__(self, trade_id: int):
        """ """
        self.trade_id = trade_id
        self.managers = []
        self.clients = []
        self.orders = []

    def add_manager(self, manager: Manager):
        """ """
        self.managers.append(manager)

    def add_client(self, client: Client):
        """ """
        self.clients.append(client)

    def add_order(self, order: Order):
        """ """
        self.orders.append(order)

    def __str__(self):
        # ToDo
        return f"{self.trade_id} {self.managers} {self.clients} {self.orders}"

    def read_managers(self, managers_fname):
        with open(managers_fname, "r") as managers_f:
            for line in managers_f:
                manager_id, name, city, comm = line.split(";")
                manager_id = int(manager_id)
                comm = float(comm)
                manager = Manager(manager_id, name, city, comm)
                self.managers.append(manager)

    def read_clients(self, clients_fname):
        with open(clients_fname, "r") as clients_f:
            for line in clients_f:
                client_id, name, city, rating, manager_id = line.split(";")
                client_id = int(client_id)
                manager_id = int(manager_id)
                client = Client(client_id, name, city, rating, manager_id)
                self.clients.append(client)

    def read_orders(self, orders_fname):
        with open(orders_fname, "r") as orders_f:
            for line in orders_f:
                order_id, manager_id, client_id, order_date, amount = line.split(";")
                order_id = int(order_id)
                manager_id = int(manager_id)
                client_id = int(client_id)
                amount = float(amount)
                order = Order(order_id, manager_id, client_id, order_date, amount)
                self.orders.append(order)


    def Kovrov_managers(self):
        """ """
        res = []
        for manager in self.managers:
            if manager.city.upper() == 'КОВРОВ':
                res.append(manager)
        return res

if __name__ == '__main__':
    trade = Trade(1)
    trade.read_managers("manager.txt")
    # ToDo
    trade.read_clients("client.txt")
    trade.read_orders("order.txt")
    
    print('Ковровские продавцы')
    print('manager_id name city comm')
    for manager in trade.Kovrov_managers():
        print(manager)
    print()
