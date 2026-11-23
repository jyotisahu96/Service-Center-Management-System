from django.urls import path
from service import views

urlpatterns = [
     # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Home
    path('', views.home, name='home'),


     # CUSTOMER

    path('customers/', views.customer_list, name='customer_list'),

    path('customers/add/', views.customer_add, name='customer_add'),

    path('customers/<int:id>/', views.customer_detail, name='customer_detail'),

    path('customers/<int:id>/edit/', views.customer_edit, name='customer_edit'),

    path('customers/<int:id>/delete/', views.customer_delete, name='customer_delete'),


    



 # DEVICE
path('devices/', views.device_list, name='device_list'),

path('devices/add/', views.device_add, name='device_add'),

path('devices/<int:id>/', views.device_detail, name='device_detail'),

path('devices/<int:id>/edit/', views.device_edit, name='device_edit'),

path('devices/<int:id>/delete/', views.device_delete, name='device_delete'),


# Technician

path(
    'technicians/',
    views.technician_list,
    name='technician_list'
),

path(
    'technicians/add/',
    views.technician_add,
    name='technician_add'
),

path(
    'technicians/<int:id>/',
    views.technician_detail,
    name='technician_detail'
),

path(
    'technicians/<int:id>/edit/',
    views.technician_edit,
    name='technician_edit'
),

path(
    'technicians/<int:id>/delete/',
    views.technician_delete,
    name='technician_delete'
),


# =========================
# SERVICE REQUEST
# =========================

path(
    'requests/',
    views.service_request_list,
    name='service_request_list'
),

path(
    'requests/add/',
    views.service_request_add,
    name='service_request_add'
),

path(
    'requests/<int:id>/',
    views.service_request_detail,
    name='service_request_detail'
),

path(
    'requests/<int:id>/edit/',
    views.service_request_edit,
    name='service_request_edit'
),

path(
    'requests/<int:id>/delete/',
    views.service_request_delete,
    name='service_request_delete'
),

# =========================
# INVOICE REQUEST
# =========================


path('invoices/', views.invoice_list, name='invoice_list'),

path('invoices/add/', views.invoice_add, name='invoice_add'),

path('invoices/<int:id>/', views.invoice_detail, name='invoice_detail'),

path('invoices/<int:id>/edit/', views.invoice_edit, name='invoice_edit'),

path('invoices/<int:id>/delete/', views.invoice_delete, name='invoice_delete'),



# =========================
# Payments
# =========================

path('payments/', views.payment_list, name='payment_list'),

path('payments/add/', views.payment_add, name='payment_add'),

path('payments/<int:id>/', views.payment_detail, name='payment_detail'),

path('payments/<int:id>/delete/', views.payment_delete, name='payment_delete'),


# =========================
# notification
# =========================
   

    path(
        'notifications/',
        views.notification_list,
        name='notification_list'
    ),

# =========================
# Reports
# =========================

 path(
        'reports/',
        views.reports,
        name='reports'
    ),

# =========================
# API
# =========================

path(
    'api/customers/',
    views.customer_api,
    name='customer_api'
),
path(
    'api/devices/',
    views.device_api,
    name='device_api'
),
path(
    'api/technicians/',
    views.technician_api,
    name='technician_api'
),
path(
    'api/requests/',
    views.service_request_api,
    name='service_request_api'
),

path(
    'api/invoices/',
    views.invoice_api,
    name='invoice_api'
),

path(
    'api/payments/',
    views.payment_api,
    name='payment_api'
),
]

