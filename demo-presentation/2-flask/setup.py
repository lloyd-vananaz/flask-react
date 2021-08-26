from setuptools import find_packages, setup

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Cors',
        'python-dotenv',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'pymysql',
        'WTForms-JSON',
        'flask-login',
        'email-validator',
        'flask-jwt-extended',
        'pytest',
        'coverage'
    ],
)