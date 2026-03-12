# event_classifier/models/event.py

class Event:
    """
    Clase para representar un evento.
    """

    def __init__(self, name, description, image=None, venue=None, city=None, address=None):
        """
        Inicializa un objeto Event.

        :param name: Nombre del evento
        :param description: Descripción del evento
        :param image: URL de la imagen del evento (opcional)
        :param venue: Lugar del evento (opcional)
        :param city: Ciudad del evento (opcional)
        :param address: Dirección completa del evento (opcional)
        """
        self.name = name
        self.description = description
        self.image = image
        self.venue = venue
        self.city = city
        self.address = address

    def to_dict(self):
        """
        Convierte el objeto Event a un diccionario.
        """
        return {
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "venue": self.venue,
            "city": self.city,
            "address": self.address
        }

    def __str__(self):
        """
        Representación legible del evento.
        """
        return f"Event(name='{self.name}', city='{self.city}', venue='{self.venue}')"

    def __repr__(self):
        return self.__str__()
