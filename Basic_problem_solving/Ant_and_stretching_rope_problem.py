def ant_reaches_end():
    rope_length = 10       
    ant_speed = 1      
    fraction = 0.0         
    time = 0               

    while fraction < 1:
        fraction += ant_speed / rope_length
        time += 1
        rope_length += 10
    return time

seconds = ant_reaches_end()
print("The ant reaches the end in", seconds, "seconds.")
