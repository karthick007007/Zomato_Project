from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
app = Flask(__name__)


def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="zomato"
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/place_order", methods=["POST"])
def place_order():

    data = request.json

    cart = data["cart"]
    address = data["address"]

    conn = create_connection()
    cursor = conn.cursor()

    user_id = 1

    for item in cart:

        item_name = item["name"]
        quantity = item["quantity"]

        cursor.execute(
            "SELECT item_id FROM items WHERE item_name = %s",
            (item_name,)
        )

        result = cursor.fetchone()

        if result:
            item_id = result[0]

            cursor.execute(
                """
                INSERT INTO orders
                (user_id, item_id, quantity, delivery_address)
                VALUES (%s, %s, %s, %s)
                """,
                (user_id, item_id, quantity, address)
            )

            order_id = cursor.lastrowid

            cursor.execute(
                "SELECT price FROM items WHERE item_id = %s",
                (item_id,)
            )

            price = cursor.fetchone()[0]

            cursor.execute(
                """
                INSERT INTO order_items
                (order_id, item_id, quantity, price)
                VALUES (%s, %s, %s, %s)
                """,
                (order_id, item_id, quantity, price)
            )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "Order placed successfully!"

    } )

@app.route("/orders-page")
def orders_page():
    return render_template("orders.html")

# ADD THIS HERE
@app.route("/orders")
def get_orders():

    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            o.order_id,
            i.item_name,
            i.price,
            o.quantity,
            o.delivery_address,
            o.order_date
        FROM orders o
        JOIN items i
            ON o.item_id = i.item_id
        ORDER BY o.order_id DESC
    """)

    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(orders)

@app.route("/analytics-page")
def analytics_page():
    return render_template("analytics.html")


@app.route("/analytics/total-revenue")
def total_revenue():

    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT SUM(price * quantity) AS total_revenue
        FROM order_items
    """)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify({
        "total_revenue": result["total_revenue"] or 0
    })

@app.route("/analytics/revenue-by-item")
def revenue_by_item():

    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            i.item_name,
            SUM(oi.price * oi.quantity) AS total_revenue
        FROM order_items oi
        JOIN items i
            ON oi.item_id = i.item_id
        GROUP BY i.item_name
        ORDER BY total_revenue DESC
    """)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)

@app.route("/analytics/revenue-by-category")
def revenue_by_category():

    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            c.category_name,
            SUM(oi.price * oi.quantity) AS total_revenue
        FROM order_items oi
        JOIN items i
            ON oi.item_id = i.item_id
        JOIN categories c
            ON i.category_id = c.category_id
        GROUP BY c.category_name
        ORDER BY total_revenue DESC
    """)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)

@app.route("/analytics/revenue-by-payment")
def revenue_by_payment():

    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            payment_method,
            SUM(amount) AS total_revenue
        FROM payments
        GROUP BY payment_method
        ORDER BY total_revenue DESC
    """)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)