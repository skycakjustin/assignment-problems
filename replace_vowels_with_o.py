
def replace_vowels_with_o(input_string):
  output_string = ''
  for char in input_string:
      if char in ['a','e','i','o','u','y']:
          output_string += 'o'
      else:
          output_string += char
  return output_string

actual_output = replace_vowels_with_o('hello there')
desired_output = 'hollo thoro'

print("testing convert_to_letters on input 'hello there'...")

assert actual_output == desired_output, "actual output '{}' does not match desired output '{}'".format(actual_output, desired_output)

print('PASSED')