RNaseDB
=======

.. py:class:: RNaseDB


   Bases: :py:class:`object`


Cython implementation of _RNaseDB


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1RNaseDB.html




.. py:method:: RNaseDB.getAllNames


Cython signature: void getAllNames(libcpp_vector[String] & all_names)




.. py:method:: RNaseDB.getEnzyme


Cython signature: const DigestionEnzymeRNA * getEnzyme(const String & name)




.. py:method:: RNaseDB.getEnzymeByRegEx


Cython signature: const DigestionEnzymeRNA * getEnzymeByRegEx(const String & cleavage_regex)




.. py:method:: RNaseDB.hasEnzyme


Cython signature: bool hasEnzyme(const String & name)




.. py:method:: RNaseDB.hasRegEx


Cython signature: bool hasRegEx(const String & cleavage_regex)




