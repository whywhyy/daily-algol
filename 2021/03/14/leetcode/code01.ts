// Binary Trees With Factors/// todo..
function numFactoredBinaryTrees(arr: number[]): number {
	let count = 0;

	const checkSet = new Set();
	const queue = [];

	for(const ele of arr){
		queue.push(ele);
		checkSet.add(ele);
	}
	
	while(queue){
		count += 1;
		const tree = queue.shift();
		// find leaf nodes
		 
	}

	return count;
};