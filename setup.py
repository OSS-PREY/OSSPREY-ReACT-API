from setuptools import setup, find_packages

setup(
    name="react_extractor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "react_extractor=react_extractor.extractor:main"
        ]
    },
)
