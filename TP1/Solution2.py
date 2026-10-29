def time_converter(total_seconds):
    hours = total_seconds // 3600
    minute = (total_seconds % 3600) // 60
    sec = (total_seconds % 60)

    print(f"{total_seconds} seconds = {hours} h {minute} min {sec} sec")

    new_total = sec + minute * 60 + hours * 3600
    print(f"Check: {new_total == total_seconds}")
    

time_converter(9875)
time_converter(3600)
time_converter(59)
time_converter(86399)

