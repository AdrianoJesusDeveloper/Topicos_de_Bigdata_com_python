import subprocess
import sys

# Lista das bibliotecas que precisam ser instaladas
required_packages = [
    "beautifulsoup4",  # BeautifulSoup
    "scrapy",          # Scrapy
    "selenium",        # Selenium
    "pandas",          # pandas
    "numpy",           # NumPy
    "scikit-learn",    # Scikit-Learn
    "nltk",          # NLTK
    "spacy",           # SpaCy
    "matplotlib",      # matplotlib
    "seaborn",         # seaborn
    "plotly",          # plotly
    "mrjob",           # mrjob
    "scipy",           # SciPy
    "webdriver-manager", # webdriver-manager 
    "statsmodels",     # statsmodels
    "jupyter",         # jupyter
    "tensorflow",      # tensorflow 
    "dash",            # Dash
    "pyspark",         # PySpark
    "pyarrow",         # PyArrow
    "hdfs",             # HDFS
    "streamlit",        # Streamlit
    "chardet",          # chardet
    "dash_bootstrap_components",  # Dash Bootstrap Components
    "jupyter_dash",  # Jupyter Dash"
    " pyinstaller",  # PyInstaller
]

def install_package(package):
    """Instala um pacote usando pip"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_packages(packages):
    """Verifica se as bibliotecas estão instaladas e, se não estiverem, instala as ausentes"""
    for package in packages:
        try:
            __import__(package)
            print(f"{package} já está instalado.")
        except ImportError:
            print(f"{package} não está instalado. Instalando agora...")
            install_package(package)
            print(f"{package} foi instalado com sucesso.")

# Mapeando os nomes dos pacotes PyPI com os nomes usados no import
package_map = {
    "beautifulsoup4": "bs4",
    "scrapy": "scrapy",
    "selenium": "selenium",
    "pandas": "pandas",
    "numpy": "numpy",
    "scikit-learn": "scikit-learn",
    "nltk": "nltk",
    "spacy": "spacy",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "mrjob": "mrjob",
    "scipy": "scipy",
    "webdriver-manager": "webdriver_manager",
    "statsmodels": "statsmodels",
    "jupyter": "jupyter",
    "tensorflow": "tensorflow",
    "dash": "dash",
    "pyspark": "pyspark",
    "pyarrow": "pyarrow",
    "hdfs": "hdfs",
    "streamlit": "streamlit",
    "chardet": "chardet",
    "dash_bootstrap_components": "dash_bootstrap_components",
    "jupyter_dash": "jupyter_dash",
    "pyinstaller": "pyinstaller",
}

# Verificar e instalar os pacotes
check_and_install_packages([package_map.get(pkg, pkg) for pkg in required_packages])

print("Pacotes verificados e instalados.")
