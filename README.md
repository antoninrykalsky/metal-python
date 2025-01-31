# metal-python


[![Experimental](https://img.shields.io/badge/Stability-Experimental-red.svg)](https://github.com/equinix-labs/equinix-labs/blob/main/uniform-standards.md)

> **[Experimental](https://github.com/equinix-labs/equinix-labs/blob/main/experimental-statement.md)**
> This is experimental. Don't use it in production. Examples demonstrate that this client is usable. Please submit patches and open issues with your experience. This repo contains Python code generated from a customized [metal_openapi.fixed.yaml](metal_openapi.fixed.yaml) based on the [Equinix Metal API spec](https://api.equinix.com/metal/v1/api-docs). The client is generated using the python-nextgen generator built into the [OpenAPITools openapi-generator](https://github.com/OpenAPITools/openapi-generator).

Python SDK for Equinix Metal API , generated with openapi-generator. Pypi package name is `equinix-metal`.

## Installation

```
python -m pip install --upgrade equinix-metal
```

## Examples

See examples in [examples](examples) directory.

## Documentation


Full Equinix Metal API documenation is available here: [https://metal.equinix.com/developers/api/](https://metal.equinix.com/developers/api/).

Generated documentation is available here: [equinix_metal/README.md](equinix_metal/README.md).


## Requirements

This project is using [OpenAPITools openapi-generator](https://github.com/OpenAPITools/openapi-generator) Docker images to generate the code. You need to have Docker installed. 

In order to limit dependencies, the Makefile uses Docker for most of the tasks. If you run the tasks for the first time, you will need to wait for Docker image download.

## Get newest API spec

Run `make fetch` to download newest API spec from upstream.


## Development

Clone this repo

```
git clone https://github.com/equinix-labs/metal-python
```

Everything in [equinix_metal](equinix_metal) directory is generated. You can change code there to debug or experiment, but be aware that it will be rewritten on next `make generate`.

Development of this package mostly means editing:
- [Makefile](Makefile)
- The spec-patching script in [scripts/patch_metal_spec.py](scripts/patch_metal_spec.py)


Once you did your edits, run `make generate` and check how the generated code has changed.

To use the regenerated code, you can install the generated package from directory:

```
pip install ./equinix_metal
```

.. and then `import equinix_metal` in a Python script.

## Release

If you want to do a new release from main branch, make sure that `make generate` doesn't taint git status.

To craft a new release, use [the release GitHub action](https://github.com/equinix-labs/metal-python/actions/workflows/release.yml). Run it for main branch.

The workflow derives new version number based on conventional commits syntax from titles of PRs since last release. It will then build new PyPi wheel package, upload it to PyPi and create new GitHub release.

Once you run the workflow, verify that:
* the [release GitHub action](https://github.com/equinix-labs/metal-python/actions/workflows/release.yml) succeeded
* there's new [release in this GitHub project](https://github.com/equinix-labs/metal-python/releases)
* new version of [equinix-metal](https://pypi.org/project/equinix-metal/#history) is avaiable on Pypi
