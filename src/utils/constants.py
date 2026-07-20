"""
Project Constants
"""

# =============================================================================
# Target Variable
# =============================================================================

TARGET = "delivery_days"

# =============================================================================
# Machine Learning Features
# =============================================================================

FEATURE_COLUMNS = [
    "payment_value",
    "payment_installments",
    "purchase_month",
    "purchase_day",
    "purchase_weekday",
    "purchase_hour",
    "approval_hours",
]

# =============================================================================
# Date Columns
# =============================================================================

DATE_COLUMNS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

# =============================================================================
# KPI Labels
# =============================================================================

KPI_REVENUE = "Revenue"
KPI_ORDERS = "Orders"
KPI_CUSTOMERS = "Customers"
KPI_SELLERS = "Sellers"
KPI_RATING = "Average Rating"
KPI_DELIVERY = "Average Delivery"

# =============================================================================
# Dashboard Pages
# =============================================================================

DASHBOARD_PAGES = [
    "Executive Dashboard",
    "Sales Analytics",
    "Customer Analytics",
    "Logistics",
    "Machine Learning",
]