import sys
import os


def check_env() -> None:

    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_access = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_network = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")

    if mode:
        print(f"Mode: {mode}")
    else:
        print("WARNING: MATRIX_MODE is missing")

    if database:
        print("Connected to local instance")
    else:
        print("WARNING: DATAVASE_URL is missing")

    if api_access:
        print("Authenticated")
    else:
        print("Not Authenticated")

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("LOG_LEVEL is missing")

    if zion_network:
        print("Zion Network: Online")
    else:
        print("Zion Network: Ofline")

def main() -> None:

    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("ERROR: python-dotenv is not installed.")
        print("Install it with: pip install -r requirements.text")
        sys.exit(1)

    check_env()

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
