from django.shortcuts import render
from django.views.generic import View

class CheckoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class TestimonialView(View):
    def get(self, request):
        return render(request, 'testimonial.html')
