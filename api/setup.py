from setuptools import find_packages, setup

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.0.1',
        'Flask-Cors==3.0.10',
        # 'mysql-connector==2.2.9',
        # 'mysql-connector-python==8.0.26',
        'python-dotenv==0.19.0',
        'Flask-SQLAlchemy==2.5.1',
        # 'Flask-Migrate==3.0.1',
        'pymysql==1.0.2',
        'WTForms-JSON==0.3.3',
        'flask-login==0.5.0',
        'email-validator==1.1.3',
        'flask-jwt-extended==4.2.3'
    ],
)