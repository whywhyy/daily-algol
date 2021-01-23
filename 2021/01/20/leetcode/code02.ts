// Valid Parentheses
function isValid(s: string): boolean {
    if (s.length % 2 === 1){
        return false;
    }
    let stack : Array<string> = [];
    
    for(let i=0; i<s.length; i++){
        if(stack.length === 0){
            stack.push(s[i])
        }else{
            if(s[i] === '{' || s[i] === '[' || s[i] === '('){
                stack.push(s[i]);
            }else{
                const last = stack.pop()
                if(s[i] === '}' && last !== '{'){
                    return false;
                }else if(s[i] === ']' && last !== '['){
                    return false;
                }else if(s[i] === ')' && last !== '('){
                    return false;
                }
            }
        }
    }

    if (stack.length === 0){
        return true;
    }else{
        return false;
    }
    
};

// 반대방향 넣고 pop 했을때 같은지 확인!
var isValid = function(s) {   
    const stack = [];
    
    for (let i = 0 ; i < s.length ; i++) {
        let c = s.charAt(i);
        switch(c) {
            case '(': 
                stack.push(')');
                break;
            case '[': 
                stack.push(']');
                break;
            case '{': 
                stack.push('}');
                break;
            default:
                if (c !== stack.pop()) {
                    return false;
                }
        }
    }
    
    return stack.length === 0;
};
