import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

DATA_PATH = Path(__file__).parents[1] / "resources.json"
REQUIRED_FIELDS = {
    "name",
    "category",
    "description",
    "first_step",
    "url",
    "source_owner",
    "last_checked",
    "keywords",
}


def load_resources():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def test_resource_directory_has_required_fields():
    data = load_resources()
    assert data, "The resource directory must not be empty."

    for item in data:
        assert REQUIRED_FIELDS.issubset(item), item.get("name", "unnamed resource")
        for field in REQUIRED_FIELDS - {"keywords"}:
            assert isinstance(item[field], str) and item[field].strip(), (item, field)


def test_resource_urls_are_secure_and_well_formed():
    for item in load_resources():
        parsed = urlparse(item["url"])
        assert parsed.scheme == "https", item["url"]
        assert parsed.netloc, item["url"]


def test_resource_names_are_unique():
    names = [item["name"].strip().casefold() for item in load_resources()]
    assert len(names) == len(set(names))


def test_resource_categories_and_keywords_are_usable():
    data = load_resources()
    assert all(item["category"].strip() for item in data)
    assert all(isinstance(item["keywords"], list) for item in data)
    assert all(item["keywords"] for item in data)


def test_review_dates_use_iso_format_and_are_not_future_dated():
    today = date.today()
    for item in load_resources():
        reviewed = date.fromisoformat(item["last_checked"])
        assert reviewed <= today, (item["name"], item["last_checked"])


def test_directory_covers_core_support_areas():
    categories = {item["category"] for item in load_resources()}
    assert "Housing & relocation" in categories
    assert "Family readiness" in categories
    assert "Spouse careers & education" in categories
    assert "Food & essential needs" in categories
    assert "Financial support" in categories
