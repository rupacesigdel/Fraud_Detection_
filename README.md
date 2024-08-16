# Fraud Detection System

## Overview

This project is a Django-based fraud detection system that leverages real-time data processing to identify potentially fraudulent transactions. The system integrates with Fluvio for real-time data streaming, and a machine learning model is used to predict fraud.

## Contain

- [Features](#features)
- [Demo Video](#demo-video)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Fluvio Integration](#fluvio-integration)
- [Data Visualization](#data-visualization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Demo Video
[Watch the demo video](https://github.com/rupacesigdel/)

## Features

- **Real-time Fraud Detection:** Integrates with Fluvio to process and analyze transaction data in real-time.
- **Django Web Interface:** Provides a web interface for creating and viewing transactions.
- **Fraud Alerts:** Flags and notifies about potentially fraudulent transactions.
- **Data Visualization:** Visualizes transaction statistics and fraud detection results.

## Technologies Used

- Python
- Django
- Fluvio
- PostgreSQL
- Rust compiler (for building Fluvio)
- Other Python packages: `pandas`, `joblib`, `matplotlib`, `psycopg2`, etc.

## Installation

### Setting Up Your Environment

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/rupacesigdel/Fraud_Detection_.git
    cd fraud-detection-system
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: source myenv\Scripts\activate
    ```

3. **Upgrade pip (if needed):**

    ```bash
    pip install --upgrade pip
    ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Install Fluvio:**
   - If you encounter issues with Fluvio installation, ensure you have Rust installed. Follow the steps below if needed:
     - Install Rust using rustup:
       ```bash
       curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
       ```
     - Restart your terminal and ensure Rust is in your PATH.

     - Try installing Fluvio again:
       ```bash
       pip install fluvio
       ```

6. **Database Setup:**

    - Configure your database settings in `settings.py`.
    - Run migrations to set up the database schema:

      ```bash
      python manage.py migrate
      ```

7. **Load Initial Data (Optional):**

    If you have initial data, you can load it using:

    ```bash
    python manage.py loaddata initial_data.json
    ```

## Project Structure
- fraud_detection_project/
- │
- ├── fraud_detection/
- │   ├── __init__.py
- │   ├── admin.py
- │   ├── apps.py
- │   ├── forms.py
- │   ├── models.py
- │   ├── tests.py
- │   ├── views.py
- │   ├── fraud_detection.py
- │   ├── templates/
- │   │   └── transactions/
- │   │       ├── create_transaction.html
- │   │       ├── transaction_detail.html
- │   │       ├── transaction_list.html
- │   │       ├── statics_view.html
- │   │       └── home.html
- │   │   └── base.html
- │   ├── static/
- │   │   └── transactions/
- │   │       └── styles.css
- │   └── migrations/
- │       └── __init__.py
- │
- ├── fraud_detection_project/
- │   ├── __init__.py
- │   ├── asgi.py
- │   ├── settings.py
- │   ├── urls.py
- │   ├── wsgi.py
- │
- ├── manage.py
- ├── model.pkl
- ├── README.md
- └── requirements.txt



## Usage

1. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the Web Application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

3. **Create Transactions:**

    - Use the "Create Transaction" page to add new transactions.
    - Transactions will be processed in real-time, and potentially fraudulent transactions will be flagged.

4. **View Transactions:**

    - Navigate to the "Transactions" page to view a list of all transactions.
    - Click on a transaction to view its details and fraud status.

## Fluvio Integration

1. **Set Up Fluvio:**

    - Ensure Fluvio is properly set up and running. Refer to the [Fluvio documentation](https://fluvio.io/docs/) for setup instructions.

2. **Start Fluvio Streams:**

    - Use the Fluvio CLI to create and manage streams. Ensure your Django application is correctly configured to interact with Fluvio.

## Data Visualization

1. **Run Data Visualization Script:**

    To generate a pie chart or other visualizations, use the provided scripts:

    ```bash
    python visualize_data.py
    ```

## Contributing

1. **Fork the Repository:**

    - Create a fork of the repository on GitHub.

2. **Create a Pull Request:**

    - Open a pull request from your forked repository to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Fluvio Team:** For providing the powerful real-time streaming platform that enables our fraud detection system to operate efficiently.
- **Django Community:** For the robust web framework that serves as the foundation of our application.
- **OpenAI:** For their research and technologies that inspired parts of the fraud detection algorithms and overall approach.
- **Stack Overflow and GitHub:** For community support and code examples that helped resolve technical challenges during development.
- **Rust Community:** For their tools and libraries that made it possible to build and integrate Fluvio into our project.

---

Feel free to customize this `README.md` file according to your project's specific details and requirements.
