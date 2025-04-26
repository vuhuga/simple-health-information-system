class HealthProgram:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.clients_enrolled = []

    def enroll_client(self, client):
        if client not in self.clients_enrolled:
            self.clients_enrolled.append(client)
            client.enroll_in_program(self)
            return True
        return False

class Client:
    def __init__(self, client_id, name, age, gender, contact_info=None):
        self.client_id = client_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info or {}
        self.enrolled_programs = []

    def enroll_in_program(self, program):
        if program not in self.enrolled_programs:
            self.enrolled_programs.append(program)
            return True
        return False

    def get_profile(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "contact_info": self.contact_info,
            "enrolled_programs": [program.name for program in self.enrolled_programs]
        }

class HealthInformationSystem:
    def __init__(self):
        self.clients = {}
        self.health_programs = {}

    def create_program(self, name, description=""):
        if name not in self.health_programs:
            self.health_programs[name] = HealthProgram(name, description)
            return True
        return False

    def register_client(self, client_id, name, age, gender, contact_info=None):
        if client_id not in self.clients:
            self.clients[client_id] = Client(client_id, name, age, gender, contact_info)
            return True
        return False

    def enroll_client_in_program(self, client_id, program_name):
        if client_id in self.clients and program_name in self.health_programs:
            client = self.clients[client_id]
            program = self.health_programs[program_name]
            return program.enroll_client(client)
        return False

    def search_client(self, query):
        results = []
        for client_id, client in self.clients.items():
            if query.lower() in client.name.lower() or query == client_id:
                results.append(client)
        return results

    def get_client_profile(self, client_id):
        if client_id in self.clients:
            return self.clients[client_id].get_profile()
        return None
