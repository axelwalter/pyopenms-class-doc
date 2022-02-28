JavaInfo
========

.. py:class:: JavaInfo


   Bases: :py:class:`object`


Cython implementation of _JavaInfo


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1JavaInfo.html




.. py:method:: JavaInfo.canRun


Cython signature: bool canRun(String java_executable)


Determine if Java is installed and reachable
-----
The call fails if either Java is not installed or if a relative location is given and Java is not on the search PATH
-----
:param java_executable: Path to Java executable. Can be absolute, relative or just a filename
:returns: Returns false if Java executable can not be called; true if Java executable can be executed




