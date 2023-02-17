# rerun-docs

This is the high-level documentation for rerun that is hosted at https://www.rerun.io/docs

## Other documentation
API-level documentation for Python and Rust are stored along with the source-code in
the main [Rerun repository](https://github.com/rerun-io/rerun)

## Contributions

Contributions are welcome via pull-request. Note that even landed PRs will not deploy to the main site
until the next time we roll out a site-update. We will generally to do this at least once per release.


## Organization

The site documentation lives in Markdown files inside `/docs`.

The entry point to the documentation is `/docs/index.md`

Code examples can be rendered in multiple languages by placing them in `code-examples`, like so:

```
/docs
    /code-examples
        /my-example
            /example.py
            /example.rs
```

## Special syntax

### Title and Navigation Order
The display titles navigation order of documentation sections are managed by the Metadata at the top of the Markdown
file:
```
---
title: Examples
order: 6
---
```


### Code Examples

Code-examples can be referenced in Markdown using this syntax:
```
code-example: my-example
```


## Markdown link checker
This is run on the CI. To run it locally:

```sh
npm install -g markdown-link-check
markdown-link-check -c markdown_link_check_config.json docs/**.md
```
