// Word Ladder
// 1468 ms
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    let word_set : Set<string> = new Set();
    wordList.forEach((v) => {
        word_set.add(v)
    });

    interface KeyValuePair {
        key: string;
        value: number;
    }

    let queue : Array<KeyValuePair> = [];

    queue.push({key:beginWord, value:0})

    while (queue.length > 0){
        const {key, value} : KeyValuePair = queue.shift();
        if (key == endWord){
            return value+1;
        }
        
        word_set.forEach((word: string) => {
            let diff_count = 0;
            for(let i = 0; i<key.length; i++){
                if(key[i] !== word[i]){
                    diff_count++;
                    // 1468 ms -> 840 ms  
                    // 2개이상은  false ! 
                    if (diff_count === 2){
                        break;
                    }
                }
            }
            if(diff_count === 1){
                //console.log({key:word, value:value+1});
                queue.push({key:word, value:value+1});
                word_set.delete(word);
            }
        });
    }
    return 0
};

// 388 ms
// 체크 했던 word 였는지 set으로 확인
// 체크한 이후 empty array 에 input
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    const foundWords = new Set<string>();
    foundWords.add(beginWord);
    let nextWords = [beginWord];
    let level = 1;
    while (nextWords.length) {
        level++;
        const currentWords = nextWords;
        nextWords = [];
        for (let word of wordList) {
            if (!foundWords.has(word)) {
                for (let currentWord of currentWords) {
                    if (offByOne(currentWord, word)) {
                        if (word === endWord) {
                            return level;
                        }
                        nextWords.push(word);
                        foundWords.add(word);
                        break;
                    }
                }
            }
        }
    }
    return 0;
};

function offByOne(word1: string, word2: string) {
    let offBy = 0;
    for (let i = 0; i < word1.length; i++) {
        if (word1[i] !== word2[i]) {
            offBy++;
            if (offBy === 2) {
                return false;
            }
        }
    }
    return !!offBy;
}

// 156 ms
// !? 
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    if (!beginWord || beginWord.length === 0) return 0
    if (!endWord || endWord.length === 0) return 0
    if (wordList.length === 0) return 0
    if (!wordList.includes(endWord)) return 0
    
    // All word lengths are the same
    const L : number = beginWord.length
    
    // Preprocess all generic (intermediate) states of the wordList
    const generic_map : Map<string, string[]> = preprocess(wordList)
    
    const queue : [string, number][] = [ [beginWord, 1] ]
    const visited : Set<string> = new Set( [beginWord] )
    
    while (queue.length) {
        const [current_word, level] = queue.shift()
        
        // Derive the intermediate states
        for (const generic_word of genericize(current_word)) {
            const words : string[] = generic_map.get(generic_word) ?? []

            for (let w of words) {
                if (w === endWord) return level + 1
                
                if (!visited.has(w)) {
                    visited.add(w)
                    queue.push( [w, level + 1] )
                }
            }
            // Exhausted the intermediate state's words,
            // so avoid a BFS cycle by deleting the key.
            generic_map.delete(generic_word)
        }
    }
    
    return 0
};

function* genericize(word) {
    const L = word.length
    for (let i = 0; i < L; i++) {
        yield word.slice(0, i) + '*' + word.slice(i + 1)
    }
}

function preprocess(wordList: string[]): Map<string, string[]> {
    const map : Map<string, string[]> = new Map()
    
    for (const word of wordList) {
        for (const generic_word of genericize(word)) {
            if (!map.has(generic_word)) {
                map.set(generic_word, [])
            }
            map.get(generic_word).push(word)
        }
    }
    return map
}