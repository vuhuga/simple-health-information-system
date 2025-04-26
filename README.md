# simple-health-information-system
Introduction
This project is designed to help health practitioners manage client registrations and enroll them in various health programs using a RESTful API built with Flask.

Features
Register new clients.

Create health programs (e.g., TB, Malaria, HIV).

Enroll clients in one or more programs.

Search and view client profiles.

Expose client data via an API for external system integration.

#Run the Flask application:
bash
python app.py

API Endpoints
Method	Endpoint	Description
POST	/create_program	Create a new health program
POST	/register_client	Register a new client
POST	/enroll_client	Enroll a client in a program
GET	/get_client/<client_id>	Retrieve client details
