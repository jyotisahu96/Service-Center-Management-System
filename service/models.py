from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Device(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    device_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    problem = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_name






class Technician(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Available', 'Available'),
            ('Busy', 'Busy'),
            ('On Leave', 'On Leave'),
        ],
        default='Available'
    )

    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name







class ServiceRequest(models.Model):

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )

    technician = models.ForeignKey(
        Technician,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    problem = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ],
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('Received', 'Received'),
            ('Inspection', 'Inspection'),
            ('Repairing', 'Repairing'),
            ('Ready', 'Ready'),
            ('Delivered', 'Delivered'),
        ],
        default='Received'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request #{self.id}"




class Invoice(models.Model):

    service_request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE
    )

    labor_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    parts_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    other_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('Unpaid', 'Unpaid'),
            ('Paid', 'Paid'),
        ],
        default='Unpaid'
    )

    def __str__(self):
        return f"Invoice #{self.id}"





class Payment(models.Model):

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('Cash', 'Cash'),
            ('UPI', 'UPI'),
            ('Card', 'Card'),
        ]
    )
    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    payment_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Successful', 'Successful'),
            ('Pending', 'Pending'),
            ('Failed', 'Failed'),
        ],
        default='Successful'
    )
    def __str__(self):
        return f"Payment #{self.id}"



class Notification(models.Model):

    title = models.CharField(max_length=200)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title