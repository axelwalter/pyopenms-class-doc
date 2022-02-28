ProteaseDB
==========

.. py:class:: ProteaseDB


   Bases: :py:class:`object`


Cython implementation of _ProteaseDB


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProteaseDB.html




.. py:method:: ProteaseDB.getAllCometNames


Cython signature: void getAllCometNames(libcpp_vector[String] & all_names)
Returns all the enzyme names available for Comet




.. py:method:: ProteaseDB.getAllCruxNames


Cython signature: void getAllCruxNames(libcpp_vector[String] & all_names)
Returns all the enzyme names available for Crux




.. py:method:: ProteaseDB.getAllMSGFNames


Cython signature: void getAllMSGFNames(libcpp_vector[String] & all_names)
Returns all the enzyme names available for MSGFPlus




.. py:method:: ProteaseDB.getAllNames


Cython signature: void getAllNames(libcpp_vector[String] & all_names)




.. py:method:: ProteaseDB.getAllOMSSANames


Cython signature: void getAllOMSSANames(libcpp_vector[String] & all_names)
Returns all the enzyme names available for OMSSA




.. py:method:: ProteaseDB.getAllXTandemNames


Cython signature: void getAllXTandemNames(libcpp_vector[String] & all_names)
Returns all the enzyme names available for XTandem




.. py:method:: ProteaseDB.getEnzyme


Cython signature: const DigestionEnzymeProtein * getEnzyme(const String & name)




.. py:method:: ProteaseDB.getEnzymeByRegEx


Cython signature: const DigestionEnzymeProtein * getEnzymeByRegEx(const String & cleavage_regex)




.. py:method:: ProteaseDB.hasEnzyme


Cython signature: bool hasEnzyme(const String & name)




.. py:method:: ProteaseDB.hasRegEx


Cython signature: bool hasRegEx(const String & cleavage_regex)




