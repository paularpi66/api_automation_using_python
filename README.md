#  API Automation Using Python

This repository contains automated tests for API endpoints using Python. The goal is to ensure the reliability, accuracy, and performance of RESTful APIs through automation.

---

#  Technologies Used

- **Python 3.x**
- **Requests** – For sending HTTP requests
- **Pytest** – For writing and running tests
- **Allure** *(optional)* – For test reporting
- **JSON** – For request/response body handling


#  Project Structure
```bash
api-automation/
│
├── tests/ # Test cases
│ └── test_users.py # Example test
│
├── utils/ # Helper functions (e.g., auth, config)
│ └── request_handler.py
│
├── data/ # Test data files (JSON or YAML)
│
├── conftest.py # Pytest fixtures
├── requirements.txt # Dependencies
└── README.md
```

---

#  How to Run

### Clone the repository


git clone https://github.com/your-username/api-automation.git
```bash
cd api-automation
```

 
## Install dependencies

 ```bash
  pip install -r requirements.txt
```

## Run tests using Pytest
```bash
  pytest -v
```
  
## Features
  . CRUD operation test cases

  . Status code and response validation

  . Parametrized test support

  . Modular structure using helper functions and fixtures

# Notes
  . Keep your sensitive data (e.g., tokens, credentials) in .env or config files (excluded via .gitignore)
  
  . Use pytest.mark.parametrize for testing multiple data scenarios
  
  . Add assertions for status codes, response schema, and data content

