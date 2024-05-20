from django.urls import path
from .views import CheckOutView, TestimonialView, CustomersView

urlpatterns = [
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('testemonial/', TestimonialView.as_view(), name="testimonial"),
    path('customers/', CustomersView.as_view(), name="customers")
]