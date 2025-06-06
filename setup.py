from setuptools import setup, find_packages

setup(
    name="quantum_gui",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyQt6",
        "qiskit",
        "matplotlib",
        "numpy",
        "scikit-learn",
        "scipy",
        "pandas",
        "networkx",
        "pytest",
        "pytest-qt",
        "pytest-cov",
        "coverage",
        "flake8",
        "black",
        "isort",
        "mypy",
        "pylint",
        #"sphinx",
        #"sphinx-rtd-theme",
        #"sphinx-autodoc-typehints",
        #"sphinxcontrib-napoleon",
        #"sphinxcontrib-plantuml",
        #"sphinxcontrib-graphviz",
        #"sphinxcontrib-bibtex",
        #"sphinxcontrib-htmlhelp",
        #"sphinxcontrib-jsmath",
    ],
    license="License.lic"
)