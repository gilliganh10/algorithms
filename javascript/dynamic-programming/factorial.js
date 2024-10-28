
const factorial = (target) => {

    // init the base case [0] with 1
    target_list = [];
    target_list.push(1);

    // result = 1
    result = 1;

    // Loop through the rest of the target
    for (let i = 1; i < target; i++) {
        result = result * i
        target_list.push(result)
    };

    return target_list

}

const factorialDynamicProgramming = (target) => {

    // init the arraay and the base values for 0 and 1

    target_list = []
    target_list.push(1, 1)

    // loop through the remaining values to the target
    for (let i = 2; i < target; i++) {
        result = i * target_list[i - 1];
        target_list.push(result);
    };

    return target_list;

};

console.log(factorial(10))

console.log(factorialDynamicProgramming(10))