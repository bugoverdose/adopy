"""
This module contains three basic classes of ADOpy: `Task`, `Model`, and `Engine`.
These classes provide built-in functions for the Adaptive Design Optimization.

.. note::

   Three basic classes are defined in the :py:mod:`adopy.base` (i.e.,
   :py:class:`adopy.base.Task`, :py:class:`adopy.base.Model`, and
   :py:class:`adopy.base.Engine`). However, for convinience, users can find it
   directly as :py:class:`adopy.Task`, :py:class:`adopy.Model`, and
   :py:class:`adopy.Engine`.
"""
from ._task import Task as _Task
from ._model import Model as _Model
from ._engine_v0 import Engine
from ._engine_v1 import Engine as EngineV1
from ._engine_v2 import Engine as EngineV2
from ._engine_v3 import Engine as EngineV3

Task = _Task
Model = _Model

__all__ = ['Task', 'Model', 'Engine', 'EngineV1', 'EngineV2', 'EngineV3']
