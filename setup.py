import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

# This call to setup() does all the work
setup(
    name='scribe-auth',
    version='0.1.0',
    description="Access Scribe's auth api for token management.",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/scribelabsai/authpy',
    author='Emmanuel Hadoux',
    author_email='emmanuel@scribelabs.ai',
    license='MIT',
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3 :: Only',
      'Development Status :: 4 - Beta',
      'Topic :: Security',
      'Topic :: Software Development :: Libraries',
      'Typing :: Typed'
    ],
    python_requires='>=3',
    packages=find_packages(exclude=('tests', '.github',)),
    install_requires=['requests'],
)