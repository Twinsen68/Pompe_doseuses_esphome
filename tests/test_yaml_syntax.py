import yaml
from pathlib import Path
import pytest

# Recursively collect YAML files
yaml_files = [
    p for p in Path('.').rglob('*.yaml')
    if '.git' not in p.parts and 'venv' not in p.parts and '.venv' not in p.parts
]

@pytest.mark.parametrize('yaml_path', yaml_files)
def test_yaml_syntax(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        yaml.safe_load(f)

