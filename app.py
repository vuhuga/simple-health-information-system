from flask import Flask, jsonify, request
from health_system import HealthInformationSystem

app = Flask(__name__)
health_system = HealthInformationSystem()

# Initialize with some sample data
health_system.create_program("TB", "Tuberculosis treatment program")
health_system.create_program("Malaria", "Malaria prevention and treatment")
health_system.create_program("HIV", "HIV/AIDS management program")
health_system.register_client("C001", "Brian Vuhuga", 21, "Male", {"phone": "0712345678"})
health_system.register_client("C002", "Jada Smith", 28, "Female", {"phone": "0787654321"})
health_system.enroll_client_in_program("C001", "TB")
health_system.enroll_client_in_program("C002", "HIV")

@app.route('/api/programs', methods=['GET', 'POST'])
def programs():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        description = data.get('description', '')
        if health_system.create_program(name, description):
            return jsonify({"message": "Program created successfully"}), 201
        return jsonify({"error": "Program already exists"}), 400
    else:
        return jsonify({"programs": list(health_system.health_programs.keys())})

@app.route('/api/clients', methods=['GET', 'POST'])
def clients():
    if request.method == 'POST':
        data = request.get_json()
        client_id = data.get('client_id')
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        contact_info = data.get('contact_info', {})
        
        if health_system.register_client(client_id, name, age, gender, contact_info):
            return jsonify({"message": "Client registered successfully"}), 201
        return jsonify({"error": "Client ID already exists"}), 400
    else:
        return jsonify({"clients": [client.get_profile() for client in health_system.clients.values()]})

@app.route('/api/clients/<client_id>', methods=['GET'])
def client_profile(client_id):
    profile = health_system.get_client_profile(client_id)
    if profile:
        return jsonify(profile)
    return jsonify({"error": "Client not found"}), 404

@app.route('/api/clients/search', methods=['GET'])
def search_client():
    query = request.args.get('q', '')
    results = health_system.search_client(query)
    return jsonify({"results": [client.get_profile() for client in results]})

@app.route('/api/enroll', methods=['POST'])
def enroll_client():
    data = request.get_json()
    client_id = data.get('client_id')
    program_name = data.get('program_name')
    
    if health_system.enroll_client_in_program(client_id, program_name):
        return jsonify({"message": "Enrollment successful"})
    return jsonify({"error": "Enrollment failed - client or program not found"}), 400

if __name__ == '__main__':
    app.run(debug=True)
