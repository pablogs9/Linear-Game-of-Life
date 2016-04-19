import random,time,os

rows, columns = os.popen('stty size', 'r').read().split()
 
printdead = ' '
printlive = u'\u2588'

if int(columns)%2 == 0:
	cellcount = int(columns)-4
else:
	cellcount = int(columns)-1-4

cellcount =80

#universe = ''.join(random.choice('01') for i in range(cellcount))
universe = '0'*int((cellcount/2)-1) + '11' + '0'*int((cellcount/2)-1)
universem1 = '0'*int((cellcount/2)-1) + '1' + '0'*int(cellcount/2)
universem2 = '0'*int(cellcount)

mapv = ''.join(random.choice('001') for i in range(16))
mapv = '0111001010101101'
mapv = bin(46414)[2:18]

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
	
	universem2 = universem1[cellcount-1] + universem1 + universem1[0]

	universem1 = universe[cellcount-1] + universe + universe[0]

	first = map[universem2[0]+universem1[cellcount-2:cellcount]+universem1[0]]
	universe = ''.join(map[universem2[k] + universem1[k-1:k+2]] for k in range(1,cellcount+1))
	
	universe = universe + first

	universem1 = universem1[1:cellcount+1]



	time.sleep(0.02)
    