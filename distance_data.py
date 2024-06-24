import csv

# Initialize empty list to hold distance data and empty dictionary to hold addresses
distance_data = []
address_dictionary = {}

with open('distance_file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Iterate through rows of csv file
    for row in reader:

        # Append the row data to the distance_data list
        distance_data.append(row)

# Function to get the distance between two locations
def get_distance(address1, address2):
    index1 = get_index(address1)
    index2 = get_index(address2)

    if index1 > index2:
        return float(distance_data[index1][index2 + 1])
    else:
        return float(distance_data[index2][index1 + 1])
    
def get_index(address):
    for i, row in enumerate(distance_data):
        if row[0] == address:
            return i
        
    return -1


# # Example usage of get_distance function
# address1 = "233 Canyon Rd"
# address2 = "1330 2100 S"
# distance = get_distance(address1, address2)
# print(f"\nDistance between {address1} and {address2}: {distance} miles\n")

