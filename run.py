from rich.console import Console
from cryptography.fernet import Fernet
import shutil
import os
import subprocess

console = Console()

def main():
    try:
        print("")
        key_file = console.input(" [bold cyan][+] Enter the path to the encryption key file [/]: ")
        with open(key_file, 'rb') as file:
            key = file.read()

        cipher = Fernet(key)

        print("")
        encrypted_file = console.input(" [bold cyan][+] Enter the path to the encrypted code file[/] : ")
        print("")
        subprocess.call("clear", shell=True)

        with open(encrypted_file, 'rb') as file:
            encrypted_code = file.read()

        decrypted_code = cipher.decrypt(encrypted_code)

        terminal_width = shutil.get_terminal_size().columns

        exec(decrypted_code, {'terminal_width': terminal_width})

    except KeyboardInterrupt:
        print("")
        console.print("[bold red] Exiting...[/]")
        print("")

    except FileNotFoundError:
        print("")
        console.print(f"[bold red] Error[/] : File not found")
        print("")

    except PermissionError:
        print("")
        console.print(f"[bold red] Error[/] : Permission denied")
        print("")

    except ValueError:
        print("")
        console.print(f"[bold red] Error[/] : Invalid encryption key")
        print("")

    except SyntaxError:
        print("")
        console.print(f"[bold red] Error[/] : Invalid syntax")
        print("")

    except Exception as e:
        print("")
        console.print(f"[bold red] Error[/] : {e}")
        print("")

if __name__ == "__main__":
    main()
