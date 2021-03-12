//  Smallest String With A Given Numeric Value

function getSmallestString(n: number, k: number): string {
    let result = 'z'.repeat(Math.floor((k-n)/25));
    if(n - result.length-1 <0){
        return result
    }
    let now = k - result.length*26 - (n - result.length-1)
    let mid = '';

    if(now !== 0 && now > 0){
        mid = String.fromCharCode(now  + "a".charCodeAt(0)-1)
    }
    let front = 'a'.repeat(n-(mid+result).length);
    return front + mid + result;
};