import json
from pathlib import Path

def test_resource_directory_has_required_fields():
    data = json.loads((Path(__file__).parents[1] / "resources.json").read_text(encoding="utf-8"))
    assert data
    required = {"name", "category", "description", "first_step", "url", "source_owner", "last_checked"}
    for item in data:
        assert required.issubset(item)
        assert item["url"].startswith("https://")
        assert item["last_checked"]

def test_resource_categories_are_nonempty():
    data = json.loads((Path(__file__).parents[1] / "resources.json").read_text(encoding="utf-8"))
    assert all(item["category"].strip() for item in data)
