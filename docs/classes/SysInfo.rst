SysInfo
=======

.. py:class:: SysInfo
   :module: pyopenms.sysinfo


   Bases: :py:class:`_ctypes.Structure`




.. py:attribute:: SysInfo.bufferram
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.freehigh
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.freeram
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.freeswap
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.loads
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.mem_unit
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.padding
   :module: pyopenms.sysinfo
   :value: 0




.. py:attribute:: SysInfo.procs
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.sharedram
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.totalhigh
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.totalram
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.totalswap
   :module: pyopenms.sysinfo


Structure/Union member




.. py:attribute:: SysInfo.uptime
   :module: pyopenms.sysinfo


Structure/Union member




.. py:function:: free_mem()
   :module: pyopenms.sysinfo




.. py:module:: pyopenms.version




.. py:module:: pyopenms


Python bindings to the OpenMS C++ library.


The pyOpenMS package contains Python bindings for a large part of the OpenMS
library (http://www.open-ms.de) for mass spectrometry based proteomics. It thus
provides providing facile access to a feature-rich, open-source algorithm
library for mass-spectrometry based proteomics analysis. These Python bindings
allow raw access to the data-structures and algorithms implemented in OpenMS,
specifically those for file access (mzXML, mzML, TraML, mzIdentML among
others), basic signal processing (smoothing, filtering, de-isotoping and
peak-picking) and complex data analysis (including label-free, SILAC, iTRAQ and
SWATH analysis tools).


For further documentation, please see https://pyopenms.readthedocs.io


Please cite:


