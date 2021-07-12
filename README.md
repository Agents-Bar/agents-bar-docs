# Agents Bar Docs

## Working

Parts of the documentation reference the `agents-bar-client-python` python client.
Make sure you're always referring to the latest version of the package.

In case you're working on both documentations at the same time then to avoid empty pushes to pip
it's recommended to build `agents-bar-client-python` locally, e.g. `python -m build` and then install
package via

```sh
$ pip install agents-bar-client-python --no-index --find-links file:///path/to/agents-bar-client-python/dist/
```
