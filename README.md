# SplineSandbox

Welcome to SplineSandbox, a powerful environment for exploring advanced mathematical concepts, developing production-ready applications, and fostering collaboration between researchers and developers. 🚀

## Getting Started

To start working with SplineSandbox, follow these steps:

### Prerequisites

1. Ensure you have [Visual Studio Code](https://code.visualstudio.com/download) installed on your machine.

2. Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for Visual Studio Code.

### Setting Up the Dev Container

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/SplineSandbox.git
   ```

2. Open Visual Studio Code and navigate to the project directory.

3. When prompted, click on the "Reopen in Container" button. This will automatically set up the development container environment defined in the `devcontainer.json` file.

### Environment Overview

SplineSandbox uses Docker Compose to create a containerized development environment with the following services:

- **app**: The primary development container with Python 3.10, Jupyter notebooks, and SQL tools. Mathematical research and development can take place here.

- **db**: A TimescaleDB instance for advanced database operations.

- **rabbitmq**: A RabbitMQ message broker for tasks and queuing.

### Using the Environment

Once the environment is set up, here's what you can do:

#### Research with Jupyter Notebooks

1. Explore the `workbooks` folder to find Jupyter notebooks for mathematical research and experimentation.

2. Use the integrated Python environment with libraries like NumPy and SciPy to perform mathematical calculations.

#### Develop Production Applications

1. Check out the `app` folder to see how mathematical concepts can be implemented in real-world applications.

2. Use Visual Studio Code's extensions for Python development and SQL tools for database interaction.

#### Collaboration

- Researchers and developers can collaborate on the same project using their preferred workflows and methodologies.

### Useful Commands

- To start Jupyter notebooks, open a terminal in Visual Studio Code and run:

  ```bash
  jupyter notebook
  ```

- To access the TimescaleDB database, use the following connection details:

  - **Server**: `db`
  - **Username**: `postgres`
  - **Password**: `postgres`
  - **Database**: `postgres`
  - **Port**: `5432`

### Contributions

We welcome contributions from researchers and developers alike! If you have mathematical insights or application ideas, feel free to create branches and open pull requests. Let's innovate together!

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

We would like to express our gratitude to the open-source community for providing tools and libraries that make projects like SplineSandbox possible.

Happy Exploring and Developing! 🚀

![SplineSandbox Logo](./images/splinelogo.jpeg)
