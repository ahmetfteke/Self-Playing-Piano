import os 
import pyautogui
from time import sleep

current_dir = os.path.dirname(os.path.realpath(__file__))

sheet_name  = "Chopin - Grande Valse Brillante op 18.txt"

def play(to_play):
	pyautogui.typewrite(to_play)
	sleep(0.1)

if __name__ == "__main__":
	music_sheet = os.path.join(current_dir, "Music Sheets", sheet_name)
	with open(music_sheet, "r") as f:
		sheet_lines = f.read().splitlines(True)

	sleep(2)

	for line in sheet_lines:
		look_for_end = False
		for alpha in line:
			if alpha != " ":
				if alpha == "[":
					to_play = ""
					look_for_end = True
				elif alpha == "]":
					look_for_end = False
					play (to_play)
				elif alpha == "|":
					sleep(0.2)

				elif look_for_end:
					to_play += alpha
				else:
					play (alpha)

			else:
				sleep(0.05)
		sleep(0.2)
