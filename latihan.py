import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])
reshape_arr = arr.reshape(5,2)
print (reshape_arr)

rand_a = np.random.randint(1,100, size=(10))
rand_b = np.random.randint(200,300, size=(10))

print (rand_a)
min_a = rand_a.min()
max_a = rand_a.max()
std_a = rand_a.std()
mean_a = rand_a.mean()
print ("Nilai minimal Array A", min_a)
print ("Nilai maximal Array A", max_a)
print ("Standar Deviasi Array A", std_a)
print ("Rata-rata Array A", mean_a)

print ("----------batas-------")

print (rand_b)
min_b = rand_b.min()
max_b = rand_b.max()
std_b = rand_b.std()
mean_b = rand_b.mean()
print ("Nilai minimal Array B", min_b)
print ("Nilai maximal Array B", max_b)
print ("Standar Deviasi Array B", std_b)
print ("Rata-rata Array B", mean_b)

print("Array A > B?", rand_a > rand_b)
print("Array A < Array B?", rand_a < rand_b)
print("Array A >= Array B?", rand_a >= rand_b)
print("Array A <= Array B?", rand_a <= rand_b)
print("Array A != Array B?", rand_a != rand_b)