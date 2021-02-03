import setuptools

with open('README.md', 'r') as f:
	long_description = f.read()

setuptools.setup(
    name='thorchain',
    version='0.0.1',
    description='THORChain library for Python',
    long_description=long_description,
    url='git@github.com:tirinox/thorchain.git',
    author='Maksim Koltsov',
    author_email='delevoper@tirinox.ru',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)