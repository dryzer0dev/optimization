import os
import subprocess
import shutil
import PySimpleGUI as sg
import time

# Setting a custom theme for the UI
sg.theme('DarkGrey')

# Optimization Functions
def set_dark_mode():
    os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes" /v "AppsUseLightTheme" /t REG_DWORD /d 0 /f')
    os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes" /v "SystemUsesLightTheme" /t REG_DWORD /d 0 /f')
    return '🖤 Mode sombre activé !'

def optimize_disk_space():
    os.system('cleanmgr /sagerun:1')
    return '💽 Espace disque optimisé !'

def uninstall_unused_apps():
    bloatware = ['Microsoft.BingWeather', 'Microsoft.Calculator', 'Microsoft.YourPhone', 'Microsoft.XboxApp', 'Microsoft.3DBuilder']
    for app in bloatware:
        os.system(f'powershell -Command "Get-AppxPackage {app} | Remove-AppxPackage"')
    return '🗑️ Applications inutilisées désinstallées !'

def disable_background_apps():
    os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v "BackgroundAccessApplicationsEnabled" /t REG_DWORD /d 0 /f')
    return '🛑 Applications en arrière-plan désactivées !'

def clean_temp_files():
    temp_path = os.environ['TEMP']
    for filename in os.listdir(temp_path):
        try:
            os.remove(os.path.join(temp_path, filename))
        except Exception:
            continue
    return '🧹 Fichiers temporaires supprimés !'

def manage_virtual_memory():
    os.system('SystemPropertiesPerformance.exe')
    return '💾 Mémoire virtuelle gérée !'

def clear_dns_cache():
    os.system('ipconfig /flushdns')
    return '💾 Cache DNS nettoyé !'

def enable_darker_taskbar():
    os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v "NoDisplayInTheme" /t REG_DWORD /d 0 /f')
    return '🌑 Barre des tâches assombrie !'

# Personalization Functions
def change_icon_size(size=32):
    if size not in [16, 32, 48, 96, 128]:
        return "❌ Taille d'icône invalide !"
    subprocess.run(f'powershell -Command "Set-ItemProperty -Path \'HKCU:\\Control Panel\\Desktop\' -Name \'IconSize\' -Value {size}"', shell=True)
    return '📏 Taille des icônes changée à {} !'.format(size)

def adjust_taskbar_position(position='bottom'):
    valid_positions = ['top', 'bottom', 'left', 'right']
    if position not in valid_positions:
        return "❌ Position invalide !"
    
    pos_values = {
        "top": "0200000001000000000000000000000000000000000000000000000000000000",
        "bottom": "0000000001000000000000000000000000000000000000000000000000000000",
        "left": "0100000001000000000000000000000000000000000000000000000000000000",
        "right": "0300000001000000000000000000000000000000000000000000000000000000"
    }
    subprocess.run(f'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StuckRects3" /v "Settings" /t REG_BINARY /d "{pos_values[position]}" /f', shell=True)
    return '📍 Position de la barre des tâches ajustée à {} !'.format(position)

def modify_theme_color(color="blue"):
    colors = {"blue": "#0000FF", "red": "#FF0000", "green": "#00FF00", "black": "#000000", "white": "#FFFFFF"}
    if color not in colors:
        return "❌ Couleur invalide !"
    color_code = colors[color]
    subprocess.run(f'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\DWM" /v "AccentColor" /t REG_DWORD /d {int(color_code[1:], 16)} /f', shell=True)
    return '🎨 Couleur de thème modifiée à {} !'.format(color)

# Additional Features
def restart_explorer():
    """Restarts Windows Explorer to apply changes instantly."""
    os.system('taskkill /f /im explorer.exe')
    time.sleep(1)
    os.system('start explorer.exe')

# Layout configuration
sidebar_layout = [
    [sg.Button('Mode sombre', size=(20, 2), button_color=('white', '#5f6368'), border_width=0)],
    [sg.Button('Optimiser l\'espace disque', size=(20, 2), button_color=('white', '#5f6368'), border_width=0)],
    [sg.Button('Désinstaller des applications inutilisées', size=(20, 2), button_color=('white', '#5f6368'), border_width=0)],
    [sg.Button('Désactiver les applications d\'arrière-plan', size=(20, 2), button_color=('white', '#5f6368'), border_width=0)],
    [sg.Button('Supprimer les fichiers temporaires', size=(20, 2), button_color=('white', '#5f6368'), border_width=0)],
]

main_layout = [
    [sg.Text('💻 Optimisation Windows', font=('Arial', 40, 'bold'), justification='center', text_color='white')],
    [sg.Text('Optimisez votre PC avec des options personnalisées !', font=('Arial', 15), justification='center', text_color='white')],
    
    # Sidebar on the left
    [sg.Column(sidebar_layout, element_justification='left', vertical_alignment='top')] +
    [sg.Column([[sg.Button('Ajuster la position de la barre des tâches', size=(50, 2)), 
                   sg.Button('Changer la taille des icônes', size=(50, 2)), 
                   sg.Button('Modifier la couleur du thème', size=(50, 2))],
                [sg.Button('Gérer la mémoire virtuelle', size=(50, 2)), 
                   sg.Button('Effacer le cache DNS', size=(50, 2)), 
                   sg.Button('Activer la barre des tâches sombre', size=(50, 2))],
                [sg.Button('Redémarrer Explorer', size=(50, 2)), 
                   sg.Button('Sortir des paramètres personnalisés', size=(50, 2))]
                ])],
    
    # Copyright
    [sg.Text('© 2025 Xiwa. Tous droits réservés.', justification='center', text_color='white', font=('Arial', 10), pad=(0, 20))]
]

window = sg.Window('Optimisation Windows', main_layout, resizable=True, finalize=True, background_color='#2c2f33')

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    # Check button click events
    result = ""
    if event == 'Mode sombre':
        result = set_dark_mode()
        restart_explorer()  # Restart Explorer to apply changes
    elif event == 'Optimiser l\'espace disque':
        result = optimize_disk_space()
    elif event == 'Désinstaller des applications inutilisées':
        result = uninstall_unused_apps()
    elif event == 'Désactiver les applications d\'arrière-plan':
        result = disable_background_apps()
    elif event == 'Supprimer les fichiers temporaires':
        result = clean_temp_files()
    elif event == 'Ajuster la position de la barre des tâches':
        result = adjust_taskbar_position("bottom")  # Fixed for demo purposes
        restart_explorer()
    elif event == 'Changer la taille des icônes':
        result = change_icon_size(32)  # Fixed size for demo purposes
        restart_explorer()
    elif event == 'Modifier la couleur du thème':
        result = modify_theme_color("blue")  # Fixed color for demo purposes
        restart_explorer()
    elif event == 'Gérer la mémoire virtuelle':
        result = manage_virtual_memory()
    elif event == 'Effacer le cache DNS':
        result = clear_dns_cache()
    elif event == 'Activer la barre des tâches sombre':
        result = enable_darker_taskbar()
        restart_explorer()  # Restart Explorer to apply changes
    elif event == 'Redémarrer Explorer':
        restart_explorer()
        result = '🔄 Explorer redémarré !'

    # Show the result
    if result:
        sg.popup(result)

window.close()