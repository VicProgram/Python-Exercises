import importlib.metadata


def check_depen(dependencies_list: list[str]) -> bool:

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    all_present = True

    for lib in dependencies_list:
        try:
            version = importlib.metadata.version(lib)
            print(f"[OK] {lib} ({version}) - Ready to load.")

        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {lib} - Please install it.")
            all_present = False

    return all_present


def main() -> None:

    dependencies_list = ["pandas", "numpy", "matplotlib"]

    if check_depen(dependencies_list):

        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("Analyzing Matrix data...")

        data = np.random.randn(1000, 2)
        frame = pd.DataFrame(data, columns=['Axis X', 'Axis Y'])
        print(f"Processing {len(frame)} data points...")
        print("Generating visualization...")

        plt.scatter(frame['Axis X'], frame['Axis Y'], alpha=0.5, color='green')
        plt.title("Matrix Data Analysis")

        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    else:
        print("\nError: Missing dependencies.")
        print("To install with pip: pip install -r requirements.txt")
        print("To install with Poetry: poetry install")


# poetry env remove --all
# poetry cache clear --all pypi

if __name__ == "__main__":

    main()
