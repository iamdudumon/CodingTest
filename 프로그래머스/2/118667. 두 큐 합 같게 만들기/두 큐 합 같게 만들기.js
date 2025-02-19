function solution(queue1, queue2) {
    let answer = 0;
    let queue = [...queue1, ...queue2]
    let qSum1 = queue1.reduce((pre, num) => pre + num),
        qSum2 = queue2.reduce((pre, num) => pre + num);
    let idx1 = 0, idx2 = queue2.length;
    let len = queue1.length * 2
    let temp;

    if ((qSum1 + qSum2) % 2 != 0)
        return -1

    while(answer <= len * 2) {
        if (qSum1 === qSum2)
            return answer;

        if(qSum1 > qSum2){
            temp = queue[idx1];
            idx1 = (idx1 + 1) % len;
            qSum1 -= temp; 
            qSum2 += temp;
            answer++;
        }
        if(qSum1 < qSum2){
            temp = queue[idx2];
            idx2 = (idx2 + 1) % len;
            qSum1 += temp; 
            qSum2 -= temp;
            answer ++;
        }
    }
    return -1;
    
}