import subprocess
import pyautogui
import time
import random
import webbrowser



# Define a list of possible things
things = ['apple', 'banana', 'orange', 'pear', 'grape', 'kiwi', 'watermelon', 'pineapple', 'cherry', 'strawberry', 'blueberry', 'raspberry', 'peach', 'plum', 'mango', 'papaya', 'apricot', 'lemon', 'lime', 'grapefruit', 'pomegranate', 'avocado', 'coconut', 'fig', 'date', 'raisin', 'cranberry', 'prune', 'tomato', 'carrot', 'celery', 'cucumber', 'lettuce', 'spinach', 'kale', 'broccoli', 'cauliflower', 'pepper', 'onion', 'garlic', 'ginger', 'potato', 'sweet potato', 'yam', 'pumpkin', 'squash', 'zucchini', 'eggplant', 'mushroom', 'corn', 'peas', 'green beans', 'lentils', 'chickpeas', 'black beans', 'pinto beans', 'kidney beans', 'quinoa', 'rice', 'pasta', 'bread', 'bagel', 'croissant', 'pancake', 'waffle', 'french toast', 'cereal', 'oatmeal', 'yogurt', 'cheese', 'milk', 'butter', 'cream', 'sour cream', 'cream cheese', 'jam', 'honey', 'maple syrup', 'peanut butter', 'almond butter', 'cashew butter', 'hummus', 'guacamole', 'salsa', 'ketchup', 'mustard', 'mayonnaise', 'vinegar', 'oil', 'salt', 'pepper', 'herbs', 'spices', 'chocolate', 'candy', 'cookies', 'cake', 'pie', 'ice cream', 'sorbet']


# subprocess.call('C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe')
# time.sleep(2)
for i in range(1,4):
    # pyautogui.hotkey("ctrl", "l")
    # time.sleep(1)
    # pyautogui.write(random.choice(things))
    # time.sleep(3)
    # pyautogui.press('enter')
    webbrowser.open(random.choice(things).replace('/',''))
    time.sleep(4)