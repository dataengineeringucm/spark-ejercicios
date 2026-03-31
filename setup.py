from setuptools import setup, find_packages

setup(
    name="spark-flights-etl",
    version="0.1.0",
    author="Master Data Engineering UCM",
    author_email="alumno@ucm.es",
    description="Ejemplos de transformaciones sobre vuelos",
    long_description="Paquete de ejemplos de transformaciones con datos de vuelos",
    long_description_content_type="text/markdown",
    url="https://github.com/nombrealumno",
    python_requires=">=3.11",
    packages=find_packages(),
    package_data={}
)
