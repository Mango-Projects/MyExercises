from pathlib import Path

CWD = Path(__file__).parent

tests = [104,110,202,204,306,310,404,406,504,510,602,610,704,706]

for number in tests:
	try:
		folder = CWD / f"{number}"
		# folder.mkdir(parents=True,exist_ok=True)
		# open(folder / "README.md", "a").close()
		# open(folder / f"PYA{number}.py", "a").close()
		open(folder / f"PYA{number}_pdf.py", "a").close()
	except: pass