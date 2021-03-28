// Reconstruct Original Digits from English
// unique 한 것들 먼저 greedy ! 
function originalDigits(s: string): string {
    const disitToString = [
        {num:0, st:'zero'},
        {num:6, st:'six'},
        {num:8, st:'eight'},
        {num:4, st:'four'},
        {num:7, st:'seven'},
        {num:2, st:'two'},
        {num:3, st:'three'},
        {num:1, st:'one'},
        {num:5, st:'five'},
        {num:9, st:'nine'},
    ];
    // greedy ? 
    const inputDict = {};
    for(let i=0; i < s.length; i++){
        if(!inputDict[s[i]]){
           inputDict[s[i]] = 1;
        }
        else{
            inputDict[s[i]] += 1;
        }
    }

    let result = '';
    for(const nowDisit of disitToString){
        const {num, st} = nowDisit
        while(true){
            let isNotFound = false;
            for(let j=0; j<st.length; j++){
                const findString = st[j];
                if(!inputDict[findString]){
                    isNotFound = true;
                }
            }
            if(isNotFound){
                break;
            }
            for(let j=0; j<st.length; j++){
                const findString = st[j];
                inputDict[findString] -= 1;
            }
            result += num.toString();
        }
    }
    return result.split('').sort((a,b) =>Number(a)-Number(b)).join('');
};


// each one -> many 
function originalDigits(s: string): string {
    const disitToString = [
        {num:0, st:'zero'},
        {num:6, st:'six'},
        {num:8, st:'eight'},
        {num:4, st:'four'},
        {num:7, st:'seven'},
        {num:2, st:'two'},
        {num:3, st:'three'},
        {num:1, st:'one'},
        {num:5, st:'five'},
        {num:9, st:'nine'},
    ];
    // greedy ? 
    const inputDict = {};
    for(let i=0; i < s.length; i++){
        if(!inputDict[s[i]]){
           inputDict[s[i]] = 1;
        }
        else{
            inputDict[s[i]] += 1;
        }
    }

    let result = '';
    for(const nowDisit of disitToString){
        const {num, st} = nowDisit
        
        let isNotFound = false;
        let minFound = Infinity;
        for(let j=0; j<st.length; j++){
            const findString = st[j];
            if(!inputDict[findString]){
                isNotFound = true;
                break;
            }
            minFound = Math.min(minFound, inputDict[findString]);
        }
        if(isNotFound){
            continue;
        }
        for(let j=0; j<st.length; j++){
            const findString = st[j];
            inputDict[findString] -= minFound;
        }
        result += num.toString().repeat(minFound);
    }
    return result.split('').sort((a,b) =>Number(a)-Number(b)).join('');
};