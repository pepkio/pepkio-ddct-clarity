# pepkio-ddct-clarity

Python client for the Pepkio `ddct-clarity` REST API tool.

## Installation

```bash
pip install pepkio-ddct-clarity
```

## Quick Start

### Python API

```python
from pepkio_ddct_clarity import PepkioClient

client = PepkioClient(api_key="<your_api_key>")

# Fetch manifest
manifest = client.get_manifest()

# Run tool using a manifest example
inp = client.get_example_input("il6_livak_example")
result = client.run(inp)

print(result.status)
print(result.result)
```

### CLI

```bash
# Set API Key
export PEPKIO_API_KEY="<your_api_key>"

# Fetch manifest
pepkio-ddct-clarity manifest

# Run example
pepkio-ddct-clarity run --example il6_livak_example
```

## Environment Variables

- `PEPKIO_API_KEY`: Production API key for `https://tools.pepkio.com`.
- `LOCAL_PEPKIO_API_KEY`: Local API key for `https://tools.localtest.me`.
- `PEPKIO_API_BASE_URL`: Base URL (default: `https://tools.pepkio.com`).
