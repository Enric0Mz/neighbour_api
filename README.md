Neighborhood Connect API
The Neighborhood Connect API is a backend application built using the Python FastAPI framework. It serves as the foundation for a neighborhood app that facilitates interaction and communication among neighbors. This README file provides an overview of the project and instructions for setting up and running the API.

Features (on develop)
The Neighborhood Connect API offers the following features:

User authentication and authorization: Users can create accounts, log in, and access protected resources based on their role (e.g., resident, administrator).
Neighbor profiles: Users can create and manage their profiles, providing information such as name, address, contact details, and interests.
Neighborhood posts: Users can create, view, and interact with posts related to their neighborhood. They can share news, ask for recommendations, organize events, and more.
Direct messaging: Users can send private messages to other neighbors, fostering direct communication and collaboration.
Notifications: Users receive notifications about new messages, comments on their posts, and other relevant activities.

Requirements
To run the Neighborhood Connect API locally, you need to have the following software installed:
Python 3.7 or above
poetry 1.1.2

Install dependecies
poetry install

Run server
make run