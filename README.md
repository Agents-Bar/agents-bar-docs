# Agents Bar Docs

## Working

Parts of the documentation reference the `ai-traineree-client` python module.
Make sure you're always referring to the latest version of the package.

In case you're working on both documentations at the same time then to avoid empty pushes to pip
it's recommended to build `ai-traineree-client` locally, e.g. `python -m build` and then install
package via

```sh
$ pip install ai-traineree-client --no-index --find-links file:///path/to/ai-traineree-client/dist/
```
