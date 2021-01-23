// Determine if Two Strings Are Close

function closeStrings(word1: string, word2: string): boolean {
    if(word1.length !== word2.length){
        return false;
    }

    let wmap1 = new Map();
    let wmap2 = new Map();
    
    for(let i=0;i<word1.length;i++){
        if(wmap1.has(word1[i])){
            wmap1.set(word1[i], wmap1.get(word1[i])+1);
        }else{
            wmap1.set(word1[i],1);
        }
    }

    for(let i=0;i<word2.length;i++){
        if(wmap2.has(word2[i])){
            wmap2.set(word2[i], wmap2.get(word2[i])+1);
        }else{
            wmap2.set(word2[i],1);
        }   
    }

    // for(let i of wmap1){
    //     if(wmap1.get(i[0]) === wmap2.get(i[0])){
    //         wmap2.delete(i[0]);
    //         wmap1.delete(i[0]);
            
    //     }
    // }

    let check1 = [];
    let charCheck1 = [];
    let check2 = [];
    let charCheck2 = [];
    

    for(let i of wmap2){
        check2.push(i[1]);
        charCheck2.push(i[0]);
    }

    for(let i of wmap1){
        check1.push(i[1]);
        charCheck1.push(i[0]);
    }

    charCheck1.sort();
    charCheck2.sort();

    check1.sort((a,b) => a-b);
    check2.sort((a,b) => a-b);

    // console.log(charCheck1, charCheck2);
    if(check1.length !== check2.length){
        return false;
    }else{
        for(let i =0;i<check1.length;i++){
            if(check1[i] !== check2[i]){
                return false;
            }
            if(charCheck1[i] !== charCheck2[i]){
                return false;
            }
        }
    }

    return true;
};

// AH! 앞에꺼 존재할때만 해당값에 넣기 구나!
function closeStrings(word1: string, word2: string): boolean {
    let map1 = new Map();
    let map2 = new Map();
    word1.split("").forEach( char =>{
         map1.get(char) ? map1.set(char,map1.get(char)+1) : map1.set(char,1);
    });
    word2.split("").forEach( char =>{
        if(map1.get(char)){
            map2.get(char) ? map2.set(char,map2.get(char)+1) : map2.set(char,1);
        }
        
    });
      return  Array.from(map1.values()).sort().join(',') == 
              Array.from(map2.values()).sort().join(',')

};

function closeStrings(word1: string, word2: string): boolean {
    if (word1.length !== word2.length) return false
    const image1 = transform(word1), image2 = transform(word2)
    for (let i = 0; i < image1.length; i += 1) {
        if ((image1[i] === 0) !== (image2[i] === 0)) return false
    }
    image1.sort((a, b) => a - b)
    image2.sort((a, b) => a - b)
    for (let i = 0; i < image1.length; i += 1) {
        if (image1[i] !== image2[i]) return false
    }
    return true

    function transform(word: string): number[] {
        const ans = new Array(26).fill(0)
        for (let i = 0; i < word.length; i += 1) {
            ans[word.charCodeAt(i) - 97] += 1
        }
        return ans
    }
}