// Valid Anagram
function isAnagram(s: string, t: string): boolean {
    return s.split('').sort().join('') === t.split('').sort().join('');
};


// 길이가 같을테니 vaild
function isAnagram(s: string, t: string): boolean {
    if (t.length != s.length) return false;
    let letterCount:Map<string,number> = new Map();
    
    for (let i:number = 0; i < s.length; i++ ){
        let currentSymbolCount = letterCount.get(s.charAt(i));
        if (currentSymbolCount == undefined) currentSymbolCount = 1;
        else currentSymbolCount++;
        letterCount.set(s.charAt(i),currentSymbolCount);
    } 
    
   for (let j:number = 0; j < t.length;  j++ ){
        let currentSymbolCount = letterCount.get(t.charAt(j));
        if ( (currentSymbolCount == undefined) || (currentSymbolCount == 0)) return false;
        else currentSymbolCount--;
        letterCount.set(t.charAt(j),currentSymbolCount);
    } 
    
    return true;

};

// GOOD
function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false
    const freq = {}
    for (let i = 0; i < s.length; i++) {
      freq[s[i]] = (freq[s[i]] || 0) + 1 // Increment frequency
      freq[t[i]] = (freq[t[i]] || 0) - 1 // Decrement frequency
    }
    // Search for non-null frequency
    for (let key of Object.keys(freq)) if (freq[key]) return false
    return true
  };


function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }

    const counter = Array(255).fill(0);

    for (let i = 0; i < s.length; i++) {
        counter[s.charCodeAt(i)]++;
        counter[t.charCodeAt(i)]--;
    }

    for (let c of counter) {
        if (c !== 0) {
            return false;
        }
    }

    return true;
};