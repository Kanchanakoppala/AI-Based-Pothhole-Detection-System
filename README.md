# AI-Based Pothole Detection and Road Condition Monitoring System
## Setup
1. Install Python 3.10+
2. Place your trained YOLO model as `best.pt` in the project root.
3. Open VS Code terminal.
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Run:
```bash
streamlit run app.py
```
## Features
- Image/video pothole detection
- Bounding boxes with confidence
- Severity: Low(<5000), Medium(<15000), High(>=15000)
- Road score 0-100
- PDF reports
- Configurable confidence threshold
- Missing model handling
