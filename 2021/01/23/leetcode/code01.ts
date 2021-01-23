// Sort the Matrix Diagonally
function diagonalSort(mat: number[][]): number[][] {
    const lastCol = mat[0].length-1;
    const lastRow = mat.length-1;

    let result = [];
    for(let i=0; i<lastRow+1;i++){
        const insert = Array(mat[0].length);
        result.push(insert)
    }

    let nowCol = 0;
    let nowRow = mat.length-1; 
    // console.log(result);
    while(nowCol !== lastCol || nowRow !== 0){
        let checkR = nowRow;
        let checkC = nowCol;

        let checkMat = [];
        let insertMat = [];
        checkMat.push([checkR,checkC]);
        insertMat.push(mat[checkR][checkC]);
        while(checkR !== lastRow && checkC !== lastCol){
            checkR +=1;
            checkC +=1;
            checkMat.push([checkR,checkC]);
            insertMat.push(mat[checkR][checkC])
        }

        insertMat.sort((a,b) => a-b);
        let j = 0;
        // console.log(checkMat);
        // console.log(insertMat);
        for(let i of checkMat){
            result[i[0]][i[1]] = insertMat[j];
            j+=1;
        }

        if(nowRow !== 0){
            nowRow -=1
        }else{
            nowCol +=1
        }
    }
    result[0][lastCol] = mat[0][lastCol];
    return result;
};

//
function diagonalSort(mat: number[][]): number[][] {
    let single:any={};
    for (let i = 0; i < mat.length; i++) {
            sortHelper(i, 0, mat);
    }
    for (let j = 0; j < mat[0].length; j++) {
            sortHelper(0, j, mat);
    }
    return mat;

};

function sortHelper(i:number, j: number, mat: number[][]) {
    let list: number[] = [];
    let x = i;
    let y = j;
    while (x < mat.length && y < mat[0].length) {
        list.push(mat[x++][y++]);
    }
    list.sort((a,b) => a-b)
    x = i;
    y = j;
    let index = 0;
    while (x < mat.length && y < mat[0].length) {
        mat[x++][y++] = list[index++];
    }
}

//
function diagonalSort(mat: number[][]): number[][] {
    if (mat.length === 0) return [];
    const rows = mat.length;
    const cols = mat[0].length;
    const sortLine = (d: number) => {
        const nums: number[] = [];
        for (let i = 0; i <= d; ++i) {
            if (i < rows && d-i < cols) {
                nums.push(mat[i][cols-d+i-1])
            }
        }
        nums.sort((a,b) => a-b);
        for (let i = 0; i <= d; ++i) {
            if (i < rows && d-i < cols) {
                mat[i][cols-d+i-1] = nums.shift();
            }
        }
    };
    const lines = rows + cols - 1;
    for (let d = 0; d < lines; ++d) {
        sortLine(d);
    }
    return mat;
};