import sys
import os
from dotenv import load_dotenv


def main() -> None:

    required_variables: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
    ]

    config:  dict[str: str] ={}

    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...")


    for variable_name in required_variables:
        value = os.getenv(variable_name)

        if not value:
            print(f"WARNING {variable_name} is not required")

        else:
            config[variable_name] = value

    if len(config) != 5:
        print()

    
