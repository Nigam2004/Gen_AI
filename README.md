## Install Miniconda

Download and install **Miniconda** from the official website:

[Download Miniconda](https://www.anaconda.com/download/success?reg=skipped-miniconda&utm_source=chatgpt.com)

## Configure Miniconda for Git Bash

After installing Miniconda, open **Git Bash** and run:

```bash
~/miniconda3/Scripts/conda.exe init bash
```

Close and reopen **Git Bash**.

### Check Conda Installation

Run:

```bash
conda --version
```

You should see something similar to:

```text
conda 25.x.x
```

### Activate the Conda Environment

If your environment is named `venv`, activate it using:

```bash
conda activate venv
```

If `venv` is a **Python virtual environment created using `python -m venv`**, do **not** use `conda activate venv`. Instead, use:

```bash
source venv/Scripts/activate
```

> **Important:** `conda activate venv/` is valid only when `venv` is a Conda environment, not when it was created with `python -m venv`.

