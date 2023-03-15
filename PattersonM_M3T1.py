# CSC 249 Data Structures
# M3T1 - Selection Sort
# Marceia Patterson
# 2/19/2023


DEBUG = True

def selectionSort(numbers):
    for i in range(len(numbers)-1):
        index_smallest = i
        
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
                if DEBUG:
                    print("\t" , "smallest: ", numbers[j] , "@" , j)
                
        temp = numbers[i]
        if DEBUG:
            print("\t\t", "swapping", numbers[i], "and", numbers[index_smallest])
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
        
        if DEBUG:
            print("PART_SORTED:", numbers)
        
        
def main():
    numbers = [15, 63, 5, 14, 89, 72, 53, 60]
    print('UNSORTED:', numbers)
    selectionSort(numbers)
    print("SORTED: ", numbers)
    

if __name__ == "__main__":
    main()