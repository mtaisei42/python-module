import sys
import importlib


def check_dependencies() -> bool:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready"
    }
    missing_dependency = True

    for package, description in packages.items():
        try:
            module = importlib.import_module(package)
            version = module.__version__
            print(f"[OK] {package} ({version}) - {description}")
        except ImportError:
            print(f"[ERROR] {package} is not installed")
            missing_dependency = False

    if not missing_dependency:
        print("\nInstall with pip, from the repository root:")
        print("pip install -r ex0/requirements.txt")
        print("\nOr install with Poetry:")
        print("cd ex0")
        print("poetry install")
        print("poetry run python loading.py")

    return missing_dependency


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    available = check_dependencies()

    print("\npip vs Poetry:")
    print("pip installs dependencies listed in requirements.txt.")
    print("Poetry manages dependencies declared in pyproject.toml.")
    print("Poetry records resolved versions in poetry.lock.")

    if not available:
        sys.exit(1)

    print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
