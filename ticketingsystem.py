import sqlite3

class TicketingSystem:
    def __init__(self, db_name):
        self.eventos = []
        self.usuarios = []
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS events (name TEXT, date TEXT, venue TEXT, capacity INTEGER, tickets_sold INTEGER, description TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, email TEXT)")
        self.conn.commit()
    
    def add_event(self, eventos):
        self.events.append(eventos)
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?, ?)", (eventos.nome, eventos.data, eventos.endereco, eventos.capacidade, eventos.tickets_vendidos, eventos.descricao))
        self.conn.commit()
    
    def add_user(self, usuario):
        self.users.append(usuario)
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (usuario.usuario, usuario.senha, usuario.email))
        self.conn.commit()
    
    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False
    
    def sell_tickets(self, event_name, quantity, username, password):
        if not self.authenticate_user(username, password):
            print("Authentication failed. Please provide valid credentials.")
            return
        
        for event in self.events:
            if event.name == event_name:
                if event.sell_tickets(quantity):
                    cursor = self.conn.cursor()
                    cursor.execute("UPDATE events SET tickets_sold = ? WHERE name = ?", (event.tickets_sold, event_name))
                    self.conn.commit()
                return
        
        print(f"Event '{event_name}' not found.")
    
    def show_events(self):
        for event in self.events:
            print(event)
            print(f"Tickets available: {event.tickets_available()}\n")
    
    def show_users(self):
        for user in self.users:
            print(user)
