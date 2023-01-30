# rerun-docs

This is the high-level documentation for rerun that is hosted at https://www.rerun.io/docs

## Other documentation
API-level documentation for Python and Rust are stored along with the source-code in
the main [Rerun repository](https://github.com/rerun-io/rerun)

## Contributions

Contributions are welcome via pull-request. Changes frequently go live on our website, but not automatically.

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
title: The Examples
order: 6
---
```


### Code Examples

Code-examples can be referenced in Markdown using this syntax:
```
code-example: my-example
```