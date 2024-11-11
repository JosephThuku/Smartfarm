from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.conf import settings
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from africastalking import AfricasTalkingGateway
from datetime import datetime
import logging

# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FarmerSignUpForm
from .models import Farmer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate

def login_view(request):
    return render(request, 'users/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login the user
    else:
        form = FarmerSignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})

# farm management
@login_required
def dashboard_view(request):
    # @Todo by @Joe and Josephine to implement the logic for the dashboard which wiil:
    # 1. Get the farmer details
    # 2. Get the farm details
    # 3. Get the latest sensor data
    # 4. Get the weather forecast
    # 5. Get the crop recommendations
    return render(request, 'users/landing.html')

#farm_management rendering
def farm_management_view(request):
    
    """farm management logic will be implemented
    here"""

    return render(request, 'users/farm_management.html')

# from .models import Farmer, Farm, SensorData
# from .forms import FarmerRegistrationForm, FarmProfileForm
# from .services import (
#     FarmManagementSystem,
#     EnvironmentalMonitor,
#     FarmAdvisor,
#     AuthenticationService
# )

# logger = logging.getLogger(__name__)

# # Web Views
# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = "farm/dashboard.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         farmer = self.request.user.farmer
        
#         # Initialize services
#         farm_manager = FarmManagementSystem(settings.OPENAI_API_KEY)
#         env_monitor = EnvironmentalMonitor(farmer.farm.id)
        
#         # Get latest sensor data
#         latest_sensor_data = SensorData.objects.filter(
#             farm=farmer.farm
#         ).latest('timestamp')
        
#         context.update({
#             'farmer': farmer,
#             'farm': farmer.farm,
#             'sensor_data': latest_sensor_data,
#             'weather_forecast': self._get_weather_forecast(farmer.farm.location),
#             'crop_recommendations': farm_manager.get_crop_recommendations(
#                 farm_data=farmer.farm.to_dict(),
#                 soil_data=latest_sensor_data.soil_data,
#                 weather_data=self._get_weather_data(farmer.farm.location)
#             )
#         })
#         return context
    
#     def _get_weather_forecast(self, location):
#         # Implementation for weather API integration
#         pass
    
#     def _get_weather_data(self, location):
#         # Implementation for historical weather data
#         pass

# class FarmerRegistrationView(CreateView):
#     template_name = "farm/registration.html"
#     form_class = FarmerRegistrationForm
#     success_url = "/dashboard/"
    
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         # Send welcome message
#         self._send_welcome_sms(form.instance)
#         return response
    
#     def _send_welcome_sms(self, farmer):
#         try:
#             gateway = AfricasTalkingGateway(
#                 settings.AT_USERNAME,
#                 settings.AT_API_KEY
#             )
#             message = f"Welcome to Smart Farm, {farmer.full_name}! Your account has been created successfully."
#             gateway.sendMessage(farmer.phone_number, message)
#         except Exception as e:
#             logger.error(f"Failed to send welcome SMS: {str(e)}")

# # USSD Views
# class USSDHandler(APIView):
#     def post(self, request):
#         session_id = request.data.get('sessionId')
#         service_code = request.data.get('serviceCode')
#         phone_number = request.data.get('phoneNumber')
#         text = request.data.get('text')
        
#         response = self._process_ussd_input(session_id, text, phone_number)
#         return Response({
#             'response': response,
#             'action': 'continue'
#         }, status=status.HTTP_200_OK)
    
#     def _process_ussd_input(self, session_id, text, phone_number):
#         # Handle USSD menu navigation
#         if not text:
#             return self._get_main_menu()
            
#         user_input = text.split('*')
#         level = len(user_input)
        
#         if level == 1:
#             return self._handle_main_menu_selection(user_input[0])
#         elif level == 2:
#             return self._handle_submenu_selection(user_input)
            
#         return "Invalid input"
    
#     def _get_main_menu(self):
#         return "\n".join([
#             "Welcome to Smart Farm",
#             "1. Weather Updates",
#             "2. Crop Recommendations",
#             "3. Market Prices",
#             "4. Report Issue",
#             "5. Settings"
#         ])
    
#     def _handle_main_menu_selection(self, selection):
#         menu_handlers = {
#             "1": self._get_weather_updates,
#             "2": self._get_crop_recommendations,
#             "3": self._get_market_prices,
#             "4": self._get_issue_report_menu,
#             "5": self._get_settings_menu
#         }
#         handler = menu_handlers.get(selection)
#         return handler() if handler else "Invalid selection"
    
#     def _handle_submenu_selection(self, inputs):
#         main_selection = inputs[0]
#         sub_selection = inputs[1]
        
#         # Implementation for submenu handling
#         pass
    
#     def _get_weather_updates(self):
#         # Implementation for weather updates
#         pass
    
#     def _get_crop_recommendations(self):
#         # Implementation for crop recommendations
#         pass
    
#     def _get_market_prices(self):
#         # Implementation for market prices
#         pass
    
#     def _get_issue_report_menu(self):
#         # Implementation for issue reporting
#         pass
    
#     def _get_settings_menu(self):
#         # Implementation for settings
#         pass

# # API Views for AJAX requests
# class SensorDataView(LoginRequiredMixin, APIView):
#     def get(self, request):
#         try:
#             farm = request.user.farmer.farm
#             latest_data = SensorData.objects.filter(
#                 farm=farm
#             ).order_by('-timestamp')[:24]  # Last 24 readings
            
#             return Response({
#                 'sensor_data': [data.to_dict() for data in latest_data]
#             }, status=status.HTTP_200_OK)
#         except Exception as e:
#             logger.error(f"Error fetching sensor data: {str(e)}")
#             return Response({
#                 'error': 'Failed to fetch sensor data'
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class FarmAnalyticsView(LoginRequiredMixin, APIView):
#     def get(self, request):
#         try:
#             farm = request.user.farmer.farm
#             env_monitor = EnvironmentalMonitor(farm.id)
            
#             # Get latest sensor data
#             latest_sensor_data = SensorData.objects.filter(
#                 farm=farm
#             ).latest('timestamp')
            
#             # Get AI analysis
#             analysis = env_monitor.analyze_conditions(latest_sensor_data)
            
#             return Response({
#                 'analysis': analysis
#             }, status=status.HTTP_200_OK)
#         except Exception as e:
#             logger.error(f"Error generating farm analytics: {str(e)}")
#             return Response({
#                 'error': 'Failed to generate analytics'
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FarmerSignUpView(CreateView):
    model = Farmer
    form_class = FarmerSignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('farm:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Welcome to SmartFarm! Please complete your profile.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class CustomLoginView(LoginView):
    print(f"Hello from the custom login view")
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, 'Login successful! Redirecting to dashboard.')
        return super().form_valid(form)  # Redirects to the dashboard automatically

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)
        
    def get_success_url(self):
        return reverse_lazy('farm:dashboard')

    def get_user(self):
        # Override to authenticate using the Farmer model
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        print(f"Hello the username is: {username} and the password is : {password}")
        return authenticate(self.request, username=username, password=password)

from transformers import pipeline
from django.http import JsonResponse
from django.views import View
from django.conf import settings

# Initialize the Hugging Face model for text generation
# You can choose a model that fits your needs, e.g., "gpt2" or "distilgpt2"
chatbot = pipeline("text-generation", model="gpt2")  # or any other model you want to use

class OpenAIChatView(View):
    def post(self, request):
        user_input = request.POST.get('user_input')
        
        try:
            # Generate a response using the Hugging Face model
            response = chatbot(user_input, max_length=100, num_return_sequences=1)
            ai_response = response[0]['generated_text']
            return JsonResponse({'response': ai_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class GenerateFarmInsightsView(View):
    def post(self, request):
        # Sample farm data
        sample_farm_data = {
            "crop_type": "corn",
            "area": "50 acres",
            "soil_type": "loamy",
            "irrigation": "drip",
            "fertilizer_used": "NPK",
            "pests": ["aphids", "corn borers"],
            "weather_conditions": "sunny with occasional rain",
        }

        # Construct the prompt for the AI
        prompt = (
            "You are an agriculture expert. Based on the following farm data, "
            "provide insights and recommendations:\n"
            f"Crop Type: {sample_farm_data['crop_type']}\n"
            f"Area: {sample_farm_data['area']}\n"
            f"Soil Type: {sample_farm_data['soil_type']}\n"
            f"Irrigation Method: {sample_farm_data['irrigation']}\n"
            f"Fertilizer Used: {sample_farm_data['fertilizer_used']}\n"
            f"Pests: {', '.join(sample_farm_data['pests'])}\n"
            f"Weather Conditions: {sample_farm_data['weather_conditions']}\n"
            "Provide actionable insights and recommendations."
        )

        try:
            # Generate a response using the Hugging Face model
            response = chatbot(prompt, max_length=150, num_return_sequences=1)
            ai_response = response[0]['generated_text']
            return JsonResponse({'response': ai_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)