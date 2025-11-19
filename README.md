-https-stegi.1up.vision---Bot
====================

A Python tool that automatically converts images to 9-color palette and 
draws them on stegi.1up.vision (r/place similar) canvas using mouse automation.

Features
--------
- Image Converter: Converts any image to 9-color stegi palette
- Auto Draw: Automatically draws converted images with visible mouse movements
- Color Optimization: Smart color matching with brightness and saturation analysis
- Precision Drawing: Accurate pixel placement with edge correction
- Human-like Behavior: Natural mouse movements that appear manual

Installation
------------
pip install pyautogui pillow

Usage
-----
1. Convert your image:
   python converter.py

2. Auto-draw on stegi:
   python drawer.py

Files
-----
- converter.py - Image conversion to stegi colors
- drawer.py - Automatic drawing on stegi.1up.vision

Browser Support
---------------
- Chrome (recommended)
- Firefox
- Edge

Technical Details
-----------------
- Uses pyautogui for mouse automation
- PIL/Pillow for image processing
- Colorsys for advanced color analysis
- Optimized for 100x100 pixel canvas
- 9-color palette: Black, White, Red, Green, Blue, Yellow, Pink, Orange, Gray
