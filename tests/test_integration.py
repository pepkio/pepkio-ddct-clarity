"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_ddct_clarity.client import PepkioClient

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, base_url = request.param
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(
            f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)"
        )
    if "localtest.me" in base_url:
        import httpx

        try:
            r = httpx.get(
                f"{base_url}/api/tools/v1/tools/ddct-clarity/manifest",
                headers={"Authorization": f"Bearer {api_key}"},
                timeout=2.0,
                verify=False,
            )
            if r.status_code >= 500:
                pytest.skip(f"Local dev server at {base_url} returned {r.status_code}")
        except httpx.RequestError:
            pytest.skip(f"Local dev server at {base_url} is unreachable")

    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "ddct-clarity"
    names = live_client.list_examples()
    assert "il6_livak_example" in names


def test_run_il6_livak_example(live_client: PepkioClient):
    inp = live_client.get_example_input("il6_livak_example")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert result.result.get("method") == "livak"
    assert result.result.get("has_blocking_errors") is False
    assert result.result.get("error") is None
