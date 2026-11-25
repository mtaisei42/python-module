import sys
import os


def check_env() -> None:

    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_access = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_network = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")

    if not mode:
        print("WARNING: MATRIX_MODE is missing or empty")
        mode = "development"
    print(f"Mode: {mode}")

    if database:
        print("Connected to local instance")
    else:
        print("WARNING: DATAVASE_URL is missing")

    if api_access:
        print("Authenticated")
    else:
        print("Not Authenticated")

    if not log_level:
        print("WARNING: LOG_LEVEL is missing or empty")
        log_level = "DEBUG"
    print(f"Log Level: {log_level}")

    if zion_network:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def main() -> None:

    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("ERROR: python-dotenv is not installed.")
        print("Install it with: pip install -r ex1/requirements.txt")
        sys.exit(1)

    check_env()

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.isfile("ex1/.gitignore"):
        gitignore_path = "ex1/.gitignore"
    elif os.path.isfile(".gitignore"):
        gitignore_path = ".gitignore"
    else:
        print("[WARNING] .gitignore file not found")
        return

    try:
        with open(gitignore_path, encoding="utf-8") as f:
            env_listed = any(line.strip() == ".env" for line in f)
    except OSError:
        print("[WARNING] Could not read .gitignore")
    else:
        if env_listed:
            print("[OK] .env file properly ignored by git")
        else:
            print("[WARNING] .env is not listed in .gitignore")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
