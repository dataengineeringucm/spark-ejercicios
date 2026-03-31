import os
import sys

import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session", autouse=True)
def spark():
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    spark = SparkSession.builder.master("local[2]").getOrCreate()
    return spark

