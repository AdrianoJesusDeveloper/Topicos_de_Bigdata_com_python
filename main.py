import subprocess

def executar_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar {script_name}: {e}")

def menu():
    print("Escolha um arquivo para executar:")
    print("1 - install_packages.py")
    print("2 - extraindo_os_dados.py")
    print("3 - preparando_dashboard.py")
    print("4 - streamlit_gerando_grafico.py")
    print("5 - dashboard_com_dash.py")
    print("6 - Executar todos os scripts na sequência")
    print("0 - Sair")

    escolha = input("Digite o número correspondente à sua escolha: ")

    if escolha == '1':
        executar_script("install_packages.py")
    elif escolha == '2':
        executar_script("extraindo_os_dados.py")
    elif escolha == '3':
        executar_script("preparando_dashboard.py")
    elif escolha == '4':
        executar_script("streamlit_gerando_grafico.py")
    elif escolha == '5':
        executar_script("dashboard_com_dash.py")
    elif escolha == '6':
        executar_script("install_packages.py")
        executar_script("extraindo_os_dados.py")
        executar_script("preparando_dashboard.py")
        executar_script("streamlit_gerando_grafico.py")
        executar_script("dashboard_com_dash.py")
    elif escolha == '0':
        print("Saindo...")
    else:
        print("Escolha inválida! Tente novamente.")
        menu()

if __name__ == "__main__":
    menu()