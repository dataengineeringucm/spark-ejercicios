
from pyspark.sql import functions as F, SparkSession

from etl.featurizer import Featurizer


def test_preprocesa(spark: SparkSession):
    df = spark.createDataFrame(
        [("2025-01-31", 1035, 0.0, 35.0, None, None, None, None),
         ("2025-02-01", 830, 1.0, None, None, None, None, None)],
        ["FlightDate", "DepTime", "Diverted",
        "CarrierDelay", "WeatherDelay", "NASDelay", "SecurityDelay", "LateAircraftDelay"]
    )

    featurizer = Featurizer(spark, {})
    preprocesado_df = featurizer.preprocesa(df)

