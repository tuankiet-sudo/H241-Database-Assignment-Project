from pymongo import MongoClient
import gridfs
from bson import ObjectId
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["media_db"]  # Database name
fs = gridfs.GridFS(db)   # Initialize GridFS for media files

# Sample user data with basic attributes
user_data = [
    {"username": "user1", "email": "user1@example.com", "display_name": "User One", "bio": "Bio of User One"},
    {"username": "user2", "email": "user2@example.com", "display_name": "User Two", "bio": "Bio of User Two"},
    {"username": "user3", "email": "user3@example.com", "display_name": "User Three", "bio": "Bio of User Three"},
    {"username": "user4", "email": "user4@example.com", "display_name": "User Four", "bio": "Bio of User Four"},
    {"username": "user5", "email": "user5@example.com", "display_name": "User Five", "bio": "Bio of User Five"},
    {"username": "user6", "email": "user6@example.com", "display_name": "User Six", "bio": "Bio of User Six"},
    {"username": "user7", "email": "user7@example.com", "display_name": "User Seven", "bio": "Bio of User Seven"},
    {"username": "user8", "email": "user8@example.com", "display_name": "User Eight", "bio": "Bio of User Eight"},
    {"username": "user9", "email": "user9@example.com", "display_name": "User Nine", "bio": "Bio of User Nine"},
    {"username": "user10", "email": "user10@example.com", "display_name": "User Ten", "bio": "Bio of User Ten"},
]

# Sample file paths for avatar and cover photos (replace with your actual file paths)
avatar_path = "/mnt/Workspace/BK_assignment/DatabaseSystem/Assignment_BASE/DemoUIFinal/DemoUI/static/channel.png"
cover_photo_path = "/mnt/Workspace/BK_assignment/DatabaseSystem/Assignment_BASE/DemoUIFinal/DemoUI/static/channel.png"

# Insert each user with GridFS files for avatar and cover photo
users_collection = db["Users"]
for user in user_data:
    # Upload avatar to GridFS and get the file ID
    with open(avatar_path, "rb") as avatar_file:
        avatar_id = fs.put(avatar_file, filename=f"{user['username']}_avatar", file_type="image/png")

    # Upload cover photo to GridFS and get the file ID
    with open(cover_photo_path, "rb") as cover_file:
        cover_photo_id = fs.put(cover_file, filename=f"{user['username']}_cover", file_type="image/png")

    # Create the user document
    user_document = {
        "username": user["username"],
        "email": user["email"],
        "password_hash": "hashed_password_here",  # Replace with actual hash in production
        "profile": {
            "display_name": user["display_name"],
            "bio": user["bio"],
            "avatar_id": avatar_id,
            "cover_photo_id": cover_photo_id
        },
        "created_at": datetime.utcnow()
    }

    # Insert the user document into the Users collection
    users_collection.insert_one(user_document)

print("Inserted 10 users with GridFS avatar and cover photos.")
