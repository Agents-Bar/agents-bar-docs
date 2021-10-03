# Agents Bar Docs

## Working

Parts of the documentation reference the [agents-bar](https://pypi.org/project/agents-bar/) python client.
Make sure you're always referring to the latest version of the package.

In case you're working on both documentations at the same time then to avoid empty pushes to pip
it's recommended to build `agents-bar` locally, e.g. `python -m build` and then install
package via

```sh
$ pip install agents-bar --no-index --find-links file:///path/to/agents-bar-client-python/dist/
```

## Development

### Local

It's recommended to create local virtual environment for Python and install all necessary dependencies from `requirements.txt`.
Then, to build in that environment, execute `make html` command.
This will create a directory `_build/html` which contains static htmls files for the doc.
To view the page one can either open the `_build/html/index.html` in browser or set a static file server.

### Docker

The page is eventually converted into deployable Docker image so it's also important to test that everything works nicely as an image.
To test, build and run, and check that changes are ok.

Build from root dir:
```bash
$ docker build -t agents-bar-docs .
```
and then you run with
```
$ docker run -it -p 80:80 agents-bar-docs
```

Now, go to http://localhost:1234 and navigate to your changes.
