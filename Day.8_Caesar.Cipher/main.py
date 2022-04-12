from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print_direction=direction
def caeser_cipher(text,shift,direction):
  temp_text=""
  if direction == "encode":
    direction=1
  else:
    direction=-1
  shift_direction=direction*shift
  for letter in text:
    position=alphabet.index(letter)
    new_position=position+shift_direction%26
    temp_text+=alphabet[new_position]

  print(f"Here's the {print_direction}d result: {temp_text}")


caeser_cipher(text,shift,direction)