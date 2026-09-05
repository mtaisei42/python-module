import sys
import importlib


def check_dependencies() -> bool:
    packages = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
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
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")
        print("\nOr install with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")

    return missing_dependency


def analyze_data() -> None:
    import numpy 
    import pandas
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")

    signals = numpy.random.randint(0, 100, size=1000)
    print("Processing 1000 data points...")

    data = pandas.DataFrame({"signal_strength": signals})
    print("Generating visualization...")

    plt.figure(figsize=(10, 5))

    plt.plot(
        data.index,
        data["signal_strength"],
        color="green"
    )

    plt.title("Matrix Signal Analysis")
    plt.xlabel("Data Point")
    plt.ylabel("Signal Strength")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!\n"
          "Results saved to: matrix_analysis.png")

def main() -> None:

    if not check_dependencies():
        sys.exit(1)

    analyze_data()

    
main()

