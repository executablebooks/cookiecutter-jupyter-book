# Cookiecutter-Jupyter-Book

![Build](https://github.com/UBC-MDS/cookiecutter-jupyter-book/workflows/Build/badge.svg)

<img align="right" src="{{cookiecutter.book_slug}}/{{cookiecutter.book_slug}}/content/img/cookiecutter-jupyter-book-hex.png" width="200">

A cookiecutter template for creating a simple [Jupyter Book](https://jupyterbook.org/intro.html). See the rendered version of this cookiecutter template [here](https://ubc-mds.github.io/cookiecutter-jupyter-book/content/introduction.html).

<br>
<br>
<br>

## Usage

1. Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/1.7.2) if you haven't installed it yet:

```
$ pip install -U cookiecutter
```

2. Use cookiecutter-jupyter-book to generate a Jupyter Book template:

```
$ cookiecutter git@github.com:UBC-MDS/cookiecutter-jupyter-book.git
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

6. Now that everything is working, you can make edits to your book by, most simply, adding pages to `my_book/content/` directory and updating the table of contents in `my_book/_toc.yml`. See the [Jupyter Book documentation](https://jupyterbook.org/intro.html) for more information on customizing your book.

7. When ready to deploy the book online, make sure your book renders locally as expected (`$ jupyter-book build my_book/`) and that you have updated the requirements.txt file to include any additional packages required to build your book. Simply push the book (including the `.github` hidden directory) to a GitHub repository. The GitHub Actions workflow provided with the cookiecutter (`my_book/.github/workflows/build-and-deploy.yml`) will automatically build and deploy your book to the `gh-pages` branch of your repository. You may need to go to the `Settings` tab of your repository and under the **GitHub Pages** heading, choose the `gh-pages branch` from the **Source** drop-down list. For alternative methods of deploying your book online, see the See the [Jupyter Book documentation](https://jupyterbook.org/intro.html).

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/cookiecutter-jupyter-book/graphs/contributors).

## Acknowledgements

This template was inspired and made possible by the [Cookiecutter project](https://github.com/cookiecutter/cookiecutter) and the [Jupyter Book project](https://github.com/executablebooks/jupyter-book).
