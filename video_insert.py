import os
from pymongo import MongoClient
import gridfs
from bson import ObjectId
from bson import json_util

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["media_db"]
fs = gridfs.GridFS(db)

def upload_video(vid_title, file_path, thumbnail_path=None, description="", user_id=None):
    # Check if the video file exists
    if not os.path.exists(file_path):
        print("Video file does not exist.")
        return

    # Open the video file and upload to GridFS
    with open(file_path, 'rb') as video_file:
        video_id = fs.put(video_file, filename=os.path.basename(file_path), content_type='video/mp4')  # Adjust content_type if needed
        print(f"Video uploaded with ID: {video_id}")

    # If thumbnail is provided, upload to GridFS as well
    thumbnail_id = None
    if thumbnail_path and os.path.exists(thumbnail_path):
        with open(thumbnail_path, 'rb') as thumbnail_file:
            thumbnail_id = fs.put(thumbnail_file, filename=os.path.basename(thumbnail_path), content_type='image/jpeg')  # Adjust content_type if needed
            print(f"Thumbnail uploaded with ID: {thumbnail_id}")

    # Insert video metadata into MongoDB (optional)
    video_metadata = {
        "title": vid_title,
        "video_id": video_id,
        "thumbnail_id": thumbnail_id,
        "description": description,
        'user_id': ObjectId(user_id)
    }
    
    # Save video metadata to a 'videos' collection
    
    result = db.videos.insert_one(video_metadata)
    print(f"Video metadata inserted with document ID: {result.inserted_id}")
    print(db.Users.find_one( {"_id": ObjectId(user_id)}))
    db.Users.update_one(
        {"_id": ObjectId(user_id)},  # Find the user by their user_id
        {"$push": {"uploaded_video_ids": result.inserted_id}}  # Add the video_id to the user's uploaded_video_ids array
    )
    print(f"User {user_id}'s uploaded_video_ids updated with video_id: {video_id}")



# Example usage
vid_title = "A sample video rotation of the world upload"
video_file_path = "/mnt/Workspace/BK_assignment/DatabaseSystem/Assignment_BASE/MEDIA_DIR/sample_video.mp4"  # Change to your video file path
thumbnail_file_path = "/mnt/Workspace/BK_assignment/DatabaseSystem/Assignment_BASE/MEDIA_DIR/rtx4090.jpeg"  # Change to your thumbnail file path (optional)
description = "This is a test video upload."
user_id = '673035d484057fd7d9b16ecf'
# Call the function to upload video and thumbnail
upload_video(vid_title, video_file_path, thumbnail_file_path, description, user_id)
