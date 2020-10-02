
# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs, Request Features or Submit Feedback

Report bugs as a [GitHub issue](https://github.com/executablebooks/cookiecutter-jupyter-book/issues).

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

If you are proposing a feature, please include:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

### Improvements

Look through the (https://github.com/executablebooks/cookiecutter-jupyter-book/issues) for bugs, feature requests, etc and feel free to contribute!

## Get Started

Ready to contribute? Here's how to set up `cookiecutter-jupyter-book` for local development.

1. Fork the `cookiecutter-jupyter-book` repo on GitHub.
2. Clone your fork locally and install requirements:

```sh
git clone git@github.com:your_name_here/cookiecutter-jupyter-book.git
pip install -r requirements.txt
```

3. Create a branch for local development:

```sh
git checkout -b name-of-your-bugfix-or-feature
```

4. Make your desired changes, run tests, and push your branch to GitHub when you're ready:

```sh
pytest
black ./ --check
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

5. Open a pull request through the GitHub website. Naming convention for pull requests is [detailed here](https://github.com/executablebooks/.github/blob/main/CONTRIBUTING.md#commit-messages). For example, a pull request that adds a new feature might be titled: `✨ NEW: validate entered github username`.