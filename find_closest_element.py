import math


def find_closest_element(input_element, element_list):
    closest_element = None
    max_similarity = -1
    for element in element_list:
        similarity = calculate_cosine_similarity(input_element, element)
        if similarity > max_similarity:
            max_similarity = similarity
            closest_element = element
    return closest_element


def calculate_cosine_similarity(string1, string2):
    def dot_product(vector1, vector2):
        dot_product = 0
        for char in vector1:
            if char in vector2:
                dot_product += vector1[char] * vector2[char]
        return dot_product

    string1_vector = create_vector(string1)
    string2_vector = create_vector(string2)
    dot_product = dot_product(string1_vector, string2_vector)
    magnitude1 = magnitude(string1_vector)
    magnitude2 = magnitude(string2_vector)
    return dot_product / (magnitude1 * magnitude2)


def create_vector(string):
    vector = {}
    for char in string:
        if char in vector:
            vector[char] += 1
        else:
            vector[char] = 1
    return vector


def magnitude(vector):
    magnitude = 0
    for char in vector:
        magnitude += vector[char] ** 2
    return math.sqrt(magnitude)

questions = ['What is the capital of France?', 'What is the highest mountain in the world?']
input_string = 'What is the capital of Germay?'
question = find_closest_element(input_string, questions)
