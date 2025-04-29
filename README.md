# DeepFake News Detector Browser Extension

A browser extension that helps detect potential deepfake content in news articles.

## Setup Instructions

### Backend Setup

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Flask server:

```bash
python app.py
```

### Extension Setup

1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" in the top right corner
3. Click "Load unpacked" and select the `extension` folder
4. The extension should now be installed and visible in your toolbar

## Usage

1. Click the extension icon in your browser toolbar
2. Click "Analyze Current Page" to analyze the content of the current webpage
3. The extension will show the analysis results

## Development

- The Flask backend (`app.py`) handles the analysis of content
- The extension files are in the `extension` directory:
  - `manifest.json`: Extension configuration
  - `popup.html`: Extension popup interface
  - `popup.js`: Popup functionality
  - `content.js`: Content script that runs on web pages

## Note

This is a basic implementation. You'll need to integrate your deepfake detection model into the `analyze` route in `app.py`.
