import gabriel10
import sys

doc = gabriel10.Document7396()

data = sys.stdin.read().split("\n")
current_line = 1
current_page = 1

for line in data:
    doc.page(current_page).text(current_line, 1, line)
    if current_line == 73:
        current_line = 1
        current_page += 1
    else:
        current_line += 1

filename = "out.pdf"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

doc.build(filename)
