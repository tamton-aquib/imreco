from setuptools import setup

setup(
    name = 'imreco',
    packages = ['imreco'],
    version = '0.0.3',
    license = 'MIT',
    description = 'A cli program to resize images and convert between different formats.',
    long_description = "Read docs at https://github.com/tamton-aquib/imreco",
    author = 'aquib',
    author_email = 'aquibjavedt007@gmail.com',
    url = 'https://github.com/tamton-aquib/imreco',
    # download_url = 'https://github.com/tamton-aquib/imreco/archive/v_001.tar.gz',
    keywords = ['image', 'resizer', 'converter'],
    install_requires = [
        'opencv-python',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        ],
    )
