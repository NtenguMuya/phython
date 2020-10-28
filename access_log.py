
# Working on an access log file.

import datetime

def update_value(response_value, total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other):
    total = total + 1
    if response_value == "200":
        two_zero_zero = two_zero_zero + 1
    elif response_value == "301":
        three_zero_one = three_zero_one + 1
    elif response_value == "302":
        three_zero_two = three_zero_two + 1
    elif response_value == "304":
        three_zero_four = three_zero_four + 1
    elif response_value == "404":
        four_zero_four = four_zero_four + 1
    elif response_value == "403":
        four_zero_three = four_zero_three + 1
    elif response_value == "429":
        four_two_nine = four_two_nine + 1
    elif response_value == "499":
        four_nine_nine = four_nine_nine + 1
    elif response_value == "500":
        five_zero_zero = five_zero_zero + 1
    elif response_value == "503":
        five_zero_three = five_zero_three + 1
    else:
        other = other + 1
       
    return total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other

def main():

    # Opening the file and reading it. Creating a output file too.
    readfile = open("/Users/levimuya/Desktop/access.log", "r")
    fw = open("/Users/levimuya/Desktop/refined_output.txt", "w+")
    time_on_minute = ""
    x = 0
   
    fw.write("Time on minute          total      200      301      302      304       404       403        429       499        500        503          other")
    total = 0
    two_zero_zero = 0
    three_zero_one = 0
    three_zero_two = 0
    three_zero_four = 0
    four_zero_four = 0
    four_zero_three = 0
    four_two_nine = 0
    four_nine_nine = 0
    five_zero_zero = 0
    five_zero_three = 0
    other = 0
    avg = 0
   
    for line in readfile:
        split_string = line.split('"')
        date_value = split_string[0].split()[3].split()[0].split("[")[1]
        response_value = split_string[2].split()[0]
       
        date_time_obj = datetime.datetime.strptime(date_value, '%d/%b/%Y:%H:%M:%S')

        time_for_log_statement = date_time_obj.strftime("%Y-%m-%d %H:%M")
       
        # Working on the first log data. Initializing time_on_minute value.
        if x == 0:
            time_on_minute = time_for_log_statement
            total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other = update_value(response_value, total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other)
            x = 1
       
        # Here updating the response code value when the time_on_minute value is initialized.        
        else:
       
            # Updating the response code when the time_on_minute value is unchanged.
            if time_on_minute == time_for_log_statement:
                total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other = update_value(response_value, total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other)

            # Updating the response code when the time_on_minute value is changed. Writing to file the data corresponding to the time_on_minute
            else:
                fw.write("\n" + time_on_minute + "          " + str(total) + "        " + str(two_zero_zero) + "        " + str(three_zero_one) + "        " + str(three_zero_two) + "        " + str(three_zero_four) + "         " + str(four_zero_four) + "         " + str(four_zero_three) + "          " + str(four_two_nine) + "           " + str(four_nine_nine) + "          " + str(five_zero_zero) + "          " + str(five_zero_three) + "           " + str(other))
                time_on_minute = time_for_log_statement
                x = 1
                total = 0
                two_zero_zero = 0
                three_zero_one = 0
                three_zero_two = 0
                three_zero_four = 0
                four_zero_four = 0
                four_zero_three = 0
                four_two_nine = 0
                four_nine_nine = 0
                five_zero_zero = 0
                five_zero_three = 0
                other = 0
               
                total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other = update_value(response_value, total, two_zero_zero, three_zero_one, three_zero_two, three_zero_four, four_zero_four, four_zero_three, four_two_nine, four_nine_nine, five_zero_zero, five_zero_three, other)
   
    #Closing the files.  
    readfile.close()  
    fw.close()
             
if __name__ == "__main__":
    main()   