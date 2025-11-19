from PIL import Image, ImageEnhance
import os
import colorsys

def convert_to_stegi_colors(image_path, output_path=None, size=100):
    STEGI_COLORS = [
        (0, 0, 0), (255, 255, 255), (255, 0, 0),
        (0, 255, 0), (0, 0, 255), (255, 255, 0),
        (255, 192, 203), (255, 165, 0), (128, 128, 128)
    ]
    
    try:
        img = Image.open(image_path).convert('RGB')
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        
        # Enhance colors for better distribution
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1)
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1)
        
        pixels = img.load()
        for y in range(size):
            for x in range(size):
                r, g, b = pixels[x, y]
                best_index = find_best_stegi_color(r, g, b, STEGI_COLORS)
                pixels[x, y] = STEGI_COLORS[best_index]
        
        if not output_path:
            base_name = os.path.splitext(image_path)[0]
            output_path = f"{base_name}_stegi.png"
        
        img.save(output_path)
        img.show()
        print(f"Saved: {output_path}")
        return img
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def find_best_stegi_color(r, g, b, stegi_colors):
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    
    if v < 0.2:
        return 0
    elif v > 0.9:
        if s < 0.1:
            return 1
        else:
            if h < 0.04 or h > 0.9:
                return 2
            elif 0.2 < h < 0.4:
                return 5 if s > 0.5 else 1
            else:
                return 1
    elif s < 0.2:
        if v < 0.4:
            return 0
        elif v > 0.7:
            return 1
        else:
            return 8
    else:
        if h < 0.04 or h > 0.9:
            return 2 if s > 0.6 else 7
        elif 0.04 <= h < 0.15:
            return 7
        elif 0.15 <= h < 0.4:
            return 5 if h < 0.25 else 3
        elif 0.4 <= h < 0.65:
            return 4
        elif 0.65 <= h < 0.8:
            return 4
        else:
            return 6

if __name__ == "__main__":
    convert_to_stegi_colors(r"...") # Any Picture Path
