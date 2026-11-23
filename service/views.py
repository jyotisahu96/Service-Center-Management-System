from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db import models

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 

from .serializers import (
    CustomerSerializer,
    DeviceSerializer,
    TechnicianSerializer,
    ServiceRequestSerializer,
    InvoiceSerializer,
    PaymentSerializer
)
from .models import Customer, Device, Technician, ServiceRequest,Invoice,Payment,Notification


def home(request):
    return redirect('dashboard')

# =========================
    # CUSTOMER
    # =========================


@login_required
@permission_required('service.view_customer', raise_exception=True)
def customer_list(request):

    search = request.GET.get('search', '')

    if search:
        customers = Customer.objects.filter(
            name__icontains=search
        )
    else:
        customers = Customer.objects.all()

    # Pagination
    paginator = Paginator(customers, 5)

    page_number = request.GET.get('page')

    customers = paginator.get_page(page_number)

    return render(request, 'service/customer_list.html', {
        'customers': customers,
        'search': search
    })



@login_required
@permission_required('service.add_customer', raise_exception=True)
def customer_add(request):

    if request.method == 'POST':

        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']

        Customer.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address
        )

        return redirect('customer_list')

    return render(request, 'service/customer_form.html')


@login_required
@permission_required('service.view_customer', raise_exception=True)
def customer_detail(request, id):

    customer = Customer.objects.get(id=id)

    return render(request, 'service/customer_detail.html', {
        'customer': customer
    })



@login_required
@permission_required('service.change_customer', raise_exception=True)
def customer_edit(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == 'POST':

        customer.name = request.POST['name']
        customer.phone = request.POST['phone']
        customer.email = request.POST['email']
        customer.address = request.POST['address']

        customer.save()

        return redirect('customer_detail', id=id)

    return render(request, 'service/customer_form.html', {
        'customer': customer
    })




@login_required
@permission_required('service.delete_customer', raise_exception=True)
def customer_delete(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == 'POST':

        customer.delete()

        return redirect('customer_list')

    return render(request, 'service/customer_confirm_delete.html', {
        'customer': customer
    })



    # =========================
    # DEVICE
    # =========================
@login_required
@permission_required('service.view_device', raise_exception=True)

def device_list(request):

    devices = Device.objects.all()

    return render(request, 'service/device_list.html', {
        'devices': devices
    })




@login_required
@permission_required('service.add_device', raise_exception=True)
def device_add(request):
    customers = Customer.objects.all()

    if request.method == 'POST':

        customer_id = request.POST['customer']
        device_name = request.POST['device_name']
        brand = request.POST['brand']
        model_number = request.POST['model_number']
        serial_number = request.POST['serial_number']
        problem = request.POST['problem']

        customer = Customer.objects.get(id=customer_id)

        Device.objects.create(
            customer=customer,
            device_name=device_name,
            brand=brand,
            model_number=model_number,
            serial_number=serial_number,
            problem=problem
        )

        return redirect('device_list')

    return render(request, 'service/device_form.html', {
        'customers': customers
    })



@login_required
@permission_required('service.view_device', raise_exception=True)

def device_detail(request, id):

    device = Device.objects.get(id=id)

    return render(request, 'service/device_detail.html', {
        'device': device
    })


@login_required
@permission_required('service.change_device', raise_exception=True)
def device_edit(request, id):

    device = Device.objects.get(id=id)
    customers = Customer.objects.all()
    if request.method == 'POST':
        customer_id = request.POST['customer']
        device.customer = Customer.objects.get(id=customer_id)

        device.device_name = request.POST['device_name']
        device.brand = request.POST['brand']
        device.model_number = request.POST['model_number']
        device.serial_number = request.POST['serial_number']
        device.problem = request.POST['problem']

        device.save()

        return redirect('device_detail', id=id)
    return render(request, 'service/device_form.html', {
        'device': device,
        'customers': customers
    })


@login_required
@permission_required('service.delete_device', raise_exception=True)
def device_delete(request, id):

    device = Device.objects.get(id=id)

    if request.method == 'POST':

        device.delete()

        return redirect('device_list')

    return render(request, 'service/device_confirm_delete.html', {
        'device': device
    })




# =========================
# TECHNICIAN
# =========================

def technician_list(request):
    technicians = Technician.objects.all()

    return render(
        request,
        'service/technician_list.html',
        {
            'technicians': technicians
        }
    )


def technician_add(request):

    if request.method == 'POST':

        Technician.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            specialization=request.POST['specialization'],
            experience=request.POST['experience'],
            status=request.POST['status']
        )

        return redirect('technician_list')

    return render(
        request,
        'service/technician_form.html'
    )


def technician_detail(request, id):

    technician = Technician.objects.get(id=id)

    return render(
        request,
        'service/technician_detail.html',
        {
            'technician': technician
        }
    )


def technician_edit(request, id):

    technician = Technician.objects.get(id=id)

    if request.method == 'POST':

        technician.name = request.POST['name']
        technician.phone = request.POST['phone']
        technician.email = request.POST['email']
        technician.specialization = request.POST['specialization']
        technician.experience = request.POST['experience']
        technician.status = request.POST['status']

        technician.save()

        return redirect(
            'technician_detail',
            id=id
        )

    return render(
        request,
        'service/technician_form.html',
        {
            'technician': technician
        }
    )


def technician_delete(request, id):

    technician = Technician.objects.get(id=id)

    if request.method == 'POST':

        technician.delete()

        return redirect('technician_list')

    return render(
        request,
        'service/technician_confirm_delete.html',
        {
            'technician': technician
        }
    )

# =====================================
# SERVICE REQUEST
# =====================================
@login_required
@permission_required('service.view_servicerequest', raise_exception=True)

def service_request_list(request):

    requests = ServiceRequest.objects.all().order_by('-created_at')

    return render(
        request,
        'service/service_request_list.html',
        {
            'requests': requests
        }
    )






@login_required
def service_request_add(request):
    devices = Device.objects.all()
    technicians = Technician.objects.all()

    if request.method == 'POST':
        device_id = request.POST['device']
        technician_id = request.POST.get('technician')
        problem = request.POST['problem']
        priority = request.POST['priority']
        status = request.POST['status']

        device = Device.objects.get(id=device_id)

        technician = None

        if technician_id:
            technician = Technician.objects.get(id=technician_id)

        service_request = ServiceRequest.objects.create(
            device=device,
            technician=technician,
            problem=problem,
            priority=priority,
            status=status
        )

        # Automatic notification
        Notification.objects.create(
            title='New Service Request',
            message=f'New service request created for {device.device_name}. Status: {status}.'
        )

        return redirect('service_request_list')

    return render(
        request,
        'service/service_request_form.html',
        {
            'devices': devices,
            'technicians': technicians
        }
    )


@login_required
@permission_required('service.view_servicerequest', raise_exception=True)

def service_request_detail(request, id):

    service_request = ServiceRequest.objects.get(
        id=id
    )

    return render(
        request,
        'service/service_request_detail.html',
        {
            'service_request': service_request
        }
    )



@login_required
def service_request_edit(request, id):
    service_request = ServiceRequest.objects.get(id=id)

    devices = Device.objects.all()
    technicians = Technician.objects.all()

    if request.method == 'POST':

        old_status = service_request.status

        device_id = request.POST['device']
        technician_id = request.POST.get('technician')

        service_request.device = Device.objects.get(id=device_id)

        if technician_id:
            service_request.technician = Technician.objects.get(id=technician_id)
        else:
            service_request.technician = None

        service_request.problem = request.POST['problem']
        service_request.priority = request.POST['priority']
        service_request.status = request.POST['status']

        service_request.save()

        # Automatic notification when status changes
        if old_status != service_request.status:

            Notification.objects.create(
                title='Service Request Status Updated',
                message=(
                    f'Request #{service_request.id} for '
                    f'{service_request.device.device_name} '
                    f'changed from {old_status} to '
                    f'{service_request.status}.'
                )
            )

        return redirect(
            'service_request_detail',
            id=id
        )

    return render(
        request,
        'service/service_request_form.html',
        {
            'service_request': service_request,
            'devices': devices,
            'technicians': technicians
        }
    )




@login_required
@permission_required('service.delete_servicerequest', raise_exception=True)

def service_request_delete(request, id):

    service_request = ServiceRequest.objects.get(
        id=id
    )

    if request.method == 'POST':

        service_request.delete()

        return redirect(
            'service_request_list'
        )

    return render(
        request,
        'service/service_request_confirm_delete.html',
        {
            'service_request': service_request
        }
    )
# =====================================
# Invoice Requset
# =====================================
@login_required
@permission_required('service.view_invoice', raise_exception=True)

def invoice_list(request):
    invoices = Invoice.objects.all().order_by('-created_at')

    return render(
        request,
        'service/invoice_list.html',
        {'invoices': invoices}
    )

@login_required
@permission_required('service.add_invoice', raise_exception=True)

def invoice_add(request):

    service_requests = ServiceRequest.objects.all()

    if request.method == 'POST':

        service_request_id = request.POST['service_request']

        labor_charge = float(request.POST.get('labor_charge') or 0)
        parts_charge = float(request.POST.get('parts_charge') or 0)
        other_charge = float(request.POST.get('other_charge') or 0)
        discount = float(request.POST.get('discount') or 0)
        tax = float(request.POST.get('tax') or 0)

        total_amount = (
            labor_charge
            + parts_charge
            + other_charge
            + tax
            - discount
        )

        service_request = ServiceRequest.objects.get(
            id=service_request_id
        )

        Invoice.objects.create(
            service_request=service_request,
            labor_charge=labor_charge,
            parts_charge=parts_charge,
            other_charge=other_charge,
            discount=discount,
            tax=tax,
            total_amount=total_amount
        )

        return redirect('invoice_list')

    return render(
        request,
        'service/invoice_form.html',
        {'service_requests': service_requests}
    )

@login_required
@permission_required('service.view_invoice', raise_exception=True)

def invoice_detail(request, id):

    invoice = Invoice.objects.get(id=id)

    return render(
        request,
        'service/invoice_detail.html',
        {'invoice': invoice}
    )

@login_required
@permission_required('service.change_invoice', raise_exception=True)

def invoice_edit(request, id):

    invoice = Invoice.objects.get(id=id)

    service_requests = ServiceRequest.objects.all()

    if request.method == 'POST':

        invoice.service_request = ServiceRequest.objects.get(
            id=request.POST['service_request']
        )

        invoice.labor_charge = float(
            request.POST.get('labor_charge') or 0
        )

        invoice.parts_charge = float(
            request.POST.get('parts_charge') or 0
        )

        invoice.other_charge = float(
            request.POST.get('other_charge') or 0
        )

        invoice.discount = float(
            request.POST.get('discount') or 0
        )

        invoice.tax = float(
            request.POST.get('tax') or 0
        )

        invoice.total_amount = (
            invoice.labor_charge
            + invoice.parts_charge
            + invoice.other_charge
            + invoice.tax
            - invoice.discount
        )

        invoice.status = request.POST['status']

        invoice.save()

        return redirect('invoice_detail', id=id)

    return render(
        request,
        'service/invoice_form.html',
        {
            'invoice': invoice,
            'service_requests': service_requests
        }
    )


@login_required
@permission_required('service.delete_invoice', raise_exception=True)

def invoice_delete(request, id):

    invoice = Invoice.objects.get(id=id)

    if request.method == 'POST':
        invoice.delete()

        return redirect('invoice_list')

    return render(
        request,
        'service/invoice_confirm_delete.html',
        {'invoice': invoice}
    )
# =====================================
# PAYMENT
# ====================================

@login_required
@permission_required('service.view_payment', raise_exception=True)

def payment_list(request):
    payments =Payment.objects.all().order_by('-payment_date')

    return render(
        request,
        'service/payment_list.html',
        {'payments': payments}
    )

@login_required
@permission_required('service.add_payment', raise_exception=True)

def payment_add(request):

    invoices = Invoice.objects.all()

    if request.method == 'POST':

        invoice_id = request.POST['invoice']

        payment_method = request.POST['payment_method']

        transaction_id = request.POST.get('transaction_id')

        amount = request.POST['amount']

        status = request.POST['status']

        invoice = Invoice.objects.get(id=invoice_id)

        Payment.objects.create(
            invoice=invoice,
            payment_method=payment_method,
            transaction_id=transaction_id,
            amount=amount,
            status=status
        )

        # Payment successful hone par invoice ko Paid kar do
        if status == 'Successful':
            invoice.status = 'Paid'
            invoice.save()

        return redirect('payment_list')

    return render(
        request,
        'service/payment_form.html',
        {'invoices': invoices}
    )

@login_required
@permission_required('service.view_payment', raise_exception=True)

def payment_detail(request, id):

    payment = Payment.objects.get(id=id)

    return render(
        request,
        'service/payment_detail.html',
        {'payment': payment}
    )

@login_required
@permission_required('service.delete_payment', raise_exception=True)

def payment_delete(request, id):

    payment = Payment.objects.get(id=id)

    if request.method == 'POST':
        payment.delete()

        return redirect('payment_list')

    return render(
        request,
        'service/payment_confirm_delete.html',
        {'payment': payment}
    )

# =====================================
# DASHBOARD
# ====================================


@login_required
def dashboard(request):

    total_customers = Customer.objects.count()
    total_devices = Device.objects.count()
    total_technicians = Technician.objects.count()
    total_requests = ServiceRequest.objects.count()
    total_invoices = Invoice.objects.count()

    paid_invoices = Invoice.objects.filter(
        status='Paid'
    ).count()

    total_revenue = sum(
        invoice.total_amount
        for invoice in Invoice.objects.filter(status='Paid')
    )

    recent_requests = ServiceRequest.objects.all().order_by(
        '-created_at'
    )[:5]

    return render(
        request,
        'service/dashboard.html',
        {
            'total_customers': total_customers,
            'total_devices': total_devices,
            'total_technicians': total_technicians,
            'total_requests': total_requests,
            'total_invoices': total_invoices,
            'paid_invoices': paid_invoices,
            'total_revenue': total_revenue,
            'recent_requests': recent_requests,
        }
    )



@login_required
def notification_list(request):
    notifications = Notification.objects.all().order_by('-created_at')

    return render(
        request,
        'service/notification_list.html',
        {
            'notifications': notifications
        }
    )


@login_required
def reports(request):

    total_customers = Customer.objects.count()
    total_devices = Device.objects.count()
    total_technicians = Technician.objects.count()
    total_requests = ServiceRequest.objects.count()
    total_invoices = Invoice.objects.count()

    total_revenue = Payment.objects.filter(
        status='Successful'
    ).aggregate(total=models.Sum('amount'))['total'] or 0

    received = ServiceRequest.objects.filter(
        status='Received'
    ).count()

    inspection = ServiceRequest.objects.filter(
        status='Inspection'
    ).count()

    repairing = ServiceRequest.objects.filter(
        status='Repairing'
    ).count()

    ready = ServiceRequest.objects.filter(
        status='Ready'
    ).count()

    delivered = ServiceRequest.objects.filter(
        status='Delivered'
    ).count()

    return render(
        request,
        'service/reports.html',
        {
            'total_customers': total_customers,
            'total_devices': total_devices,
            'total_technicians': total_technicians,
            'total_requests': total_requests,
            'total_invoices': total_invoices,
            'total_revenue': total_revenue,

            'received': received,
            'inspection': inspection,
            'repairing': repairing,
            'ready': ready,
            'delivered': delivered,
        }
    )


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customer_api(request):

    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
        

        



    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def device_api(request):

    devices = Device.objects.all()

    serializer = DeviceSerializer( 
        devices,
      many=True)
    
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def technician_api(request):

    technicians = Technician.objects.all()

    serializer = TechnicianSerializer(technicians, many=True)
    
    return Response(serializer.data)






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def service_request_api(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    serializer = ServiceRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def invoice_api(request):
    invoices = Invoice.objects.all().order_by('-created_at')
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_api(request):
    payments = Payment.objects.all().order_by('-payment_date')
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)