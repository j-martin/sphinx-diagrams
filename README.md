# sphinx-diagrams

This is a rough (incomplete, but working) Sphinx extension for
[Diagrams](https://github.com/mingrammer/diagrams). Please refer to the [open
issue for Sphinx support](https://github.com/mingrammer/diagrams/issues/2) for
the latest up-to-date version when officially supported.

## Usage

### Adding the extension

`conf.py`

```conf.py
extensions = [
    "sphinx_diagrams.sphinx_diagrams",
]

```

### Adding the diagram

`source/diagrams_infrastructure.py`

```python
import sys

from diagrams import Diagram, Cluster
from diagrams.gcp.compute import KubernetesEngine

with Diagram("GKE", filename=sys.argv[1], show=sys.argv[2].lower() == 'true'):
    with Cluster("GCP Project"):
        KubernetesEngine("Primary Cluster")
```

Note that the extension will pass two arguments to your diagram script. The
first one is the `filename` (`sys.argv[1]`) it expects (it needs to match the one outputted by
`diagrams`) and the value `false` as `sys.argv[2]`. The later can be used to
tell your script not to show (open) the generate diagram.

### Referencing the diagram

`source/index.rst`

```rst
Diagram - Deployment
====================

.. diagrams:: diagrams_infrastructure.py
  :filename: diagram-deployment.png
  :extra_args: will not be consumed by the example script above. Your script could though.
```

## Credit

This code is based on
[sphinx.graphviz](https://github.com/buildthedocs/sphinx.graphviz/).

SPDX-License-Identifier: BSD-2-Clause
