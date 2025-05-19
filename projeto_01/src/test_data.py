import pytest
import pandas as pd

@pytest.fixture(scope="session")
def data():
  local_path = "clean_data.csv"
  df = pd.read_csv(local_path)
  return df

def test_data_length(data):
  assert len(data) == 894

def test_number_of_columns(data):
  assert data.shape[1] == 14

def test_column_presence_and_type(data):
  required_columns = {
      "age":pd.api.types.is_int64_dtype,
      "sex":pd.api.types.is_int64_dtype,
      "cp":pd.api.types.is_int64_dtype,
      "trestbps":pd.api.types.is_object_dtype,
      "chol":pd.api.types.is_object_dtype,
      "fbs":pd.api.types.is_object_dtype,
      "restecg":pd.api.types.is_object_dtype,
      "thalachh":pd.api.types.is_object_dtype,
      "exang":pd.api.types.is_object_dtype,
      "oldpeak":pd.api.types.is_float_dtype,
      "slope":pd.api.types.is_object_dtype,
      "ca":pd.api.types.is_object_dtype,
      "thal":pd.api.types.is_object_dtype,
      "target":pd.api.types.is_int64_dtype
  }

  assert set(data.columns.values).issuperset(set(required_columns.keys()))
  for col_name, format_verification_funct in required_columns.items():
    assert format_verification_funct(data[col_name]), f"Column {col_name} failed test {format_verification_funct.__name__}"


