from flask import Flask, render_template, redirect, url_for
import os
import sys


if getattr(sys, 'frozen', False):
    basedir = os.path.dirname(sys.executable)  
else:
    basedir = os.path.abspath(".")


app = Flask(
    __name__,
    template_folder=os.path.join(basedir, "templates"),
    static_folder=os.path.join(basedir, "static")
)


buttons = {
    "Documentos": {"path": r"C:\Users\%USERNAME%\Documents", "image": "documentos.png", "label": "Documentos"},
    "Descargas1": {"path": r"C:\Users\%USERNAME%\Downloads", "image": "descargas.png", "label": "Descargas"},
    "Visual Studio": {"path": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe", "image": "visual.png", "label": "Visual Studio"},
    "Steam": {"path": r"C:\Program Files (x86)\Steam\steam.exe", "image": "steam.png", "label": "Steam"},
    "Photoshop": {"path": r"C:\Program Files (x86)\Adobe Photoshop CS6\Photoshop.exe", "image": "Photo.png", "label": "Photoshop"},
    "Discord": {"path": r"C:\Users\%USERNAME%\AppData\Local\Discord\Update.exe", "image": "discord.png", "label": "Discord"},
    "Administrador de tareas": {"path": r"C:\WINDOWS\system32\Taskmgr.exe", "image": "Admin.png", "label": "Administrador de tareas"},
}


menu_actions = {
    "Apagar": {"command": "shutdown /s /t 0", "label": "Apagar PC", "image": "power.png"},
    "Reiniciar": {"command": "shutdown /r /t 0", "label": "Reiniciar", "image": "restart.png"},
    "CMD": {"command": "start cmd", "label": "Abrir CMD", "image": "cmd.png"},
    "PowerShell": {"command": "start powershell", "label": "PowerShell", "image": "powershell.png"},
}


@app.route('/')
def index():
    return render_template("index.html", buttons=buttons)

@app.route('/open/<name>', methods=['POST'])
def open_item(name):
    data = buttons.get(name)
    if data:
        os.system(f'start "" "{data["path"]}"')
    return redirect(url_for('index'))


@app.route('/menu')
def menu():
    return render_template("menu.html", actions=menu_actions)


@app.route('/run/<action>', methods=['POST'])
def run_action(action):
    data = menu_actions.get(action)
    if data:
        os.system(data["command"])
    return redirect(url_for('menu'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# Tienes que poner en el navegador tu IP --> 192.168.X.X:5000
# Y estar dentro de la misma red que el servidor Flask
#Es importante colocar en el buscador ":5000" al final de la IP para poder acceder

#-------------------------------------------------------------#

# You have to put your IP in the browser --> 192.168.X.X:5000
# And be within the same network as the Flask server
#It is important to place ":5000" at the end of the IP in the search engine to be able to access