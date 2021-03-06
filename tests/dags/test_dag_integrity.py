"""Test integrity of DAGs."""

import glob
import importlib.util
import os
import sys

import pytest
from airflow.models import DAG
from airflow.utils.dag_cycle_tester import test_cycle


DAG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "dags/**_dag.py")
# DAG_PATH = '/Users/sq/Projects/travel-jump/dags/activities_dag.py'
print(DAG_PATH)
DAG_FILES = glob.glob(DAG_PATH)
print(DAG_FILES)


@pytest.mark.parametrize("dag_file", DAG_FILES)
def test_dag_integrity(dag_file):
    """Import DAG files and check for DAG."""
    module_name, _ = os.path.splitext(dag_file)
    module_path = os.path.join(DAG_PATH, dag_file)
    mod_spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(mod_spec)
    mod_spec.loader.exec_module(module)

    dag_objects = [var for var in vars(module).values() if isinstance(var, DAG)]
    assert dag_objects

    for dag in dag_objects:
        # Test cycles
        dag.test_cycle()