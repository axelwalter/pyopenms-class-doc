Base64
======

.. py:class:: Base64


   Bases: :py:class:`object`


Cython implementation of _Base64


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Base64.html




.. py:attribute:: Base64.ByteOrder


alias of :py:class:`pyopenms.pyopenms_3.__ByteOrder`


.. py:method:: Base64.decode32


Cython signature: void decode32(const String & in_, ByteOrder from_byte_order, libcpp_vector[float] & out, bool zlib_compression)




.. py:method:: Base64.decode64


Cython signature: void decode64(const String & in_, ByteOrder from_byte_order, libcpp_vector[double] & out, bool zlib_compression)




.. py:method:: Base64.decodeIntegers


Cython signature: void decodeIntegers(const String & in_, ByteOrder from_byte_order, libcpp_vector[int] & out, bool zlib_compression)
Decodes a Base64 string to a vector of integer numbers




.. py:method:: Base64.decodeStrings


Cython signature: void decodeStrings(const String & in_, libcpp_vector[String] & out, bool zlib_compression)
Decodes a Base64 string to a vector of (null-terminated) strings




.. py:method:: Base64.encode32


Cython signature: void encode32(libcpp_vector[float] & in_, ByteOrder to_byte_order, String & out, bool zlib_compression)




.. py:method:: Base64.encode64


Cython signature: void encode64(libcpp_vector[double] & in_, ByteOrder to_byte_order, String & out, bool zlib_compression)




.. py:method:: Base64.encodeIntegers


Cython signature: void encodeIntegers(libcpp_vector[int] & in_, ByteOrder to_byte_order, String & out, bool zlib_compression)
Encodes a vector of integer point numbers to a Base64 string




.. py:method:: Base64.encodeStrings


Cython signature: void encodeStrings(libcpp_vector[String] & in_, String & out, bool zlib_compression)
Encodes a vector of strings to a Base64 string




