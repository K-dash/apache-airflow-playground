# Apache Airflow Playground

This repository provides a playground environment for Apache Airflow using Docker Compose and Visual Studio Code's Remote - Containers extension.

## Development with .devcontainer

This project is set up to use Visual Studio Code's Remote - Containers extension, which allows you to develop inside a Docker container. This ensures a consistent development environment across different machines.

### Prerequisites

- Docker
- Docker Compose
- Visual Studio Code
- Remote - Containers extension for VS Code

## Package Management with Poetry

This project uses Poetry for package management, but installs packages globally in the Airflow image's Python environment instead of creating a virtual environment. This approach allows us to manage additional packages while leveraging the existing Airflow setup.


## Usage

To start developing with the .devcontainer:

1. Clone this repository.
```bash
git clone https://github.com/K-dash/apache-airflow-playground.git
cd apache-airflow-playground
```

2. Open the project in Visual Studio Code.
```bash
code .
```


3. When prompted by VS Code, click "Reopen in Container". Alternatively, you can.
- Press `F1` and select `Remote-Containers: Reopen in Container`
- Click the green button in the lower-left corner and select `Reopen in Container`

4. Wait for the container to build and start. This may take a few minutes the first time.

5. Once the container is running, you'll have a full Airflow development environment ready to use.

6. You can access the Airflow web interface at `http://localhost:8080` (default credentials: airflow/airflow).

7. To add an arbitrary package, run the command `poetry add <package-name>`.

8. Start developing your DAGs in the `dags` directory.

Now you're ready to start working with Apache Airflow in a containerized development environment!
