# Learning Transformers

A learning environment for transformers to interfere a large language model (LLM).

## Installation

### 1. Install Git and Conda

Download and install the latest versions:

* [Git](https://git-scm.com/downloads)
* [Git Large File Storage](https://git-lfs.com)
* [Miniconda](https://conda.io/projects/conda/en/stable/user-guide/install)

### 2. Clone the repository from GitHub

Clone the repository to a nice place on your machine via:

```Shell
git clone https://github.com/countzero/learning_transformers
```

### 3. Create a new Conda environment

Create a new Conda environment for this project with a specific version of Python:

```Shell
conda create --name learning_transformers python=3.10
```

### 4. Initialize Conda for shell interaction

To make Conda available in you current shell execute the following:

```Shell
conda init
```

**Hint:** You can always revert this via `conda init --reverse`.

### 5. Activate the Conda environment

And activate the new environment via:

```Shell
conda activate learning_transformers
```

### 6. Install all dependencies

Within the working directory of the repository and inside the `learning_transformers` Conda Environment execute the following to install all required Python packages:

```Shell
pip install --requirement ./requirements.txt
```

### 7. Download a large language model

Download a large language model (LLM) with weights in the pytorch format into the `./models` directory. You can for example download the [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b) model:

```Shell
git clone https://huggingface.co/tiiuae/falcon-7b-instruct ./models/falcon-7b-instruct
git lfs pull
```

**Hint:** See the [🤗 Open LLM Leaderboard]https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard for best in class open source large language models.

## Usage

### Execute

```Shell
python ./main.py
```

### Benchmark

You can measure the execution time on your machine with the following commands:

#### Unix

```Bash
time python ./main.py
```

#### Windows

```PowerShell
Measure-Command { python .\main.py | Out-Host }
```
