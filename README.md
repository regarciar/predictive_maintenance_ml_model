# predictive_maintenance_ml_model

Machine learning model applied to failure prediction and remaining useful life estimation

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

---

<body>
    <h2> <b> How to Run </b> </h2>
    <p>
    <ol>
        <li> Clone this repository. </li>
        <li> Execute the following instruccions inside of project root directory (predictive maintenance ml model folder
        ). </li>
        <li> Install/ update pip. </li>
    </ol>
    </p>
</body>

<b> On Windows </b>

    To install
        python get-pip.py
    To upgrade
        python -m pip install -U pip

<b> On Linux </b>

    To install
        sudo apt-get install python-pip
    To upgrade
        sudo pip install -U pip

<body>
    <p>
    <ol type="1" start="4">
        <li> Install/ update virtualenv. </li>
    </ol>
    </p>
</body>

<b> On Windows </b>

    To install
        pip install virtualenv
    To upgrade
        pip install virtualenv --upgrade

<b> On Linux </b>

    To install
        sudo pip3 install virtualenv
    To upgrade
        sudo pip3 install virtualenv --upgrade

<body>
    <p>
    <ol type="1" start="5">
        <li> Create virtual environment. </li>
    </ol>
    </p>
</body>

    python3 -m venv model_dependencies

<body>
    <p>
    <ol type="1" start="6">
        <li> Activate virtual enviroment. </li>
    </ol>
    </p>
</body>

    source model_dependencies/bin/activate

<body>
    <p>
    <ol type="1" start="7">
        <li> Install all projects dependencies. </li>
    </ol>
    </p>
</body>

    pip install --default-timeout=100 future -r requirements.txt

<body>
    <p>
    <ol type="1" start="8">
        <li> Deactivate virtual enviroment. </li>
    </ol>
    </p>
</body>

    deactivate
