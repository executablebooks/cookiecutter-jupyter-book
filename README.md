# Cookiecutter-Jupyter-Book

![tests](https://github.com/UBC-MDS/cookiecutter-jupyter-book/workflows/tests/badge.svg)

<p align="center">
  <img src="logo.png" width="160">
</p>

A cookiecutter template for creating a simple [Jupyter Book](https://jupyterbook.org/intro.html). See the rendered version of this cookiecutter template [here](https://ubc-mds.github.io/cookiecutter-jupyter-book/content/introduction.html).

## Usage

1. Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/1.7.2) if you haven't installed it yet:

```bash
pip install -U cookiecutter
```

2. Use `cookiecutter-jupyter-book` to generate a Jupyter Book template and fill out the requested information (default templating values are shown in square brackets `[]` and will be used if no other information is entered):

```bash
cookiecutter git@github.com:UBC-MDS/cookiecutter-jupyter-book.git

full_name [Captain Planet]: Tomas Beuzen
github_username [tomasbeuzen]:
book_name [my-book]:
book_slug [my_book]:
book_short_description [This cookiecutter creates a simple boilerplate for a Jupyter Book.]: My first Jupyter Book!
version ['0.1.0']:
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
Choose from 1, 2, 3, 4, 5 [1]:
Select include_github_actions:
1 - yes
2 - no
Choose from 1, 2 [1]:
```

3. Install the Jupyter Book package requirements from the `requirements.txt` file (it is recommended to do this in a virtual environment, e.g., using [conda](https://docs.conda.io/en/latest/)):

```
$ conda create --name mybook python=3.8 -y
$ conda activate mybook
$ pip install -r requirements.txt
```

4. Build the HTML render of your Jupyter Book:

```
$ jupyter-book build my_book/
```

5. View your rendered book in `my_book/_build/html/index.html`.

6. Make edits to your book by adding more content, updating the table of contents in `my_book/_toc.yml`, and and/or by editing the configuration file `my_book/_config.yml`. See the [Jupyter Book documentation](https://jupyterbook.org/intro.html) for more information on customizing your book.

7. `cookiecutter-jupyter-book` comes with a GitHub Actions workflow to help easily deploy your book online with the free [GitHub Pages](https://pages.github.com/) services. This workflow file would have been included in your directory structure if you chose `yes` for `Select include_github_actions` in Step 2 above. When ready to deploy your book online:
   1. Make sure your book builds locally as expected (`jupyter-book build my_book/`) and that you have updated the `requirements.txt` file to include any additional packages required to build your book;
   2. Create a new [GitHub repository](https://github.com/new) to host your book;
   3. Push your book (including the `.github` hidden directory) to your GitHub repository. The GitHub Actions workflow provided with the cookiecutter (`my_book/.github/workflows/deploy.yml`) will automatically deploy your book to the `gh-pages` branch of your repository. You may need to go to the `Settings` tab of your repository and under the **GitHub Pages** heading, choose the `gh-pages branch` from the **Source** drop-down list. For alternative methods of deploying your book online, see the See the [Jupyter Book documentation](https://jupyterbook.org/intro.html).

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/cookiecutter-jupyter-book/graphs/contributors).

## Acknowledgements

This template was inspired and made possible by the [Cookiecutter project](https://github.com/cookiecutter/cookiecutter) and the [Jupyter Book project](https://github.com/executablebooks/jupyter-book).
