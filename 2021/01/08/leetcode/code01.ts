// Check If Two String Arrays are Equivalent
function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    return word1.join('') === word2.join('') ? true : false;
};


// 굳이 3항 연산자 쓰지 않아도됨;;
function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    return word1.join("") === word2.join("");
};
