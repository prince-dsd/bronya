# 📚 Bronya Project

Welcome to the **Bronya** project! This repository contains a comprehensive setup for a web scraping and data processing application using Scrapy, RabbitMQ, and various other tools and libraries.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.10+
- Node.js 12.20.1+
- Docker
- RabbitMQ

### 📦 Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/bronya.git
   cd bronya
   ```

2. **Set up the environment:**
   ```sh
   cp .env.example .env
   # Update .env with your configuration
   ```

3. **Install dependencies:**
   ```sh
   poetry install
   ```

4. **Run database migrations:**
   ```sh
   poetry run alembic upgrade head
   ```

### 🐳 Docker Setup

1. **Build and run Docker containers:**
   ```sh
   docker-compose up --build
   ```

### 🕸️ Running Scrapy Spiders

To run a specific spider, use the following command:
```sh
scrapy crawl <spider_name>
```

### 🛠️ Development

#### Linting and Formatting

- **Pylint:**
   ```sh
   pylint <your_python_files>
   ```

- **Black:**
   ```sh
   black <your_python_files>
   ```

- **isort:**
   ```sh
   isort <your_python_files>
   ```

#### Pre-commit Hooks

Ensure code quality by using pre-commit hooks:
```sh
pre-commit install
```

### 📜 Configuration

Configuration files:
- `.env`: Environment variables
- `settings.py`: Scrapy settings
- `alembic.ini`: Database migration settings
- `pyproject.toml`: Project dependencies and configurations

### 📂 Project Structure

```plaintext
bronya/
├── alembic.ini
├── commands/
├── database/
├── deploy.sh
├── Dockerfile.rabbitmq
├── items/
├── loaders/
├── middlewares/
├── pipelines/
├── pm2.config.js
├── pyproject.toml
├── README.md
├── rmq/
├── scrapy.cfg
├── settings.py
├── spiders/
├── tests/
└── utils/
```

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on the code of conduct and the process for submitting pull requests.

### 📧 Contact

For any inquiries, please contact [Prince Kumar](mailto:neo11prince@gmail.com).

Happy coding! 🎉