def n_m_1(seq):
    if len(seq) == m:
        print(*seq)
        return
    
    for i in range(n):
        if not i+1 in seq:
            n_m_1(seq + [i+1])
            

        
n, m = map(int, input().split())
n_m_1([])