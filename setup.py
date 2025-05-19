try:
    from setuptools import setup, find_packages
except ImportError:
    # Fallback для случаев, когда Pylance не видит setuptools
    pass

setup(
    name="library_api",
    version="0.1",
    packages=find_packages(),
)
