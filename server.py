from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS

# Sample product data (you can expand this list as needed)
products = [
    {
        'id': 1,
        'name': 'Laptop XYZ',
        'price': 999.99,
        'description': 'A high-performance laptop with 16GB RAM and 512GB SSD.',
        'image_url': 'https://via.placeholder.com/150'
    },
    {
        'id': 2,
        'name': 'Smartphone ABC',
        'price': 599.99,
        'description': 'A sleek smartphone with a 6.5-inch display and a 48MP camera.',
        'image_url': 'https://via.placeholder.com/150'
    },
    {
        'id': 3,
        'name': 'Headphones 123',
        'price': 199.99,
        'description': 'Noise-cancelling over-ear headphones with great sound quality.',
        'image_url': 'https://via.placeholder.com/150'
    }
]

# Simulating an order database
orders = {}

# Sample route for testing
@app.route('/')
def home():
    return 'Welcome to the AI Shopping Assistant!'

# Chat route (example)
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    # Extract the user's message
    user_message = data.get('message', '').lower()

    # AI's response logic
    if any(greeting in user_message for greeting in ['hello', 'hi', 'good morning', 'hey']):
        ai_reply = "Hello! How can I assist you with your shopping today?"
    elif "order" in user_message or "buy" in user_message:
        ai_reply = "Sure! What product would you like to order?"
    elif "shipping" in user_message or "deliver" in user_message:
        ai_reply = "I can assist with your shipping! Could you please provide your address?"
    elif "track" in user_message or "status" in user_message:
        order_number = data.get('order_number', None)
        if order_number and order_number in orders:
            order = orders[order_number]
            ai_reply = f"Your order {order_number} is {order['status']}. We are processing it."
        else:
            ai_reply = "Please provide a valid order number to track."
    elif "bill" in user_message or "total" in user_message:
        # Calculate total for the user's order
        order_id = random.randint(1000, 9999)  # Generate a random order ID
        order_items = data.get('order_items', [])
        total_price = sum([item['price'] * item['quantity'] for item in order_items])
        
        # Store order
        orders[order_id] = {
            'items': order_items,
            'total': total_price,
            'status': 'Being Processed'
        }
        
        ai_reply = f"Your order has been placed successfully. Your order ID is {order_id}. The total bill is ${total_price:.2f}."
    elif "products" in user_message or "product" in user_message:
        # Display product suggestions
        ai_reply = "Here are some products you might like:\n"
        for product in products:
            ai_reply += f"\n{product['name']} - ${product['price']}\n{product['description']}\n"
        ai_reply += "\nWould you like to place an order?"
    else:
        ai_reply = f"Sorry, I didn't quite understand that. You said: {user_message}. Can I help with something related to orders or shipping?"

    # Respond with AI's message
    return jsonify({'message': ai_reply})

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
