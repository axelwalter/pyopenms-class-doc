LibSVMEncoder
=============

.. py:class:: LibSVMEncoder


   Bases: :py:class:`object`


Cython implementation of _LibSVMEncoder


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1LibSVMEncoder.html


 Serves for encoding sequences into feature vectors
 -----
 The class can be used to construct composition vectors for
 sequences. Additionally the vectors can be encoded into
 the libsvm format




.. py:method:: LibSVMEncoder.predictPeptideRT


Cython signature: libcpp_vector[double] predictPeptideRT(libcpp_vector[String] sequences, const SVMWrapper & svm, const String & allowed_characters, unsigned int maximum_sequence_length)




