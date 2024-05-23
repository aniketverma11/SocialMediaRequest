This is a Django-based social media application developed for educational purposes. It provides basic social networking functionalities such as user registration, friend requests, and friend lists.

## Installation

### Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/social-media-app.git
cd social-media-app
```

## Setup Python Virtual Environment (optional but recommended)

```
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# For macOS/Linux
source env/bin/activate
# For Windows
.\env\Scripts\activate

```

## Install Requirements

```pip install -r requirements.txt

```
## Apply Migrations
```python manage.py migrate
```

##  Run the Development Server

```python manage.py runserver
```


# Django Docker Compose Example

This is a simple Django project configured to run with Docker Compose. It includes a Dockerfile for building the Django application image and a docker-compose.yml file to orchestrate the services.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to run the Django application with Docker Compose:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-django-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-django-project
    ```

3. Build the Docker containers:

    ```bash
    docker-compose build
    ```

4. Start the containers:

    ```bash
    docker-compose up
    ```

5. Once the containers are running, open your web browser and go to [http://localhost:8000](http://localhost:8000) to view the Django application.

## Additional Commands

### Stop the Containers

To stop the containers, press `Ctrl + C` in the terminal where they are running.

### Clean Up

To stop and remove the containers, networks, and volumes created by Docker Compose, run:

```bash
docker-compose down
