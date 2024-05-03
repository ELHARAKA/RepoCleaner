from setuptools import setup, find_packages

setup(
    name='repocleaner',
    version='1.0.1',
    packages=find_packages(),
    description='A utility to manage GitHub repositories',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Fahd El Haraka',
    author_email='fahd@web3dev.ma',
    url='https://github.com/ELHARAKA/RepoCleaner',
    license='MIT',
    install_requires=[
        'pyfiglet', 'requests'
    ],
    entry_points={
        'console_scripts': [
            'repocleaner=repocleaner:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.10',
)