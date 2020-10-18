# sphinx-diagrams

This is a rough (incomplete, but working) Sphinx extension for
[Diagrams](https://github.com/mingrammer/diagrams). Please refer to the [open
issue for Sphinx support](https://github.com/mingrammer/diagrams/issues/2) for
the latest up-to-date version when officially supported.

## Usage

### Install

The package is not currently published to pypi. As of 2020-08-20 you can install
via git.

```bash
$ pip3 install sphinx-diagrams
```

### Adding the extension

`conf.py`

```conf.py
extensions = [
    "sphinx_diagrams",
]
```

### Adding the diagram (inline)

The simplest way is to use `SphinxDiagram` and inline the code in your document.
Consider using an external diagram/python script (see below) as it has much
shorter iteration loop than running sphinx and most likely better supported by
your editor or IDE.

`source/index.rst`

```rst
Diagram - Deployment
====================

.. diagrams::
  from diagrams import Cluster
  from diagrams.k8s.compute import Deployment
  from sphinx_diagrams import SphinxDiagram

  with SphinxDiagram(title="GKE"):
      with Cluster("GCP Project"):
          KubernetesEngine("Primary Cluster")
```


### Adding a diagram (external python code)


#### Write the code

`source/diagrams_infrastructure.py`

You can still use `SphinxDiagram` in your own code. This class handles arguments
like `:filename:` and visibility (showing the diagram via `xdg-open/open`) for
you.

```python
from diagrams import Cluster
from diagrams.k8s.compute import Deployment
from sphinx_diagrams import SphinxDiagram

with SphinxDiagram(title="GKE"):
    with Cluster("GCP Project"):
        KubernetesEngine("Primary Cluster")

```

Alternatively, you can use `Diagram` (from `diagrams`) directly. Note that the
extension will pass two arguments to your diagram script. The first one is the
`filename` as `sys.argv[1]` it expects (it needs to match the one outputted by
`diagrams`) and the value `false` as `sys.argv[2]`. The later can be used to
tell your script not to show (open) the generate diagram.

```python
import sys

from diagrams import Diagram, Cluster
from diagrams.gcp.compute import KubernetesEngine

with Diagram("GKE", filename=sys.argv[1], show=sys.argv[2].lower() == 'true'):
    with Cluster("GCP Project"):
        KubernetesEngine("Primary Cluster")
```


#### Referencing the diagram

`source/index.rst`

```rst
Diagram - Deployment
====================

.. diagrams:: diagrams_infrastructure.py
  :filename: diagram-deployment.png
```

If using `SphinxDiagram` (above) or if the filename of the diagram script is the
same as the output file (e.g.: `diagrams_infrastructure.py =>
diagrams_infrastructure.png`) then the `:filename:` is not necessary.

```rst
Diagram - Deployment
====================

.. diagrams:: diagrams_infrastructure.py
```
## Credit

This code is based on
[sphinx.graphviz](https://github.com/buildthedocs/sphinx.graphviz/).

SPDX-License-Identifier: BSD-2-Clause
