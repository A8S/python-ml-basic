import random
import math

#Euclidian Distance b/w 2 points
def eucliDist(p0,p1):
    dist = 0.0
    for i in range(0,len(p0)):
        dist += (p0[i] - p1[i])**2
    return math.sqrt(dist)


    
#K-Means Algorithm
def k_means(k,datapoints):

    # d - Dimensionality of D.P
    d = len(datapoints[0]) 
    
    
    Max_Iterations = 1000
    i = 0
    
    cluster = [0] * len(datapoints)
    prev_cluster = [-1] * len(datapoints)
    
    # for Randomly Choosing Centers for the Clusters
    cluster_centers = []
    for i in range(0,k):
        new_cluster = []
        #for i in range(0,d):
        #    new_cluster += [random.randint(0,10)]
        cluster_centers += [random.choice(datapoints)]
        
        
        force_recalculation = False
    
    while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation) :
        
        prev_cluster = list(cluster)
        force_recalculation = False
        i += 1
    
        #Update Point's 
        for p in range(0,len(datapoints)):
            min_dist = float("inf")
            
            #Check min_distance against all centers
            for c in range(0,len(cluster_centers)):
                
                dist = eucldist(datapoints[p],cluster_centers[c])
                
                if (dist < min_dist):
                    min_dist = dist  
                    cluster[p] = c   # Reassign Point to new Cluster
        
        
        #Update the Cluster position
        for k in range(0,len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0,len(datapoints)):
                if (cluster[p] == k): 
                    for j in range(0,d):
                        new_center[j] += datapoints[p][j]
                    members += 1
            
            for j in range(0,d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members) 
                
               
                else: 
                    new_center = random.choice(datapoints)
                    force_recalculation = True
                    print "Forced Recalculation..."
                    
            
            cluster_centers[k] = new_center
    
        
    print "======== Results ========"
    print "Clusters", cluster_centers
    print "Iterations",i
    print "Assignments", cluster
    
    
#testing
if __name__ == "__main__":
  
    datapoints = [(3,1),(22,6),(1,2),(10,1),(1,11),(10,10),(5,6),(17,7),(9,10),(1,13),(12,10),(13,4),(9,9)]

    k = 2 #no of kluster
      
kmeans(k,datapoints) 
