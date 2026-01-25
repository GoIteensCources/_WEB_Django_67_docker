from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail

from order.forms import OrderForm
from order.models import Order

from django.core import validators
from django.core.exceptions import ValidationError


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form.errors)

        email_validator = validators.EmailValidator()
                
        if form.is_valid():
            try:
                email_validator(form.cleaned_data['email'])
            except ValidationError as e:
                form.add_error('email', 'Введіть коректну електронну адресу.')
                return render(request, 'order/order_form.html', {'form': form})

            order = form.save()
            print(order)

        # --- Email адміну ---
        subject_admin = f"Нове замовлення від {order.name}"
        message_admin = render_to_string('order/emails/order_notification.html', {'order': order})
        send_mail(
            subject=subject_admin,
            message='hello, admin!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            html_message=message_admin,
        )

        print('email sent to admin')
            
        # --- Email клієнту ---
        subject_client = "Дякуємо за ваше замовлення!"
        message_client = render_to_string('order/emails/order_confirmation.html', {'order': order})
        send_mail(
            subject_client,
            '',
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            html_message=message_client,
        )

        return redirect('order:order_thanks')
    
    form = OrderForm()
    return render(request, 'order/order_form.html', {'form': form})


def order_thanks(request):
    return render(request, 'order/order_thanks.html')


# ==========================================
def show_orders(request):
    
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})