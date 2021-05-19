// Find Duplicate File in System
function findDuplicate(paths: string[]): string[][] {
    const contentANDFilename = {};
    const arr = paths.reduce((arr:string[], param) => {
        const splited = param.split (' ');
        const prefixPath = splited[0];
        splited.slice(1).map((fileANDcontent) => arr.push(prefixPath + '/' + fileANDcontent))
        return arr;
    }, [])

    arr.map((param) => {
        const arr = param.split('(');
        const filePath = arr[0];
        const content = arr[1].slice(0,-1);

        if(contentANDFilename[content]){
            contentANDFilename[content].push(filePath);   
        }else{
            contentANDFilename[content] = [filePath];   
        }
    })

    const result = [];
    Object.keys(contentANDFilename).map((key) => {
        if(contentANDFilename[key].length >= 2){
            result.push(contentANDFilename[key]);
        } 
    })
    return result;
};