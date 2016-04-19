import random,time,os

rows, columns = os.popen('stty size', 'r').read().split()
 
printdead = ' '
printlive = u'\u2588'

if int(columns)%2 == 0:
	cellcount = int(columns)-4
else:
	cellcount = int(columns)-1-4


universe = '0'*int((cellcount/2)-1) + '11' + '0'*int((cellcount/2)-1)
universem1 = '0'*int((cellcount/2)-1) + '1' + '0'*int(cellcount/2)
universem2 = '0'*int(cellcount)
#universe = ''.join(random.choice('01') for i in range(cellcount))

#46414 22428 5763 54166
mapv = bin(46414)[2:18]
mapv = '0'*(16-len(mapv)) + mapv

map = {
 '0000': mapv[15],
 '0100': mapv[14],
 '0010': mapv[13], # INIT
 '0110': mapv[12],
 '0001': mapv[11],
 '0101': mapv[10],
 '0011': mapv[9],
 '0111': mapv[8],
 '1000': mapv[7],
 '1100': mapv[6],
 '1010': mapv[5],
 '1110': mapv[4],
 '1001': mapv[3],
 '1101': mapv[2],
 '1011': mapv[1],
 '1111': mapv[0],
 }

print universem2.replace('0', printdead).replace('1', printlive)
print universem1.replace('0', printdead).replace('1', printlive)

while True:
	print universe.replace('0', printdead).replace('1', printlive)

	universem2 = universem1
	universem1 = universe 

	universe = ''.join(map[universem2[0]+universem1[cellcount-1]+universem1[0:2]])

	for i in range(1,cellcount-1):
		universe = universe + (map[universem2[i]+universem1[i-1:i+2]])


	universe = universe + (map[universem2[cellcount-1]+universem1[cellcount-2:cellcount]+universem1[0]])

	time.sleep(0.06)
    