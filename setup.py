from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="email-automation-system",
    version="1.0.0",
    author="Eroniyom",
    author_email="eroniyom@example.com",
    description="Advanced email automation system with bulk sending and template management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eroniyom/email-automation-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Email",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "email-automation=email_automation:main",
        ],
    },
    keywords="email automation bulk sending smtp templates scheduling",
    project_urls={
        "Bug Reports": "https://github.com/Eroniyom/email-automation-system/issues",
        "Source": "https://github.com/Eroniyom/email-automation-system",
        "Documentation": "https://github.com/Eroniyom/email-automation-system#readme",
    },
)
