"""Calculate the ppmi-value, and transform a matrix with these ppmi-values

You need to input a list to get the right dictionary.
And these Python programme is fit for the task in Übungsblatt 09:

        drink alcohol ecstasy
water   648     51      2
vodka   42      6       0
acid    11      31      4

For other instance you need to rewrite the "name" in function "ppmi".
The length of each row vector is not limited.

"""


def count_ppmi(target, sum_x, sum_y, sum_all, *, decimal=3):
    """Count the value of ppmi.

    :param target: an element in the matrix
    :param sum_x: the sum of the elements in a row on the table
    :param sum_y: the sum of the elements in a column on the table
    :param sum_all: the sum of all the elements
    :param decimal: the result is kept to 3 decimal place
    :return: results to 3 decimal places
    """
    import math
    try:
        result = math.log2((target * sum_all) / (sum_x * sum_y))
    except ValueError:
        # if the value of target is 0, we define the result as 0
        return 0
    return round(result, decimal)


def determine_value(value):
    """Determine the final result.

    :param value: the result from count_ppmi
    :return: the final value
    """
    if value < 0:
        # if the value is negative, we define the result as 0
        return 0
    return value


def get_column_sum(column_number, table):
    """Get sum of all the elements from the table.

    :param column_number: form 0
    :param table: the table you want to operate
    :return: the sum of the column you want to calculate
    """
    j = 0
    list_of_column = []
    while j < len(table):
        list_of_column.append(table[j][column_number])
        j += 1
    return sum(list_of_column)


def get_row_sum(raw_number, table):
    """Get sum of all the elements from the table.

    :param raw_number:
    :param table: the table you want to operate
    :return: the sum of the row you want to calculate
    """
    return sum(table[raw_number])


def calculate_sum(matrix):
    """Calculates the sum of all the numbers in a two-dimensional list.

    :param matrix: the table you want to operate
    :return: the sum of table you want to calculate
    """
    total = 0
    for row in matrix:
        for cell in row:
            total += cell
    return total


def ppmi_matrix(matrix, *, name=None):
    """Form a table with corresponding value, which is calculated from ppmi algorithm.

    :param matrix: the word-word-matrix
    :param name: the name of rows
    :return: the word-word-matrix, which is modified by the ppmi algorithm
    """
    if name is None:
        name = ["water", "vodka", "acid"]
        # if necessary, rewrite hear to adapt it to other instances
    sum_all = calculate_sum(matrix)
    result_all = {}
    i = 0
    for x0 in matrix:
        j = 0
        result_part = []
        for x1 in x0:
            result_part.append(determine_value(count_ppmi(x1, get_row_sum(i, matrix),
                                                          get_column_sum(j, matrix), sum_all)))
            j += 1
        result_all.update({name[i]: result_part})
        i += 1
    print(f"The modified matrix is {result_all}")
    return result_all


def dot_product(a, b):
    """Calculate dot product.

    :param a: vektor a
    :param b: vektor b
    :return: dot product
    """
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def vector_magnitude(vector):
    """Calculate vector magnitude.

    :param vector:
    :return: vector magnitude
    """
    square_sum = 0
    for component in vector:
        square_sum += component ** 2
    magnitude = square_sum ** 0.5
    return magnitude


def cosine_similarity(a, b):
    """Calculate cosine similarity.

    :param a: vector a
    :param b: vector b
    :return: cosine similarity
    """
    result = dot_product(a, b) / (vector_magnitude(a) * vector_magnitude(b))
    print(f"The cosine similarity of {a} and {b} is {result}")
    return result


if __name__ == "__main__":
    word_word_matrix = [[648, 51, 2], [42, 6, 0], [11, 31, 4]]
    m = ppmi_matrix(word_word_matrix)
    cosine_similarity(m["water"], m["vodka"])
    cosine_similarity(m["water"], m["acid"])
    cosine_similarity(m["acid"], m["vodka"])
