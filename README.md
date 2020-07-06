# Cookiecutter-Jupyter-Book

Cookiecutter template for creating a simple [Jupyter Book](https://jupyterbook.org/intro.html).

## Usage

1. Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/1.7.2) if you haven't installed it yet:

```
$ pip install -U cookiecutter
```

2. Use cookiecutter-jupyter-book to generate a Jupyter Book template:

```
$ cookiecutter git@github.com:UBC-MDS/cookiecutter-jupyter-book.gi
```

3. Install the Jupyter Book cookiecutter template package requirements from the requirement.txt file (it is recommended to do this in a virtual environment, e.g., using conda):

```
$ conda create --name my-book python=3.7 -y
$ conda activate my-book
$ pip install -r requirements.txt
```

4. Try building the html render of the Jupyter Book cookiecutter template:

```
$ jupyter-book build my_book/
```

5. View the rendered book in `my_book/_build/html/index.html`.

6. Make edits to the book.

7. When ready to deploy the book online, simply push the book (including the `.github` hidden directory) to a GitHub repository. The GitHub Actions workflow provided with the cookiecutter (`my_book/.github/workflows/build-and-deploy.yml`) will automatically build and deploy your book to the `gh-pages` branch of your repository. You may need to go to the `Settings` tab of your repository and under the **GitHub Pages** heading, choose the `gh-pages branch` from the **Source** drop-down list.


## Acknowledgements

This template was inspired and made possible by the [Cookiecutter project](https://github.com/cookiecutter/cookiecutter) and the [Jupyter Book project](https://github.com/executablebooks/jupyter-book).
