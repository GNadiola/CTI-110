import time
time_elapsed = 330

for x in range(time_elapsed, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
