class Event:
    def __init__(self, nome, data, endereco, capacidade, descricao):
        self.nome = nome
        self.data = data
        self.endereco = endereco
        self.capacidade = capacidade
        self.tickets_vendidos = 0
        self.descricao = descricao
    
    def tickets_disponiveis(self):
        return self.capacidade - self.tickets_vendidos
    
    def vender_tickets(self, quantidade):
        if quantidade <= self.tickets_disponiveis():
            self.tickets_vendidos += quantidade
            print(f"{quantidade} ticket(s) vendidos para {self.nome} on {self.data}.")
            return True
        else:
            print(f"Desculpe, apenas {self.tickets_disponiveis()} ticket(s) disponiveis para {self.nome} on {self.data}.")
            return False
    
    def __str__(self):
        return f"{self.nome} em {self.data} no {self.endereco}\nDescrição: {self.descricao}\n"
