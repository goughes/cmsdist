### RPM external py2-histogrammar 1.0.7
## INITENV +PATH PYTHONPATH %{i}/$PYTHON_LIB_SITE_PACKAGES

%define pip_name histogrammar

## IMPORT build-with-pip
define PipPostBuild \
perl -p -i -e "s|^#!.*python(.*)|#!/usr/bin/env python$1|" `grep -r -e "^#\!.*python.*" %i | cut -d: -f1`
