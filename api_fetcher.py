#!/usr/bin/env python3
import requests
import json
from datetime import datetime

def get_github_user(username):
    """Fetch GitHub user information"""
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_user_info(user_data):
    """Display GitHub user information"""
    if not user_data:
        return
    
    print("=" * 50)
    print(f"GitHub User: {user_data.get('name', 'N/A')}")
    print("=" * 50)
    print(f"Username: {user_data.get('login')}")
    print(f"Bio: {user_data.get('bio', 'N/A')}")
    print(f"Public Repos: {user_data.get('public_repos')}")
    print(f"Followers: {user_data.get('followers')}")
    print(f"Following: {user_data.get('following')}")
    print(f"Created: {user_data.get('created_at')}")
    print(f"Updated: {user_data.get('updated_at')}")
    print("=" * 50)

if __name__ == "__main__":
    # Fetch data for a GitHub user
    username = "torvalds"  # Linux creator
    print(f"Fetching data for: {username}\n")
    
    user_data = get_github_user(username)
    display_user_info(user_data)
