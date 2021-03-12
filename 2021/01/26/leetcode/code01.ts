// Path With Minimum Effort
function minimumEffortPath(heights: number[][]): number {
    let result = [];
    for(let i = 0; i<heights.length; i++){
        const insert = Array(heights[0].length).fill(-Infinity);
        result.push(insert)
    }
    console.log(heights);
    for(let i =0 ; i<heights.length; i++){
        for(let j=0; j<heights[0].length; j++){
            if(i===0 || j===0){
                if(i===0 && j===0){
                    continue
                }else if(i===0){
                    result[i][j] = Math.max(result[i][j-1],Math.abs(heights[i][j]-heights[i][j-1]))
                }else{
                    result[i][j] = Math.max(result[i-1][j],Math.abs(heights[i-1][j]-heights[i][j]))
                }
            }else{
                result[i][j] = Math.min(
                                        Math.max(Math.abs(heights[i][j]-heights[i][j-1]),result[i][j-1]),
                                        Math.max(Math.abs(heights[i][j]-heights[i-1][j]),result[i-1][j])
                                        )
            }
        }
    }
    console.log(result);
    return result[heights.length-1][heights[0].length-1];
};