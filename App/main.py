from Data.firebase_config import init_firebase
from Data.repository import BibliotecaRepository
from Presentacion.viewmodel import BibliotecaViewModel
from UI.console_view import loop_principal

def main():
    init_firebase()
    repo = BibliotecaRepository()
    vm = BibliotecaViewModel(repo)
    loop_principal(vm)

if __name__ == "__main__":
    main()

