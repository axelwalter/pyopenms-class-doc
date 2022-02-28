CrossLinksDB
============

.. py:class:: CrossLinksDB


   Bases: :py:class:`object`


Cython implementation of _CrossLinksDB


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1CrossLinksDB.html




.. py:method:: CrossLinksDB.findModificationIndex


Cython signature: size_t findModificationIndex(const String & mod_name)




.. py:method:: CrossLinksDB.getAllSearchModifications


Cython signature: void getAllSearchModifications(libcpp_vector[String] & modifications)




.. py:method:: CrossLinksDB.getBestModificationByDiffMonoMass


Cython signature: const ResidueModification * getBestModificationByDiffMonoMass(double mass, double max_error, const String residue, TermSpecificity term_spec)




.. py:method:: CrossLinksDB.getModification


- Cython signature: const ResidueModification * getModification(size_t index)
- Cython signature: const ResidueModification * getModification(const String & mod_name)
- Cython signature: const ResidueModification * getModification(const String & mod_name, const String & residue, TermSpecificity term_spec)




.. py:method:: CrossLinksDB.getNumberOfModifications


Cython signature: size_t getNumberOfModifications()




.. py:method:: CrossLinksDB.has


Cython signature: bool has(String modification)




.. py:method:: CrossLinksDB.isInstantiated


Cython signature: bool isInstantiated()




.. py:method:: CrossLinksDB.readFromOBOFile


Cython signature: void readFromOBOFile(const String & filename)




.. py:method:: CrossLinksDB.searchModifications


Cython signature: void searchModifications(libcpp_set[const ResidueModification *] & mods, const String & mod_name, const String & residue, TermSpecificity term_spec)




.. py:method:: CrossLinksDB.searchModificationsByDiffMonoMass


Cython signature: void searchModificationsByDiffMonoMass(libcpp_vector[String] & mods, double mass, double max_error, const String & residue, TermSpecificity term_spec)




