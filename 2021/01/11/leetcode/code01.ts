// Merge Sorted Array
/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let idx1 : number = 0;
    let idx2 : number = 0;

    while (m > 0 || n >0){
        if (m>0 && n > 0){
            if(nums1[idx1] > nums2[idx2]){
                nums1.splice(idx1, 0, nums2[idx2]);
                nums1.pop();
                n-=1;
                idx1+=1;
                idx2+=1;
            }else{
                m-=1;
                idx1+=1;
            }
        }
        else if(n>0){
            nums1.splice(idx1, 0, nums2[idx2]);
            nums1.pop();
            n-=1;
            idx1+=1;
            idx2+=1;
        }else{
            break;
        }
    }
};

// nums1 은 고정적인 길이 이므로,
// num2 의 input 수만큼 앞에서 삭제후 남은 길이만큼 nums1에 input
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    nums1.length = m;
    nums2.length = n;
    let counter = 0;
    n = 0;
    while (counter < nums1.length) {
        if (nums2[n] < nums1[counter]) {
            nums1.splice(counter, 0, nums2[n]);
            n += 1;
        }
        counter += 1;
    }
    nums2.splice(0, n);
    if (nums2.length) {
        nums1.push(...nums2);
    }
};


function merge(nums1: number[], m: number, nums2: number[], n: number): void {

    let i1 = 0; // index for nums1
    let i2 = 0; // index for nums2

    let inserts = 0;
    while (i2< n){
        while ( nums1[i1] < nums2[i2] && i1 < m+inserts){
            i1++;
    

        nums1.splice(i1, 0, nums2[i2]);
        inserts++;
        i2++;
        i1++;
    }

    nums1.splice(m+n, inserts);
};

function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    nums1.splice(m, nums1.length - m)
    let last = 0;
    for(let i = 0; i < n; i++){ 
        while(nums2[i] >= nums1[last]){
            last++;
            
        }
        nums1.splice(last, 0, nums2[i]);
    }    
};