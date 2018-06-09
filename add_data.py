import os
 
txt_files = os.listdir("addition_data/")
f1 = open("new_tags.html", 'w')
f1.write("<html><table><thead></thead><tbody>")
for file in txt_files:
	f = open("addition_data/%s" % file, 'r')
	print("____________%s____________" % file)
	# f1.write("____________%s____________\n" % file)
	f1.write("<tr><td>%s</td></tr>" % file)
	lines = [x.strip() for x in f.readlines()]
	for line in lines:
		if '%' not in line:
			# f1.write("%s\n" % line)
			f1.write("<tr><td>%s</td></tr>" % line)
			print(line)

f1.write("</tbody></table></html>")
