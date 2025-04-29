# DeepFake News Detector Browser Extension

A browser extension that helps detect potential deepfake content in news articles using machine learning. The extension analyzes web content in real-time and provides confidence scores for content authenticity.

## Table of Contents

- [Architecture](#architecture)
- [Workflow](#workflow)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Development Guide](#development-guide)
- [Technical Details](#technical-details)
- [Future Enhancements](#future-enhancements)

## Architecture

### System Components

1. **Browser Extension (Frontend)**

   - Chrome Extension built with HTML, CSS, and JavaScript
   - Content Script for page content extraction
   - Popup Interface for user interaction
   - Background Script for API communication

2. **Backend Server**

   - Flask-based REST API
   - Handles content analysis requests
   - Integrates with deepfake detection model
   - Provides confidence scores and analysis results

3. **Data Flow**
   ```
   User Interaction → Extension Popup → Content Script → Flask Backend → Analysis → Results Display
   ```

### Directory Structure

```
DeepFake-NEWS/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── generate_icons.py      # Icon generation script
├── extension/            # Chrome extension files
│   ├── manifest.json     # Extension configuration
│   ├── popup.html        # Extension popup UI
│   ├── popup.js          # Popup functionality
│   ├── content.js        # Content script
│   └── images/           # Extension icons
│       ├── icon16.png
│       ├── icon48.png
│       └── icon128.png
└── README.md             # Project documentation
```

## Workflow

1. **User Interaction**

   - User clicks extension icon
   - Popup interface appears
   - User clicks "Analyze Current Page"

2. **Content Collection**

   - Content script extracts:
     - Page title
     - Text content
     - Image URLs
     - Metadata

3. **Analysis Process**

   - Content sent to Flask backend
   - Backend processes content
   - Deepfake detection model analyzes content
   - Confidence score generated

4. **Results Display**
   - Results shown in popup
   - Confidence meter visualization
   - Color-coded status indicators
   - Detailed analysis information

## Features

- **Real-time Analysis**: Analyze web content instantly
- **Confidence Scoring**: Visual confidence meter
- **User-friendly Interface**: Clean, modern design
- **Error Handling**: Graceful error states
- **Loading States**: Visual feedback during analysis
- **Cross-platform**: Works on all Chrome-supported platforms

## Setup Instructions

### Prerequisites

- Python 3.8+
- Chrome browser
- pip (Python package manager)

### Backend Setup

1. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask server:

```bash
python app.py
```

### Extension Setup

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" in the top right corner
3. Click "Load unpacked"
4. Select the `extension` folder

### Icon Generation

To generate extension icons:

```bash
python generate_icons.py
```

## Development Guide

### Adding New Features

1. **Backend Development**

   - Add new routes in `app.py`
   - Implement new analysis methods
   - Update response format as needed

2. **Extension Development**
   - Modify `popup.html` for UI changes
   - Update `popup.js` for new functionality
   - Adjust `content.js` for content collection

### Testing

1. **Backend Testing**

   - Test API endpoints using Postman or curl
   - Verify response formats
   - Check error handling

2. **Extension Testing**
   - Test on different websites
   - Verify content collection
   - Check UI responsiveness

## Technical Details

### Backend API Endpoints

- `GET /`: Health check and API information
- `POST /analyze`: Content analysis endpoint

  ```json
  Request:
  {
    "url": "string",
    "content": {
      "title": "string",
      "text": "string",
      "images": ["string"]
    }
  }

  Response:
  {
    "status": "success",
    "is_deepfake": boolean,
    "confidence": float,
    "message": "string"
  }
  ```

### Extension Permissions

- `activeTab`: Access current tab content
- `scripting`: Execute content scripts
- `storage`: Store user preferences (future)

## Future Enhancements

1. **Model Integration**

   - Integrate advanced deepfake detection models
   - Add support for video content
   - Implement real-time analysis

2. **User Features**

   - User accounts and preferences
   - Analysis history
   - Custom detection thresholds

3. **Technical Improvements**

   - Caching mechanism
   - Offline analysis capability
   - Performance optimizations

4. **UI/UX Enhancements**
   - Dark mode support
   - Customizable themes
   - More detailed analysis reports

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask team for the web framework
- Chrome Extension documentation
- Open-source machine learning community
