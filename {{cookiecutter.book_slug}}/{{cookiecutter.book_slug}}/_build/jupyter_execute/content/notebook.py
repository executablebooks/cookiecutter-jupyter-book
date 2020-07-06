# An Example Jupyter Notebook

This notebook demonstrates a few of they key content types that can be included in a Jupyter Book. See the official [Jupyter Book](https://jupyterbook.org/intro.html) documentation for a more comprehensive look into the possible content types, structure and configuration of the book.

## Code

We can include code within our notebook that will be executed when the book is built. Any code output will be displayed in the rendered book.

import pandas as pd

print("Let's display a Pandas dataframe!")
pd.DataFrame({"Column 1": [1, 2, 3],
              "Column 2": [4.0, 5.0, 6.0],
              "Column 3": ["a", "b", "c"]})

In fact, these code blocks can even be executed by a Reader within the rendered Jupyter Book itself! Take a look at this [Jupyter Book documentation](https://jupyterbook.org/interactive/launchbuttons.html) to learn more!

## Images

In addition to Jupyter Notebook markdown, Jupyter Book supports a special flavor of markdown called MyST ([Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/)). MyST is essentially a markdown equivalent of the reStructuredText syntax and supports a broad range of more advanced functionality. For example, an image (with caption and a reference tag) can be included in a Jupyter Book using the following syntax:

````
```{figure} img/cookiecutter-jupyter-book-hex.png
---
width: 400px
name: cookiecutter-jupyter-book-hex
---
The cookiecutter-jupyter-book hex!
```
````

```{figure} img/cookiecutter-jupyter-book-hex.png
---
width: 400px
name: cookiecutter-jupyter-book-hex
---
The cookiecutter-jupyter-book hex!
```

## Admonitions

Admonitions can be used to highlight a particular block of text, for example a tip or a warning. The syntax for an admonition is as follows:

````
```{note}
Here is a note!
```
````

A full list of possible admonitions and other special content blocks can be seen in the [sphinx-book-theme documentation](https://sphinx-book-theme.readthedocs.io/en/latest/reference/demo.html). Here are just a few examples:

```{note}
I am a useful note!
```

```{tip}
I am a helpful tip!
```

```{warning}
I am a dire warning!
```

## References

Citations and bibliographies can be included in your book using references that are stored in the `references.bib` bibtex file included in this cookiecutter template using the following syntax:

```
{cite}`beuzen2019pybeach`
```

For example, `pybeach` {cite}`beuzen2019pybeach` is a Python package I published in the Journal of Open Source Software. 

We can even include multiple citations using this syntax:

```
{cite}`beuzen2019pybeach,beuzen2019variable`
```

For example, I've written a few pieces of Python software including `pybeach` and `CVNetica_VS` {cite}`beuzen2019pybeach,beuzen2019variable`.

We can include a bibliography of the entire bibtext file, like the one at the bottom of this page, using the following directive:

````
```{bibliography} ../references.bib
```
````



## Bibliography

```{bibliography} ../references.bib
```

