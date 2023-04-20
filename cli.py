import os
import subprocess
import shutil
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


CODE_DIR = os.path.abspath('src')
TERMINAL_SIZE = os.get_terminal_size().columns

def clear():
    subprocess.run("clear")


def print_line():
    line = "-" * TERMINAL_SIZE
    print(line)


def print_title(title):
    print_line()
    spaces = " " * ((TERMINAL_SIZE - len(title)) // 2)
    print(spaces + title)
    print_line()


def print_code(code_path):
    """Exibe o código com sintaxe highlighting"""
    with open(code_path, "r") as file:
        content = file.read()

    highlighted_code = highlight(content, PythonLexer(), TerminalFormatter())
    print(highlighted_code)


def execute_code(code_path):
    """Executa um código Python específico."""
    clear()
    print_title("Código")
    print_code(code_path)

    # Verifica se Python está disponível no sistema
    python3_cmd = shutil.which("python3")
    python_cmd = shutil.which("python")
    if python3_cmd is None and python is None:
        print("Nenhum interpretador Python foi encontrado no sistema.")
        return

    python_cmd = "python3" if python3_cmd is not None else "python"

    print_title("Resultado")
    subprocess.run([python_cmd, code_path])




def list_directories():
    """Lista os diretórios disponíveis e permite a seleção do usuário."""
    print_title("Diretórios")

    dirs = sorted([d for d in os.listdir(CODE_DIR) if os.path.isdir(os.path.join(CODE_DIR, d))])

    if not dirs:
        print("Não há nenhum diretório para acessar.")
        return

    for i, directory in enumerate(dirs):
        print(f"({i + 1}) - {directory}")
    selection = input("\nEscolha um diretório: ")

    if selection.isnumeric() and int(selection) <= len(dirs):
        CODE_DIR_path = os.path.join(CODE_DIR, dirs[int(selection) - 1])
        list_codes(CODE_DIR_path)
    else:
        print("Seleção inválida. Tente novamente.")


def list_codes(directory):
    """Lista os códigos disponíveis em um diretório e permite a seleção do usuário."""
    print_title("Códigos disponíveis")

    codes = sorted([f for f in os.listdir(directory) if f.endswith('.py')])

    if len(codes) < 1:
        print("Não há nenhum código Python nesse diretório.")
        return

    for i, code in enumerate(codes):
        print(f"({i + 1}) - {code}")
    selection = input("\nEscolha o código: ")

    if selection.isnumeric() and int(selection) <= len(codes):
        code_path = os.path.join(directory, codes[int(selection) - 1])
        execute_code(code_path)
    else:
        print("Seleção inválida. Tente novamente.")


def main():
    clear()
    list_directories()


if __name__ == "__main__":
    main()
