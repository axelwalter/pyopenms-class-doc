PSProteinInference
==================

.. py:class:: PSProteinInference


   Bases: :py:class:`object`


Cython implementation of _PSProteinInference


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PSProteinInference.html




.. py:method:: PSProteinInference.calculateProteinProbabilities


Cython signature: void calculateProteinProbabilities(libcpp_vector[PeptideIdentification] & ids)




.. py:method:: PSProteinInference.findMinimalProteinList


Cython signature: size_t findMinimalProteinList(libcpp_vector[PeptideIdentification] & peptide_ids)




.. py:method:: PSProteinInference.getNumberOfProtIds


Cython signature: int getNumberOfProtIds(double protein_id_threshold)




.. py:method:: PSProteinInference.getProteinProbability


Cython signature: double getProteinProbability(const String & acc)




.. py:method:: PSProteinInference.getSolver


Cython signature: SOLVER getSolver()




.. py:method:: PSProteinInference.isProteinInMinimalList


Cython signature: bool isProteinInMinimalList(const String & acc)




