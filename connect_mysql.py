import mysql.connector
import json
import pprint
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Shipping_Data(BaseModel):
    order_id: str
    customer_name: str
    region: str
    shipping_address: str
    weight_kg: float
    shipping_cost_usd: float
    status: str
    order_date: str
    delivery_date: str

connection = mysql.connector.connect(
    user='root',
    password='367676',
    host='localhost',
    database='testdb'
)

cursor = connection.cursor()
print("✅ Connection to database successfully.")

with open("data.json", "r") as file:
    records = json.load(file)
def wholedata():
    cursor.execute("DROP TABLE IF EXISTS ShippingData;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ShippingData (
        id INT AUTO_INCREMENT PRIMARY KEY,
        order_id VARCHAR(20),
        customer_name VARCHAR(100),
        region VARCHAR(50),
        shipping_address TEXT,
        weight_kg FLOAT,
        shipping_cost_usd DECIMAL(10,2),
        status VARCHAR(20),
        order_date DATE,
        delivery_date DATE
    );
    """)

    for record in records:
        cursor.execute("""
            INSERT INTO ShippingData 
            (order_id, customer_name, region, shipping_address, weight_kg, shipping_cost_usd, status, order_date, delivery_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            record["order_id"],
            record["customer_name"],
            record["region"],
            record["shipping_address"],
            record["weight_kg"],
            record["shipping_cost_usd"],
            record["status"],
            record["order_date"],
            record["delivery_date"]
        ))

    connection.commit()
    print("Order data inserted successfully!")
    cursor.execute("SELECT * FROM ShippingData;")
    rows = cursor.fetchall()
    for row in rows:
        pprint.pprint(row)

    cursor.close()
    connection.close()
    return {"message: Data Inserted Successfully"}

@app.get("/getUsingOrderid/{_id}")
def getDataByOrderId(_id):
    connection = mysql.connector.connect(
    user='root',
    password='367676',
    host='localhost',
    database='testdb')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM ShippingData WHERE order_id = "{_id}"')
    res=list(cursor)
    cursor.close()
    connection.close()
    return {"Data":res}


@app.get("/customer-data/{_region}")
def getDataRegion(_region):
    connection = mysql.connector.connect(
    user='root',
    password='367676',
    host='localhost',
    database='testdb')
    cursor = connection.cursor()
    cursor.execute(f'SELECT customer_name FROM ShippingData WHERE region = "{_region}";')
    customer_names=list(cursor)
    cursor.close()
    connection.close()
    return {"Data":customer_names}
    
@app.put("/insert_data/")
def insert_data(_shipping:Shipping_Data):
    connection = mysql.connector.connect(
        user='root',
        password='367676',
        host='localhost',
        database='testdb')
    cursor = connection.cursor()
    query = """
        INSERT INTO ShippingData 
        (order_id, customer_name, region, shipping_address, weight_kg, shipping_cost_usd, status, order_date, delivery_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        _shipping.order_id,
        _shipping.customer_name,
        _shipping.region,
        _shipping.shipping_address,
        _shipping.weight_kg,
        _shipping.shipping_cost_usd,
        _shipping.status,
        _shipping.order_date,
        _shipping.delivery_date
    )

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Data inserted successfully"}


@app.post("/post_data/{_order_id}")
def update_data(_order_id, updated_dt:Shipping_Data):
    connection = mysql.connector.connect(
        user='root',
        password='367676',
        host='localhost',
        database='testdb')
    cursor = connection.cursor()
    query = """
        UPDATE ShippingData
        SET 
            customer_name = %s,
            region = %s,
            shipping_address = %s,
            weight_kg = %s,
            shipping_cost_usd = %s,
            status = %s,
            order_date = %s,
            delivery_date = %s
        WHERE order_id = %s;
    """
    values = (
        updated_dt.order_id,
        updated_dt.customer_name,
        updated_dt.region,
        updated_dt.shipping_address,
        updated_dt.weight_kg,
        updated_dt.shipping_cost_usd,
        updated_dt.status,
        updated_dt.order_date,
        updated_dt.delivery_date
    )

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Data Updated successfully"}


@app.delete("/delete_data/{_order_id}")
def deleteData(_order_id):
    connection = mysql.connector.connect(
    user='root',
    password='367676',
    host='localhost',
    database='testdb')
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM ShippingData WHERE order_id = "{_order_id}";')
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message: Deleted Successfully"}

connection.close()

# Execution in ubuntu:
# 1.activate virtual environment
# 2.python3 connect_mysql.py if we want to move to sql do it as below mentioned

# execution in SQL
# 1.mysql -u root -p
# 2.SHOW DATABASES;
# 3.USE testdb;
# 4.SHOW TABLES;
# 5.SELECT * FROM ShippingData;

# SELECT * FROM ShippingData
# WHERE order_id=_order_id;


# SQL quries
# 1. SELECT * FROM ShippingData WHERE order_id="ORD1038";
# 2. SELECT * FROM ShippingData WHERE region="Australia";
# 3. INSERT INTO ShippingData 
# VALUES (NULL, 'ORD1005', 'John Doe', 'India', 'Bangalore, KA', 2.5, 45.00, 'Delivered', '2025-10-01', '2025-10-05');
# 4. UPDATE ShippingData SET status = 'Delivered', delivery_date = '2025-10-29' WHERE order_id = 'ORD1005';
# 5. DELETE FROM ShippingData WHERE order_id = 'ORD1005';
