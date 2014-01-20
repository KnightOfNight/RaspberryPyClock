#!/usr/bin/python


import string
import logging
import Adafruit
from Display import Display
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate


#logging.basicConfig( level = logging.DEBUG )


# ask a yes or no question
def yesno ( prompt = "Yes or no?", value = "yes" ):
	if value == "yes":
		answer = "[YES] no"
		selected = True

	elif value == "no":
		answer = "yes [NO]"
		selected = False

	else:
		raise ValueError("Incorrect value " + value)

	display = Display()

	display.message(prompt + "\n" + answer)

	while True:

		if display.button_select():
			display.clear()
			return(selected)

		elif display.button_left() or display.button_right():
			if selected:
				answer = "yes [NO]"
				selected = False
			else:
				answer = "[YES] no"
				selected = True

			display.message(prompt + "\n" + answer)


def letter_choices():
	letters = []

	letters.append(' ')

	# uppercase letters
	for i in range (65, 91):
		letters.append(chr(i))

	# lowercase letters
	for i in range (97, 122):
		letters.append(chr(i))

	# numbers
	for i in range (48, 58):
		letters.append(chr(i))

	# all other symbols
	for i in range (33, 48):
		letters.append(chr(i))
	for i in range (58, 65):
		letters.append(chr(i))
	for i in range (91, 97):
		letters.append(chr(i))
	for i in range (123, 127):
		letters.append(chr(i))

	return(letters)


def text (prompt = "Enter text...", value = ""):
	maxlen = 16

	if len(value) > maxlen:
		raise ValueError("Value too long")

	display = Display()

	letters = letter_choices()
	answer = []
	column = 0

	if value:
		for i in range(0, len(value)):
			answer.append(value[i])
	else:
		for i in range (0, maxlen):
			answer.append(' ')

	display.message( prompt + "\n" + string.join(answer, '') )
	display.move_cursor(col = column, row = 1)
	display.blink_cursor()

	while True:

		if display.button_select():
			return( string.join(answer, '') )

		elif display.button_left():
			if column > 0:
				column -= 1
				display.move_cursor(col = column, row = 1)

		elif display.button_right():
			if column < 15:
				column += 1
				display.move_cursor(col = column, row = 1)

		elif display.button_up():
			letter = answer[column]
			index = letters.index(letter)
			if index < (len(letters) - 1):
				index += 1
			else:
				index = 0

			answer[column] = letters[index]
			display.message( prompt + "\n" + string.join(answer, '') )
			display.move_cursor(col = column, row = 1)

		elif display.button_down():
			letter = answer[column]
			index = letters.index(letter)
			if index > 0:
				index -= 1
			else:
				index = len(letters) - 1

			answer[column] = letters[index]
			display.message( prompt + "\n" + string.join(answer, '') )
			display.move_cursor(col = column, row = 1)


def longtext (prompt = "Enter text...", value = ""):
	display = Display()

	letters = letter_choices()	# possible character values

	cursor_column = 0			# the column where the cursor is at
	answer_column = 0			# the current column somewhere in the answer
	display_column = 0			# the column to start displaying at

	# initialize the answer
	answer = []
	if value:
		for i in range(0, len(value)):
			answer.append(value[i])
	else:
		answer.append(' ')

	display.message( prompt + "\n" + string.join(answer, '')[display_column:16] )
	display.move_cursor(col = cursor_column, row = 1)
	display.blink_cursor()

	while True:

		if display.button_select():
			return( string.join(answer, '').strip() )

		elif display.button_left():
			logging.debug("left")

			logging.debug( "before start column = " + str(display_column) )
			logging.debug( "before answer column = " + str(answer_column) )
			logging.debug( "before cursor column = " + str(cursor_column) )

			if cursor_column > 0:
				logging.debug( "decrementing cursor column and moving cursor" )
				cursor_column -= 1
				display.move_cursor(col = cursor_column, row = 1)

				answer_column -= 1

			elif answer_column > 0:
				logging.debug( "decrementing answer and start column and scrolling display" )
				answer_column -= 1
				display_column -= 1
				display.message( prompt + "\n" + string.join(answer, '')[display_column:display_column+16] )
				display.move_cursor(col = cursor_column, row = 1)

			else:
				logging.debug( "not moving any cursors, already at start of display and of answer" )

			logging.debug( "after start column = " + str(display_column) )
			logging.debug( "after answer column = " + str(answer_column) )
			logging.debug( "after cursor column = " + str(cursor_column) )

		elif display.button_right():
			logging.debug( "right" )

			logging.debug( "before start column = " + str(display_column) )
			logging.debug( "before answer column = " + str(answer_column) )
			logging.debug( "before cursor column = " + str(cursor_column) )

			answer_column += 1
			if answer_column == len(answer):
				logging.debug( "appending space" )
				answer.append(' ')

			if cursor_column < 15:
				logging.debug( "incrementing cursor column and moving cursor" )
				cursor_column += 1
				display.move_cursor(col = cursor_column, row = 1)

			else:
				logging.debug( "incrementing start column and scrolling answer" )
				display_column += 1
				display.message( prompt + "\n" + string.join(answer, '')[display_column:display_column+16] )
				display.move_cursor(col = cursor_column, row = 1)

			logging.debug( "after start column = " + str(display_column) )
			logging.debug( "after answer column = " + str(answer_column) )
			logging.debug( "after cursor column = " + str(cursor_column) )

		elif display.button_up():
			letter = answer[answer_column]
			index = letters.index(letter)
			if index < (len(letters) - 1):
				index += 1
			else:
				index = 0

			answer[answer_column] = letters[index]
			display.message( prompt + "\n" + string.join(answer, '')[display_column:display_column+16] )
			display.move_cursor(col = cursor_column, row = 1)

		elif display.button_down():
			letter = answer[answer_column]
			index = letters.index(letter)
			if index > 0:
				index -= 1
			else:
				index = len(letters) - 1

			answer[answer_column] = letters[index]
			display.message( prompt + "\n" + string.join(answer, '')[display_column:display_column+16] )
			display.move_cursor(col = cursor_column, row = 1)


# basic tests
if __name__ == '__main__':
	print "'" + longtext( value = "answer" ) + "'"
	print "'" + longtext( value = "a really really very very long answer" ) + "'"

	print text( prompt = "tilde ~~~" )

	print text()

	print text( value = "smeg off!" )

	print yesno()

	print yesno(prompt = "Are you sure?")

	print yesno(prompt = "Really sure?", value="no")

	print yesno(value="test")

	display = Display()
	display.stop()

