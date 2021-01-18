// Count Sorted Vowel Strings
// https://www.youtube.com/watch?v=gdt7HQF56OI
function countVowelStrings(n: number): number {
    let result : number[][] = []; 
    let input :  number[] = [1,1,1,1,1];
    result.push(input);
    for(let i=0; i<n-1; i++){
        let input = [];
        let reSum = result[i].reduce((a,b) => a + b , 0)
        input.push(reSum);
        reSum -= result[i][0];
        input.push(reSum);
        reSum -= result[i][1];
        input.push(reSum);
        reSum -= result[i][2];
        input.push(reSum);
        reSum -= result[i][3];
        input.push(reSum);
        ///
        result.push(input);
    }
    return result[result.length-1].reduce((a,b) => a + b , 0)

};