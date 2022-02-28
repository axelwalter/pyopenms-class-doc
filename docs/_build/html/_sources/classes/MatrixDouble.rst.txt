MatrixDouble
============

.. py:class:: MatrixDouble


   Bases: :py:class:`object`


Cython implementation of _Matrix[double]


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Matrix[double].html




.. py:method:: MatrixDouble.clear


Cython signature: void clear()




.. py:method:: MatrixDouble.colIndex


Cython signature: size_t colIndex(size_t index)
Calculate the column from an index into the underlying vector. Note that Matrix uses the (row,column) lexicographic ordering for indexing




.. py:method:: MatrixDouble.cols


Cython signature: size_t cols()




.. py:method:: MatrixDouble.getValue


Cython signature: double getValue(size_t i, size_t j)




.. py:method:: MatrixDouble.get_matrix


Cython signature: numpy_matrix get_matrix()






.. py:method:: MatrixDouble.get_matrix_as_view


Cython signature: numpy_matrix get_matrix()






.. py:method:: MatrixDouble.index


Cython signature: size_t index(size_t row, size_t col)




.. py:method:: MatrixDouble.indexPair


Cython signature: libcpp_pair[size_t,size_t] indexPair(size_t index)




.. py:method:: MatrixDouble.resize


- Cython signature: void resize(size_t i, size_t j, double value)
- Cython signature: void resize(libcpp_pair[size_t,size_t] & size_pair, double value)




.. py:method:: MatrixDouble.rowIndex


Cython signature: size_t rowIndex(size_t index)
Calculate the row from an index into the underlying vector. Note that Matrix uses the (row,column) lexicographic ordering for indexing




.. py:method:: MatrixDouble.rows


Cython signature: size_t rows()




.. py:method:: MatrixDouble.setValue


Cython signature: void setValue(size_t i, size_t j, double value)




.. py:method:: MatrixDouble.set_matrix


Cython signature: numpy_matrix set_matrix()






.. py:method:: MatrixDouble.sizePair


Cython signature: libcpp_pair[size_t,size_t] sizePair()




