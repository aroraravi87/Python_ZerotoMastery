# GUI Display

picture=[
		[0,0,1,0,0],
		[0,1,1,1,0],
		[1,1,1,1,1],
		[0,1,1,1,0],
		[0,0,1,0,0]
]

fill='$'
empty=' '
for row in picture:
	for pixel in row:
		print(empty if pixel==0 else fill ,end='');
	print(empty) #Need a new line after every row.