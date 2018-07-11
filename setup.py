from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="create_airflow_user",
    version='0.1',
    author="Matthias Mintert",
    author_email="matthias@mintert.net",
    description="Small script to create airflow users via cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattfoxxx/create_airflow_user",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    py_modules=['create_airflow_user'],
    install_requires=[
        'Click',
        'apache-airflow>=1.8',
    ],
    entry_points={
        'console_scripts': [
            'create_airflow_user=create_airflow_user.create_user:create_user',  # command=package.module:function
        ],
    },
)

