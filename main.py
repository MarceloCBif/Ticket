from eventos import Event
from user import User
from ticketingsystem import TicketingSystem
from jinja2 import Environment, FileSystemLoader

def gerar_html(eventos, usuarios):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    rendered_html = template.render(events=eventos, users=usuarios)
    return rendered_html

# Exemplo de uso
ticketing_system = TicketingSystem("ticketing_system.db")

evento1 = Event("Apresentacao", "2023-07-10", "Praça da Bandeira", 1000, "Show do Mucosa Suína.")
evento2 = Event("Peça de Teatro", "2023-07-15", "Teatro Municipal", 500, "Choradeira no teatro.")
evento3 = Event("Show de Comédia", "2023-07-20", "Prefeitura", 200, "Show de horrores na prefa.")

ticketing_system.add_event(evento1)
ticketing_system.add_event(evento2)
ticketing_system.add_event(evento3)

usuario1 = User("bisteca", "bistequera", "bisteca@gmail.com")
usuario2 = User("prim", "primzera", "prim@gmail..com")


ticketing_system.add_user(usuario1)
ticketing_system.add_user(usuario2)

ticketing_system.sell_tickets("Apresentacao", 3, "bisteca", "bistequera")
ticketing_system.sell_tickets("Peça de Teatro", 2, "bisteca", "bistequera")
ticketing_system.sell_tickets("Show de Comédia", 5, "bisteca", "bistequera")

rendered_html = gerar_html(ticketing_system.events, ticketing_system.users)

# Exibindo o HTML
print(rendered_html)
