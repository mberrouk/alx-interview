#!/usr/bin/python3
"""
	Given an n X n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
	"""
		Rotate matrix and edited it.
	"""
	matrixLen = len(matrix)
	newMatrix = []
	j = 0

	while j < matrixLen:
		i = matrixLen - 1
		tmprow = []
		while i >= 0:
			tmprow.append(matrix[i][j])
			i -= 1
		newMatrix.append(tmprow)
		j += 1

	for i in range(matrixLen):
		matrix[i] = newMatrix[i]

