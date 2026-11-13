# Pepkio DDCT Clarity

Run containerized RT-qPCR relative quantification using Livak 2^-ΔΔCt and Pfaffl models with multi-reference normalization via the Pepkio API without local Python setup.

# What It Does

The image runs `pepkio-ddct-clarity`, a command-line client for the Pepkio DDCT Clarity REST API. It standardizes relative gene expression calculations by ingesting raw Ct / Cq values, normalizing target genes against single or multiple reference controls via geometric mean averaging, evaluating technical replicate consistency, and computing fold-change values with asymmetric confidence intervals using either the Livak ($2^{-\Delta\Delta C_t}$) or Pfaffl efficiency-corrected model.

Relative quantification workflows support drug response profiling, siRNA/CRISPR knockdown validation, differential expression verification from RNA-seq studies, and biomarker screening. Computation runs on Pepkio servers; provide a network connection and an API key with `tools:run` scope for `run` commands.

# Features

- Dual quantification models: standard Livak $2^{-\Delta\Delta C_t}$ (100% efficiency) and Pfaffl efficiency-corrected model for custom primer pair efficiencies
- Multi-reference gene geometric normalization adhering to MIQE guidelines
- Exact asymmetric Gaussian error propagation across technical and biological replicates
- Technical replicate outlier detection flagging high-variance replicates ($\Delta C_t$ standard deviation $> 0.5$)
- Preconfigured manifest examples (`il6_livak_example`, `no_target_gene_blocks`)
- Manifest inspection without an API key

# Quick Start

```bash
docker pull pepkio/ddct-clarity:0.1.0
docker run --rm -e PEPKIO_API_KEY="your-key" pepkio/ddct-clarity:0.1.0 \
  run --example il6_livak_example
```

Manifest only (no API key):

```bash
docker run --rm pepkio/ddct-clarity:0.1.0 manifest --examples
```

Set `PEPKIO_API_BASE_URL` to override the API host (default: `https://tools.pepkio.com`). Create an API key with **tools:run** scope at https://www.pepkio.com/account/api-keys.

# Quick Example

Execute relative quantification using the built-in `il6_livak_example` dataset:

```bash
export PEPKIO_API_KEY="your-key"

docker run --rm \
  -e PEPKIO_API_BASE_URL=https://tools.pepkio.com \
  -e PEPKIO_API_KEY="$PEPKIO_API_KEY" \
  pepkio/ddct-clarity:0.1.0 run --example il6_livak_example
```

# Typical Use Cases

- Quantifying target gene fold changes across drug treatments, genetic knockdowns, or disease models
- Orthogonal RT-qPCR validation of differentially expressed genes identified from transcriptomic RNA-seq screens
- Housekeeping gene stability evaluation and multi-reference geometric mean normalization
- Adjusting relative quantification with measured primer amplification efficiencies
- Automated qPCR plate processing in bioinformatics workflows, CI/CD runners, and containerized pipelines

# Scientific Background

Relative quantification determines the fold change of target gene expression in experimental samples compared to a calibrator control group, normalized against endogenous reference genes.

The Livak ($2^{-\Delta\Delta C_t}$) method assumes equal, near-100% amplification efficiency ($E=2$) across all reactions, calculating $\Delta C_t = C_{t,\text{target}} - C_{t,\text{reference}}$ and $\Delta\Delta C_t = \Delta C_{t,\text{treated}} - \Delta C_{t,\text{control}}$. The Pfaffl model corrects for experimental primer efficiencies ($E = 10^{-1/\text{slope}}$) measured from standard curves. Because fold change is an exponential transformation, error propagation in linear space is mathematically invalid; computing asymmetric confidence intervals ($2^{-(\Delta\Delta C_t \pm SE)}$) accurately captures biological and technical variance bounds.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/ddct-clarity

The web application adds interactive 96/384-well plate visualizers, graphical fold-change charts, plate QC heatmaps, printable bench worksheets, and shareable permalinks.

# Documentation and Resources

GitHub Repository (source and Dockerfile): https://github.com/pepkio/pepkio-ddct-clarity

Web Application: https://www.pepkio.com/tools/ddct-clarity

PyPI Package: https://pypi.org/project/pepkio-ddct-clarity/

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

A semantic, AI-native version of this document in the K2F format is available at https://k2f.dev (https://k2f.dev/v/afe18aa1bbae6fb19ca7dd6d6ac2c7e442a629d4b2679c201c6e94e19e6426f2)
