DecoyGenerator
==============

.. py:class:: DecoyGenerator


   Bases: :py:class:`object`


Cython implementation of _DecoyGenerator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DecoyGenerator.html




.. py:method:: DecoyGenerator.reversePeptides


Cython signature: AASequence reversePeptides(const AASequence & protein, const String & protease)
Reverses the protein's peptide sequences between enzymatic cutting positions




.. py:method:: DecoyGenerator.reverseProtein


Cython signature: AASequence reverseProtein(const AASequence & protein)
Reverses the protein sequence




.. py:method:: DecoyGenerator.setSeed


Cython signature: void setSeed(uint64_t)




.. py:method:: DecoyGenerator.shufflePeptides


Cython signature: AASequence shufflePeptides(const AASequence & aas, const String & protease, const int max_attempts)
Shuffle the protein's peptide sequences between enzymatic cutting positions, each peptide is shuffled @param max_attempts times to minimize sequence identity




