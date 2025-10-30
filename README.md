**Shipping Data API using FastAPI & MySQL**
A backend web application built with FastAPI that performs CRUD operations on shipping order data stored in a MySQL database.
The project demonstrates API design, database integration, JSON data import, and backend logic — showcasing Python backend development skills.

✨ Features
---------------------------
✅ FastAPI-based RESTful API
✅ MySQL database connection and CRUD operations
✅ Pydantic model for data validation
✅ JSON file import and table creation
✅ Modular endpoints for:

Sample Quries:
---------------------------
Get order by ID
Get customers by region
Insert new shipping record
Update existing order
Delete order record

Tech Stack
--------------------------
| Component        | Technology                |
| ---------------- | ------------------------- |
| **Language**     | Python 3                  |
| **Framework**    | FastAPI                   |
| **Database**     | MySQL                     |
| **Validation**   | Pydantic                  |
| **Testing Tool** | FastAPI Docs (Swagger UI) |
| **Environment**  | Ubuntu / VS Code          |


📁 Project Structure
---------------------------
ShippingDataAPI/
│
├── connect_mysql.py        # Main FastAPI app file
├── data.json               # Sample dataset to insert into MySQL
├── requirements.txt        # Dependencies (fastapi, mysql-connector-python, uvicorn)
└── README.md               # Project documentation

📡 API Endpoints
---------------------------
| Method     | Endpoint                   | Description                                 |
| ---------- | -------------------------- | ------------------------------------------- |
| **GET**    | `/getUsingOrderid/{_id}`   | Fetch order details by `order_id`           |
| **GET**    | `/customer-data/{_region}` | Get all customer names in a specific region |
| **PUT**    | `/insert_data/`            | Insert new shipping data                    |
| **POST**   | `/post_data/{_order_id}`   | Update existing order record                |
| **DELETE** | `/delete_data/{_order_id}` | Delete a record using order ID              |

🧮 Sample SQL Queries
---------------------------
SELECT * FROM ShippingData WHERE order_id="ORD1038";
SELECT customer_name FROM ShippingData WHERE region="Australia";
INSERT INTO ShippingData VALUES (NULL, 'ORD1005', 'John Doe', 'India', 'Bangalore, KA', 2.5, 45.00, 'Delivered', '2025-10-01', '2025-10-05');
UPDATE ShippingData SET status = 'Delivered', delivery_date = '2025-10-29' WHERE order_id = 'ORD1005';
DELETE FROM ShippingData WHERE order_id = 'ORD1005';

⚙️ Setup Instructions
---------------------------
1️⃣ Clone Repository
git clone https://github.com/<your-username>/shipping-data-api-fastapi-mysql.git
cd shipping-data-api-fastapi-mysql
2️⃣ Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
3️⃣ Install Dependencies
pip install fastapi uvicorn mysql-connector-python
4️⃣ Setup MySQL Database
Open MySQL shell:
mysql -u root -p
CREATE DATABASE testdb;
USE testdb;
5️⃣ Run the FastAPI App
uvicorn connect_mysql:app --reload



