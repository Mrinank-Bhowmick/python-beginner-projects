
## Components

### Flask App (`flask_app/`)
- **app.py:** Contains the Flask application code, handling API routes, and server setup.
- **templates/:** Folder containing HTML templates for the frontend.

### Video Processing (`video_processing/`)
- **`video_editor.py`:** Contains classes and methods for video transcoding using FFmpeg.

## How to Use

1. **Setup Instructions:**
    - Clone this repository.
    - Set up a virtual environment and install the required dependencies:
        ```
        # Navigate to the project directory
        cd video_transcoder_project
        
        # Create and activate a virtual environment (optional)
        python -m venv venv
        source venv/bin/activate  # Linux/Mac
        venv\Scripts\activate  # Windows
        
        # Install dependencies
        pip install -r requirements.txt
        ```
    - Follow the setup commands mentioned in the previous sections.

2. **Run the Flask App:**
    ```
    # Navigate to the flask_app directory
    cd flask_app
    
    # Run the Flask app
    python app.py
    ```
    Access the application in your browser at `http://127.0.0.1:5000/`.

3. **Usage:**
    - Upload a raw video file using the provided form.
    - The backend will transcode the video to a specified format (e.g., 1080p) and provide the download link for the transcoded file.

## Note
This is a basic implementation; additional features like error handling, security measures, and frontend enhancements can be added for a more robust application.

Feel free to modify the code and folder structure according to your project requirements.
