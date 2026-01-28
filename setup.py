from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ng20lda",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for 20newsgroups data processing and LDA topic modeling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ng20lda",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "scikit-learn>=1.0.0",
        "numpy>=1.20.0",
        "typer>=0.9.0",
        "fastapi>=0.110.0",
        "uvicorn>=0.27.0",
        "matplotlib>=3.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "hypothesis>=6.0.0",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ng20lda=ng20lda.cli.typer_app:app",
        ],
    },
)
