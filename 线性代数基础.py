# -*- coding: utf-8 -*-

# -- Sheet 2 --

import numpy as np

matrix = np.array([[1, -1, 3],[1, 1, 6],[3, 8, 9]])
matrix.flatten() # alternatively, matrix.reshape(1, -1)

# **1. 单个矩阵**


# rank: dimensions of vector space spanned by cols and rows
np.linalg.matrix_rank(matrix)

# determinant
np.linalg.det(matrix)

# 取对角元素
matrix.diagonal()

# trace: sum of diagonal
matrix.trace() # alternatively, sum(matrix.diagonal())

# eigenvalues, eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
eigenvalues
eigenvectors # 标量大小改变，方向不变

# Inverse
matrix @ np.linalg.inv(matrix) # 结果=I

# **2. 矩阵运算**


a = np.array([[1, 1], [1, 2]])
b = np.array([[1, 3], [1, 2]])
print(a);print(b)
print('--')
print(a@b) # np.dot(a, b)
print(a*b) # element-wise

