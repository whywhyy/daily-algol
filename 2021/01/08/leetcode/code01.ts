// Check If Two String Arrays are Equivalent
function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    return word1.join('') === word2.join('') ? true : false;
};


// 굳이 3항 연산자 쓰지 않아도됨;;
function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    return word1.join("") === word2.join("");
};

function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    let ex1 = "";
    let ex2 = "";
    let in1 = 0;
    let in2 = 0;
    
    while (in1 < word1.length || in2 < word2.length) {
        if (ex1 === ex2 && !ex1) {
            ex1 = word1[in1];
            in1++;
            continue;
        }
        
        if (!!ex1) {
            if (in2 >= word2.length) {
                return false;
            }
            ex2 = word2[in2];
            in2++;
        } else if (!!ex2) {
            if (in1 >= word1.length) {
                return false;
            }
            ex1 = word1[in1];
            in1++;
        }
        

        
        if (ex2.length >= ex1.length) {
            if (ex2.indexOf(ex1) !== 0) {
                return false;
            }

            ex2 = ex2.substring(ex1.length);
            ex1 = "";
        } else {
           if (ex1.indexOf(ex2) !== 0) {
                return false;
            }

            ex1 = ex1.substring(ex2.length);
            ex2 = "";
        }
        
    }
    
    
    return ex1 === ex2 && ex1 === "";
};