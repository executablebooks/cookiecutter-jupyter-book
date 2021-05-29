# Change Log

## v0.8 2020-05-29

- 🔧 MAINTAIN: support new toc format (@TomasBeuzen) (PR: #26)
- 🔧 MAINTAIN: update templating files from Jupyter Book repo (@TomasBeuzen) (PR: #24)

## v0.7 2020-10-02

- 🔧 MAINTAIN: change "master" to "main" for this repo and all CC templates (@TomasBeuzen) (PR: #22)

## v0.6 2020-10-02

General improvement to the repo in this version, with updated docs and new tests. We've also added preliminary support for GitLab CI.

- ✨ NEW: CC now includes a `.gitlab-ci.yml` (thanks @slemonide & acknowledgements to @bsamadi for the source file) (PR: #9)
- ✨ NEW: adding new test regime using pytest (@TomasBeuzen) (PR: #19)
- ✨ NEW: validate entered github username on github.com (@TomasBeuzen) (PR: #5)

- 👌 IMPROVE: CC is now more host-agnostic, supporting both GitHub and GitLab, with various changes to the .json file and post-gen script. The goal is to improve support fot GitLab as its support in JupyterBook grows (PR: )
- 👌 IMPROVE: add "None" option to licenses (@TomasBeuzen) (PR: #17)
- 👌 IMPROVE: change "full_name" to "author_name" in CC json for clarity (@TomasBeuzen) (PR: #2)
  
- 🐛 FIX: bad reference in LICENSE (@TomasBeuzen) (PR: #16)
- 🐛 FIX: Need to have `-r` when installing from requirements.txt (@slemonide) (PR: #8)
  
- 🔧 MAINTAIN: update book template to latest Jupyter Book files (@TomasBeuzen) (PR: #11)
  
- 📚 DOCS: update contributing docs (@TomasBeuzen) (PR: #6, #16) 
- 📚 DOCS: fix typo in markdown.md (@westurner) (PR: #12)
- 📚 DOCS: add changelog (@TomasBeuzen) (PR: #20)

## v0.1 - v0.5

- Preliminary works
