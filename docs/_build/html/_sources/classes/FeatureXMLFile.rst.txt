FeatureXMLFile
==============

.. py:class:: FeatureXMLFile


   Bases: :py:class:`object`


Cython implementation of _FeatureXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureXMLFile.html




.. py:method:: FeatureXMLFile.getOptions


Cython signature: FeatureFileOptions getOptions()
Access to the options for loading/storing




.. py:method:: FeatureXMLFile.load


Cython signature: void load(String, FeatureMap &)
Loads the file with name `filename` into `map` and calls updateRanges()




.. py:method:: FeatureXMLFile.loadSize


Cython signature: size_t loadSize(String path)




.. py:method:: FeatureXMLFile.setOptions


Cython signature: void setOptions(FeatureFileOptions)
Setter for options for loading/storing




.. py:method:: FeatureXMLFile.store


Cython signature: void store(String, FeatureMap &)
Stores the map `feature_map` in file with name `filename`




