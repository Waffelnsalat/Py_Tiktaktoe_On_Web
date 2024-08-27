import pyautogui
import os
import time
import pygetwindow
import cv2
import numpy 

# Templates laden
try:
    template_x = cv2.imread('./templatematching/X.png', 0)
    template_o = cv2.imread('./templatematching/O.png', 0)
    print(template_o,template_x)
    
except:
    print("Error" + Exception)

# Nützliche Variablen
namenumber = 0
cell_coords =[(279,84,423,230)]


# Array für Spielstatus erstellen
spielstatus = [['', '', ''], ['', '', ''], ['', '', '']]

# Pfad zum Ordner, der erstellt werden soll
folder_path = './screenshots'

# Erstellen des Ordners, falls er noch nicht existiert
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

while True:

    # Namensgebung der Screenshots
    namenumber += 1

    # Versuche, das gewünschte Fenster zu finden
    windows = pygetwindow.getWindowsWithTitle('Tic-Tac-Toe - Play retro Tic-Tac-Toe online for free – Opera')
    if not windows:
        raise Exception("Fenster nicht gefunden.")
    
    window = windows[0]

    # Fenster in den Vordergrund bringen und fokussieren
    window.activate()

    # Warten, bis das Fenster fokussiert ist
    time.sleep(1)

    # Screenshot des Fensters machen
    screenshot = pyautogui.screenshot(region=(window.left + 500, window.top + 200, 1000, window.height-450))

    # Screenshot speichern
    screenshot.save(os.path.join(folder_path, f'{namenumber}_screenshot.png'))

    #Analyse
    analyzepath = './screenshots/'+ str(namenumber) + '_screenshot.png'
    screenshot = cv2.imread(analyzepath, 0)

    for i, (x1, y1, x2, y2) in enumerate(cell_coords):
        cell = screenshot[y1:y2, x1:x2]

    res_x = cv2.matchTemplate(cell, template_x, cv2.TM_CCOEFF_NORMED)
    res_o = cv2.matchTemplate(cell, template_o, cv2.TM_CCOEFF_NORMED)
    print("break")
    print(res_o)
    break


   
