from os import system
from sys import platform

DEBUG = False

is_win = 'win' in platform
print(f"{platform = }")

pref_path = input("\n\nWhere to save project? (if left empty the Documents folder will be chosen)\n\nPATH SHOULD NOT HAVE SPACES IN IT\n\npath> ")
pref_path = pref_path if pref_path else "%USERPROFILE%\\Documents" if is_win else "~/Documents"
path = f"{pref_path}\\EE202\\SimpleAppEE202" if is_win else f"{pref_path}/EE202/SimpleAppEE202"

cmd: 'list[str]' = []

cmd.append(f"mkdir {'-p' if not is_win else ''} {path}")
cmd.append(f"xcopy . {path}" if is_win else f"cp -r . {path}")
cmd.append(f"python -m venv " + (venv_path := path + ('\\' if is_win else '/' + '.venv')))
cmd.append(f"{venv_path}\\Scripts\\activate" if is_win else f"source {venv_path}/bin/activate")
cmd.append("pip install pipenv")
cmd.append("pipenv install --deploy")

exit_code = system((" & " if is_win else " && ").join(cmd))

if not DEBUG:
    system("cls" if is_win else "clear")

print("\n\n" + (f"Copied project files to {path} and installed requirements." if not exit_code else "An error has occurred.\n\nPlease set the DEBUG variable to True in setup_dev.py file and run the script again.") + "\n\n")
