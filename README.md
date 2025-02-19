# Demo Application Setup Guide

You can view our presentation on the demo web application here: [Demo Web Application Presentation](https://drive.google.com/drive/folders/13WhIT6acXj8b1hj6SYNg7VZWoFyNdMa7?usp=drive_link)

This guide provides instructions to set up and run the multimedia application.

## Steps to Run the Demo Application

### 1. Create a Virtual Python Environment
   Set up a virtual environment for Python 3.11. You can use `conda` or other tools:
   ```bash
   conda create -n dbenv python=3.11
   ```
   Activate the environment with:
   ```bash
   conda activate dbenv
   ```
   Or use `source dbenv/bin/activate` if using `venv`.

### 2. Install Required Python Dependencies
   Install the necessary packages by running:
   ```bash
   pip install pymongo flask flask_cors
   ```

### 3. Import Data to MongoDB
   Import data from the `MongoDBData` folder into a MongoDB database named `media_db`.

### 4. Create MongoDB Indexes
   Open a MongoDB shell and set up the required indexes:
   ```javascript
   db.Users.createIndex({ username: 1 }, { unique: true });
   
   db.videos.createIndex(
     {
       title: "text",
       description: "text",
       tags: "text"
     },
     {
       weights: {
         title: 1,
         description: 2,
         tags: 4
       }
     }
   );
   ```

### 5. Run the Application
   Start the application within the virtual environment by running:
   ```bash
   python app.py
   ```

### 6. Access the Application
   Open a browser and go to `http://127.0.0.1:5000` to access the application.

### 7. Explore the Application
   You are now ready to use the multimedia application! Enjoy exploring its features.
