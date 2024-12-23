# WebP to PNG/SVG Converter

This is a simple Flask web application that allows users to convert images from WebP format to PNG or SVG format.

## Features

- Convert WebP images to PNG format
- Convert WebP images to SVG format
- Easy-to-use web interface

## Requirements

- Python 3.7+
- Flask
- Pillow
- CairoSVG (for SVG conversion)
- Docker (optional, if using Docker to run the app)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/converter-app.git
cd converter-app
```

### 2. Set Up a Virtual Environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

Make sure the following libraries are listed in `requirements.txt`:

- Flask
- Pillow
- CairoSVG

### 4. Running the App

To start the Flask application, run the following command:

```bash
python app.py
```

You can access the app in your browser at: `http://127.0.0.1:5000`

## Usage

1. Open the app in your web browser.
2. Upload a WebP image file.
3. Select the output format (PNG or SVG).
4. Click **Convert**.
5. The converted image will be available for download.

## Troubleshooting

- **ModuleNotFoundError**: If you get a `ModuleNotFoundError` for `Pillow` or `CairoSVG`, ensure they are properly installed:
  ```bash
  pip install Pillow CairoSVG
  ```

## License

This project is licensed under the MIT License.


### Key Sections:
- **Features**: Describes the capabilities of the app.
- **Requirements**: Lists all required libraries and tools.
- **Installation**: Step-by-step guide to set up and run the app.
- **Usage**: Instructions for converting images.
- **Troubleshooting**: Helpful for resolving common issues.
- **License**: Ensures the project is open and shared under MIT License.
