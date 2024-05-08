# Vendor Management System

## Overview

This is a Django REST framework project for managing vendors, purchase orders, and evaluating vendor performance metrics.

# to generate superuser token for apis.
```bash
python manage.py createsuperuser

python manage.py drf_create_token <username> # use superuser username
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Arvindsain/vendor_system.git
cd vendor_management_system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the API.

## API Endpoints

### 1. Vendor Profile Management

# Note: vendor code is auto created.

- **Create Vendor:**
  - Method: POST
  - URL: `/api/vendors/`
  - Payload: Provide vendor details in the request body.

- **List All Vendors:**
  - Method: GET
  - URL: `/api/vendors/`

- **Retrieve Vendor Details:**
  - Method: GET
  - URL: `/api/vendors/{vendor_id}/`

- **Update Vendor Details:**
  - Method: PUT
  - URL: `/api/vendors/{vendor_id}/`
  - Payload: Provide updated vendor details in the request body.

- **Delete Vendor:**
  - Method: DELETE
  - URL: `/api/vendors/{vendor_id}/`

- **Retrieve Vendor Performance Metrics:**
  - Method: GET
  - URL: `/api/vendors/{vendor_id}/performance/`

- **Get Historical performance instances of vendor or all:**
  - This api is read only.
  - Method: GET
  - URL: for particular vendor: `/vendor/historical_performance/?vendor_id={vendor_id}`, to get all vendors: `/vendor/historical_performance/`

### 2. Purchase Order Tracking

# Note: po number is auto created.

- **Create Purchase Order:**
  - Method: POST
  - URL: `/api/purchase_orders/`
  - Payload: Provide purchase order details in the request body.

- **List All Purchase Orders:**
  - Method: GET
  - URL: `/api/purchase_orders/`

- **Retrieve Purchase Order Details:**
  - Method: GET
  - URL: `/api/purchase_orders/{po_id}/`

- **Update Purchase Order:**
  - Method: PUT
  - URL: `/api/purchase_orders/{po_id}/`
  - Payload: Provide updated purchase order details in the request body.

- **Delete Purchase Order:**
  - Method: DELETE
  - URL: `/api/purchase_orders/{po_id}/`

- **Acknowledge Purchase Order:**
  - Method: POST
  - URL: `/api/purchase_orders/{po_id}/acknowledge/`
  - This endpoint will update acknowledgment_date and trigger the recalculation of average_response_time 