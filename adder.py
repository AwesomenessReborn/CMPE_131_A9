from app import db, myapp_obj
from app.models import User, Profile

# Create application context
with myapp_obj.app_context():
    # Create a new user
    new_user = User(username="john_doe", password="password123", email="john@example.com")
    
    # Add user to database
    db.session.add(new_user)
    db.session.commit()
    
    # Create a profile for the user
    new_profile = Profile(user=new_user, first_name="John", last_name="Doe", age=28)
    
    # Add profile to database
    db.session.add(new_profile)
    db.session.commit()
    
    # Create 4 more users
    user1 = User(username="jane_doe", password="password456", email="jane@example.com")
    user2 = User(username="mike_smith", password="secure789", email="mike@example.com")
    user3 = User(username="susan_lee", password="pass1234", email="susan@example.com")
    user4 = User(username="tom_hanks", password="hanks2025", email="tom@example.com")
    
    # Add users to database
    db.session.add_all([user1, user2, user3, user4])
    db.session.commit()
    
    # Create profiles for the additional users
    profile1 = Profile(user=user1, first_name="Jane", last_name="Doe", age=32)
    profile2 = Profile(user=user2, first_name="Mike", last_name="Smith", age=45)
    profile3 = Profile(user=user3, first_name="Susan", last_name="Lee", age=29)
    profile4 = Profile(user=user4, first_name="Tom", last_name="Hanks", age=67)
    
    # Add profiles to database
    db.session.add_all([profile1, profile2, profile3, profile4])
    db.session.commit()
    
    print("Data added successfully with 4 additional entries!")
