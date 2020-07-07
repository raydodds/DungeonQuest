import random as r


def time_to_tarrasque(mean_years):
	counter = 0
	while r.randint(0, mean_years) != 0:
		counter += 1

	return counter

if __name__ == "__main__":
	
	_sum = 0
	_min = 10000000000000000
	_max = -1
	for i in range(0, 10000):
		ttt = time_to_tarrasque(750)
		_sum += ttt
		if ttt < _min:
			_min = ttt
		if ttt > _max:
			_max = ttt
	
	print(f'Average years: {_sum/10000}')
	print(f'Min/max years: {_min}/{_max}')
