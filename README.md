# personalized_education_tests

🚀 API Automation Framework with Python & Pytest

This project is a data-driven API automation framework designed using Python, Pytest, and PyCharm, focused on testing the full user journey of an e-learning platform. The test suite validates critical API functionalities such as user authentication, profile management, CV data extraction, and course operations.


---

📌 Key Features

✅ Modular and scalable architecture

✅ Data-driven testing using JSON/CSV files

✅ Centralized configuration for environments

✅ Dynamic request/response validation

✅ Git-integrated and clean repo management

✅ Human-readable test reports

✅ Easily extendable test cases



---

📂 Project Structure

api_automation/
│
├── configs/
│   └── config.yaml                # Base URL, credentials, tokens
│
├── data/
│   └── user_data.json             # Test data for different APIs
│
├── tests/
│   ├── test_login.py             # Login API test
│   ├── test_profile.py           # Update profile, upload profile picture
│   ├── test_cv_extract.py        # Extract CV details
│   ├── test_course.py            # Enroll in course, check details
│   └── test_logout.py            # Logout API test
│
├── utils/
│   ├── request_handler.py        # Wrapper for GET, POST, PUT, etc.
│   └── assertions.py             # Custom assertions for validation
│
├── .gitignore                    # Ignore sensitive & unnecessary files
├── requirements.txt              # Required libraries
├── pytest.ini                    # Pytest configurations
└── README.md                     # Project overview


---

🔐 Covered Test Scenarios

Module	Endpoint Functionality

Auth	Login, Logout
User Profile	Update profile info
	Upload profile picture
CV Parser	Extract structured CV data
Courses	Enroll in a course
	Fetch course details



---

⚙️ Technologies Used

🐍 Python 3.x

🧪 Pytest

🛠️ PyCharm

📤 Requests Library

📊 JSON/YAML

🧾 Allure (optional for reports)



---

📁 Configuration

All environment-specific data (base URL, credentials, etc.) is placed in:

# config.yaml
base_url: "https://api.example.com"
credentials:
  username: "testuser"
  password: "securepass123"


---

🧪 How to Run Tests

1. 🔧 Install dependencies



pip install -r requirements.txt

2. ▶️ Run the test suite



pytest -v --tb=short --capture=no

3. 📈 (Optional) Generate Allure report



pytest --alluredir=allure-results
allure serve allure-results


---

🧹 .gitignore Highlights

__pycache__/
*.pyc
.env
allure-results/
*.log
.idea/


---

📌 Skills Highlighted

API Automation Design

Data-Driven Test Strategy

Modular Code & Reusability

CI/CD-ready Test Architecture

Secure Credential Handling

Real-World API Testing Expertise



---

🤝 Contributing

Pull requests and improvements are welcome! Feel free to fork and enhance the framework to fit your needs.


---

📧 Contact

Arpita Paul
SQA Engineer | API & Web Automation Specialist
LinkedIn | GitHub


---
