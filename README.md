# Django Payment Gateway and Session System

A simple Django-based payment gateway and session management system. It allows users to add products to their cart, manage the cart session, and proceed with checkout and mock payment.

## Features

- Add, update, and remove products from the cart.
- Cart data persisted in user session.
- Simulated payment gateway for processing mock payments.
- Checkout and order summary views.

## Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/django-payment-gateway.git
cd django-payment-gateway


2. Install Dependencies
pip install -r requirements.txt

3. Run Migrations
python manage.py migrate

4. Start the Server
python manage.py runserver
```

Access the app at http://127.0.0.1:8000/.

Configuration

Sessions: Cart data is stored in the Django session.

Payment Gateway: Currently a mock; integrate real gateways like Stripe/PayPal by modifying the checkout view.

How it Works

Add to Cart: Products are added to the cart and stored in the session.

Checkout: Users review cart items and proceed to payment.

Payment: A mock payment is processed upon checkout.

## Structure
```
/cart             # Cart functionality
/store            # Product and order models
/payment          # Payment gateway integration
/templates        # HTML templates
/static           # Static files
manage.py         # Project management
requirements.txt  # Dependencies



