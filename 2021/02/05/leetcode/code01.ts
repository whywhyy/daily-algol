// Simplify Path
function simplifyPath(path: string): string {
    const pathArr = path.split('/');
    console.log(pathArr)
    const result = []
    for(let i=0; i < pathArr.length; i++){
        if(pathArr[i] === '..'){
            if(result.length >= 1){
                result.pop();
            }
        }
        if(pathArr[i] !== '' && pathArr[i] !== '.' && pathArr[i] !== '..'){
            result.push(pathArr[i])
        }
    }
    
    return result ? '/' + result.join('/') : '/'; 
};

function simplifyPath(path: string): string {
    const paths = path.split('/')
    const stack = []
    paths.forEach(p => {
        if (!p || p === '.') {
        // do nothing
        } else if (p == '..') {
        stack.pop()
        } else {
        stack.push(p)
        }
    })
    return `/${stack.join('/')}`
}


// GOOD
function simplifyPath(path: string): string {
    const result: string[] = []
    for (const p of path.split('/')) {
        if (p == '' || p == '.') {
            continue
        }
        if (p == '..') {
            result.pop()
        } else {
            result.push(p)
        }
    }
    return `/${result.join('/')}`
};

function simplifyPath(path: string): string {

    const paths = path.split('/').filter(p => p && p !== '.');

    const res = [];

    for(const p of paths){

        if( p !== '..' ){
        res.push(p);
        continue;
        }

        if( res.length ) res.pop();
    }

    return '/' + res.join('/');
}