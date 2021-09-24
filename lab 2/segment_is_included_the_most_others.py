T=[[0,7],[2,6],[5,6],[5,7],[3,9],[1,8],[2,4]]


def find_the_best_span(T):
	start=[0]*len(T)
	end_l=[0]*len(T)
	last=-float('inf')
	T.sort()
	count=0
	i_temp=0
	for i in range(len(T)):
		count=count+1
		if last!=T[i][0]:
			start[i-i_temp]=count
			end_l[i]=(T[i][1],i-i_temp,T[i][0])
			last=T[i][0]

		else:
			i_temp=i_temp+1
			start[i-i_temp]=count
			end_l[i]=(T[i][1],i-i_temp)

	while i_temp>0:
		start.pop()
		i_temp=i_temp-1


	end_l.sort()
	last=-float('inf')
	end=[0]*len(T)
	i_temp=0
	count=0
	res=[0]*len(end_l)

	for i in range(len(end_l)):
		count=count+1
		if last!=end_l[i][0]:
			end[i-i_temp]=count
			last=end_l[i][0]
			res[i]=i-i_temp
			
		else:
			i_temp=i_temp+1
			end[i-i_temp]=count
			res[i]=i=i_temp
	
	while i_temp>0:
		end.pop()
		i_temp=i_temp-1



	max=0
	idx_of_max=[]
	for i in range(len(end_l)):
		if end[res[0]]-start[end_l[i][1]]>=max:
			max=end[res[0]]-start[end_l[i][1]]
			idx_of_max=(end_l[i][2],end_l[i][0])

	print(idx_of_max)




find_the_best_span(T)