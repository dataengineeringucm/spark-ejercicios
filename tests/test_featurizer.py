from datetime import datetime

from pyspark.sql import functions as F, SparkSession

from etl.featurizer import Featurizer


def test_preprocesa(spark: SparkSession):
    df = spark.createDataFrame(
        [("2025-01-31", 1035, 0.0, 35.0, None, None, None, None),
         ("2025-02-01", 830, 1.0, None, None, None, None, None)],
        schema="FlightDate string, DepTime int, Diverted float, " +
               "CarrierDelay float, WeatherDelay float, NASDelay float, SecurityDelay float, LateAircraftDelay float"
    )

    featurizer = Featurizer(spark, {})
    preprocesado_df = featurizer.preprocesa(df)

    f1, f2 = preprocesado_df.collect()

    assert(f1.Diverted is False and
           f1.WeatherDelay == 0.0 and f1.NASDelay == 0.0 and f1.SecurityDelay == 0.0 and f1.LateAircraftDelay == 0.0)

    assert(f2.Diverted is True and f2.CarrierDelay == 0.0 and
           f2.WeatherDelay == 0.0 and f2.NASDelay == 0.0 and f2.SecurityDelay == 0.0 and f2.LateAircraftDelay == 0.0)

    assert(preprocesado_df.dtypes[-1] == ("FlightTs", "timestamp"))  # la última pareja de la lista de tipos
    assert(f1.FlightTs == datetime(2025, 1, 31, 10, 35))
    assert(f2.FlightTs == datetime(2025, 2, 1, 8, 30))

    preprocesado_df.show()
