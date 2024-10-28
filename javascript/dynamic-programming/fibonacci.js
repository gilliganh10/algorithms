

let arr = [0, 1]

for (let i = 1; i < 11; i++) {
    
    let ultimate = arr[arr.length - 1]
    let penultimate = arr[arr.length - 2]
    let next_number = ultimate + penultimate;

    arr.push(next_number);
}

console.log(arr)