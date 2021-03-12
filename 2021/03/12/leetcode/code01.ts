// Check If a String Contains All Binary Codes of Size K
function hasAllCodes(s: string, k: number): boolean {
  if(s.length < k){
    return false;
  }
  const calSet = new Set();
  for(let i=0; i < s.length-k+1; i++){
    calSet.add(s.slice(i, i+k));
  }

  if(calSet.size === 2**k){
    return true;
  }
  return false;
};