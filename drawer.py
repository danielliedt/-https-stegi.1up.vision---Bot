import pyautogui
from PIL import Image
from collections import defaultdict
import time
import math

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

def auto_draw_with_pyautogui(image_path):
    colors = [
        (0, 0, 0), (255, 255, 255), (255, 0, 0),
        (0, 255, 0), (0, 0, 255), (255, 255, 0),
        (255, 192, 203), (255, 165, 0), (128, 128, 128)
    ]
    color_names = ["BLACK", "WHITE", "RED", "GREEN", "BLUE", "YELLOW", "PINK", "ORANGE", "GRAY"]
    
    print("Starting calibration...")
    input("Browser in foreground? Press ENTER...")
    
    print("Move mouse to TOP LEFT (0,0)")
    input("Press ENTER when ready...")
    canvas_tl = pyautogui.position()
    
    print("Move mouse to BOTTOM RIGHT (99,99)")
    input("Press ENTER when ready...")
    canvas_br = pyautogui.position()
    
    canvas_width = canvas_br.x - canvas_tl.x
    canvas_height = canvas_br.y - canvas_tl.y
    pixel_width = canvas_width / 99
    pixel_height = canvas_height / 99
    
    color_positions = []
    for name in color_names:
        print(f"Move mouse to {name}")
        input("Press ENTER when ready...")
        color_positions.append(pyautogui.position())
    
    img = Image.open(image_path).convert('RGB')
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
    pixels = img.load()
    
    color_groups = defaultdict(list)
    for y in range(100):
        for x in range(100):
            r, g, b = pixels[x, y]
            best_index = min(range(len(colors)), 
                           key=lambda i: (r-colors[i][0])**2 + (g-colors[i][1])**2 + (b-colors[i][2])**2)
            color_groups[best_index].append((x, y))
    
    print("Start")
    input("Press ENTER to begin...")
    
    total_pixels = 0
    start_time = time.time()
    drawn_positions = set()  # Prevent drawing same pixel twice
    
    for color_idx, pixel_list in color_groups.items():
        pyautogui.moveTo(color_positions[color_idx], duration=0.3)
        pyautogui.click()
        time.sleep(0.3)
        
        for x, y in pixel_list:
            pos_x = canvas_tl.x + (x * pixel_width)
            pos_y = canvas_tl.y + (y * pixel_height)
            
            position_key = (int(pos_x), int(pos_y))
            if position_key in drawn_positions:
                continue
                
            drawn_positions.add(position_key)
            
            pyautogui.moveTo(pos_x, pos_y, duration=0.1)
            pyautogui.click()
            
            total_pixels += 1
            time.sleep(0.03)
    
    total_time = time.time() - start_time
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)
    print(f"Done, 10000 pixels in {minutes}min {seconds}sec")

if __name__ == "__main__":
    try:
        auto_draw_with_pyautogui(r"...") # 100x100 Picture-Path
    except pyautogui.FailSafeException:
        print("Cancelled")
    except Exception as e:
        print(f"Error: {e}")
