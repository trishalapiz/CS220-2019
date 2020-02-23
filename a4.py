"""ASSIGNMENT FOUR"""
"""
#EXAMPLE INPUT

2
8
-36.8533 174.749 Auckland
-37.788 175.265 Hamilton
-37.7012 176.154785 Tauranga
-38.677 176.0669 Taupo
-39.926 175.045 Wanganui
-39.4956 176.9 Napier
-40.3465 175.6055 Palmerston North
-41.2943 174.7595 Wellington
300
2
48.4275 -123.367259 Victoria
44.653 -63.588867 Halifax
1000
"""

import math

def main():

    #NUMBER OF TEST CASES
    n = int(input().strip()) 
        
    for o in range(n): #GOING THROUGH ALL TEST CASES
        city_list = [] #storing points and cities
            
        #NUMBER OF CITIES
        m = int(input().strip()) 

        #process the input by gropuing the cities' and its lng/lat together
        for i in range(m): 
            city_list.append(input().strip().split(' ', 2)) 

        tank_distance = float(input().strip()) #total distance travelled with single tank
        
        #MAKE CITIES THE DICTIONARY KEYS using dict comprehension
        initial_dict = {city[2] : city[0:2] for city in city_list} 

        #INITIALISE MATRIX
        distance_matrix = [[0] * m for _ in range(m)]
        adjacency_matrix = [[0] * m for _ in range(m)]

        cities = list(initial_dict.keys()) #put the keys into a list
        
        #INDEXES FOR MATRIX SINCE DICT DOESN'T HAVE INTEGER INDICES
        count1 = 0
        count2 = 0
        
        #PUTTING DISTANCES IN A MATRIX
        for city in initial_dict: #row
            for city2 in initial_dict: #column
                #if calculated distance between 2 cities is less than the total tank distance
                d = calc_distance(initial_dict[city][0], initial_dict[city2][0], initial_dict[city][1], initial_dict[city2][1])
                
                if d < tank_distance:
                    distance_matrix[count1][count2] = d
                else:
                    distance_matrix[count1][count2] = math.inf #not connected
            
                count2 += 1
            count2 = 0 #reset
            count1 += 1
        
        #reset counts for next test cases
        count1 = 0
        count2 = 0

        #SET UP ADJACENCY MATRIX
        for s in range(m):
            for t in range(m):
                if distance_matrix[s][t] < tank_distance and distance_matrix[s][t] > 0:
                    #cities only connected if the distance between them is less than the tank distance
                    adjacency_matrix[s][t] = 1

        new_dict = {} #see which cities are connected

        for k in range(m): #k = row
            key = cities[k]
            new_dict[key] = {} #create a sub dictionary to show neighbours connected to current vertex
            for z in range(m): #z = column
                if adjacency_matrix[k][z] == 1:
                    key2 = cities[z]
                    new_dict[key][key2] = distance_matrix[k][z] #insert distance in sub dictionary
        #print("new dict is {}".format(new_dict))
        print(dijkstra(new_dict, cities[0], cities[-1]))
                 
            
"""--------------------------------------------------------------------------"""
def calc_distance(cityLat1, cityLat2, cityLng1, cityLng2): #1 = first city // 2 = second city
    R = 6371 #Earth's radius
    change_in_lat = math.fabs(math.radians(float(cityLat2)) - math.radians(float(cityLat1))) #made number absolute
    change_in_lng = math.fabs(math.radians(float(cityLng2)) - math.radians(float(cityLng1)))  #made number absolute
    a = math.pow(math.sin(change_in_lat/2), 2) + math.cos(math.radians(float(cityLat1))) * math.cos(math.radians(float(cityLat2))) * math.pow(math.sin(change_in_lng / 2), 2) 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d #return disted arc between 2 cities
"""--------------------------------------------------------------------------"""
def dijkstra(graph, start, end): #SIMPLE DIJKSTRA
    #graph = {'Auckland': {'Hamilton': 113.50828301955525, 'Tauranga': 156.0743174512238, 'Taupo': 233.53661873261896}, 'Hamilton': {'Auckland': 113.50828301955525, 'Tauranga': 78.82898882433817, 'Taupo': 121.14973188997753, 'Wanganui': 238.4964898177952, 'Napier': 237.0913990021661, 'Palmerston North': 286.0061748579422},....}
    distance = {}
    pred = {}
    path = []
    
    for node in graph: 
        distance[node] = math.inf
    distance[start] = 0
    
    while graph: #finding the next node
        traversed = None
        
        for node in graph: #selecting which node to traversed to
            if traversed is None:
                traversed = node 
            elif distance[node] < distance[traversed]:
                traversed = node
        #print("* Selected node is {}".format(traversed))

        for city, dist in graph[traversed].items(): #updating distances
            if dist + distance[traversed] < distance[city]:
                #print("--> if {}'s current distance {} + distance[{}] < distance[{}]:".format(city, dist, traversed, city))
                distance[city] = dist + distance[traversed]
                #print("-----> distance[{}] = {} + distance[{}]".format(city, dist, traversed))
                pred[city] = traversed
                #print("-----> pred[{}] = {}".format(city, traversed))
        graph.pop(traversed)

    #print("distances are {}".format(distance))
    while end != start: #responsbile for shortest path sequence
        try:
            path.insert(0,end) 
            end = pred[end]
        except KeyError:
            return "Not possible"
       
    path.insert(0,start)
    #print("path is: {}".format(path))
    
    if distance[end] != math.inf:

        end_string = ""
        
        for p in path:
            if p != path[-1]: #path[-1] == end
                end_string = end_string + str(p) + ", "
            else:
                end_string = end_string + str(p)

        return end_string

main()



