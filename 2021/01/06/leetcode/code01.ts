// Kth Missing Positive Number
function findKthPositive(arr: number[], k: number): number {
    let now : number = 1;
    // 이미  strictly increasing order ;;
    // 안해도 됬었음..
    arr.sort((n1,n2) => n1 - n2);
    
    let i : number = 0;
    while (i < arr.length){
        if (arr[i] === now){
            i+=1;
        }else{
            k -= 1;
            if (k===0){
                return now;
            }
        }
        now+=1;
    }
    now -=1
    return now + k;

};

// some() 메서드는 배열 안의 어떤 요소라도 주어진 판별 함수를 통과하는지 테스트합니다.
// GOOD 
// arr + k 까지 받으며 arr 에 i 값 존재하면 input 하지않음.
// return missingnumbers[k-1] 
function findKthPositive(arr: number[], k: number): number {
    const missingNumbers: number[] = [];
    console.log(arr[arr.length-1]+k);
    for(let i = 1; i <= arr[arr.length-1] + k; i++){
        missingNumbers.push(i)
        if(arr.some(x => x == i)){
            missingNumbers.pop()
        }
    }
    console.log(missingNumbers);
    return missingNumbers[k-1];
};

// map type -> key value 
// [1,1] ~ [x,x] 저장이후
// arr 에 존재하는 값들 모두 제거
// m 의 k-1 번째 return 
// ... -> rest operator 
function findKthPositive(arr: number[], k: number): number {
    let m = new Map();
  for (let i = 1; i <= arr[arr.length-1] + k; i++) m.set(i,1);
  arr.forEach(num => m.delete(num));
  return [...m.keys()][k-1];
};

// 첫번째꺼와 동일
function findKthPositive(arr: number[], k: number): number {
    const missingNumbers: number[] = [];
        for(let i = 1; i <= arr[arr.length-1] + k; i++){
            missingNumbers.push(i)
            if(arr.some(x => x == i)){
                missingNumbers.pop()
            }
    }
    return missingNumbers[k-1];
};