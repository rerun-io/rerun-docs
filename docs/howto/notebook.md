---
title: Using Rerun with Notebooks
order: 1
description: How to embed Rerun in notebooks like Jupyter or Colab
---

As of Rerun 0.5.0, Rerun now has limited support for embedding the Rerun viewer directly within IPython-style notebooks.
This makes it extremely easy to iterate on API calls as well as to share data with others.

Rerun has been tested with:
 - [Jupyter Notebook Classic](https://jupyter.org/)
 - [Jupyter Lab](https://jupyter.org/)
 - [VSCode](https://code.visualstudio.com/blogs/2021/08/05/notebooks)
 - [Google Colab](https://colab.research.google.com/)

## Basic Concept

Rather than logging to a file or a remote server, the Rerun SDK is configured to store data in
a local [MemoryRecording](https://ref.rerun.io/docs/python/latest/package/rerun/recording/#rerun.recording.MemoryRecording).

This `MemoryRecording` is then used to produce an inline HTML snippet that can be directly displayed
in most notebook environments. The snippet fully contains an embedded copy of an RRD file and some javascript
that loads that RRD file into an iFrame. 

Each cell is fully isolated from the other notebook cells and will only display the data from the
provided RRD.

## The APIs

In order to create a new `MemoryRecording`, you can simply call:
```
rec = rr.memory_recording()
```
Note that this is an alternative to calling `rr.connect()` or `rr.save()`.

After creating this `MemoryRecording` all the normal Rerun commands will work as expected and log
to this recording instance.

When you are ready to show it you can return it at the end of your cell or call [rec.show()](https://ref.rerun.io/docs/python/latest/package/rerun/recording/#rerun.recording.MemoryRecording.show).

Specifically the `show()` API allows you to additionally specify the width and height of the IFrame:
```
rec.show(width=400, height=400)
```

## A working example

### Running locally

The easiest way to get a feel for working with notebooks is to use it.

The GitHub repo includes a [notebook example](https://github.com/rerun-io/rerun/blob/main/examples/python/notebook/cube.ipynb).

If you have a local checkout of Rerun, you can:
```
cd examples/python/notebook
pip install -r requirements.txt
jupyter notebook cube.ipynb
```

This will open a browser window showing the notebook where you can follow along.

### Running in Google Colab

We also host a copy of the notebook in [Google Colab](https://colab.research.google.com/drive/1R9I7s4o6wydQC_zkybqaSRFTtlEaked_)

Note that if you copy and run the notebook yourself, the first Cell installs Rerun into the Colab environment.
After running this cell you will need to restart the Runtime for the Rerun package to show up successfully.

## Sharing your notebook

Because the embedded Rerun viewer in the notebook is just an embedded HTML snippet it also works with
tools like nbconvert.

For example, you can convert the notebook to HTML using the following command:
```
jupyter nbconvert --to=html --ExecutePreprocessor.enabled=True examples/python/notebook/cube.ipynb
```

This will create a new file `cube.html` that could be hosted on any static web server such as gh-pages.

## Limitations

While convenient, the approach of fully inlining an RRD file as an HTML snippet has some drawbacks. In particular, it
results in a very large HTML file that is not very efficient for sharing.

## Future Work

We are actively working on improving the notebook experience and welcome any feedback or suggestions.
The ongoing roadmap is being tracked in [GitHub issue #1815](https://github.com/rerun-io/rerun/issues/1815)



