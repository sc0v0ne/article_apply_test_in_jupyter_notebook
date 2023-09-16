## Article apply test in jupyter notebook

I created this project to redo a college project. Where I applied methods from the refactoring book.

[Post Dev.to](https://dev.to/sc0v1n0/applying-tests-to-jupyter-notebook-functions-and-refactoring-old-code-p76)

📗 Book: [Refactoring - Improving the design of existing code - Martin Fowler](https://www.amazon.com/-/pt/dp/B087N8LKYB/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=M4T29CCKD30E&keywords=refatora%C3%A7%C3%A3o&qid=1651322207&sprefix=refatora%C3%A7%C3%A3o%2Caps%2C203&sr=8-1)

> FOWLER, Martin. “Replace Query with Parameter” no código. *In*: REFATORAÇÃO: Aperfeiçoando o design de códigos existentes. 2. ed. [*S. l.*: *s. n.*], 2019. cap. 11.
> 

**Inicialize this project:**

- Poetry installed

- 2º step:

```bash

poetry shell

```

- 3º step:

```bash

poetry install

```

- 4º step:

```bash

jupyter notebook

```

- 5º step tests:

```bash

pytest -v

```

**Update warning notebook:**

Warning:

```bash

.venv/lib/python3.9/site-packages/jupyter_client/connect.py:20
  /home/machine_user/Documents/projects_github/replace_query_with_parameter/.venv/lib/python3.9/site-packages/jupyter_client/connect.py:20: DeprecationWarning: Jupyter is migrating its paths to use standard platformdirs
  given by the platformdirs library.  To remove this warning and
  see the appropriate new directories, set the environment variable
  `JUPYTER_PLATFORM_DIRS=1` and then run `jupyter --paths`.
  The use of platformdirs will be the default in `jupyter_core` v6
    from jupyter_core.paths import jupyter_data_dir, jupyter_runtime_dir, secure_write

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

```

Execute in terminal:

```bash

export JUPYTER_PLATFORM_DIRS=1

```

```bash

jupyter --paths

```
