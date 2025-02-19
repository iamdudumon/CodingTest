function solution(queue1, queue2) {
    let cnt = 0;
    let Queue1 = 0, Queue2 = 0;
    let halfS = 0;
    let idx1 = 0, idx2 = queue2.length;
    let temp;
    let queue = []
    let len = queue1.length + queue2.length

    queue1.forEach((num1) => {
        Queue1 += num1;
        queue.push(num1)
    });
    queue2.forEach((num2)=> {
        Queue2 += num2;
        queue.push(num2)
    });
    
    if ((Queue1 + Queue2) % 2 != 0)
        return -1
    halfS = (Queue1 + Queue2) / 2;

    while(cnt <= len * 3){
        if (Queue1 === halfS)
            return cnt ;

        if(Queue1 > halfS){
            temp = queue[idx1++ % len];
            Queue1 -= temp; 
            // Queue2 += temp; 
            cnt++;
        }
        if(Queue1 < halfS){
            temp = queue[idx2++ % len];
            Queue1 += temp; 
            // Queue2 -= temp; 
            cnt ++;
        }
    }
    return -1;
    
}