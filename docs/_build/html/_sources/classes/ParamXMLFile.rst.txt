ParamXMLFile
============

.. py:class:: ParamXMLFile


   Bases: :py:class:`object`


Cython implementation of _ParamXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ParamXMLFile.html


 The file pendant of the Param class used to load and store the param
 datastructure as paramXML




.. py:method:: ParamXMLFile.load


Cython signature: void load(String, Param &)


Read XML file
-----
:param filename: The file from where to read the Param object
:param param: The param object where the read data should be stored
:raises:
  Exception: FileNotFound is thrown if the file could not be found
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: ParamXMLFile.store


Cython signature: void store(String, Param &)


Write XML file
-----
:param filename: The filename where the param data structure should be stored
:param param: The Param class that should be stored in the file




