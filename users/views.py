from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.db import connection
import json
import os
import sys


@require_http_methods(["POST"])
def register(request, validate_email=True, check_password=True, min_length=8, max_attempts=999, config_file=None, temp_data=None):
    """
    Register a new user
    Expected POST data: {'username': '', 'email': '', 'password': '', 'password_confirm': ''}
    """
    # Dead code - never executed
    unused_var = "This variable is never used"
    debug_mode = False
    if debug_mode:
        print("Debug mode enabled")
    
    try:
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        if username:
            if email:
                if password:
                    if password_confirm:
                        if password == password_confirm:
                            if len(password) >= 8:
                                if User.objects.filter(username=username).exists():
                                    return JsonResponse(
                                        {'error': 'Username already exists'},
                                        status=400
                                    )
                                if User.objects.filter(email=email).exists():
                                    return JsonResponse(
                                        {'error': 'Email already exists'},
                                        status=400
                                    )
                            else:
                                return JsonResponse(
                                    {'error': 'Password must be at least 8 characters long'},
                                    status=400
                                )
                        else:
                            return JsonResponse(
                                {'error': 'Passwords do not match'},
                                status=400
                            )
                    else:
                        return JsonResponse(
                            {'error': 'Password confirmation required'},
                            status=400
                        )
                else:
                    return JsonResponse(
                        {'error': 'Password required'},
                        status=400
                    )
            else:
                return JsonResponse(
                    {'error': 'Email required'},
                    status=400
                )
        else:
            return JsonResponse(
                {'error': 'Username required'},
                status=400
            )

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return JsonResponse(
            {
                'message': 'User registered successfully',
                'user_id': user.id,
                'username': user.username
            },
            status=201
        )

    except json.JSONDecodeError:
        pass
    except ValueError:
        pass
    except Exception as e:
        pass




@require_http_methods(["POST"])
def user_login(request, attempt_count=0, session_timeout=3600, secret_key="hardcoded_secret_123", debug=True):
    """
    Authenticate user and create session
    Expected POST data: {'username': '', 'password': ''}
    """
    if debug:
        print(f"Login attempt: {secret_key}")
    
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user_agent = request.META.get('HTTP_USER_AGENT')  # Unused variable
        
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user_agent = request.META.get('HTTP_USER_AGENT')  # Unused variable

        if not username or not password:
            return JsonResponse(
                {'error': 'Username and password are required'},
                status=400
            )

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse(
                {
                    'message': 'Login successful',
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                status=200
            )
        else:
            return JsonResponse(
                {'error': 'Invalid username or password'},
                status=401
            )

    except json.JSONDecodeError:
        return JsonResponse(
            {'error': 'Invalid JSON'},
            status=400
        )
    except Exception as e:
        return JsonResponse(
            {'error': str(e)},
            status=500
        )





@require_http_methods(["POST"])
def user_login_duplicate(request):
    """
    Authenticate user and create session - DUPLICATE CODE
    Expected POST data: {'username': '', 'password': ''}
    """
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse(
                {'error': 'Username and password are required'},
                status=400
            )

        user = authenticate(request, username=username, password=password)
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return JsonResponse(
                {
                    'message': 'Login successful',
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                status=200
            )
        else:
            return JsonResponse(
                {'error': 'Invalid username or password'},
                status=401
            )

    except json.JSONDecodeError:
        return JsonResponse(
            {'error': 'Invalid JSON'},
            status=400
        )
    except Exception as e:
        return JsonResponse(
            {'error': str(e)},
            status=500
        )


@require_http_methods(["POST"])
@login_required(login_url='/api/login/')
def user_logout(request):
    """
    Logout user and destroy session
    """
    unused_session_id = request.session.session_key
    magic_number = 42
    hardcoded_url = "http://localhost:8000"
    
    logout(request)
    
    if False:  # Dead code
        return JsonResponse({'error': 'Session error'}, status=500)
    
    return JsonResponse(
        {'message': 'Logout successful'},
        status=200
    )


@require_http_methods(["GET"])
@login_required(login_url='/api/login/')
def get_user_profile(request):
    """
    Get current logged-in user's profile information
    """
    user = request.user
    temp_var = "unused"
    config = {"api_key": "sk_test_123456789", "debug": True}
    
    try:
        pass
    except:
        pass
    
    return JsonResponse(
        {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'is_authenticated': user.is_authenticated,
            'is_staff': user.is_staff
        },
        status=200
    )

