from setuptools import setup, find_packages

setup(
    name="trident_bpm",  # Name of your package
    version="0.1.0",
    description="A package for BPM-related tasks and modules",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(where="src"),  # Locate all packages inside src/
    package_dir={"": "src"},  # Specify the source directory
    install_requires=[
        "torch",
        "transformers",
        "pandas",
        "omegaconf",
        "scikit-learn",
        "lightning",
        "datasets",
        "pickle5",
    ],  # Add dependencies
    python_requires=">=3.8",  # Minimum Python version
)