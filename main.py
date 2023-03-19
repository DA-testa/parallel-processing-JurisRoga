# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    beig_laiks_threads = [0] * n
    nakam_thread = 0
    for i in range(m):
        thread = nakam_thread
        sakum_laiks = beig_laiks_threads[thread]
        beig_laiks = sakum_laiks + data[i]
        beig_laiks_threads[thread] = beig_laiks
        output.append((thread, sakum_laiks))
        nakam_thread = (nakam_thread + 1) % n
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in result:
        print(i[0], i[1])


if __name__ == "__main__":
    main()
