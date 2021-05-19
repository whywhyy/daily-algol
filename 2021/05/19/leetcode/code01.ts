// Find Duplicate File in System
function findDuplicate(paths: string[]): string[][] {
    const contentANDFilename = {};
    const contentANDFilename = paths.reduce((arr:string[], param) => {
        const splited = param.split (' ');
        const prefixPath = splited[0];
        splited.slice(1).map((fileANDcontent) => arr.push(prefixPath + '/' + fileANDcontent))
        return arr;
    }, {})

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

// refactor
// 무거워지는 변수? 가 많아지는지 조금 느려짐.
// Find Duplicate File in System
function findDuplicate(paths: string[]): string[][] {

    const contentANDFilename = paths.reduce((result, param) => {
        const splited = param.split (' ');
        const prefixPath = splited[0];
        const pathsArr = splited.slice(1).map((fileANDcontent) => prefixPath + '/' + fileANDcontent)
        const pathANDContent = pathsArr.map((pathANDContent) => pathANDContent.split(/\(|\)/));
        pathANDContent.map((pAndc) => {
            const p = pAndc[0];
            const c = pAndc[1];
            ((result[c]) || (result[c]=[])).push(p);
        })
        return result;
    }, {})


    return Object.values<string[]>(contentANDFilename).filter((arr) => arr.length >=2 );
};

/*
** const [name, content] = parts[j].split(/\(|\)/);
** => reg 
** (map[content] || (map[content] = [])).push([parts[0], name].join('/'));
** => 초기값 설정법 무엇 굳
** Object.values<string[]>(map).filter(v => v.length > 1);
** 아 Object 에 <> 로 형정의 하면 되네
*/ 
function findDuplicate(paths: string[]): string[][] {
    const map = {};

    for (let i = 0; i < paths.length; i++) {
        const parts = paths[i].split(' ');
        for (let j = 1; j < parts.length; j++) {
            const [name, content] = parts[j].split(/\(|\)/);
            (map[content] || (map[content] = [])).push([parts[0], name].join('/'));
        }
    }

    return Object.values<string[]>(map).filter(v => v.length > 1);
};

function findDuplicate(paths: string[]): string[][] {
    const map = new Map<string, string[]>();
    
    for (const s of paths) {
        const tmp = s.split(' ');
        const path = tmp.shift();
        for (const file of tmp) {
            const i = file.indexOf('(');
            const pathFile = path + '/' + file.slice(0, i);
            const content = file.slice(i + 1, file.length - 1);
            
            if (map.has(content)) {
                map.get(content).push(pathFile);
            }
            else {
                map.set(content, [pathFile]);
            }
        }
    }
    
    const result = [];
    for (const files of map.values()) {
        if (files.length > 1) {
            result.push(files);
        }
    }
    
    return result;
};