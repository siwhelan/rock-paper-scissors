# Rock Paper Scissors Game

This project is a web-based implementation of the classic game Rock, Paper, Scissors. It allows users to play against a computer opponent that randomly selects its move.

## Features

- Play Rock, Paper, Scissors against a computer opponent.
- Responsive design for desktop and mobile users.
- Results displayed with each round played.

## Built With

- Python (Flask)
- HTML/CSS (Tailwind CSS)
- Docker for containerization
- Deployed on Elastic Beanstalk

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- pip and pipenv
- Docker (for containerization)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/siwhelan/rock-paper-scissors.git
   ```

### Navigate to the project directory:

```
sh
Copy code
cd Project-Name
```

### Install Python dependencies:

```
sh
Copy code
pipenv install
```

### Running Locally

To run the application locally:

```
sh
Copy code
pipenv run python app.py
```

The application will be available at http://localhost:5000.

### Docker Usage

To build and run the application using Docker:

### Build the Docker image:

```
sh
Copy code
docker build -t rock-paper-scissors .
```

### Run the Docker container:

```
sh
Copy code
docker run -p 5000:5000 rock-paper-scissors
```

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request
