# Pepkio DDCT Clarity

Perform automated RT-qPCR relative gene expression calculations using Livak $2^{-\Delta\Delta C_t}$ and Pfaffl models with multi-reference gene geometric normalization and Gaussian error propagation from Python scripts and pipelines.

# What It Does

Processing real-time quantitative PCR (RT-qPCR) data in spreadsheets often leads to mathematical errors during logarithmic error propagation, reference gene normalization, and efficiency correction.

**Pepkio DDCT Clarity** standardizes relative gene expression analysis by providing a programmatic computational engine. It ingests raw $C_t$ / $C_q$ values, normalizes target genes against single or multiple reference genes via geometric mean averaging, applies either the standard Livak ($2^{-\Delta\Delta C_t}$) model or the Pfaffl efficiency-corrected model, detects technical replicate outliers, and calculates fold-change values with asymmetric confidence intervals.

Programmatic runs connect to the Pepkio Tools API. An API key is required for executing analyses.

# Features

- **Dual Quantification Models:** Standard Livak $2^{-\Delta\Delta C_t}$ (assuming 100% efficiency) and Pfaffl efficiency-corrected model for custom primer pair efficiencies ($E = 10^{-1/\text{slope}}$).
- **Multi-Reference Gene Normalization:** Normalize target genes against single or geometric mean of multiple housekeeping genes (*GAPDH*, *ACTB*, *18S*, etc.) following MIQE guidelines.
- **Gaussian Error Propagation:** Propagate variance across technical and biological replicates to compute exact asymmetric upper and lower fold-change confidence bounds ($2^{-(\Delta\Delta C_t \pm SE)}$).
- **Outlier Detection:** Flag high-variance technical replicates ($\Delta C_t$ standard deviation $> 0.5$) for dataset quality control.
- **Python API & CLI:** Access via `PepkioClient` Python SDK or the `pepkio-ddct-clarity` command-line utility.
- **Built-in Examples:** Inspect tool manifests and run pre-configured qPCR datasets without manual payload construction.

# Installation

```bash
pip install pepkio-ddct-clarity
```

Set an API key with `tools:run` scope before executing analysis runs:

```bash
export PEPKIO_API_KEY="your-key"
```

Obtain an API key from your [Pepkio Account API Keys](https://www.pepkio.com/account/api-keys) settings.

# Quick Example

```python
import os
from pepkio_ddct_clarity import PepkioClient

# Initialize client with API key from environment
with PepkioClient() as client:
    # Load default qPCR dataset example
    inp = client.get_example_input("default_ddct")
    
    # Run relative quantification analysis
    result = client.run(inp)
    
    if result.result:
        print("Target Gene:", result.result.get("target_gene"))
        print("Fold Change (2^-ddCt):", result.result.get("fold_change"))
        print("Delta Delta Ct:", result.result.get("ddct"))
```

CLI command:

```bash
pepkio-ddct-clarity run --example default_ddct
```

Manifest inspection (`pepkio-ddct-clarity manifest`) does not require an API key.

# Typical Use Cases

- Quantifying target gene fold-change across drug treatment, siRNA knockdown, or gene overexpression conditions
- Orthogonal RT-qPCR validation of differentially expressed genes (DEGs) identified in RNA-seq studies
- Benchmarking reference gene stability and normalizing with multi-housekeeping gene panels
- Calculating primer pair amplification efficiencies from serial dilution standard curves
- Automating 96-well and 384-well qPCR plate data processing in LIMS or Python bioinformatic pipelines

# Scientific Background

Relative quantification calculates the fold change in expression of a target gene in treated samples relative to a control calibrator sample, adjusted for total RNA input using reference genes.

- **Livak ($2^{-\Delta\Delta C_t}$) Method:** Assumes equal, 100% amplification efficiency ($E=2$) for target and reference genes. $\Delta C_t = C_{t,\text{target}} - C_{t,\text{reference}}$, and $\Delta\Delta C_t = \Delta C_{t,\text{treated}} - \Delta C_{t,\text{control}}$.
- **Pfaffl Method:** Accounts for gene-specific amplification efficiencies ($E = 10^{-1/\text{slope}}$) calculated from standard curves: $\text{Ratio} = (E_{\text{target}}^{\Delta C_{t,\text{target}}}) / (E_{\text{ref}}^{\Delta C_{t,\text{ref}}})$.
- **Error Propagation:** Technical replicate standard deviations combine via quadrature ($s_{\Delta C_t} = \sqrt{s_{\text{target}}^2 + s_{\text{ref}}^2}$). Because fold change is exponential, reporting symmetric errors is mathematically invalid; asymmetric upper and lower confidence limits ($2^{-(\Delta\Delta C_t \pm SE)}$) represent true variance bounds.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/ddct-clarity

The web application includes interactive 96/384-well plate visualizers, graphical fold-change charts, printable bench worksheets, and shareable permalinks to reload saved analysis states.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-ddct-clarity

Web Application: https://www.pepkio.com/tools/ddct-clarity

# About Pepkio

Pepkio develops software tools and provides bioinformatics analysis services for life science research. See https://www.pepkio.com for additional tools and services.

# Keywords

ddct clarity, qPCR relative quantification, 2^-ddCt calculator, Livak method, Pfaffl method, RT-qPCR fold change, cycle threshold, Cq value normalization, housekeeping gene normalization, multi-reference gene, geometric mean normalization, MIQE compliance, primer efficiency calculation, error propagation qPCR, asymmetric confidence intervals, replicate outlier detection, RNA-seq validation, gene expression quantification, delta delta Ct, Python qPCR API, pepkio-ddct-clarity, real-time PCR calculation, qPCR plate analysis, gene knockdown quantification, differential gene expression, how to calculate 2^-ddCt in Python, RT-qPCR multi reference gene normalization, Pfaffl efficiency corrected relative quantification, propagate standard deviation in qPCR fold change, calculate delta delta Ct with multiple housekeeping genes, qPCR technical replicate outlier detection threshold, validate RNA-seq DEG results with RT-qPCR, MIQE compliant qPCR relative expression pipeline, automated qPCR delta delta Ct calculator API, calculate asymmetric error bounds for gene fold change, Python package for real-time PCR relative quantification, bulk qPCR plate reader data analysis in Python
