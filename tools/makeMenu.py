# Author: mfwass
# Date: March 12th, 2016
#
# This is very hacky, it is just to make my life easier.

title = '''
<thead>
  <tr>
    %s
  </tr>
</thead>
'''
tbody = '''
<tbody>
  %s
</tbody>
'''
tr = '''
  <tr>
    %s
  </tr>
'''
td = '''
    <td>%s</td>
'''

f = open("newMenu.html", 'wb')
counter = 1
columns = []
f.write("<!-- Menu columns -->")

print("#" * 41 + "\n# Piero's Website Menu Generator v1.0.0 #\n" + "#" * 41 + '\n')

while True:
    inp = raw_input("Column %s: " % counter)
    if inp == ':done:':
        break
    counter += 1
    # gonna trust input and not implement sanity checking
    columns.append(inp)

output = ""
for column in columns:
    output += "%s" % (td % column)

output = title % output

output = output.replace('\n\n','\n')
output = output.replace('    \n','')
f.write(output)

# cleanup
del output
output = ""
out = ""

items = []
writeOut = True

f.write("<!-- Start of menu row items -->")

while True:
    for i in xrange(counter - 1):
        item = raw_input("%s: " % columns[i])
        if item == ':done:':
            writeOut = False
            break
        items.append(item)

    if writeOut == True:
        for item in items:
            output += "%s" % (td % item)

        output = tr % output

        # making output look pretty
        output = output.replace('\n\n','\n')
        output = output.replace('    \n','')
        output = output.replace('  \n','')

        # the output <3
        #f.write(output)
        # EXAMPLE OUTPUT:
        # <tr>
        #   <td>Plain</td>
        #   <td>$8.99</td>
        #   <td>$10.75</td>
        #   <td>No Toppings</td>
        # </tr>
    else:
        break # to kill the loop, without this it doesn't take ':done:' for an answer.
    out += output
    output = ""
    items = []

out = tbody % out
out = out.replace('\n\n', '\n')
out = out.replace('  \n', '')
f.write(out)
f.close()
